with open('data.py', 'a', encoding='utf-8') as f:
    f.write('\n\nSETS_BY_ID = {s["id"]: s for s in SETS}\n')
    f.write('STUDENTS = [{"id": 1, "first_name": "Test Pupil"}, {"id": 2, "first_name": "Hassan A"}]\n')
