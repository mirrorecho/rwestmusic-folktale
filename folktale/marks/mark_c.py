import abjad, calliope

from folktale.scores.score import FolktaleScore
# from folktale.stories.clang import ClangStory
from folktale.stories import arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack


from folktale.libraries import pitch_range_helpers

class StackC(move_stack.SingMoveStack): pass

class BlockC(move_stack.ChordsToBlock): pass

# TO DO; this extra inheritance is nasty
class GridC(calliope.PitchesThroughGrid, calliope.PhraseBlock): pass

STACK_C = StackC()
move_stack.SingSeq()(STACK_C)
move_stack.MoveStack(
    stack_intervals=(10,5,0),
    add_pitches = (-2,),
    )(STACK_C)

BLOCK_C = BlockC(STACK_C)

BLOCK_C_GRIDS = [
    GridC(pb, 
        name="mark_c_"+ pb.name,
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = pitch_range_helpers.midhigh_string_ranges()
        ) for pb in BLOCK_C.to_block_list()
]

BLOCK_C_GRIDS[2][0].respell = "sharps"


BLOCK_C_GRIDS[3][0].respell = "sharps"
BLOCK_C_GRIDS[3][1][-2].respell = "sharps"
BLOCK_C_GRIDS[3][1][-1].respell = "sharps"
BLOCK_C_GRIDS[3][2].respell = "sharps"
BLOCK_C_GRIDS[3][3].respell = "sharps"

class LineBlockC(calliope.LineBlock): pass

FINAL_BLOCK_C = LineBlockC.from_block_list(BLOCK_C_GRIDS)


def show_final_block():
    calliope.PhrasePhrases()(FINAL_BLOCK_C)
    calliope.Label()(FINAL_BLOCK_C[0].phrases)
    FINAL_BLOCK_C.illustrate_me(
        as_midi=True,
        )
# show_final_block()

# --------------------------------------

a = arranger.Arranger(
    line_block = FINAL_BLOCK_C,
    rehearsal_mark_number = 3,
    defined_length = 64,
    )

# a.staves["piano1"].append(move_chords_line)
a.block_cells_to_staff(1, "flute", (1,4,7,9,11,12,13))
a.block_cells_to_staff(1, "violin1", (1,4,7,9,11,12,13))


a.block_cells_to_staff(0, "oboe", (1,4,7,9,11,12,13))
a.block_cells_to_staff(0, "viola", (1,4,7,9,11,12,13))

a.line_to_staff(0, "piano1", 
    transforms=(calliope.SlurCells(),)
    )
a.line_to_staff(3, "piano2", 
    transforms=(calliope.SlurCells(),)
    )


# a.line_to_staff(3, "piano1", (PulseEvents(beats=0.25),))

calliope.PulseEvents(beats=1)(a.score.staves["oboe"])

calliope.SlurCells()(a.score.staff_groups["short_score"])

from calliope.transforms.poke import Poke


s0 = a.line_block[0]()

Poke(selection=s0.phrases[3,4])(s0)

# --------------------------------------

a.block_to_short_score()
a.illustrate_score(
    # as_midi=True
    with_short_score = True
    )


# calliope.SlurCells()(FINAL_BLOCK_C)

# print(FINAL_BLOCK_C[0][0])





# FINAL_BLOCK_C.illustrate_me()



# MOVE_BLOCK_GRID.illustrate_me()

# MOVE_STACK_KWARGS = dict(
#     pitch_grid_type=PitchGridC,
#     add_pitches=[p -6 for p in sing_stack.SING_CELLS_PITCHES_GROUP_2[-1][1:2]],
#     pitch_ranges = pitch_range_helpers.midhigh_string_ranges(),
#     )

# def tally_phrase(index, pitch_ranges=mid):
#     move_stack.tally_sing_crunch(index, **MOVE_STACK_KWARGS)

