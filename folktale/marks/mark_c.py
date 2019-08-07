import abjad, calliope

from folktale.scores.score import FolktaleScore
# from folktale.stories.clang import ClangStory
from folktale.stories.arranger import Arranger, PulseEvents
from folktale.stories import move_stack

a = Arranger(
    line_block = move_stack.sing_crunch_lb(),
    # chords_line =  move_stack.sing_chords_line(),
    )

a.block_to_short_score()

# a.staves["piano1"].append(move_chords_line)
a.block_cells_to_staff(1, "flute", (1,4,7,9,11,12,13))
a.block_cells_to_staff(1, "violin1", (1,4,7,9,11,12,13))


a.block_cells_to_staff(0, "oboe", (1,4,7,9,11,12,13))
a.block_cells_to_staff(0, "viola", (1,4,7,9,11,12,13))

# a.line_to_staff(3, "piano1", (PulseEvents(beats=0.25),))

PulseEvents(beats=1)(a.score.staves["oboe"])

calliope.SlurCells()(a.score.staff_groups["short_score"])

from calliope.transforms.poke import Poke


s0 = a.line_block[0]()


Poke(selection=s0.phrases[3,4])(s0)

s0.illustrate_me()

# a.score.illustrate_me(
#     as_midi=True,
#     )