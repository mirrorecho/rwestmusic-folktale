import abjad

import calliope

# from folktale.lines import sing_line # for testing


class SweetDuo(calliope.FromSelectableFactory):
    """
    harmonizes with the first note and the next note that's 
    "sweet" (either a third, 4th, or 5th away by default).
    """
    sweet_pitches = (3,4,5,7,8,9)

    def get_branches(self, *args, **kwargs):

        # TO DO: not very elegant, but it works
        try:
            first_pitch = self.selectable.note_events[0].pitch
            next_pitch = next((e.pitch for e in self.selectable.note_events[1:]
                if (first_pitch - e.pitch) % 12 in self.sweet_pitches
                ), None
                )
            my_pitches = [first_pitch, next_pitch] if next_pitch else first_pitch
        except:
            my_pitches = None

        return [
        calliope.Event(
            beats=sum(e.beats for e in self.selectable.events),
            pitch=my_pitches)
        ]



class SweetDuoCell(SweetDuo, calliope.Cell): pass

class SweetDuoCellsPhrase(calliope.FromSelectableFactory, calliope.Phrase): 
    def get_branch(self, node, *args, **kwargs):
        return SweetDuoCell(node)


class SweetDuoCellsPhrasesLine(calliope.FromSelectableFactory, calliope.Line):
    """
    all cells in the original line become sweet duo harmonies... 
    assumes cells are grouped under phrases
    """
    def get_branch(self, node, *args, **kwargs):
        return SweetDuoCellsPhrase(node)


# TO DO: 
# this could be made into a more universal "change mode" machine
# right now, it only works  to change F# to F
class AsMinor(calliope.Transform):

    def transform(self, selectable, **kwargs):
        for e in selectable.note_events:
            if e.pitch % 12 == 6:
                e.pitch -= 1



# # TESTING:
# s = sing_line.SingLine()
# # print(s.cells[0])

# SweetDuoCellsPhrasesLine(s).illustrate_me()
# # SweetDuoCell(s.cells[0]).illustrate_me()
