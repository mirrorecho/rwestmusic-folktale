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


class SingO(sing_line.SingBlock):
    pass

SING_O = SingO().transformed(calliope.Transpose(interval=4))

SING_LINE_INTRO = sing_line.SingLine().transformed(calliope.Transpose(interval=2))

move_stack.SingSeq(interval=7, pitch=0, smart_range=(0,12)).transform(
    SING_LINE_INTRO[1]
    )

calliope.Transpose(interval=2)(SING_LINE_INTRO[2])


SING_O[0].insert(0,SING_LINE_INTRO[0]())
SING_O[0].insert(1,SING_LINE_INTRO[1]())
SING_O[0].insert(2,SING_LINE_INTRO[2]())


SING_O[1].insert(0,calliope.Phrase(
    calliope.Cell(
        rhythm=(sum([p.beats for p in SING_O[0][:3]]),), 
        pitches=(None,)
    )
    ))

SING_O.extend([
    harmony.SweetDuoCellsPhrasesLine(SING_O[0]),
    harmony.SweetDuoCellsPhrasesLine(SING_O[1]),
    ]
    )

for p in SING_O.phrases:
    p.respell = "sharps"

def show_final_block():
    calliope.PhrasePhrases()(SING_O)
    calliope.Label()(SING_O[0].cells)
    calliope.Label()(SING_O[1].phrases)
    SING_O.illustrate_me(
        as_midi=True
        )

 # show_final_block()
# --------------------------------------

a = arranger.Arranger(
    line_block = SING_O,
    rehearsal_mark_number = 14,
    defined_length = 64,
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

a.illustrate_score(
    as_midi=True,
    with_short_score=True
    )

# --------------------------------------