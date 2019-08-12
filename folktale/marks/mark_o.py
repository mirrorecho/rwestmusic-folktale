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