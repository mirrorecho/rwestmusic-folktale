import abjad, calliope

from folktale.scores.score import FolktaleScore
# from folktale.stories.clang import ClangStory


from folktale.stories import folk
from folktale.stories import arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.stories import harmony
from folktale.lines import sing_line


class SingM(sing_line.SingBlock):
    pass

SING_M = SingM()

SING_LINE_INTRO = sing_line.SingLine()[:3]

SING_M[0].insert(0,SING_LINE_INTRO[0]())
SING_M[0].insert(1,SING_LINE_INTRO[1]())
SING_M[0].insert(2,SING_LINE_INTRO[2]())

folk.Stutter()(SING_M[0].cells[4])

folk.Stutter(times=2)(SING_M[0].cells[6,7].note_events[:3])

folk.Stutter(times=2)(SING_M[0].cells[8])

SING_M[1].insert(0,calliope.Phrase(
    rhythm=(sum([p.beats for p in SING_M[0][:3]]),), 
    pitches=(None,)
    ))

SING_M.extend([
    harmony.SweetDuoCellsPhrasesLine(SING_M[0]),
    ]
    )


def show_final_block():
    calliope.PhrasePhrases()(SING_M)
    calliope.Label()(SING_M[0].cells)
    calliope.Label()(SING_M[1].phrases)
    SING_M.illustrate_me(
        as_midi=True
        )

# show_final_block()
 
# --------------------------------------

a = arranger.Arranger(
    line_block = SING_M,
    )

a.line_to_staff(2, "viola", 
    transforms=(
        calliope.CropChords(below=-1),
        # calliope.Transpose(interval=-12),
        )
    )

# a.line_to_staff(3, "piano1", 
#     # transforms=(
#     #     calliope.CropChords(above=-2),
#     #     calliope.Transpose(interval=-12),
#     #     )
#     )

# a.line_to_staff(2, "piano2", 
#     transforms=(
#         calliope.CropChords(above=-1),
#         # calliope.Transpose(interval=-12),
#         )
#     )


# a.line_to_staff(0, "violin1", 
#     # transforms=(calliope.SlurCells(),)
#     )
# a.line_to_staff(2, "violin2", 
#     transforms=(calliope.CropChords(below=2),)
#     )
# a.line_to_staff(2, "viola", 
#     transforms=(calliope.CropChords(above=-1,below=1),)
#     )
# a.line_to_staff(2, "cello", 
#     transforms=(
#         calliope.CropChords(above=-2),
#         calliope.Transpose(interval=-12),
#         )
#     )


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