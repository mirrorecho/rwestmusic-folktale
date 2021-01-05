import abjad, calliope

from folktale.scores.score import FolktaleScore

from folktale.stories import arranger

from folktale.marks import (
    mark_0, 
    mark_a,
    mark_b,
    mark_c,
    # mark_d,
    # mark_e,
    # mark_f,
    # mark_g,
    # mark_h,
    # mark_i,
    # mark_j,
    # mark_k,
    # mark_l, 
    # mark_m,
    # mark_n,
    # mark_o,
    # mark_p,
    # mark_q,
    # mark_r,
    )


FINAL_SCORE_A = arranger.Arranger.from_arranger_segments(
    mark_0.a,
    mark_a.a,
    # mark_b.a,
    # mark_c.a,
    )


FINAL_SCORE_A.illustrate_me(
    with_short_score=False
    )