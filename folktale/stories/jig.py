import abjad, calliope

from folktale.lines.sing_line import SingLine, SingPhraseA0, SingPhraseA1, SingPhraseB

class Stutter(calliope.Transform):
    def transform(self, selectable, **kwargs):
        last_selectable = selectable[-1]
        my_index = last_selectable.my_index
        my_parent = last_selectable.parent

        for i, event in enumerate(selectable.events):
            my_parent.insert(my_index+i+1, event())

class JigPitches(calliope.Transform):
    def transform(self, selectable, **kwargs):

        l1 = selectable
        l1["phrase0"]["sing_cell0"].events[0].pitch += 7
        l1["phrase0"]["sing_cell1"].events[0].pitch += 5

        l1["phrase0"]["sing_cell2"].events[0].pitch += 5
        l1["phrase0"]["sing_cell2"].events[1].pitch += 12
        l1["phrase0"]["sing_cell2"].events[2].pitch += 5
        #  ------

        l1["phrase1"]["sing_cell0"].events[0].pitch += 7
        l1["phrase1"]["sing_cell0"].events[3].pitch += 7

        l1["phrase1"]["sing_cell1"].events[1].pitch -= 5
        l1["phrase1"]["sing_cell1"].events[2].pitch += 5

        l1["phrase1"]["sing_cell2"].events[0].pitch += 5
        l1["phrase1"]["sing_cell2"].events[1].pitch += 12
        l1["phrase1"]["sing_cell2"].events[2].pitch += 5
        #  ------

        l1["phrase2"]["sing_cell0"].events[2].pitch += 5
        l1["phrase2"]["sing_cell0"].events[3].pitch += 7

        # l1["phrase2"]["sing_cell1"].events[1].pitch += 7
        # l1["phrase2"]["sing_cell1"].events[2].pitch += 5

        # l1["phrase2"]["sing_cell2"].events[0].pitch -= 5
        l1["phrase2"]["sing_cell2"].events[1].pitch += 5

        l1["phrase2"]["sing_cell3"].events[0].pitch += 7
        # l["phrase2"]["sing_cell3"].events[1].pitch += 12
        #  ------

        l1["phrase3"]["sing_cell0"].events[0].pitch += 7

        l1["phrase3"]["sing_cell1"].events[0].pitch += 5

        l1["phrase3"]["sing_cell2"].events[0].pitch += 5
        l1["phrase3"]["sing_cell2"].events[1].pitch += 12
        l1["phrase3"]["sing_cell2"].events[2].pitch += 5

        for e in l1["phrase3"].events:
            e.pitch = e.pitch - 7

        return l1


class JigRhythm(calliope.Transform):
    def transform(self, selectable, **kwargs):
        # Pretty good for rhythm
        for p in selectable.phrases[0,1,3]:
            p.rhythm = (0.75, 0.25, 0.5, 0.5)*3
        selectable.phrases[2].rhythm = [0.5]*10 + [1]

# l = SingLine().transformed(JigPitches(), JigRhythm())

# l.illustrate_me()


class JigBlock(calliope.FromSelectableFactory, calliope.LineBlock):
    def get_branch(self, node, *args, **kwargs):
        return node(*args, **kwargs)

    def get_branches(self, *args, **kwargs):
        my_lines = [
        ]
        return my_lines



# l2 = l0()

# for e in l0["phrase3"].events:
#     e.pitch = e.pitch - 7


# # OK, not great
# # for e1,e0 in zip(l1.note_events, l0.note_events):
# #     if e1.pitch != e0.pitch:
# #         e1.pitch = [e1.pitch, e0.pitch]

# # # A little better
# # for e1,e2 in zip(l2.note_events, l1.note_events):
# #     e1.pitch = [e1.pitch+2, e2.pitch]
# #     e1.respell = "sharps"

# # for e in l1.events:
# #     e.beats = e.beats / 2





# l2 = l1()
# l2.insert(0, calliope.Phrase(rhythm=(12,), pitches=(None,)))
# l2.pop("phrase1")

# #
# for e in l2.select["phrase2","phrase3"].note_events:
#     e.pitch += 5

# l1.extend((
#     calliope.Phrase(rhythm=(6,), pitches=(None,)),
#     l1["phrase1"](name="phrase4"),
#     l1["phrase2"](name="phrase5"),
#     l1["phrase3"](name="phrase6"),
#     ))

# for e in l1.select["phrase4", "phrase5", "phrase6"].note_events:
#     e.pitch -= 2 

# l1.append(SingLine.phrase0(name="phrase7"))
# l1["phrase7"].events[-1].beats=2

# l1.append(l1["phrase2"](name="phrase8"))
# l1["phrase8"].events[1,3].setattrs(beats=1)


# calliope.Transpose(interval=-9)(l1.select["phrase7", "phrase8"])
# l1["phrase7"].transpose(-9)

# for e in l1.select["phrase7", "phrase8"].note_events:
#     e.pitch -= 9


 # l.events(beats=0.5).setattrs(beats=0.75)
# l.events(beats=1).setattrs(beats=0.25)
# for e in l.events:
#     e.rhythm=(-0.5,0.5)
# l.phrases[0,1,3].setattrs(rhythm = (0.5,1,0.5)*4)
# l.phrases(2).setattrs(rhythm = (0.5,1,0.5)*2 + (0.5,1,1,1,0.5))


# TO DO: create story for turning line into pulsing rhythm in groups
# of 9.

# l = calliope.LineBlock()
# l.extend((l0,l1,l2))

# l2["phrase0"]["sing_cell1"].rhythm=(0.5,0.5,1,0.5,0.5)



# Stutter()(l0.events[5,6,7])