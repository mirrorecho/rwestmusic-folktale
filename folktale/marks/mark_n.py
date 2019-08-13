import abjad, calliope

from folktale.scores.score import FolktaleScore
# from folktale.stories.clang import ClangStory

from folktale.lines import sing_line
from folktale.libraries import tally_apps

from folktale.stories import folk
from folktale.stories import harmony
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig

from folktale.stories import arranger


class SingN(sing_line.SingBlock):
    pass

SING_N = SingN().transformed(calliope.Transpose(interval=2))

SING_LINE_INTRO = sing_line.SingLine()

move_stack.SingSeq(interval=7, pitch=0, smart_range=(0,12)).transform(
    SING_LINE_INTRO[1]
    )

calliope.Transpose(interval=2)(SING_LINE_INTRO[2])


SING_N[0].insert(0,SING_LINE_INTRO[0]())
SING_N[0].insert(1,SING_LINE_INTRO[1]())
SING_N[0].insert(2,SING_LINE_INTRO[2]())


SING_N[1].insert(0,calliope.Phrase(
    rhythm=(sum([p.beats for p in SING_N[0][:3]]),), 
    pitches=(None,)
    ))


SING_N.append(
    harmony.SweetDuoCellsPhrasesLine(SING_N[0])
    )

for p in SING_N.phrases:
    p.respell = "sharps"

def show_final_block():
    calliope.PhrasePhrases()(SING_N)
    calliope.Label()(SING_N[0].phrases)
    calliope.Label()(SING_N[1].phrases)
    SING_N.illustrate_me(
        as_midi=True
        )

# show_final_block()
# --------------------------------------

a = arranger.Arranger(
    line_block = SING_N,
    )

a.line_to_staff(0, "viola", 
    transforms=(
        # calliope.CropChords(below=-1),
        calliope.Transpose(interval=-12),
        )
    )

a.line_to_staff(1, "cello", 
    transforms=(
        # calliope.CropChords(below=-1),
        calliope.Transpose(interval=-12),
        )
    )

a.line_to_staff(2, "violin1", 
    transforms=(
        calliope.CropChords(below=1),
        # calliope.Transpose(interval=-12),
        )
    )
a.line_to_staff(2, "violin2", 
    transforms=(
        calliope.CropChords(above=1),
        # calliope.Transpose(interval=-12),
        )
    )

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