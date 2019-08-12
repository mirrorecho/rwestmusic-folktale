import abjad, calliope

class SingPhraseA0(calliope.Phrase):
    respell = "flats"
    class SingCell0(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1, .5, .5, 1)
        init_pitches = (7, 12, 14, 9)
    class SingCell1(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (.5, .5, 1)
        init_pitches = (11, 14, 9)
    class SingCell2(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (.5, .5, 1)
        init_pitches = (11,  2, 4)
    class SingCell3(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1,  1 )
        init_pitches = (12, 11)

class SingPhraseA1(SingPhraseA0):
    class SingCell0(SingPhraseA0.SingCell0):
        init_pitches = (7, 9, 12, 7)
    class SingCell1(SingPhraseA0.SingCell1):
        init_pitches = (16, 14, 7)

class SingPhraseB(SingPhraseA0):
    class SingCell0(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1, 1, .5, .5)
        init_pitches = (7, 9, 7, 4)
    class SingCell1(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1, .5, .5)
        init_pitches = (9, 7, 4)
    class SingCell2(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1, 1)
        init_pitches = (7, 0)
    class SingCell3(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1, 1)
        init_pitches = (2, 4)

class SingLine(calliope.Line):
    phrase0 = SingPhraseA0
    phrase1 = SingPhraseA1
    phrase2 = SingPhraseB
    phrase3 = SingPhraseA0



class CounterPhraseA0(calliope.Phrase):
    class CounterCell0(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (2,1)
        init_pitches = (-5,-6)
    class CounterCell1(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1,1)
        init_pitches = (-5,-6)
    class CounterCell2(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1.5, 1.5)
        init_pitches = (-5, -12) # NOTE: going up an octave here is also nice
    class CounterCell3(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1,  1 )
        init_pitches = (-10, -8)

class CounterPhraseB(calliope.Phrase):
    class CounterCell0(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (.5,1,0.5)
        init_pitches = (-6,-3,-1)
    class CounterCell1(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1.5, 0.5)
        init_pitches = (0, -1)
    class CounterCell2(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (.5, 1)
        init_pitches = (-5, -6)
    class CounterCell3(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1.5,)
        init_pitches = (-8, )

class CounterPhraseA1(CounterPhraseA0): 
    class CounterCell3(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1,  3 )
        init_pitches = (-13, -12)

class CounterPhraseC(calliope.Phrase): 
    class CounterCell0(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1,)
        init_pitches = (-6,)
    class CounterCell1(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1,1)
        init_pitches = (-5,-6)
    class CounterCell2(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (2,2)
        init_pitches = (-5,-8)


class CounterLine(calliope.Line):
    phrase0 = CounterPhraseA0
    phrase1 = CounterPhraseB
    phrase2 = CounterPhraseA1
    phrase3 = CounterPhraseC

class SingBlock(calliope.LineBlock):
    sing_line = SingLine
    counter_line = CounterLine

s = SingBlock().transformed(calliope.SlurCells())
for p in s[1].phrases[0,2]:
    for e in p.note_events[:-3]:
        e.pitch -= 12


# calliope.Label()(s[0].phrases)
# calliope.Label()(s[1].phrases)

# class SingBlockStaffGroup(calliope.StaffGroup): pass

# sg = SingBlockStaffGroup(
#     calliope.Staff(s[0]()),
#     calliope.Staff(s[1](), clef="bass"),
#     )
# sg.illustrate_me(
#     as_midi=True
#     )