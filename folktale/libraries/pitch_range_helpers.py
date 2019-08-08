import pandas as pd
import calliope

#TO DO... is this even used???

def hill_range(start, steps, increment=1, span=12):
    hill_range = [start + increment*i for i in range(steps)]
    hill_range += reversed(hill_range)
    return [(b, b+span) for b in hill_range]

def hill_ranges(steps, span=13):
    return pd.DataFrame.from_records([
                hill_range(5, steps, 2, span), # flute
                hill_range(-4, steps, 2, span), # clarinet
                hill_range(9, steps, -3, span), # viola
                hill_range(-3, steps, -3, span), # cello
            ])

def midhigh_string_ranges():
    return pd.DataFrame.from_records([
                [ (9, 28), ], # violin1
                [ (9, 28), ], # violin2
                [ (2, 21), ], # viola
                [ (-10, 9), ], # cello
            ])

def mid_string_ranges():
    return pd.DataFrame.from_records([
                [ (9, 23), ], # violin1
                [ (0, 16), ], # violin2
                [ (-6, 14), ], # viola
                [ (-15, 5), ], # cello
            ])

def mid_ranges():
    return pd.DataFrame.from_records([
                [ (0, 24), ], 
            ])


def one_octave():
    return pd.DataFrame.from_records([
                [ (0, 12), ], 
            ])