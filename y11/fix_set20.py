import sqlite3
conn = sqlite3.connect('latin_gcse.db')
rows = conn.execute("SELECT pupil_id FROM pupil_progress WHERE set_id=9 AND status='passed'").fetchall()
print(f'Found {len(rows)} pupils with Set 9 passed')
for (pid,) in rows:
    conn.execute("""INSERT INTO pupil_progress (pupil_id, set_id, status, best_score)
                   VALUES (?,20,'available',0)
                   ON CONFLICT(pupil_id,set_id) DO UPDATE SET
                   status=CASE WHEN status='locked' THEN 'available' ELSE status END""", (pid,))
    print(f'  Unlocked Set 20 for pupil_id={pid}')
conn.commit()
conn.close()
print('Done')
