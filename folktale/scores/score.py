import abjad
import calliope

class FolktaleScore(calliope.Score):
    stylesheets=("../../stylesheets/score.ily",)

    class Strings(calliope.StaffGroup):
        class Violin1(calliope.Staff):
            instrument=abjad.Violin(
                name="Violin 1", short_name="vln.1")

        class Violin2(calliope.Staff):
            instrument=abjad.Violin(
                name="Violin 2", short_name="vln.2")

        class Viola(calliope.Staff):
            instrument=abjad.Viola(
                name="Viola", short_name="vla.")

        class Cello(calliope.Staff):
            instrument=abjad.Cello(
                name="Cello", short_name="vc.")
            clef="bass"

        class Bass(calliope.Staff):
            instrument=abjad.Cello(
                name="Bass", short_name="vc.")
            clef="bass"

    class Harp(calliope.Harp): pass
        # instrument=abjad.Harp(
        #     name="Bass", short_name="vc.")
        # clef="bass"

    class Piano(calliope.Piano): pass
        # instrument=abjad.Piano(
        #     name="Bass", short_name="vc.")
        # clef="bass"