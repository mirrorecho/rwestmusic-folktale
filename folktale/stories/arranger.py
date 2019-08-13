import abjad, calliope

from folktale.scores.score import FolktaleScore


# TO DO: maybe this should be a story
class Arranger(calliope.CalliopeBase):
    score = None
    line_block = None
    # chords_line = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = FolktaleScore()

    def line_to_staff(self, line_index, staff_name, transforms=()):
        my_line = self.line_block[line_index]()
        for t in transforms:
            t(my_line)
        self.score.staves[staff_name].append(my_line)

    # TO DO: this is confusing between selection and selectable
    # ... should be more like the above with an absract selection
    def poke_to_staff(self, selection, selectable, staff_name, transforms=()):
        calliope.Poke(selection=selection)(selectable)
        for t in transforms:
            t(selectable)
        self.score.staves[staff_name].append(selectable)

    def block_cells_to_staff(self, line_index, staff_name, cell_indices):
        self.score.staves[staff_name].append(
            calliope.Line(*[
                c() if i in cell_indices 
                else calliope.Cell( pitches=(None,), rhythm=(c.beats,) )
                for i, c in enumerate(self.line_block[line_index].cells)
                ])
            )

    # TO DO: is this used????
    def chords_to_staff(self, staff_name, cell_events_dict): pass
        # score.staves[staff_name].append(
        #     calliope.Line(*[
        #         c for c in 
        #         ])
        #     )

    def block_to_short_score(self):
        for i,l in enumerate(self.line_block):
            try:
                self.score.staff_groups["short_score"][i].append(l())
            except:
                print("OH NO SHORT SCORE!", self.line_block)

    def copy_score_staves(self, incoming_score):
        for staff in incoming_score.staves:
            print(staff.name)
            if len(staff.lines) > 0:
                self.score.staves[staff.name].append(staff.lines[0]() )

    def illustrate_score(self,
        with_short_score = False,
        **kwargs,
        ):

        if not with_short_score:
            self.score.pop(-1)
        
        self.score.illustrate_me(
            **kwargs
            )

    # def pulse_events_to_staff(self, line_index, staff_name)
