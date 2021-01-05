import abjad, calliope

from folktale.stories import arranger 
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.lines import sing_line

class JigJ(jig.JigHarmonizedBlock):
    pass

JIG_J = JigJ(sing_line.SingLine())

def show_final_block():
    calliope.PhrasePhrases()(JIG_J)
    calliope.Label()(JIG_J[0].phrases)
    calliope.Label()(JIG_J[1].phrases)
    JIG_J.illustrate_me(
        as_midi=True
        )

# show_final_block()

# --------------------------------------

a = arranger.Arranger(
    line_block = JIG_J,
    rehearsal_mark_number = 10,
    defined_length = 100,
    )

a.line_to_staff(0, "violin1", 
    # transforms=(calliope.SlurCells(),)
    )
a.line_to_staff(2, "violin2", 
    transforms=(calliope.CropChords(below=2),)
    )
a.line_to_staff(2, "viola", 
    transforms=(calliope.CropChords(above=-1,below=1),)
    )
a.line_to_staff(2, "cello", 
    transforms=(
        calliope.CropChords(above=-2),
        calliope.Transpose(interval=-12),
        )
    )


# a.line_to_staff(3, "piano2", 
#     transforms=(
#         # calliope.Transpose(interval=-12),
#         calliope.SlurCells(),
#         )
#     )

# a.line_to_staff(5, "violin1", 
#     transforms=(
#         calliope.SlurCells(),
#         )
#     )
# a.line_to_staff(6, "violin2", 
#     transforms=(
#         # calliope.Transpose(interval=-12),
#         calliope.SlurCells(),
#         )
#     )
# a.line_to_staff(7, "viola", 
#     transforms=(
#         # calliope.Transpose(interval=-12),
#         calliope.SlurCells(),
#         )
#     )
# a.line_to_staff(3, "cello", 
#     transforms=(
#         # calliope.Transpose(interval=-12),
#         calliope.SlurCells(),
#         )
#     )
# a.line_to_staff(4, "bass", 
#     transforms=(
#         # calliope.Transpose(interval=-12),
#         calliope.SlurCells(),
#         )
#     )

# show_final_block()

def decorate_short_score():
    calliope.Label()(a.score.staff_groups["short_score"][0].cells)
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