\version "2.19.82"
\language "english"

\header {
    tagline = ##f
}

\layout {}

\paper {}

\score {
    \new StaffGroup
    <<
        \new Staff
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            {
                g'4
                ^ \markup { 0 }
                (
                c''8
                [
                d''8
                ]
                a'4
                b'8
                ^ \markup { 1 }
                [
                d''8
                ]
                a'4
                b'8
                ^ \markup { 2 }
                [
                d'8
                ]
                e'4
                c''4
                ^ \markup { 3 }
                b'4
                )
                g'4
                ^ \markup { 4 }
                (
                a'8
                [
                c''8
                ]
                g'4
                e''8
                ^ \markup { 5 }
                [
                d''8
                ]
                g'4
                b'8
                ^ \markup { 6 }
                [
                d'8
                ]
                e'4
                c''4
                ^ \markup { 7 }
                b'4
                )
                g'4
                ^ \markup { 8 }
                (
                a'4
                g'8
                [
                e'8
                ]
                a'4
                ^ \markup { 9 }
                g'8
                [
                e'8
                ]
                g'4
                ^ \markup { 10 }
                c'4
                d'4
                ^ \markup { 11 }
                e'4
                )
                g'4
                ^ \markup { 12 }
                (
                c''8
                [
                d''8
                ]
                a'4
                b'8
                ^ \markup { 13 }
                [
                d''8
                ]
                a'4
                b'8
                ^ \markup { 14 }
                [
                d'8
                ]
                e'4
                c''4
                ^ \markup { 15 }
                b'4
                )
            }
        }
        \new Staff
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            {
                \clef "bass"
                g2
                ^ \markup { 0 }
                (
                fs4
                g4
                fs4
                g4
                ~
                g8
                [
                c8
                ~
                ]
                c4
                d4
                e4
                )
                fs8
                ^ \markup { 1 }
                [
                (
                a8
                ~
                ]
                a8
                [
                b8
                ]
                c'4
                ~
                c'8
                [
                b8
                ]
                g8
                [
                fs8
                ~
                ]
                fs8
                [
                e8
                ~
                ]
                e4
                )
                g4
                ^ \markup { 2 }
                ~
                (
                g4
                fs4
                g4
                fs4
                g4
                ~
                g8
                [
                c8
                ~
                ]
                c4
                b,4
                c2
                ~
                c4
                )
                fs4
                ^ \markup { 3 }
                (
                g4
                fs4
                g2
                e2
                )
            }
        }
        \new Staff
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            {
                \clef "bass"
                c'2
                ~
                (
                c'4
                b4
                ~
                b2
                c'2
                ~
                c'4
                d'4
                ~
                d'2
                )
                c'1
                (
                b1
                c'1
                b1
                c'1
                b1
                )
            }
        }
        \new Staff
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            {
                \clef "bass"
                r4
                (
                a,4
                ~
                a,4
                r4
                g,2
                r4
                a,4
                ~
                a,4
                r4
                b,2
                )
                r4
                (
                a,4
                ~
                a,2
                r4
                g,4
                ~
                g,2
                r4
                a,4
                ~
                a,2
                r4
                g,4
                ~
                g,2
                r4
                a,4
                ~
                a,2
                r4
                g,4
                ~
                g,2
                )
            }
        }
    >>
    \midi {}
}