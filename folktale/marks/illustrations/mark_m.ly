\version "2.19.82"
\language "english"

\header {
    tagline = ##f
}

\layout {}

\paper {}

\score {
    <<
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
        {
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
    >>
    \midi {}
}