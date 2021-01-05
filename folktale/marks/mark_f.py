import abjad, calliope

from folktale.stories import arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.lines import sing_line


from folktale.libraries import pitch_range_helpers

class LineF(sing_line.SingLine): pass

class BlockF(move_stack.ChordsToBlock): pass

# TO DO; this extra inheritance is nasty
class GridF(calliope.PitchesThroughGrid, calliope.PhraseBlock): pass

STACK_F = LineF()

jig.JigPitches()(STACK_F)
jig.JigRhythm()(STACK_F)

STACK_F.extend(STACK_F()[:-1])

# move_stack.SingSeq()(STACK_D)

move_stack.MoveStack(
    stack_intervals=(6,5,-2,-4),
    add_pitches = (),
    )(STACK_F)

BLOCK_F = BlockF(STACK_F)
# BLOCK_D[4].phrases[0].pitches = BLOCK_D[2].phrases[0].pitches

# BLOCK_D.illustrate_me()

BLOCK_F_GRIDS = [
    GridF(pb, 
        name="mark_f_" + pb.name + "_" + str(i),
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = pitch_range_helpers.down_ranges(12) if i < 2
            else pitch_range_helpers.midlow_string_ranges()
        ) for i, pb in enumerate(BLOCK_F.to_block_list())
]

class LineBlockF(calliope.LineBlock): pass

FINAL_BLOCK_F = LineBlockF.from_block_list(BLOCK_F_GRIDS)


def show_final_block():
    calliope.PhrasePhrases()(FINAL_BLOCK_F)
    calliope.Label()(FINAL_BLOCK_F[0].phrases)
    FINAL_BLOCK_F.illustrate_me(
        as_midi=True
        )


# --------------------------------------

a = arranger.Arranger(
    line_block = FINAL_BLOCK_F,
    rehearsal_mark_number = 6,
    defined_length = 100,
    )

# a.line_to_staff(0, "piano1", 
#     transforms=(calliope.SlurCells(),)
#     )
# a.line_to_staff(6, "piano2", 
#     transforms=(
#         calliope.Transpose(interval=-12),
#         calliope.SlurCells(),
#         )
#     )

# show_final_block()

def decorate_short_score():
    calliope.Label()(a.score.staff_groups["short_score"][0].phrases)
    calliope.PhrasePhrases()(a.score.staff_groups["short_score"][0])
    calliope.Label()(a.score.staff_groups["short_score"][1].cells)
    calliope.SlurCells()(a.score.staff_groups["short_score"][1])
    calliope.Label()(a.score.staff_groups["short_score"][2].events)

a.block_to_short_score()
decorate_short_score()

a.score.illustrate_me(
    as_midi=True
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