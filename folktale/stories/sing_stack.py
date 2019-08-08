import abjad, calliope


from folktale.lines.sing_line import SingLine

s = SingLine()

SING_CHORDS_FROM_CELLS = calliope.Line(
    *[calliope.Cell(
        factory=calliope.ChordsFromSelectable(p.cells),
        )
    for p in s.phrases]
    )

SING_CHORDS_FROM_CELLS.events.setattrs(beats=1)
calliope.SlurCells()(SING_CHORDS_FROM_CELLS)

SING_CELLS_PITCHES = [c.pitch for c in SING_CHORDS_FROM_CELLS.events]

SING_CELLS_PITCHES_GROUP_2 = [
    sorted(set(a) | set(b)) 
    for a,b in zip(SING_CELLS_PITCHES[:-1], SING_CELLS_PITCHES[1:])
    ]

SING_CHORDS_FROM_CELLS_GROUP_2 = calliope.Cell(
    pitches=(SING_CELLS_PITCHES_GROUP_2), 
    rhythm=(1,)*len(SING_CELLS_PITCHES_GROUP_2)
    )

# SING_CHORDS_FROM_CELLS_GROUP_2.illustrate_me()