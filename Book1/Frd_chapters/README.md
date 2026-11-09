# FRD — chapter files

One file per chapter, numbered so they sort in reading order.
Edit a single chapter without touching the rest.

## Dividers — NOT interchangeable

    <p align="center">&#42; &#42; &#42;</p>       scene break (80)
    <p align="center">&#9670; &#9670; &#9670;</p>    grey-memory shift (12)

A chapter never ends on `* * *` — the chapter break already does that job.
The only divider that may close a chapter is `◆ ◆ ◆`, where the chapter
hands over into or out of a grey memory (ch29, ch30, ch39, ch40).

Written as HTML entities on purpose. Bare asterisks get mangled on
round-trip through other tools — that is what corrupted an earlier
copy of this manuscript. Leave them in this form.

## Italics

`*single asterisks*`. Keep them balanced; an odd count in a
paragraph breaks formatting on build.

## Conventions

See `../Frd Style Sheet.md`. In short: British spelling; Boltcaster,
Falka(s), Kro, Ork; Causeway and Titan always capitalised; the
ellipsis is the single character …; a spaced em dash ( — ), never a
spaced hyphen.

## Acts

Three named acts, listed in `acts.md` (name | title | first chapter):
*The Quiet Town* (1–9), *Where the Lines Point* (10–31), *The Open Book*
(32–41). Chapters stay numbered only. `join.py` inserts the act headings.

## Reassembling

    python3 join.py > "../Frd manuscript.md"

Front matter, the three act headings and all 41 chapters, in order. The chapter files are
the source of truth; `Frd manuscript.md` is derived from them.
