import abjad, calliope

from folktale.scores.score import FolktaleScore
from folktale.stories.clang import ClangStory

from folktale.marks.mark_0 import get_score

f = get_score()

f.illustrate_me(
    as_midi=True,
    )