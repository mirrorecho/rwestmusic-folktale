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



