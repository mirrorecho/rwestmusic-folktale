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
            g'8
            ]
            d'4
            b'8
            [
            a'8
            ]
            d'4
            fs'8
            [
            a'8
            ]
            b'4
            d'4
            cs'4
            )
            a'4
            ^ \markup { 2 }
            (
            b'4
            a'8
            [
            fs'8
            ]
            b'4
            a'8
            [
            fs'8
            ]
            a'4
            d'4
            e'4
            fs'4
            )
            a'4
            ^ \markup { 3 }
            (
            d''8
            [
            e''8
            ]
            b'4
            cs''8
            [
            e''8
            ]
            b'4
            cs''8
            [
            e'8
            ]
            fs'4
            d''4
            cs''4
            )
            a'4
            ^ \markup { 4 }
            (
            b'8
            [
            d''8
            ]
            a'4
            fs''8
            [
            e''8
            ]
            a'4
            cs''8
            [
            e'8
            ]
            fs'4
            d''4
            cs''4
            )
            a'4
            ^ \markup { 5 }
            (
            b'4
            a'8
            [
            fs'8
            ]
            b'4
            a'8
            [
            fs'8
            ]
            a'4
            d'4
            e'4
            fs'4
            )
            a'4
            ^ \markup { 6 }
            (
            d''8
            [
            e''8
            ]
            b'4
            cs''8
            [
            e''8
            ]
            b'4
            cs''8
            [
            e'8
            ]
            fs'4
            d''4
            cs''4
            )
        }
        {
            r1
            ^ \markup { 0 }
            r1
            r1
            r1
            r1
            r1
            r2
            r4
            a4
            ^ \markup { 1 }
            ~
            (
            a4
            gs4
            a4
            gs4
            a4
            ~
            a8
            [
            d8
            ~
            ]
            d4
            e4
            fs4
            )
            gs8
            ^ \markup { 2 }
            [
            (
            b8
            ~
            ]
            b8
            [
            cs'8
            ]
            d'4
            ~
            d'8
            [
            cs'8
            ]
            a8
            [
            gs8
            ~
            ]
            gs8
            [
            fs8
            ~
            ]
            fs4
            )
            a2
            ^ \markup { 3 }
            (
            gs4
            a4
            gs4
            a4
            ~
            a8
            [
            d8
            ~
            ]
            d4
            cs4
            d4
            ~
            d2
            )
            gs4
            ^ \markup { 4 }
            (
            a4
            gs4
            a4
            ~
            a4
            fs4
            ~
            fs4
            )
        }
        {
            <g' c''>2
            ~
            (
            <g' c''>4
            <b' d''>4
            ~
            <b' d''>4
            <d' b'>4
            ~
            <d' b'>4
            c''4
            ~
            c''4
            )
            <d' g'>4
            ~
            (
            <d' g'>2
            <d' b'>2
            <fs' a'>2
            d'2
            )
            <fs' a'>2
            ~
            (
            <fs' a'>4
            <fs' b'>4
            ~
            <fs' b'>4
            <d' a'>4
            ~
            <d' a'>4
            e'4
            ~
            e'4
            )
            <a' d''>4
            ~
            (
            <a' d''>2
            <cs'' e''>2
            <e' cs''>2
            d''2
            )
            <a' d''>2
            ~
            (
            <a' d''>4
            <a' fs''>4
            ~
            <a' fs''>4
            <e' cs''>4
            ~
            <e' cs''>4
            d''4
            ~
            d''4
            )
            <fs' a'>4
            ~
            (
            <fs' a'>2
            <fs' b'>2
            <d' a'>2
            e'2
            )
            <a' d''>2
            ~
            (
            <a' d''>4
            <cs'' e''>4
            ~
            <cs'' e''>4
            <e' cs''>4
            ~
            <e' cs''>4
            d''4
            ~
            d''4
            )
        }
    >>
    \midi {}
}