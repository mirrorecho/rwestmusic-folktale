import pandas as pd
import calliope

#TO DO... is this even used???

def hill_range(start, steps, increment=1, span=12):
    hill_range = [start + increment*i for i in range(steps)]
    hill_range += reversed(hill_range)
    return [(b, b+span) for b in hill_range]

# TO DO: rething for FOLKTALE
def hill_ranges(steps, span=13):
    return pd.DataFrame.from_records([
                hill_range(5, steps, 2, span), # flute
                hill_range(-4, steps, 2, span), # clarinet
                hill_range(9, steps, -3, span), # viola
                hill_range(-3, steps, -3, span), # cello
            ])


def down_range(start, steps, increment=-2, span=14):
    down_range = [start + increment*i for i in range(steps)]
    return [(b, b+span) for b in down_range]

def down_ranges(steps, span=14):
    return pd.DataFrame.from_records([
                down_range(19, steps, -2, span), # flute
                down_range(19, steps, -2, span), # violin 1
                down_range(19, steps, -2, span), # violin 2
                down_range(12, steps, -1, span), # oboe
                down_range(12, steps, -2, span), # viola
                down_range(1, steps, -2, span), # cello
                down_range(3, steps, -2, span), # bass
            ])

def midhigh_string_ranges():
    return pd.DataFrame.from_records([
                [ (9, 28), ], # violin1
                [ (9, 28), ], # violin2
                [ (2, 21), ], # viola
                [ (-10, 9), ], # cello
                [ (-10, 9), ], # cello/bass
            ])

def mid_string_ranges():
    return pd.DataFrame.from_records([
                [ (9, 23), ], # violin1
                [ (0, 16), ], # violin2
                [ (-6, 14), ], # viola
                [ (-15, 5), ], # cello
                [ (-15, 5), ], # cello/bass
            ])

def midlow_string_ranges():
    return pd.DataFrame.from_records([
                [ (-1, 14), ], # violin1
                [ (-3, 12), ], # violin2
                [ (-8, 7), ], # viola
                [ (-20, -5), ], # cello
                [ (-20, -5), ], # cello/bass
            ])

def low_string_ranges():
    return pd.DataFrame.from_records([
                [ (-5, 8), ], # violin1
                [ (-5, 8), ], # violin2
                [ (-12, 1), ], # viola
                [ (-24, -11), ], # cello
                [ (-20, -8), ], # cello/bass
            ])

def mid_ranges():
    return pd.DataFrame.from_records([
                [ (0, 24), ], 
            ])


def one_octave():
    return pd.DataFrame.from_records([
                [ (0, 12), ], 
            ])


print(down_range(0,12))