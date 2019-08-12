import abjad, calliope

from folktale.scores.score import FolktaleScore
# from folktale.stories.clang import ClangStory

from folktale.lines import sing_line

from folktale.stories import folk
from folktale.stories.arranger import Arranger
from folktale.libraries import tally_apps
from folktale.stories import move_stack
from folktale.stories import sing_stack
from folktale.stories import jig
from folktale.stories import harmony
from folktale.stories import copland


class SingR(sing_line.SingBlock):
    pass

SING_R = SingR()
harmony.AsMinor()(SING_R[1])

# SING_R[0].events[0].pitch += 7
# SING_R[1].events[0].pitch -= 5

# calliope.Transpose(interval=-2)(SING_R[0])
# calliope.Transpose(interval=-2)(SING_R[1])

# calliope.Transpose(interval=5)(SING_R[0].cells[6,7])
# calliope.Transpose(interval=5)(SING_R[0].phrases[2,3])


SING_R.extend(copland.CoplandBlock()
    # .transformed(calliope.Transpose(interval=7))
    )

SING_R[2].insert(0,calliope.Phrase(
    calliope.Cell(rhythm=(8,), pitches=(None,))
    ))
SING_R[3].insert(0,calliope.Phrase(
    calliope.Cell(rhythm=(8,), pitches=(None,))
    ))
SING_R.extend(copland.CoplandBlock()
    # .transformed(calliope.Transpose(interval=7))
    )


SING_R[3].cells[3].rhythm=[1,3,2,2]
SING_R[5].cells[3].rhythm=[1,3,2,2]

SING_R[2].cells[3].pitches=[-8,-8]
SING_R[4].cells[3].pitches=[-8,-8]

SING_R[3].cells[3].pitches=[None,-24,None,-24]
SING_R[5].cells[3].pitches=[None,-24,None,-24]


class SingRStaffGroup(calliope.StaffGroup): pass

def show_final_block():
    calliope.PhrasePhrases()(SING_R)

    calliope.Label()(SING_R[0].phrases)
    calliope.Label()(SING_R[1].phrases)
    calliope.Label()(SING_R[2].cells)
    calliope.Label()(SING_R[4].cells)

    sg = SingRStaffGroup(
        *[calliope.Staff(s()) for s in SING_R],
        )

    sg.staves[1:].setattrs(clef="bass")

    sg.illustrate_me(
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