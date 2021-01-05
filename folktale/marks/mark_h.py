import abjad, calliope

from folktale.stories import arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.lines import sing_line


from folktale.libraries import pitch_range_helpers

class JigH(jig.JigBlock): pass

class BlockH(move_stack.ChordsToBlock): pass

# TO DO; this extra inheritance is nasty
class GridH(calliope.PitchesThroughGrid, calliope.PhraseBlock): pass

JIG = JigH(sing_line.SingLine())


# TO DO MAYBE: use MoveStack to implement this
for i,e in enumerate(JIG.note_events):
    e.pitch = [
         e.pitch + 1 + n for n in ([0,0,3,7] if i % 2 == 0 else [0,0,7,10])
    ]  + [2]

for i,p in enumerate(JIG[0].phrases):
    first_phrase_pitch = p.events[0].pitch
    if first_phrase_pitch:
        first_phrase_pitch = first_phrase_pitch[0]
    for e in p.note_events:
        first_pitch = e.pitch[0]
        if i < 2:
            e.pitch += [first_phrase_pitch, first_pitch, first_pitch]  
        elif i < 5:
            e.pitch += [first_phrase_pitch, first_pitch, -3] 
        else:
            e.pitch += [2, -3, -3]

for i,p in enumerate(JIG[1].phrases):
    first_phrase_pitch = p.events[0].pitch
    if first_phrase_pitch:
        first_phrase_pitch = first_phrase_pitch[0]
    for e in p.note_events:
        first_pitch = e.pitch[0]
        if i < 3:
            e.pitch += [first_phrase_pitch, first_pitch, first_pitch]  
        elif i < 4:
            e.pitch += [first_phrase_pitch, first_pitch, -3] 
        else:
            e.pitch += [2, -3, -6]

BLOCK_H_0 = BlockH(JIG[0])
BLOCK_H_1 = BlockH(JIG[1])

BLOCK_H_0_BLOCK_LIST = BLOCK_H_0.to_block_list()
BLOCK_H_0_BLOCK_LIST.pop(-1)
BLOCK_H_0_BLOCK_LIST.pop(-1)


BLOCK_H_GRIDS_0 = [
    GridH(pb, 
        name="mark_h0_" + pb.name + "_" + str(i),
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = 
            pitch_range_helpers.down_ranges(12) if i in (2,6)
            else pitch_range_helpers.low_string_ranges() if i == 7
            else pitch_range_helpers.midlow_string_ranges()
        ) for i, pb in enumerate(BLOCK_H_0_BLOCK_LIST)
]
BLOCK_H_GRIDS_1 = [
    GridH(pb, 
        name="mark_h1_" + pb.name + "_" + str(i),
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = pitch_range_helpers.down_ranges(12) if i in (2,4)
            else pitch_range_helpers.midlow_string_ranges()
        ) for i, pb in enumerate(BLOCK_H_1.to_block_list())
]

class LineBlockH(calliope.LineBlock): pass

FINAL_BLOCK_H = LineBlockH.from_block_list(BLOCK_H_GRIDS_0)
FINAL_BLOCK_H.extend(LineBlockH.from_block_list(BLOCK_H_GRIDS_1))


def show_final_block():
    calliope.PhrasePhrases()(FINAL_BLOCK_H)
    calliope.Label()(FINAL_BLOCK_H[0].phrases)
    calliope.Label()(FINAL_BLOCK_H[8].phrases)
    FINAL_BLOCK_H.illustrate_me(
        as_midi=True
        )

# --------------------------------------


a = arranger.Arranger(
    line_block = FINAL_BLOCK_H,
    rehearsal_mark_number = 8,
    defined_length = 100,
    )

a.line_to_staff(0, "piano1", 
    transforms=(calliope.SlurCells(),)
    )
a.line_to_staff(3, "piano2", 
    transforms=(
        # calliope.Transpose(interval=-12),
        calliope.SlurCells(),
        )
    )

a.line_to_staff(5, "violin1", 
    transforms=(
        calliope.SlurCells(),
        )
    )
a.line_to_staff(6, "violin2", 
    transforms=(
        # calliope.Transpose(interval=-12),
        calliope.SlurCells(),
        )
    )
a.line_to_staff(7, "viola", 
    transforms=(
        # calliope.Transpose(interval=-12),
        calliope.SlurCells(),
        )
    )
a.line_to_staff(3, "cello", 
    transforms=(
        # calliope.Transpose(interval=-12),
        calliope.SlurCells(),
        )
    )
a.line_to_staff(4, "bass", 
    transforms=(
        # calliope.Transpose(interval=-12),
        calliope.SlurCells(),
        )
    )

# show_final_block()

def decorate_short_score():
    calliope.Label()(a.score.staff_groups["short_score"][0].phrases)
    calliope.PhrasePhrases()(a.score.staff_groups["short_score"][0])
    calliope.Label()(a.score.staff_groups["short_score"][1].cells)
    calliope.SlurCells()(a.score.staff_groups["short_score"][1])
    calliope.Label()(a.score.staff_groups["short_score"][2].events)

a.block_to_short_score()
decorate_short_score()

a.illustrate_score(
    as_midi=True,
    with_short_score=True
    )

# --------------------------------------



# a = Arranger(
#     line_block = move_stack.sing_crunch_lb(
#         **MOVE_STACK_KWARGS
#         ),
#     # chords_line =  move_stack.sing_chords_line(),
#     )

# a.block_to_short_score()

# # a.staves["piano1"].append(move_chords_line)
# a.block_cells_to_staff(1, "flute", (1,4,7,9,11,12,13))
# a.block_cells_to_staff(1, "violin1", (1,4,7,9,11,12,13))


# a.block_cells_to_staff(0, "oboe", (1,4,7,9,11,12,13))
# a.block_cells_to_staff(0, "viola", (1,4,7,9,11,12,13))

# # a.line_to_staff(3, "piano1", (PulseEvents(beats=0.25),))

# calliope.PulseEvents(beats=1)(a.score.staves["oboe"])

# calliope.SlurCells()(a.score.staff_groups["short_score"])

# from calliope.transforms.poke import Poke


# s0 = a.line_block[0]()

# Poke(selection=s0.phrases[3,4])(s0)

# a.score.illustrate_me(
#     as_midi=True,
#     )