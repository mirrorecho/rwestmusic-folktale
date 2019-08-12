import abjad

import calliope

# TO DO: NOT TOO ELEGANT, but works... 
class Stutter(calliope.Transform):
    times = 1

    def transform(self, selectable, **kwargs):
        last_selectable = selectable[-1]
        my_index = last_selectable.my_index
        my_parent = last_selectable.parent
        
        event_list = list(selectable.events)

        for j in range(self.times):
            for i, event in enumerate(event_list):
                my_parent.insert(my_index+i+1, event())
