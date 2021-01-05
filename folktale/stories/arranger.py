import abjad, calliope

from folktale.scores.score import FolktaleScore


# TO DO: maybe this should be a story
class Arranger(calliope.CalliopeBase):
    score = None
    defined_length = None
    rehearsal_mark_number = None

    line_block = None # this is for the short score

    # def line_to_staff(self, line_index, staff_name, transforms=()):
    #     my_line = self.line_block[line_index]()
    #     for t in transforms:
    #         t(my_line)
    #     self.score.staves[staff_name].append(my_line)
    #     if len(self.score.staves[staff.name].segments) == 0:
    #         my_segment = calliope.Segment(
    #             defined_length = self.defined_length,
    #             rehearsal_mark_number = self.rehearsal_mark_number
    #             )
    #     else:
    #         my_segment = self.score.staves[staff.name].segments[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = FolktaleScore()
        for staff in self.score.staves:
            staff.append(
                calliope.Segment(
                    name=staff.name,
                    rehearsal_mark_number = self.rehearsal_mark_number,
                    defined_length = self.defined_length,
                    )
                )

    def line_to_staff(self, line_index, staff_name, transforms=()):
        my_line = self.line_block[line_index]()
        for t in transforms:
            t(my_line)
        self.score.segments[staff_name].append(my_line)

    # TO DO: this is confusing between selection and selectable
    # ... should be more like the above with an absract selection
    def poke_to_staff(self, selection, selectable, staff_name, transforms=()):
        calliope.Poke(selection=selection)(selectable)
        for t in transforms:
            t(selectable)
        self.score.segments[staff_name].append(selectable)

    def block_cells_to_staff(self, line_index, staff_name, cell_indices):
        self.score.segments[staff_name].append(
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
                self.score.staff_groups["short_score"][i].segments[0].append(l())
            except:
                print("OH NO SHORT SCORE!", self.line_block)

    @classmethod
    def from_arranger_segments(self, *incoming_arrangers):
        my_score = incoming_arrangers[0].score()
        for arr in incoming_arrangers[1:]:
            for segment in arr.score.segments: 
                my_score.staves[segment.name].append(segment())
        return my_score

    # def from_score_segments(self, *incoming_arranger):
    #     for segment in incoming_arranger.score.segments:
    #         # print("YO", segment.name)
    #         self.score.staves[segment.name].append(segment())

    #         # print(staff.name)
    #         # if len(staff.lines) > 0:
    #         #     my_segment = calliope.Segment(
    #         #         staff.lines[0]
    #         #         )
    #         #     self.score.staves[staff.name].append(my_segment)

    #             # if len(self.score.staves[staff.name].lines) == 0:
    #             #     self.score.staves[staff.name].append(staff.lines[0])
    #             # else:
    #             #     self.score.staves[staff.name].lines[0].extend(staff.lines[0])

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
