import numpy as np
import pandas as pd

import abjad, calliope

from folktale.lines.sing_line import SingLine, SingPhraseA1, SingPhraseA2, SingPhraseB
from folktale.libraries.tally_apps import (
    LINE_SMOOTH_TALLY_APPS,LINE_SMOOTH_TALLY_APPS2)

class SingSeq(calliope.Transform):
    """
    transposes an inteveral every time (original) melodic note is X
    """
    interval = -7
    pitch = 11

    def transform(self, selectable, **kwargs):
        transpose = 0
        for event in selectable.note_events:
            if event.pitch == self.pitch:
                transpose += self.interval
            event.pitch = event.pitch + transpose

class AddPitchToChord(calliope.Transform):
    pitch = 4

    def transform(self, selectable, **kwargs):
        for event in selectable.note_events:
            event.pitch.append(self.pitch)

class ChordSelect(calliope.Transform):
    index=0

    def transform(self, selectable, **kwargs):
        for event in selectable.note_events:
            event.pitch = event.pitch[self.index]

# TO DO MAYBE: is this a factory?
class MoveStory(calliope.CalliopeBase):
    selectable = None

    name = None
    tally_apps = ()
    move_pitch=11
    move_interval=-7
    smart_range=(-3,24)
    stack_intervals=(0,5,10)
    add_pitches=(3,)

    @property
    def row_count(self):
        return len(self.stack_intervals) + len(self.add_pitches)

    def tell(self):
        """
        converts to a stacked harmonies that transpose as pitch occurs
        """
        return self.selectable.transformed(
            SingSeq(interval=self.move_interval, pitch=self.move_pitch),
            calliope.SmartRange(smart_range=self.smart_range),
            calliope.StackPitches(intervals=self.stack_intervals),
            *[AddPitchToChord(pitch=p) for p in self.add_pitches],
            )

    def as_pitch_grid(self, tally_apps=()):
        pg_data = pd.DataFrame.from_records(self.selectable.pitches).transpose() 
        pg = calliope.PitchGrid(name=self.name or getattr(self.selectable, "name", None))
        pg.init_data(start_data=pg_data)
        pg.add_tally_apps(*self.tally_apps)
        pg.tally_me()
        return pg

    def get_grid_pitches(self):
        return self.as_pitch_grid().data.transpose().values.tolist()

    def update_pitches_from_grid(self):
        self.selectable.pitches = self.get_grid_pitches()

    def grid_pitch_calc(self):
        self.as_pitch_grid().tally_loop()

    def illustrate_me(self):
        self.selectable.illustrate_me()

    def as_row(self, index):
        return self.selectable().transformed(ChordSelect(index=index)) 

    def update_smart_ranges_rows(self, smart_range=None):
        smart_range = smart_range or self.smart_range
        new_pitches = [
            self.as_row(index=i).transformed(
                calliope.SmartRange(smart_range=smart_range)
                ).pitches
            for i in range(self.row_count)
        ]
        self.selectable.pitches = list(zip(*new_pitches))

    def as_score(self):
        return calliope.Score(*[
            calliope.Staff(
                self.as_row(index=i) 
                # to consider  adding in a smart range
                )
            for i in range(self.row_count)
            ])


def sing_up():
    l = MoveStory(
        selectable=SingLine(name="sing_up"), 
        tally_apps=LINE_SMOOTH_TALLY_APPS2,
        add_pitches=(4,),
        )
    l.tell()
    l.update_smart_ranges_rows()
    l.update_pitches_from_grid()
    return l

def tally_sing_up():
    l = sing_up()
    l.grid_pitch_calc()


# l = sing_up()
# print(l.as_pitch_grid().tallies)

sing_up().illustrate_me()

# sing_up_4ths.illustrate_me()







