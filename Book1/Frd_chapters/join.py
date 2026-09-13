#!/usr/bin/env python3
import glob, os
here=os.path.dirname(os.path.abspath(__file__))
out=[]
fm=os.path.join(here,'00_front-matter.md')
if os.path.exists(fm): out.append(open(fm,encoding='utf-8').read().strip())
for p in sorted(glob.glob(os.path.join(here,'[0-4][0-9]_*.md'))):
    if p.endswith('00_front-matter.md'): continue
    out.append(open(p,encoding='utf-8').read().strip())
print("\n\n".join(out))
