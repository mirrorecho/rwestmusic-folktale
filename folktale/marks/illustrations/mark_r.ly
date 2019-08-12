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
                [
                d''8
                ]
                a'4
                b'8
                [
                d'8
                ]
                e'4
                c''4
                b'4
                )
                g'4
                ^ \markup { 1 }
                (
                a'8
                [
                c''8
                ]
                g'4
                e''8
                [
                d''8
                ]
                g'4
                b'8
                [
                d'8
                ]
                e'4
                c''4
                b'4
                )
                g'4
                ^ \markup { 2 }
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
                g'4
                c'4
                d'4
                e'4
                )
                g'4
                ^ \markup { 3 }
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
                b'8
                [
                d'8
                ]
                e'4
                c''4
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
                f4
                g4
                f4
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
                f8
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
                f8
                ~
                ]
                f8
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
                f4
                g4
                f4
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
                f4
                ^ \markup { 3 }
                (
                g4
                f4
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
                r1
                ^ \markup { 0 }
                r1
                f2
                ^ \markup { 1 }
                ~
                (
                f4
                e4
                ~
                e2
                f2
                ^ \markup { 2 }
                ~
                f4
                g4
                ~
                g2
                )
                e1
                ^ \markup { 3 }
                (
                e1
                f1
                ^ \markup { 4 }
                e1
                f1
                ^ \markup { 5 }
                e1
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
                r1
                r1
                r4
                d,4
                ~
                d,4
                r4
                c,2
                r4
                d,4
                ~
                d,4
                r4
                e,2
                r4
                (
                c,4
                ~
                c,2
                r2
                c,2
                r4
                d,4
                ~
                d,2
                r4
                c,4
                ~
                c,2
                r4
                d,4
                ~
                d,2
                r4
                c,4
                ~
                c,2
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
                f2
                ^ \markup { 0 }
                ~
                (
                f4
                e4
                ~
                e2
                f2
                ^ \markup { 1 }
                ~
                f4
                g4
                ~
                g2
                )
                f1
                ^ \markup { 2 }
                (
                e1
                e1
                ^ \markup { 3 }
                e1
                f1
                ^ \markup { 4 }
                e1
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
                d,4
                ~
                d,4
                r4
                c,2
                r4
                d,4
                ~
                d,4
                r4
                e,2
                )
                r4
                (
                d,4
                ~
                d,2
                r4
                c,4
                ~
                c,2
                r4
                c,4
                ~
                c,2
                r2
                c,2
                r4
                d,4
                ~
                d,2
                r4
                c,4
                ~
                c,2
                )
            }
        }
    >>
    \midi {}
}