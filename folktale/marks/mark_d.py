import abjad, calliope

from folktale.scores.score import FolktaleScore
# from folktale.stories.clang import ClangStory
from folktale.stories.arranger import Arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack


from folktale.libraries import pitch_range_helpers

class StackD(move_stack.SingMoveStack): pass

class BlockD(move_stack.ChordsToBlock): pass

# TO DO; this extra inheritance is nasty
class GridD(calliope.PitchesThroughGrid, calliope.PhraseBlock): pass

STACK_D = StackD()
move_stack.SingSeq()(STACK_D)
move_stack.MoveStack(
    stack_intervals=(10,5,0),
    add_pitches = (-2,-4),
    )(STACK_D)

BLOCK_D = BlockD(STACK_D)
BLOCK_D[4].phrases[0].pitches = BLOCK_D[2].phrases[0].pitches

# BLOCK_D.illustrate_me()

BLOCK_D_GRIDS = [
    GridD(pb, 
        name="mark_d_"+ pb.name,
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = pitch_range_helpers.midhigh_string_ranges()
        ) for pb in BLOCK_D.to_block_list()
]

class LineBlockD(calliope.LineBlock): pass

FINAL_BLOCK_D = LineBlockD.from_block_list(BLOCK_D_GRIDS)


def show_final_block():
    calliope.PhrasePhrases()(FINAL_BLOCK_D)
    calliope.Label()(FINAL_BLOCK_D[0].phrases)
    FINAL_BLOCK_D.illustrate_me(
        as_midi=True,
        )

show_final_block()


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