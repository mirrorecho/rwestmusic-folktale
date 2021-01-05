import abjad, calliope

from folktale.stories import arranger 
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.stories import harmony
from folktale.lines import sing_line


class JigK(jig.JigHarmonizedBlock):
    pass

JIG_K = JigK(sing_line.SingLine()).transformed(
    calliope.Transpose(interval=-4)
    )


def show_final_block():
    calliope.PhrasePhrases()(JIG_K)
    calliope.Label()(JIG_K[0].phrases)
    calliope.Label()(JIG_K[1].phrases)
    JIG_K.illustrate_me(
        as_midi=True
        )

# show_final_block()

# --------------------------------------

a = arranger.Arranger(
    line_block = JIG_K,
    rehearsal_mark_number = 11,
    defined_length = 100,
    )

a.line_to_staff(3, "piano1", 
    # transforms=(
    #     calliope.CropChords(above=-2),
    #     calliope.Transpose(interval=-12),
    #     )
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

a.illustrate_score(
    as_midi=True,
    with_short_score=True
    )

# --------------------------------------