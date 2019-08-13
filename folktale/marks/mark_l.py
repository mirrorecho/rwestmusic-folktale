import abjad, calliope

from folktale.stories import arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.lines import sing_line


class JigL(jig.JigHarmonizedBlock):
    pass



JIG_L = JigL(sing_line.SingLine()).transformed(
    calliope.Transpose(interval=-8)
    )


def show_final_block():
    calliope.PhrasePhrases()(JIG_L)
    calliope.Label()(JIG_L[0].phrases)
    calliope.Label()(JIG_L[1].phrases)
    JIG_L.illustrate_me(
        as_midi=True
        )

# show_final_block()

# --------------------------------------

a = arranger.Arranger(
    line_block = JIG_L,
    )

a.line_to_staff(3, "piano1", 
    # transforms=(
    #     calliope.CropChords(above=-2),
    #     calliope.Transpose(interval=-12),
    #     )
    )

a.line_to_staff(2, "piano2", 
    transforms=(
        calliope.CropChords(above=-1),
        # calliope.Transpose(interval=-12),
        )
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

def decorate_short_score():
    calliope.Label()(a.score.staff_groups["short_score"][0].cells)
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

