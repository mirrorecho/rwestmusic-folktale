import abjad, calliope


from folktale.stories import arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.lines import sing_line


from folktale.libraries import pitch_range_helpers

class JigG(jig.JigBlock): pass

class BlockG(move_stack.ChordsToBlock): pass

# TO DO; this extra inheritance is nasty
class GridG(calliope.PitchesThroughGrid, calliope.PhraseBlock): pass

JIG = JigG(sing_line.SingLine())

# TO DO MAYBE: use MoveStack to implement this
for i,e in enumerate(JIG.note_events):
    e.pitch = [
         e.pitch + n for n in ([0,0,3,7] if i % 2 == 0 else [0,0,7,10])
    ]  + [2]

BLOCK_G_0 = BlockG(JIG[0])
BLOCK_G_1 = BlockG(JIG[1])

BLOCK_G_GRIDS_0 = [
    GridG(pb, 
        name="mark_g0_" + pb.name + "_" + str(i),
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = 
            pitch_range_helpers.down_ranges(12) if i in (2,6)
            else pitch_range_helpers.low_string_ranges() if i == 7
            else pitch_range_helpers.midlow_string_ranges()
        ) for i, pb in enumerate(BLOCK_G_0.to_block_list())
]
BLOCK_G_GRIDS_1 = [
    GridG(pb, 
        name="mark_g1_" + pb.name + "_" + str(i),
        tally_apps = tally_apps.LINE_SMOOTH_TALLY_APPS2,
        pitch_ranges = pitch_range_helpers.down_ranges(12) if i in (2,4)
            else pitch_range_helpers.midlow_string_ranges()
        ) for i, pb in enumerate(BLOCK_G_1.to_block_list())
]

class LineBlockG(calliope.LineBlock): pass

FINAL_BLOCK_G = LineBlockG.from_block_list(BLOCK_G_GRIDS_0)
FINAL_BLOCK_G.extend(LineBlockG.from_block_list(BLOCK_G_GRIDS_1))

def show_final_block():
    calliope.PhrasePhrases()(FINAL_BLOCK_G)
    calliope.Label()(FINAL_BLOCK_G[0].phrases)
    calliope.Label()(FINAL_BLOCK_G[5].phrases)
    FINAL_BLOCK_G.illustrate_me(
        as_midi=True
        )

# --------------------------------------

a = arranger.Arranger(
    line_block = FINAL_BLOCK_G,
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



# show_final_block()

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