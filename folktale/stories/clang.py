import numpy as np
import pandas as pd

import abjad, calliope
from folktale.lines.sing_line import SingLine, SingPhraseA0, SingPhraseA1, SingPhraseB
from folktale.stories.move_stack import SingSeq

class Clang(calliope.Event):
    init_rhythm = (1,)
    # init_pitches = ((24,35,45),) 
    # init_pitches = ((12,23,33),) 

    class AccentMe(calliope.Transform):
        def transform(self, selectable, **kwargs):
            selectable.tag(">")

class ClangC(Clang):
    init_pitches = ((12,23,33),)     

class ClangG(Clang):
    init_pitches = ((18,19,28, 40),) 


class Stutter(calliope.Transform):
    def transform(self, selectable, **kwargs):
        last_selectable = selectable[-1]
        my_index = last_selectable.my_index
        my_parent = last_selectable.parent

        for i, event in enumerate(selectable.events):
            my_parent.insert(my_index+i+1, event())


# TO DO MAYBE: consider reviving:
class ClangPhrase(calliope.FromSelectableFactory, calliope.Phrase):

    def get_clang_pitches(self):
        return {
            7: {
                "intervals": (11, 12, 21, 33),
                # "offset":1,
            },
            11: {
                "intervals": (0, 7, 13, 24),
                # "offset":1,
            },
            12: {
                "intervals": (0,11,21),
                # "offset":1,
            },
        }

    def get_clang(self, pitch):
        pitch_class = pitch % 12
        for p,d in self.get_clang_pitches().items():
            if p % 12 == pitch_class:
                return d

    # in this context, a branch is a CELL
    def get_branch(self, node, *args, **kwargs):

        my_events=[]

        beats_last_clang = 0

        for event in node:
            
            clang_dict = self.get_clang(event.pitch)

            if clang_dict:
                beats_before = event.beats_before(node)
                space_beats = beats_before - beats_last_clang

                if space_beats > 0: 
                    self.info(space_beats)
                    my_events.append(
                        calliope.Event(
                            pitch = None,
                            beats = space_beats,
                            )
                    )

                my_events.append(calliope.Event(
                        pitches = [[p + event.pitch for p in clang_dict["intervals"]]],
                        rhythm = (event.beats,),
                    ))
                beats_last_clang += space_beats + event.beats

        # TO DO: this -1 below does NOT make sense???
        remaining_beats = node.beats - beats_last_clang
        print(node.beats, remaining_beats)

        if remaining_beats > 0:
            my_events.append(
                calliope.Event(
                    pitch = None,
                    beats = remaining_beats,
                    )
            )

        return calliope.Cell(*my_events)


class ClangChordsLine(calliope.FromSelectableFactory, calliope.Line):
    chord_indices = (
            (1,3,4),
            (-1,-2,-3),
        )

    # in this case, node is a Phrase
    def get_branch(self, node, *args, **kwargs):
        return calliope.Phrase(
                calliope.Cell(
                    pitches = (sorted([e.pitch for e in node.events[self.chord_indices[0]]]),),
                    rhythm = (node[0].beats + node[1].beats,)
                ),
                calliope.Cell(
                    pitches = (sorted([e.pitch for e in node.events[self.chord_indices[1]]]),),
                    rhythm = (node[2].beats + node[3].beats,)
                ),
            )


class ClangBlock(calliope.FromSelectableFactory, calliope.LineBlock):
    clang_phrase_type = ClangPhrase
    clang_chords_line_type = ClangChordsLine

    def get_branches(self, *args, **kwargs):
        return [
            calliope.Line(
                *[self.clang_phrase_type(p) for p in self.selectable.phrases]
            ),
            self.selectable(),
            self.clang_chords_line_type(self.selectable),
        ]




