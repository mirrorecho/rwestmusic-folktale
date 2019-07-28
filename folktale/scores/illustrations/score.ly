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
        \context StaffGroup = "strings"
        <<
            \context Staff = "violin1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    d''4
                    (
                    c''8
                    [
                    d''8
                    ]
                    a'4
                    e''8
                    [
                    d''8
                    ]
                    a'4
                    )
                    e''8
                    [
                    (
                    d''8
                    ]
                    a'4
                    c''4
                    b'4
                    )
                    d''4
                    (
                    a'8
                    [
                    c''8
                    ]
                    d''4
                    e''8
                    [
                    a'8
                    ]
                    c''4
                    )
                    e''8
                    [
                    (
                    d''8
                    ]
                    a'4
                    c''4
                    b'4
                    )
                    g'4
                    (
                    a'4
                    g'8
                    [
                    e'8
                    ]
                    a'4
                    g'8
                    [
                    e'8
                    ]
                    )
                    g'4
                    (
                    c'4
                    d'4
                    e'4
                    )
                    g'4
                    (
                    c''8
                    [
                    d''8
                    ]
                    a'4
                    b'8
                    [
                    d''8
                    ]
                    a'4
                    )
                    b'8
                    [
                    (
                    d'8
                    ]
                    e'4
                    c''4
                    b'4
                    )
                }
            }
            \context Staff = "violin2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
            \context Staff = "viola"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
            \context Staff = "cello"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
            \context Staff = "bass"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
        >>
        \context PianoStaff = "harp"
        <<
            \context Staff = "harp1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
            \context Staff = "harp2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
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
            }
            \context Staff = "piano2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
        >>
    >>
}