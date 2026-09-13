# FRD / THIRD — chapter files

One file per chapter, numbered so they sort in reading order.
Edit a single chapter without touching the rest.

## Dividers — NOT interchangeable

    <p align="center">&#42; &#42; &#42;</p>       scene break (116)
    <p align="center">&#9670; &#9670; &#9670;</p>    grey-memory shift (12)

Written as HTML entities on purpose. Bare asterisks get mangled on
round-trip through other tools — that is what corrupted an earlier
copy of this manuscript. Leave them in this form.

## Italics

`*single asterisks*`. Keep them balanced; an odd count in a
paragraph breaks formatting on build.

## Reassembling

    python3 join.py > Frd_manuscript.md

Front matter plus all 41 chapters, in order. Send that back to
rebuild the EPUB/PDF.
