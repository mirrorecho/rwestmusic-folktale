\version "2.19.82"
\language "english"

\include "../../stylesheets/score.ily"

\header {
    tagline = ##f
}

\layout {}

\paper {}

\score {
    \new Score
    <<
        \context StaffGroup = "winds"
        <<
            \context Staff = "flute"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { Flute }
                        \set Staff.shortInstrumentName = \markup { Fl. }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "oboe"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { Oboe }
                        \set Staff.shortInstrumentName = \markup { Ob. }
                        \mark #14
                        R1 * 16
                    }
                }
            }
        >>
        \context PianoStaff = "piano"
        <<
            \context Staff = "piano1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { Piano }
                        \set Staff.shortInstrumentName = \markup { Pf. }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "piano2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { Piano }
                        \set Staff.shortInstrumentName = \markup { Pf. }
                        \mark #14
                        \clef "bass"
                        R1 * 16
                    }
                }
            }
        >>
        \context StaffGroup = "strings"
        <<
            \context Staff = "violin1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \accidentalStyle modern-cautionary
                    \set Staff.instrumentName = \markup { "Violin 1" }
                    \set Staff.shortInstrumentName = \markup { Vln.1 }
                    \mark #14
                    <d''>2
                    ~
                    <d''>4
                    <e''>4
                    ~
                    <e''>4
                    <cs''>4
                    ~
                    <cs''>4
                    d''4
                    ~
                    d''4
                    <a'>4
                    ~
                    <a'>2
                    <a'>2
                    <e'>2
                    d'2
                    <b'>2
                    ~
                    <b'>4
                    <cs''>4
                    ~
                    <cs''>4
                    <b'>4
                    ~
                    <b'>4
                    fs'4
                    ~
                    fs'4
                    <e''>4
                    ~
                    <e''>2
                    <fs''>2
                    <ds''>2
                    e''2
                    <e''>2
                    ~
                    <e''>4
                    <gs''>4
                    ~
                    <gs''>4
                    <ds''>4
                    ~
                    <ds''>4
                    e''4
                    ~
                    e''4
                    <b'>4
                    ~
                    <b'>2
                    <cs''>2
                    <b'>2
                    fs'2
                    <e''>2
                    ~
                    <e''>4
                    <fs''>4
                    ~
                    <fs''>4
                    <ds''>4
                    ~
                    <ds''>4
                    e''4
                    ~
                    e''4
                    r4
                }
            }
            \context Staff = "violin2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \accidentalStyle modern-cautionary
                    \set Staff.instrumentName = \markup { "Violin 2" }
                    \set Staff.shortInstrumentName = \markup { Vln.2 }
                    \mark #14
                    <a'>2
                    ~
                    <a'>4
                    <cs''>4
                    ~
                    <cs''>4
                    <e'>4
                    ~
                    <e'>4
                    d''4
                    ~
                    d''4
                    <d'>4
                    ~
                    <d'>2
                    <fs'>2
                    <cs'>2
                    d'2
                    <gs'>2
                    ~
                    <gs'>4
                    <gs'>4
                    ~
                    <gs'>4
                    <e'>4
                    ~
                    <e'>4
                    fs'4
                    ~
                    fs'4
                    <b'>4
                    ~
                    <b'>2
                    <ds''>2
                    <fs'>2
                    e''2
                    <b'>2
                    ~
                    <b'>4
                    <b'>4
                    ~
                    <b'>4
                    <fs'>4
                    ~
                    <fs'>4
                    e''4
                    ~
                    e''4
                    <gs'>4
                    ~
                    <gs'>2
                    <gs'>2
                    <e'>2
                    fs'2
                    <b'>2
                    ~
                    <b'>4
                    <ds''>4
                    ~
                    <ds''>4
                    <fs'>4
                    ~
                    <fs'>4
                    e''4
                    ~
                    e''4
                    r4
                }
            }
            \context Staff = "viola"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \accidentalStyle modern-cautionary
                    \set Staff.instrumentName = \markup { Viola }
                    \set Staff.shortInstrumentName = \markup { Vla. }
                    \mark #14
                    a4
                    d'8
                    [
                    e'8
                    ]
                    b4
                    cs'8
                    [
                    e'8
                    ]
                    b4
                    cs'8
                    [
                    e8
                    ]
                    fs4
                    d'4
                    cs'4
                    a4
                    b8
                    [
                    d8
                    ]
                    a4
                    fs8
                    [
                    e8
                    ]
                    a4
                    cs8
                    [
                    e8
                    ]
                    fs4
                    d4
                    cs4
                    b4
                    cs'4
                    b8
                    [
                    gs8
                    ]
                    cs'4
                    b8
                    [
                    gs8
                    ]
                    b4
                    e4
                    fs4
                    gs4
                    b4
                    e'8
                    [
                    fs'8
                    ]
                    cs'4
                    ds'8
                    [
                    fs'8
                    ]
                    cs'4
                    ds'8
                    [
                    fs8
                    ]
                    gs4
                    e'4
                    ds'4
                    b4
                    cs'8
                    [
                    e'8
                    ]
                    b4
                    gs'8
                    [
                    fs'8
                    ]
                    b4
                    ds'8
                    [
                    fs8
                    ]
                    gs4
                    e'4
                    ds'4
                    b4
                    cs'4
                    b8
                    [
                    gs8
                    ]
                    cs'4
                    b8
                    [
                    gs8
                    ]
                    b4
                    e4
                    fs4
                    gs4
                    b4
                    e'8
                    [
                    fs'8
                    ]
                    cs'4
                    ds'8
                    [
                    fs'8
                    ]
                    cs'4
                    ds'8
                    [
                    fs8
                    ]
                    gs4
                    e'4
                    ds'4
                    r4
                }
            }
            \context Staff = "cello"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { Cello }
                        \set Staff.shortInstrumentName = \markup { Vc. }
                        \mark #14
                        \clef "bass"
                        R1 * 6
                    }
                    r2
                    r4
                    b,4
                    ~
                    b,4
                    as,4
                    b,4
                    as,4
                    b,4
                    ~
                    b,8
                    [
                    e,8
                    ~
                    ]
                    e,4
                    fs,4
                    gs,4
                    as,8
                    [
                    cs8
                    ~
                    ]
                    cs8
                    [
                    ds8
                    ]
                    e4
                    ~
                    e8
                    [
                    ds8
                    ]
                    b,8
                    [
                    as,8
                    ~
                    ]
                    as,8
                    [
                    gs,8
                    ~
                    ]
                    gs,4
                    b,2
                    as,4
                    b,4
                    as,4
                    b,4
                    ~
                    b,8
                    [
                    e,8
                    ~
                    ]
                    e,4
                    ds,4
                    e,4
                    ~
                    e,2
                    as,4
                    b,4
                    as,4
                    b,4
                    ~
                    b,4
                    gs,4
                    ~
                    gs,4
                    r4
                }
            }
            \context Staff = "bass"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { Bass }
                        \set Staff.shortInstrumentName = \markup { Cb. }
                        \mark #14
                        \clef "bass"
                        R1 * 16
                    }
                }
            }
        >>
        \context StaffGroup = "short_score"
        <<
            \context Staff = "s0"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \accidentalStyle modern-cautionary
                    \set Staff.instrumentName = \markup { "S 0" }
                    \set Staff.shortInstrumentName = \markup { S.0 }
                    \mark #14
                    a'4
                    ^ \markup { 0 }
                    (
                    d''8
                    [
                    e''8
                    ]
                    b'4
                    cs''8
                    ^ \markup { 1 }
                    [
                    e''8
                    ]
                    b'4
                    cs''8
                    ^ \markup { 2 }
                    [
                    e'8
                    ]
                    fs'4
                    d''4
                    ^ \markup { 3 }
                    cs''4
                    )
                    a'4
                    ^ \markup { 4 }
                    (
                    b'8
                    [
                    d'8
                    ]
                    a'4
                    fs'8
                    ^ \markup { 5 }
                    [
                    e'8
                    ]
                    a'4
                    cs'8
                    ^ \markup { 6 }
                    [
                    e'8
                    ]
                    fs'4
                    d'4
                    ^ \markup { 7 }
                    cs'4
                    )
                    b'4
                    ^ \markup { 8 }
                    (
                    cs''4
                    b'8
                    [
                    gs'8
                    ]
                    cs''4
                    ^ \markup { 9 }
                    b'8
                    [
                    gs'8
                    ]
                    b'4
                    ^ \markup { 10 }
                    e'4
                    fs'4
                    ^ \markup { 11 }
                    gs'4
                    )
                    b'4
                    ^ \markup { 12 }
                    (
                    e''8
                    [
                    fs''8
                    ]
                    cs''4
                    ds''8
                    ^ \markup { 13 }
                    [
                    fs''8
                    ]
                    cs''4
                    ds''8
                    ^ \markup { 14 }
                    [
                    fs'8
                    ]
                    gs'4
                    e''4
                    ^ \markup { 15 }
                    ds''4
                    )
                    b'4
                    ^ \markup { 16 }
                    (
                    cs''8
                    [
                    e''8
                    ]
                    b'4
                    gs''8
                    ^ \markup { 17 }
                    [
                    fs''8
                    ]
                    b'4
                    ds''8
                    ^ \markup { 18 }
                    [
                    fs'8
                    ]
                    gs'4
                    e''4
                    ^ \markup { 19 }
                    ds''4
                    )
                    b'4
                    ^ \markup { 20 }
                    (
                    cs''4
                    b'8
                    [
                    gs'8
                    ]
                    cs''4
                    ^ \markup { 21 }
                    b'8
                    [
                    gs'8
                    ]
                    b'4
                    ^ \markup { 22 }
                    e'4
                    fs'4
                    ^ \markup { 23 }
                    gs'4
                    )
                    b'4
                    ^ \markup { 24 }
                    (
                    e''8
                    [
                    fs''8
                    ]
                    cs''4
                    ds''8
                    ^ \markup { 25 }
                    [
                    fs''8
                    ]
                    cs''4
                    ds''8
                    ^ \markup { 26 }
                    [
                    fs'8
                    ]
                    gs'4
                    e''4
                    ^ \markup { 27 }
                    ds''4
                    )
                    r4
                }
            }
            \context Staff = "s1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 1" }
                        \set Staff.shortInstrumentName = \markup { S.1 }
                        \mark #14
                        R1 * 6
                    }
                    r2
                    r4
                    b4
                    ^ \markup { 1 }
                    ~
                    (
                    b4
                    as4
                    )
                    b4
                    ^ \markup { 2 }
                    (
                    as4
                    )
                    b4
                    ^ \markup { 3 }
                    ~
                    (
                    b8
                    [
                    e8
                    ~
                    ]
                    e4
                    )
                    fs4
                    ^ \markup { 4 }
                    (
                    gs4
                    )
                    as8
                    ^ \markup { 5 }
                    [
                    (
                    cs'8
                    ~
                    ]
                    cs'8
                    [
                    ds'8
                    ]
                    )
                    e'4
                    ^ \markup { 6 }
                    ~
                    (
                    e'8
                    [
                    ds'8
                    ]
                    )
                    b8
                    ^ \markup { 7 }
                    [
                    (
                    as8
                    ~
                    ]
                    as8
                    )
                    [
                    gs8
                    ^ \markup { 8 }
                    ~
                    ]
                    gs4
                    b2
                    ^ \markup { 9 }
                    (
                    as4
                    )
                    b4
                    ^ \markup { 10 }
                    (
                    as4
                    )
                    b4
                    ^ \markup { 11 }
                    ~
                    (
                    b8
                    [
                    e8
                    ~
                    ]
                    e4
                    )
                    ds4
                    ^ \markup { 12 }
                    (
                    e4
                    ~
                    e2
                    )
                    as4
                    ^ \markup { 13 }
                    b4
                    ^ \markup { 14 }
                    (
                    as4
                    )
                    b4
                    ^ \markup { 15 }
                    ~
                    (
                    b4
                    gs4
                    ~
                    gs4
                    )
                    r4
                }
            }
            \context Staff = "s2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \accidentalStyle modern-cautionary
                    \set Staff.instrumentName = \markup { "S 2" }
                    \set Staff.shortInstrumentName = \markup { S.2 }
                    \mark #14
                    <a' d''>2
                    ^ \markup { 0 }
                    ~
                    <a' d''>4
                    <cs'' e''>4
                    ^ \markup { 1 }
                    ~
                    <cs'' e''>4
                    <e' cs''>4
                    ^ \markup { 2 }
                    ~
                    <e' cs''>4
                    d''4
                    ^ \markup { 3 }
                    ~
                    d''4
                    <d' a'>4
                    ^ \markup { 4 }
                    ~
                    <d' a'>2
                    <fs' a'>2
                    ^ \markup { 5 }
                    <cs' e'>2
                    ^ \markup { 6 }
                    d'2
                    ^ \markup { 7 }
                    <gs' b'>2
                    ^ \markup { 8 }
                    ~
                    <gs' b'>4
                    <gs' cs''>4
                    ^ \markup { 9 }
                    ~
                    <gs' cs''>4
                    <e' b'>4
                    ^ \markup { 10 }
                    ~
                    <e' b'>4
                    fs'4
                    ^ \markup { 11 }
                    ~
                    fs'4
                    <b' e''>4
                    ^ \markup { 12 }
                    ~
                    <b' e''>2
                    <ds'' fs''>2
                    ^ \markup { 13 }
                    <fs' ds''>2
                    ^ \markup { 14 }
                    e''2
                    ^ \markup { 15 }
                    <b' e''>2
                    ^ \markup { 16 }
                    ~
                    <b' e''>4
                    <b' gs''>4
                    ^ \markup { 17 }
                    ~
                    <b' gs''>4
                    <fs' ds''>4
                    ^ \markup { 18 }
                    ~
                    <fs' ds''>4
                    e''4
                    ^ \markup { 19 }
                    ~
                    e''4
                    <gs' b'>4
                    ^ \markup { 20 }
                    ~
                    <gs' b'>2
                    <gs' cs''>2
                    ^ \markup { 21 }
                    <e' b'>2
                    ^ \markup { 22 }
                    fs'2
                    ^ \markup { 23 }
                    <b' e''>2
                    ^ \markup { 24 }
                    ~
                    <b' e''>4
                    <ds'' fs''>4
                    ^ \markup { 25 }
                    ~
                    <ds'' fs''>4
                    <fs' ds''>4
                    ^ \markup { 26 }
                    ~
                    <fs' ds''>4
                    e''4
                    ^ \markup { 27 }
                    ~
                    e''4
                    r4
                }
            }
            \context Staff = "s3"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 3" }
                        \set Staff.shortInstrumentName = \markup { S.3 }
                        \mark #14
                        R1 * 6
                    }
                    r2
                    r4
                    b4
                    ~
                    b2
                    b2
                    <e b>2
                    ~
                    <e b>4
                    fs4
                    ~
                    fs4
                    <as cs'>4
                    ~
                    <as cs'>4
                    e'4
                    ~
                    e'4
                    b4
                    ~
                    b8
                    [
                    gs8
                    ~
                    ]
                    gs4
                    b2
                    ~
                    b4
                    b4
                    ~
                    b4
                    <e b>4
                    ~
                    <e b>2
                    ds1
                    as4
                    b4
                    ~
                    b4
                    <gs b>4
                    ~
                    <gs b>2
                    ~
                    <gs b>4
                    r4
                }
            }
            \context Staff = "s4"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 4" }
                        \set Staff.shortInstrumentName = \markup { S.4 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s5"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 5" }
                        \set Staff.shortInstrumentName = \markup { S.5 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s6"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 6" }
                        \set Staff.shortInstrumentName = \markup { S.6 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s7"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 7" }
                        \set Staff.shortInstrumentName = \markup { S.7 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s8"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 8" }
                        \set Staff.shortInstrumentName = \markup { S.8 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s9"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 9" }
                        \set Staff.shortInstrumentName = \markup { S.9 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s10"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 10" }
                        \set Staff.shortInstrumentName = \markup { S.10 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s11"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 11" }
                        \set Staff.shortInstrumentName = \markup { S.11 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s12"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 12" }
                        \set Staff.shortInstrumentName = \markup { S.12 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s13"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 13" }
                        \set Staff.shortInstrumentName = \markup { S.13 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s14"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 14" }
                        \set Staff.shortInstrumentName = \markup { S.14 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
            \context Staff = "s15"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    {
                        \accidentalStyle modern-cautionary
                        \set Staff.instrumentName = \markup { "S 15" }
                        \set Staff.shortInstrumentName = \markup { S.15 }
                        \mark #14
                        R1 * 16
                    }
                }
            }
        >>
    >>
    \midi {}
}