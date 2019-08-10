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
            }
            \context Staff = "oboe"
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
        \context StaffGroup = "strings"
        <<
            \context Staff = "violin1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
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
        \context StaffGroup = "short_score"
        <<
            \context Staff = "s0"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \set Staff.instrumentName = \markup { "S 0" }
                    \set Staff.shortInstrumentName = \markup { S.0 }
                    r4
                    (
                    <c'' f'' e'''>8
                    [
                    r8
                    ]
                    <a'' bf'' a''' e''''>4
                    )
                    <b' a'' c''' c''''>8
                    [
                    (
                    r8
                    ]
                    <a'' bf'' a''' e''''>4
                    )
                    <b' a'' c''' c''''>8
                    [
                    (
                    r8
                    ]
                    r4
                    )
                    <c'' f'' e'''>4
                    (
                    <b' a'' c''' c''''>4
                    )
                    r4
                    (
                    <a'' bf'' a''' e''''>8
                    [
                    <c'' f'' e'''>8
                    ]
                    r4
                    r2
                    )
                    <b' a'' c''' c''''>8
                    [
                    (
                    r8
                    ]
                    r4
                    )
                    <c'' f'' e'''>4
                    (
                    <b' a'' c''' c''''>4
                    )
                    r4
                    (
                    <a'' bf'' a''' e''''>4
                    r4
                    )
                    <a'' bf'' a''' e''''>4
                    (
                    r2
                    )
                    <c' f' e''>4
                    r4
                    r2
                    r8
                    [
                    <a'' bf'' a''' e''''>8
                    ]
                    r4
                    r8
                    [
                    <a'' bf'' a''' e''''>8
                    ]
                    r4
                    r8
                    [
                    <a'' bf'' a''' e''''>8
                    ]
                    <b' a'' c''' c''''>4
                    r2
                    <a'' bf'' a''' e''''>4
                    (
                    <b' a'' c''' c''''>8
                    [
                    <a'' bf'' a''' e''''>8
                    ]
                    r4
                    r8
                    )
                    [
                    <b' a'' c''' c''''>8
                    ]
                    r4
                    r8
                    [
                    <b'' a''' c'''' c'''''>8
                    ]
                    r2
                    r4
                    <b' a'' c''' c''''>4
                    (
                    r4
                    <b' a'' c''' c''''>8
                    [
                    r8
                    ]
                    r4
                    )
                    <b' a'' c''' c''''>8
                    [
                    r8
                    ]
                    <b' a'' c''' c''''>4
                    (
                    <b' a'' c''' c''''>4
                    )
                    r1
                    r1
                    r2
                    <c'' f'' e'''>4
                    r4
                    r2
                    <c' f' e''>8
                    [
                    (
                    r8
                    ]
                    r4
                    r4
                    )
                    <c''' f''' e''''>4
                    r2
                    r4
                    <c'' f'' e'''>4
                    r4
                    <c'' f'' e'''>4
                    (
                    r2
                    r4
                    )
                    <c'' f'' e'''>4
                    (
                    r1
                    r2
                    r4
                    )
                    <a''' bf''' a'''' e'''''>4
                    <c''' f''' e''''>4
                    (
                    <b'' a''' c'''' c'''''>4
                    )
                }
            }
            \context Staff = "s1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \set Staff.instrumentName = \markup { "S 1" }
                    \set Staff.shortInstrumentName = \markup { S.1 }
                    g'4
                    (
                    c''8
                    [
                    d''8
                    ]
                    a'4
                    )
                    b'8
                    [
                    (
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
                    )
                    c''4
                    (
                    b'4
                    )
                    g'4
                    (
                    a'8
                    [
                    c''8
                    ]
                    g'4
                    )
                    e''8
                    [
                    (
                    d''8
                    ]
                    g'4
                    )
                    b'8
                    [
                    (
                    d'8
                    ]
                    e'4
                    )
                    c''4
                    (
                    b'4
                    )
                    g'4
                    (
                    a'4
                    g'8
                    [
                    e'8
                    ]
                    )
                    a'4
                    (
                    g'8
                    [
                    e'8
                    ]
                    )
                    g'4
                    (
                    c'4
                    )
                    d'4
                    (
                    e'4
                    )
                    g'4
                    (
                    g'8
                    [
                    a'8
                    ]
                    e'4
                    )
                    fs'8
                    [
                    (
                    a'8
                    ]
                    e'4
                    )
                    fs'8
                    [
                    (
                    a'8
                    ]
                    b'4
                    )
                    d''4
                    (
                    cs''4
                    )
                    a'4
                    (
                    b'8
                    [
                    a'8
                    ]
                    e'4
                    )
                    cs'8
                    [
                    (
                    b'8
                    ]
                    e''4
                    )
                    gs''8
                    [
                    (
                    b''8
                    ]
                    cs''4
                    )
                    e''4
                    (
                    ds''4
                    )
                    b'4
                    (
                    cs''4
                    b'8
                    [
                    gs'8
                    ]
                    )
                    cs''4
                    (
                    b'8
                    [
                    gs'8
                    ]
                    )
                    b'4
                    (
                    b'4
                    )
                    cs''4
                    (
                    ds''4
                    )
                    gf''4
                    (
                    gf''8
                    [
                    af''8
                    ]
                    ef''4
                    )
                    f''8
                    [
                    (
                    af''8
                    ]
                    ef''4
                    )
                    f''8
                    [
                    (
                    af''8
                    ]
                    bf''4
                    )
                    df''4
                    (
                    c''4
                    )
                    af'4
                    (
                    bf'8
                    [
                    af'8
                    ]
                    ef'4
                    )
                    c'8
                    [
                    (
                    bf'8
                    ]
                    ef''4
                    )
                    g''8
                    [
                    (
                    bf''8
                    ]
                    c'''4
                    )
                    ef''4
                    (
                    d''4
                    )
                    bf'4
                    (
                    c''4
                    bf'8
                    [
                    g'8
                    ]
                    )
                    c''4
                    (
                    bf'8
                    [
                    g'8
                    ]
                    )
                    bf'4
                    (
                    bf'4
                    )
                    c''4
                    (
                    d''4
                    )
                    f''4
                    (
                    f''8
                    [
                    g''8
                    ]
                    d''4
                    )
                    e''8
                    [
                    (
                    g''8
                    ]
                    d''4
                    )
                    e''8
                    [
                    (
                    g''8
                    ]
                    a''4
                    )
                    c'''4
                    (
                    b''4
                    )
                }
            }
            \context Staff = "s2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    \set Staff.instrumentName = \markup { "S 2" }
                    \set Staff.shortInstrumentName = \markup { S.2 }
                    <g' a' b' c''>1
                    ~
                    <g' a' b' c''>4
                    <d' e' b' c''>4
                    ~
                    <d' e' b' c''>2
                    ~
                    <d' e' b' c''>4
                    <g' g' a' e''>4
                    ~
                    <g' g' a' e''>2
                    ~
                    <g' g' a' e''>2
                    <d' e' b' c''>2
                    ~
                    <d' e' b' c''>2
                    <e' g' a' a'>2
                    ~
                    <e' g' a' a'>2
                    ~
                    <e' g' a' a'>4
                    <c' d' e' g'>4
                    ~
                    <c' d' e' g'>2
                    ~
                    <c' d' e' g'>4
                    <e' fs' g' g'>4
                    ~
                    <e' fs' g' g'>1
                    <a' b' cs'' d''>1
                    <cs' e' a' b'>1
                    ~
                    <cs' e' a' b'>4
                    <cs'' ef'' e'' b''>4
                    ~
                    <cs'' ef'' e'' b''>2
                    ~
                    <cs'' ef'' e'' b''>4
                    <af' b' cs'' cs''>4
                    ~
                    <af' b' cs'' cs''>2
                    ~
                    <af' b' cs'' cs''>2
                    <b' b' cs'' ef''>2
                    ~
                    <b' b' cs'' ef''>2
                    <ef'' f'' fs'' fs''>2
                    ~
                    <ef'' f'' fs'' fs''>2
                    ~
                    <ef'' f'' fs'' fs''>4
                    <c'' cs'' af'' bf''>4
                    ~
                    <c'' cs'' af'' bf''>2
                    ~
                    <c'' cs'' af'' bf''>4
                    <c' ef' af' bf'>4
                    ~
                    <c' ef' af' bf'>1
                    <d'' ef'' bf'' c'''>1
                    <g' bf' c'' c''>1
                    ~
                    <g' bf' c'' c''>4
                    <bf' bf' c'' d''>4
                    ~
                    <bf' bf' c'' d''>2
                    ~
                    <bf' bf' c'' d''>4
                    <d'' e'' f'' f''>4
                    ~
                    <d'' e'' f'' f''>2
                    ~
                    <d'' e'' f'' f''>2
                    <g'' a'' b'' c'''>2
                    ~
                    <g'' a'' b'' c'''>2
                }
            }
            \context Staff = "s3"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
            \context Staff = "s4"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
            }
        >>
    >>
}