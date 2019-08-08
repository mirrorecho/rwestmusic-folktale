import abjad, calliope

from folktale.scores.score import FolktaleScore
from folktale.stories.clang import ClangStory

from folktale.stories.arranger import Arranger

class GroupUp(calliope.Transform):
    def transform(self, selectable, **kwargs):
        for branch in selectable:
            last_pitch = None
            for e in branch.note_events:
                while last_pitch is not None and e.pitch <= last_pitch:
                    e.pitch += 12
                last_pitch = e.pitch


# TO DO MAYBE: a ClangArranger for the first 3 marks
a = Arranger(
    line_block = ClangStory().tell()
    )

a.block_to_short_score()

# a.line_to_staff(0, "piano1", 
#     transforms=(calliope.CropChords(below=-2,),)
#     )
# a.line_to_staff(0, "piano2", 
#     transforms=(calliope.CropChords(above=-2,),)
#     )
# a.score.staves["piano2"].clef = "treble"

# a.line_to_staff(2, "violin1", 
#     transforms=(
#         calliope.CropChords(index=-1),
#         calliope.PulseEvents()
#         )
#     )
# a.line_to_staff(2, "violin2", 
#     transforms=(
#         calliope.CropChords(index=1),
#         calliope.PulseEvents()
#         )
#     )
# a.line_to_staff(2, "viola", 
#     transforms=(
#         calliope.CropChords(index=0),
#         calliope.PulseEvents()
#         )
#     )
# a.score.staff_groups["strings"].events.tag(":16")

# melody_line = a.line_block[1]

# bass_line = melody_line()

# a.poke_to_staff(
#     bass_line.events(pitch_class=7),
#     bass_line,
#     "bass",
#     transforms = (
#         calliope.SmartRange(smart_range=(0,12)),
#         )
#     )

# flute_line = melody_line()

# a.poke_to_staff(
#     flute_line.cells(4,8,12),
#     flute_line,
#     "flute",
#     )
# GroupUp()(a.score.staves["flute"].cells)

# # TO DO MAYBE... make this oboe line implementation less custom?
# oboe_line = calliope.Line(
#     calliope.Event(
#         rest=True, 
#         beats=sum([p.beats for p in melody_line.phrases[:3]])
#         )
#     )

# for p,p1 in zip(melody_line.phrases[3:-1], melody_line.phrases[4:]):
#     oboe_line.append( calliope.Event(rest=True, beats=p[0].beats) )
#     oboe_line.append( calliope.Event(pitch=p1.events[0].pitch, beats=p[1].beats) )

# a.score.staves["oboe"].append(oboe_line)

calliope.SlurCells()(a.score.staff_groups("short_score"))

a.score.illustrate_me(
    # as_midi=True,
    )

