import abjad, calliope

from folktale.scores.score import FolktaleScore
from folktale.stories.clang import ClangStory

clang_lb = ClangStory().tell()

f = FolktaleScore()

f.staves["s1"].append(clang_lb[0]())
f.staves["s2"].append(clang_lb[1]())

f.illustrate_me()