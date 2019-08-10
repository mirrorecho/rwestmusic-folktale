import abjad, calliope

from folktale.scores.score import FolktaleScore

from folktale.lines.sing_line import SingLine, SingPhraseA0, SingPhraseA1, SingPhraseB

from folktale.stories.move_stack import SingSeq
from folktale.stories.clang import ClangBlock, Stutter
from folktale.stories.arranger import Arranger

# class GroupUp(calliope.Transform):
#     def transform(self, selectable, **kwargs):
#         for branch in selectable:
#             last_pitch = None
#             for e in branch.note_events:
#                 while last_pitch is not None and e.pitch <= last_pitch:
#                     e.pitch += 12
#                 last_pitch = e.pitch


# TO DO MAYBE: a ClangArranger for the first 3 marks
def get_line():
    s = SingLine()

    s.extend([SingPhraseA1(),SingPhraseB(),SingPhraseA0()])

    SingSeq(interval=7, pitch=0, smart_range=(0,12)).transform(s)

    calliope.SmartRange().transform(s)

    s["phrase0"].respell = "sharps"
    s["phrase1"].respell = "sharps"
    s["phrase2"].respell = "sharps"
    s["phrase3"].respell="flats"

    # s.insert(0, SingPhraseA0())
    # s.insert(1, SingPhraseA1())
    # s.insert(2, SingPhraseB())
    # s.insert(3, SingPhraseA0())

    s.events[0].pitch += 5 # SPECIAL case for first event  

    Stutter()(s["phrase0"].events[1,2,3])
    Stutter()(s["phrase0"].events[11,12,13,14])

    Stutter()(s["phrase1"].events[0,1])
    Stutter()(s["phrase1"].events[11,12,13])

    # Stutter()(s["phrase2"].events[0,1])


    # Stutter()(s["phrase0"].events[5,6,7])

    # Stutter()(s["phrase0"].events[-2,-1])
    # Stutter()(s["phrase0"].events[-2,-1])

    return s


a = Arranger(
    line_block = ClangBlock(get_line())
    )

a.block_to_short_score()

calliope.SlurCells()(a.score.staff_groups("short_score"))

a.score.illustrate_me(
    # as_midi=True,
    )
