import abjad, calliope

class SingPhraseA1(calliope.Phrase):
    respell = "flats"
    class SingCell1(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1, .5, .5, 1, .5, .5, 1)
        init_pitches = (7, 12, 14, 9, 11, 14, 9)
    class SingCell2(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (.5, .5, 1, 1,  1 )
        init_pitches = (11,  2, 4, 12, 11)

class SingPhraseA2(SingPhraseA1):
    class SingCell1(SingPhraseA1.SingCell1):
        init_pitches = (7, 9, 12, 7, 16, 14, 7)

class SingPhraseB(SingPhraseA1):
    class SingCell1(calliope.Cell):
        # time_signature = (5, 4)
        init_rhythm =  (1, 1, .5, .5, 1, .5, .5)
        init_pitches = (7, 9, 7, 4, 9, 7, 4)
    class SingCell2(calliope.Cell):
        # time_signature = (4, 4)
        init_rhythm =  (1, 1, 1,  1 )
        init_pitches = (7, 0, 2, 4)

class SingLine(calliope.Line):
    phrase1 = SingPhraseA1
    phrase2 = SingPhraseA2
    phrase3 = SingPhraseB
    phrase4 = SingPhraseA1

