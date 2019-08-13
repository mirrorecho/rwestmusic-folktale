import abjad
import calliope

class FolktaleScore(calliope.Score):
    stylesheets=("../../stylesheets/score.ily",)

    class Winds(calliope.StaffGroup):
        class Flute(calliope.Staff):
            instrument=abjad.Flute(
                name="Flute", short_name="fl.")

        class Oboe(calliope.Staff):
            instrument=abjad.Oboe(
                name="Oboe", short_name="ob.")

    class Piano(calliope.Piano): pass
        # instrument=abjad.Piano(
        #     name="Bass", short_name="vc.")
        # clef="bass"

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
                name="Bass", short_name="cb.")
            clef="bass"

    class ShortScore(calliope.StaffGroup):
        class S0(calliope.Staff):
            instrument=abjad.Instrument(
                name="S 0", short_name="s.0")
        class S1(calliope.Staff):
            instrument=abjad.Instrument(
                name="S 1", short_name="s.1")
        class S2(calliope.Staff):
            instrument=abjad.Piano(
                name="S 2", short_name="s.2")
        class S3(calliope.Staff):
            instrument=abjad.Piano(
                name="S 3", short_name="s.3")
        class S4(calliope.Staff):
            instrument=abjad.Piano(
                name="S 4", short_name="s.4")
        class S5(calliope.Staff):
            instrument=abjad.Piano(
                name="S 5", short_name="s.5")
        class S6(calliope.Staff):
            instrument=abjad.Piano(
                name="S 6", short_name="s.6")
        class S7(calliope.Staff):
            instrument=abjad.Piano(
                name="S 7", short_name="s.7")
        class S8(calliope.Staff):
            instrument=abjad.Piano(
                name="S 8", short_name="s.8")
        class S9(calliope.Staff):
            instrument=abjad.Piano(
                name="S 9", short_name="s.9")
        class S10(calliope.Staff):
            instrument=abjad.Piano(
                name="S 10", short_name="s.10")
        class S11(calliope.Staff):
            instrument=abjad.Piano(
                name="S 11", short_name="s.11")
        class S12(calliope.Staff):
            instrument=abjad.Piano(
                name="S 12", short_name="s.12")
        class S13(calliope.Staff):
            instrument=abjad.Piano(
                name="S 13", short_name="s.13")
        class S14(calliope.Staff):
            instrument=abjad.Piano(
                name="S 14", short_name="s.14")
        class S15(calliope.Staff):
            instrument=abjad.Piano(
                name="S 15", short_name="s.15")



