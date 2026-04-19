from data import SETS

node1 = [s for s in SETS if s['node']==1 and not s.get('optional')]
print('Non-optional Node 1 sets in order:')
for s in node1:
    print(f"  id={s['id']} title={s['title']}")

print()
for s in SETS:
    if s['id']==8:
        c = s.get('content', {})
        sents = c.get('sentences', [])
        print(f"Set 8 has {len(sents)} sentences")
        if sents:
            print(f"First: {sents[0]['latin']}")
        else:
            print("EMPTY - this will crash and block progression!")
