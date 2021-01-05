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

class MarkQ(calliope.Arrangement, FolktaleScore):
    def get_short_score():
        self.poke_to_staff()


calliope.illustrate_me(MarkQ)


class SingR(sing_line.SingBlock):
    pass

SING_R = SingR()
# harmony.AsMinor()(SING_R[1])

# calliope.Transpose(interval=5)(SING_R[0].cells[6,7])
# calliope.Transpose(interval=5)(SING_R[0].phrases[2,3])


SING_R.extend(copland.CoplandBlock().transformed(
    calliope.Transpose(interval=7)
    ))


class SingRStaffGroup(calliope.StaffGroup): pass

def show_final_block():
    calliope.PhrasePhrases()(SING_R)

    calliope.Label()(SING_R[0].cells)
    calliope.Label()(SING_R[1].phrases)

    sg = SingRStaffGroup(
        *[calliope.Staff(s()) for s in SING_R],
        )

    sg.staves[1:].setattrs(clef="bass")

    sg.illustrate_me(
        as_midi=True
        )

show_final_block()

class ShortScoreQ(calliope.ShortScore):
    staves = 5
    clefs = ("treble","treble","treble","bass")

class Arrangement(calliope.Arrangement, FolktaleScore):
    short_score_staves = 5

    def get_short_score(self):


class Arrangement(calliope.FromSelectableFactory, FolktaleScore):
    branch_type = calliope.Segment

    def get_branch(self, node, *args, **kwargs):
        return node(*args, **kwargs)

    def get_branches(self, *args, **kwargs):
        for s in self.staves:
            s.append(calliope.Segment(
                name = s.name,

                ))
        return self




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