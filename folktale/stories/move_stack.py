import numpy as np
import pandas as pd

import abjad, calliope

from folktale.lines.sing_line import SingLine, SingPhraseA0, SingPhraseA1, SingPhraseB
from folktale.libraries.tally_apps import (
    LINE_SMOOTH_TALLY_APPS,LINE_SMOOTH_TALLY_APPS2)


class SingSeq(calliope.Transform):
    """
    transposes an inteveral every time (original) melodic note is X
    """
    interval = -7
    pitch = 11
    smart_range=(-3,24)

    def transform(self, selectable, **kwargs):
        transpose = 0
        for event in selectable.note_events:
            if event.pitch % 12 == self.pitch % 12:
                transpose += self.interval
            event.pitch = event.pitch + transpose

        calliope.SmartRange(smart_range=self.smart_range)(selectable)


class AddPitchesToChords(calliope.Transform):
    pitches = (4,)

    def transform(self, selectable, **kwargs):
        for event in selectable.note_events:
            event.pitch.extend(self.pitches)


class ChordSelect(calliope.Transform):
    index=0

    def transform(self, selectable, **kwargs):
        for event in selectable.note_events:
            event.pitch = event.pitch[self.index]


class ChordsToBlock(calliope.FromSelectableFactory, calliope.LineBlock):

    def get_branch(self, node, index, *args, **kwargs):
        return node(*args, **kwargs).transformed(ChordSelect(index=index))

    def get_branches(self, *args, **kwargs):
        chord_length = len(self.selectable.note_events[0].pitch)
        return [self.get_branch(self.selectable, i, *args, **kwargs) for i in range(chord_length)]


class MoveStack(calliope.Transform):
    stack_intervals=(10,5,0)
    add_pitches=(3,)

    # @property
    # def row_count(self):
    #     return len(self.stack_intervals) + len(self.add_pitches)

    def transform(self, selectable, **kwargs):
        calliope.StackPitches(intervals=self.stack_intervals)(selectable)
        AddPitchesToChords(pitches = self.add_pitches)(selectable)


class SingMoveStack(calliope.Line):
    move_phrase_a0 = SingPhraseA0
    move_phrase_a1 = SingPhraseA1
    move_phrase_b = SingPhraseB
    move_phrase_a0_1 = SingPhraseA0
    move_phrase_a1_1 = SingPhraseA1
    move_phrase_b_1 = SingPhraseB
    move_phrase_a0_2 = SingPhraseA0

    # seq_me = SingSeq
    # move_me = MoveStack



# as a test...
# MOVE_BLOCK = ChordsToBlock(selectable=SingMoveStack()[0])

# MOVE_BLOCK_GRID = MoveBlockGrid(MOVE_BLOCK,
#     tally_apps=LINE_SMOOTH_TALLY_APPS2,
#     )


# print(MOVE_BLOCK_GRID.data)
# print(MOVE_BLOCK_GRID.data.iloc[0])

# move_block_grid.illustrate_me()


#     # name = None
#     # tally_apps = ()
#     # move_pitch=11
#     # move_interval=-7
#     # smart_range=(-3,24)
#     # stack_intervals=(10,5,0)
#     # add_pitches=(3,)
#     # pitch_grid_type = calliope.PitchGrid # TO DO: this is nasty
#     # pitch_ranges = None

#     # @property
#     # def row_count(self):
#     #     return len(self.stack_intervals) + len(self.add_pitches)


#     def get_grid_pitches(self):
#         return self.as_pitch_grid().data.transpose().values.tolist()

#     def update_pitches_from_grid(self):
#         self.selectable.pitches = self.get_grid_pitches()

#     def grid_pitch_calc(self):
#         self.as_pitch_grid().tally_loop()

#     def as_row(self, index):
#         return self.selectable().transformed(ChordSelect(index=index)) 

#     def update_smart_ranges_rows(self, smart_range=None):
#         smart_range = smart_range or self.smart_range
#         new_pitches = [
#             self.as_row(index=i).transformed(
#                 calliope.SmartRange(smart_range=smart_range)
#                 ).pitches
#             for i in range(self.row_count)
#         ]
#         self.selectable.pitches = list(zip(*new_pitches))


# def sing_up():
#     l = MoveStory(
#         selectable=SingLine(name="sing_up"), 
#         tally_apps=LINE_SMOOTH_TALLY_APPS2,
#         add_pitches=(4,),
#         )
#     l.tell()
#     l.update_smart_ranges_rows()
#     l.update_pitches_from_grid()
#     return l



# def sing_crunch(phrase, 
#     **kwargs):

#     l = MoveStory(
#         selectable=phrase, 
#         tally_apps=LINE_SMOOTH_TALLY_APPS2,
#         **kwargs
#         )
#     l.tell2()
#     l.update_smart_ranges_rows()
#     l.update_pitches_from_grid()
#     return l

# def sing_crunch_list(**kwargs):
#     sing_line_move = sing_move()
#     phrase_grid_list = [
#         sing_crunch(p, **kwargs) for p in sing_line_move.selectable.phrases
#     ]
#     return phrase_grid_list

# def tally_sing_crunch(index, **kwargs):
#     p = sing_crunch_list(**kwargs)[index]
#     p.grid_pitch_calc()

# class SingCrunchLineBlock(calliope.LineBlock): pass

# def sing_crunch_lb(**kwargs):
#     my_list = sing_crunch_list(**kwargs)
#     row_count = my_list[0].row_count

#     lb = SingCrunchLineBlock()

#     for i in range(row_count):
#         lb.append(
#             calliope.Line(
#                 *[p.as_row(i) for p in my_list]
#                 )
#             )

#     return lb

# class SingCrunchLine(calliope.Line): pass

# def sing_chords_line(**kwargs):
#     my_list = sing_crunch_list(**kwargs)

#     return SingCrunchLine(*[p.selectable() for p in my_list])


# lb = sing_crunch_lb()
# calliope.SlurCells()(lb)
# lb.illustrate_me()




# sing_crunch_list()[0].as_score().illustrate_me()

# sing_crunch_list()[1].illustrate_me()



# l = sing_up2()
# score = l.as_score()
# score.illustrate_me(as_midi=True)

# print(l.as_pitch_grid().tallies)




# sing_up_4ths.illustrate_me()







