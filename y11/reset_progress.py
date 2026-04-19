"""
Reset script: wipe progress for Hassan A and create a fresh TEST PUPIL
so we can test from scratch without affecting real student data.
"""
import sqlite3

conn = sqlite3.connect('latin_gcse.db')
conn.row_factory = sqlite3.Row

# 1. Find Hassan A
hassan = conn.execute("SELECT id, first_name FROM pupils WHERE first_name='Hassan A'").fetchone()
if hassan:
    pid = hassan['id']
    print(f"Found Hassan A: id={pid}")
    # Delete all progress records for Hassan
    conn.execute("DELETE FROM pupil_progress WHERE pupil_id=?", (pid,))
    print(f"  Cleared {conn.total_changes} progress rows")
else:
    print("Hassan A not found")

# 2. Create a fresh TEST pupil if one doesn't exist
existing_test = conn.execute("SELECT id FROM pupils WHERE first_name='Test Pupil'").fetchone()
if existing_test:
    tp_id = existing_test['id']
    conn.execute("DELETE FROM pupil_progress WHERE pupil_id=?", (tp_id,))
    print(f"Existing Test Pupil (id={tp_id}) progress cleared")
else:
    conn.execute("INSERT INTO pupils (first_name) VALUES ('Test Pupil')")
    tp_id = conn.execute("SELECT id FROM pupils WHERE first_name='Test Pupil'").fetchone()['id']
    print(f"Created Test Pupil: id={tp_id}")

conn.commit()
conn.close()
print("Done. Hassan A and Test Pupil both start fresh.")
