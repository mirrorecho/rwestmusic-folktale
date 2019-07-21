import abjad, calliope

LINE_SMOOTH_TALLY_APPS = (
    calliope.TallyCircleOfFifthsRange(over_range_multiplier=-120), 
    calliope.TallyParallelIntervals(interval_ratings=[(0,-60), (7,-20)]), 
    calliope.TallyMelodicIntervals(
            interval_ratings=[(0, -100), (1,80), (2,110), (3,80), (4,20), (6,-40), (8,-40), (9,-40), (10,-40), (11,-50), (12,-9)], 
            over_incremental_multiplier=(12,-120),
            # up_rating=20,
            # down_rating=-9,
            ),
    calliope.TallyRepeatedJumps(),
    )


LINE_SMOOTH_TALLY_APPS2 = (
    calliope.TallyCircleOfFifthsRange(over_range_multiplier=-120), 
    calliope.TallyParallelIntervals(interval_ratings=[(0,-60), (7,-20)]), 
    calliope.TallyMelodicIntervals(
            interval_ratings=[(0, -100), (1,80), (2,110), (3,80), (4,20), (6,-40), (8,-40), (9,-40), (10,-40)], 
            up_rating=20,
            down_rating=-9,
            ),
    calliope.TallyRepeatedJumps(),
    )