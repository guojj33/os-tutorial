import os

fs = os.listdir('./')
new_fs = []
for f in fs:
    if len(f) > 3 and (f[2] == '-'):
        new_fs.append(f)
fs = new_fs
di = {}
for f in fs:
    print(f[:2])
    di[int(f[:2])] = f
di = dict(sorted(di.items()))
print(di)
with open('index.md', 'w') as fo:
    for d in di:
        fo.write('[{}](./{}/README.md)\n'.format(di[d], di[d]))
