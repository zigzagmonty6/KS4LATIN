"""
Latin GCSE Mastery Platform — Database helpers
"""
import sqlite3
import contextlib

DB_PATH = "latin_gcse.db"

def init_db():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS pupils (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS pupil_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pupil_id INTEGER NOT NULL,
                set_id INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'locked',
                best_score REAL NOT NULL DEFAULT 0,
                UNIQUE(pupil_id, set_id),
                FOREIGN KEY(pupil_id) REFERENCES pupils(id)
            );

            CREATE TABLE IF NOT EXISTS attempt_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pupil_id INTEGER NOT NULL,
                set_id INTEGER NOT NULL,
                question_type TEXT,
                question_text TEXT,
                pupil_answer TEXT,
                correct_answer TEXT,
                result TEXT,
                time_taken_ms INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY(pupil_id) REFERENCES pupils(id)
            );
        """)
        # Seed pupils from STUDENTS list
        from data import STUDENTS
        for name in STUDENTS:
            db.execute(
                "INSERT OR IGNORE INTO pupils (first_name) VALUES (?)", (name,)
            )
        # Unlock all introduction sets (node 0) for all pupils
        from data import SETS
        intro_set_ids = [s["id"] for s in SETS if s["node"] == 0]
        pupils = db.execute("SELECT id FROM pupils").fetchall()
        for p in pupils:
            for sid in intro_set_ids:
                db.execute(
                    """INSERT INTO pupil_progress (pupil_id, set_id, status, best_score)
                       VALUES (?, ?, 'available', 0)
                       ON CONFLICT(pupil_id, set_id) DO UPDATE SET
                       status = CASE WHEN status = 'locked' THEN 'available' ELSE status END""",
                    (p["id"], sid)
                )

@contextlib.contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
