# FRD — chapter files

One file per chapter, numbered so they sort in reading order.
Edit a single chapter without touching the rest.

## Dividers — NOT interchangeable

    <p align="center">&#42; &#42; &#42;</p>       scene break (115)
    <p align="center">&#9670; &#9670; &#9670;</p>    grey-memory shift (12)

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

## Reassembling

    python3 join.py > "../Frd manuscript.md"

Front matter plus all 41 chapters, in order. The chapter files are
the source of truth; `Frd manuscript.md` is derived from them.
