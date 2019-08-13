import abjad, calliope

from folktale.scores.score import FolktaleScore

from folktale.lines.sing_line import SingLine, SingPhraseA0, SingPhraseA1, SingPhraseB

from folktale.stories import folk
from folktale.stories import move_stack
from folktale.stories import clang
from folktale.stories import arranger

class GroupUp(calliope.Transform):
    def transform(self, selectable, **kwargs):
        for branch in selectable:
            last_pitch = None
            for e in branch.note_events:
                while last_pitch is not None and e.pitch <= last_pitch:
                    e.pitch += 12
                last_pitch = e.pitch


# TO DO MAYBE: a ClangArranger for the first 3 marks
def get_line():
    s = SingLine()


    s.extend([SingPhraseA1(),SingPhraseB(),SingPhraseA0()])

    move_stack.SingSeq(interval=7, pitch=0, smart_range=(0,12)).transform(s)

    calliope.SmartRange().transform(s)

    s["phrase0"].respell = "sharps"
    s["phrase1"].respell = "sharps"
    s["phrase2"].respell = "sharps"
    s["phrase3"].respell="flats"

    s.insert(0, SingPhraseA0())
    s.insert(1, SingPhraseA1())
    s.insert(2, SingPhraseB())

    # s.events[0].pitch += 5 # SPECIAL case for first event  

    # Stutter()(s["phrase0"].events[1,2,3])
    # Stutter()(s["phrase0"].events[11,12,13,14])

    # Stutter()(s["phrase1"].events[0,1])
    # Stutter()(s["phrase1"].events[11,12,13])

    # Stutter()(s["phrase2"].events[0,1])


    # Stutter()(s["phrase0"].events[5,6,7])

    # Stutter()(s["phrase0"].events[-2,-1])
    # Stutter()(s["phrase0"].events[-2,-1])

    return s

class ClangPhraseB(clang.ClangPhrase):
    def get_clang_pitches(self):
        return {
            9: {
                "intervals": (12, 13, 24, 31),
                # "offset":1,
            },
            11: {
                "intervals": (0, 10, 13, 25),
                # "offset":1,
            },
            12: {
                "intervals": (0,5,16),
                # "offset":1,
            },
        }

class ClangChordsLineB(clang.ClangChordsLine):
    chord_indices = (
            (0,1,3,4),
            (-1,-2,-3,-4),
        )

my_line_block = clang.ClangBlock(
        get_line(),
        clang_phrase_type = ClangPhraseB,
        clang_chords_line_type = ClangChordsLineB
        )

# TO DO: transform to add trailing rest:
my_line_block[0].append(
    calliope.Phrase(
        calliope.Cell(rhythm=(2,), pitches=(None,))
    )
    )
my_line_block[1].append(
    calliope.Phrase(
        calliope.Cell(rhythm=(2,), pitches=(None,))
    )
    )
my_line_block[2].append(
    calliope.Phrase(
        calliope.Cell(rhythm=(2,), pitches=(None,))
    )
    )

a = arranger.Arranger(
    line_block = my_line_block
    )

# --------------------------------------
# START STANDARD 0,A,B ARRANGING:

a.line_to_staff(0, "piano1", 
    transforms=(calliope.CropChords(below=-2,),)
    )
a.line_to_staff(0, "piano2", 
    transforms=(calliope.CropChords(above=-2,),)
    )

a.score.staves["piano1"].note_events[0].tag("8va", "ff")
a.score.staves["piano1"].note_events[-1].tag("8va!")
a.score.staves["piano2"].clef = "treble"
a.score.staff_groups["piano"].note_events.tag(">")

melody_line = a.line_block[1]

bass_line = melody_line()

a.poke_to_staff(
    bass_line.events(pitch_class=7),
    bass_line,
    "bass",
    transforms = (
        calliope.SmartRange(smart_range=(0,12)),
        )
    )

flute_line = melody_line()

a.poke_to_staff(
    flute_line.cells(4,8,12),
    flute_line,
    "flute",
    )
GroupUp()(a.score.staves["flute"].cells)
for c in a.score.staves["flute"].cells:
    if not c[0].rest:
        c[0].tag("mp", r"\<", "(")
        c[-2].tag(")")
        c[-1].tag(".", ">", "f", r"\!")


# TO DO MAYBE... make this oboe line implementation less custom?
oboe_line = calliope.Line(
    calliope.Event(
        rest=True, 
        beats=sum([p.beats for p in melody_line.phrases[:3]])
        )
    )

for p,p1 in zip(melody_line.phrases[3:-1], melody_line.phrases[4:]):
    oboe_line.append( calliope.Event(rest=True, beats=p[0].beats) )
    oboe_line.append( calliope.Event(pitch=p1.events[0].pitch, beats=p[1].beats) )

a.score.staves["oboe"].append(oboe_line)

a.line_to_staff(2, "violin1", 
    transforms=(
        calliope.CropChords(index=-1),
        calliope.PulseEvents()
        )
    )
a.line_to_staff(2, "violin2", 
    transforms=(
        calliope.CropChords(index=-2),
        calliope.PulseEvents()
        )
    )
a.line_to_staff(2, "viola", 
    transforms=(
        calliope.CropChords(index=1),
        calliope.PulseEvents()
        )
    )
a.line_to_staff(2, "cello", 
    transforms=(
        calliope.CropChords(index=0),
        calliope.PulseEvents(),
        calliope.Transpose(interval=-12),
        )
    )

a.score.staves["violin1"].note_events.tag(":16")
a.score.staves["violin2"].note_events.tag(":16")
a.score.staves["viola"].note_events.tag(":16")
a.score.staves["cello"].note_events.tag(":16")

# END STANDARD 0,A,B ARRANGING
# --------------------------------------

a.block_to_short_score()
a.score.illustrate_me(
    as_midi=True
    )