#!/usr/bin/env python3
# Rejoin front matter + act headings + chapters into one manuscript.
#   python3 join.py > "../Frd manuscript.md"
import glob, os, re
here=os.path.dirname(os.path.abspath(__file__))
acts={}
ap=os.path.join(here,'acts.md')
if os.path.exists(ap):
    for line in open(ap,encoding='utf-8'):
        m=re.match(r'\s*(Act [A-Za-z]+)\s*\|\s*(.+?)\s*\|\s*(\d+)\s*$',line)
        if m: acts[int(m.group(3))]=(m.group(1),m.group(2))
out=[]
fm=os.path.join(here,'00_front-matter.md')
if os.path.exists(fm): out.append(open(fm,encoding='utf-8').read().strip())
for p in sorted(glob.glob(os.path.join(here,'[0-4][0-9]_*.md'))):
    if p.endswith('00_front-matter.md'): continue
    n=int(os.path.basename(p)[:2])
    if n in acts: out.append(f"# {acts[n][0]}: *{acts[n][1]}*")
    out.append(open(p,encoding='utf-8').read().strip())
print("\n\n".join(out))
