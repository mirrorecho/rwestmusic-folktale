
import abjad
import calliope

# An homage to Copland's Concerto for Clarinet... 
# ... a quote similar to the first couple harmonies, but in reverse

class UpperCell(calliope.Cell):
    init_pitches = (-7,-8)
    init_rhythm = (3,3)

class LowerCell(calliope.Cell):
    init_pitches = (None, -22, None, -24,)
    init_rhythm = (1,2,1,2)

class UpperCellHigh(UpperCell):
    init_pitches = (-7,-5)

class LowerCellHigh(LowerCell):
    init_pitches = (None, -22, None, -20,)

class UpperCellLong(UpperCell):
    init_rhythm = (4,4)

class LowerCellLong(LowerCell):
    init_rhythm = (1,3,1,3)


class CoplandBlock(calliope.LineBlock):
    class UpperLine(calliope.Line):
        class Phrase0(calliope.Phrase):
            cell0 = UpperCell
            cell1 = UpperCellHigh

        class Phrase1(calliope.Phrase):
            cell0 = UpperCellLong
            cell1 = UpperCellLong
            cell2 = UpperCellLong

    class LowerLine(calliope.Line):
        class Phrase0(calliope.Phrase):
            cell0 = LowerCell
            cell1 = LowerCellHigh

        class Phrase1(calliope.Phrase):
            cell0 = LowerCellLong
            cell1 = LowerCellLong
            cell2 = LowerCellLong

# CoplandBlock().illustrate_me(
#     as_midi=True
#     )