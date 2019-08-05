import abjad, calliope

from folktale.scores.score import FolktaleScore
from folktale.stories.clang import ClangStory

def get_score():
    f = FolktaleScore()

    clang_lb = ClangStory().tell()

    f.staves["s1"].append(clang_lb[0]())
    f.staves["s2"].append(clang_lb[1]())
    f.staves["s3"].append(clang_lb[2]())

    phrases = list(clang_lb[1].phrases)

    # TO DO: get all melody phrases upfront... IMPROVE PERFORMANCE!


    # TO DO: these are creating LINES for every phrase... FIX!
    for p in clang_lb[0].phrases:
        f.staves["piano1"].append(
            calliope.Line(
                calliope.Phrase(
                    *[calliope.Cell(
                        *[e(pitch=e() if e.rest else e.pitch[-2:]) for e in c.events]
                        )
                    for c in p.cells])
                )
            )
        f.staves["piano2"].append(
            calliope.Line(
                calliope.Phrase(
                    *[calliope.Cell(
                        *[e(pitch=e() if e.rest else e.pitch[:-2]) for e in c.events]
                        )
                    for c in p.cells])
                )
            )

    f.staves["piano2"].clef = "treble"


    for p in clang_lb[2].phrases:
        f.staves["violin1"].append(
            calliope.Line(
                calliope.Phrase(
                    *[calliope.Cell(
                        rhythm = [0.5 for r in range(int(c.beats * 2))],
                        pitches = ([c[0].pitch[0] for r in range(int(c.beats * 2))])
                        )
                    for c in p.cells])
                )
            )
        f.staves["violin2"].append(
            calliope.Line(
                calliope.Phrase(
                    *[calliope.Cell(
                        rhythm = [0.5 for r in range(int(c.beats * 2))],
                        pitches = ([c[0].pitch[1] for r in range(int(c.beats * 2))])
                        )
                    for c in p.cells])
                )
            )
        f.staves["viola"].append(
            calliope.Line(
                calliope.Phrase(
                    *[calliope.Cell(
                        rhythm = [0.5 for r in range(int(c.beats * 2))],
                        pitches = ([c[0].pitch[2] for r in range(int(c.beats * 2))])
                        )
                    for c in p.cells])
                )
            )
    print("YO WHO WHO") 

    f.staves["violin1", "violin2", "viola"].events.tag(":16")

    for p in phrases:
        f.staves["bass"].append(
            calliope.Line(
                calliope.Phrase(
                    *[calliope.Cell(
                        *[
                        e(pitch=7) if e.pitch % 12 == 7 
                        else e(rest=True) for e in c.events]
                        )
                    for c in p.cells])
                )
            )


    oboe_line = calliope.Line()
    oboe_line.append( 
        calliope.Event(
            rest=True, 
            beats=sum([p.beats for p in phrases[:3]])
            )
        )

    print("YO Ha") 

    for p,p1 in zip(phrases[3:-1], phrases[4:]):
        oboe_line.append( calliope.Event(rest=True, beats=p[0].beats) )

        oboe_line.append( calliope.Event(pitch=p1.events[0].pitch, beats=p[1].beats) )


    f.staves["oboe"].append(oboe_line)


    flute_line = calliope.Line()
    flute_line.append(calliope.Event(rest=True, beats=phrases[0].beats))


    for p in phrases[1:4]: 
        flute_line.append(
            calliope.Phrase(*[
                calliope.Cell(
                    *[e(rest= i % 3 < 2) for i,e in enumerate(c.events)]
                    ) for c in p.cells
                ])
            )
    for p in phrases[4:]: 
        flute_line.append(
            calliope.Phrase(*[
                calliope.Cell(
                    *[e(rest= i % 2 == 0) for i,e in enumerate(c.events)]
                    ) for c in p.cells
                ])
            )


    f.staves["flute"].append(flute_line)

    calliope.SlurCells()(f.staff_groups("short_score"))

    print("YO HAY HAY")  

    return f



# f.illustrate_me(
#     as_midi=True,
#     )


# s = abjad.Score()
# s.extend([
#     abjad.Staff("c'1"),
#     abjad.Staff("c1"),
#     ])

# instrument = abjad.Instrument(
#                 name="S 1", 
#                 markup=abjad.Markup("S 1"),
#                 short_name="s.1",
#                 short_markup=abjad.Markup("s.1"),
#                 )

# instrument_command = abjad.LilyPondLiteral(
#     r"\set Staff.instrumentName = " + format(instrument.markup), 
#     "before")
# short_instrument_command =  abjad.LilyPondLiteral(
#     r"\set Staff.shortInstrumentName = " + format(instrument.short_markup), 
#     "before")

# abjad.attach(instrument_command, abjad.select(s[0]).leaves()[0])
# abjad.attach(short_instrument_command, abjad.select(s[0]).leaves()[0])


# print(format(s))