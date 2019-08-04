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
            \context Staff = "s1"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
                    <fs'' g'' e''' e''''>4
                    (
                    <c'' b'' a'''>8
                    [
                    r8
                    ]
                    r4
                    <b' fs'' c''' b'''>8
                    [
                    r8
                    ]
                    r4
                    )
                    <b' fs'' c''' b'''>8
                    [
                    (
                    r8
                    ]
                    r4
                    <c'' b'' a'''>4
                    <b' fs'' c''' b'''>4
                    )
                    <fs'' g'' e''' e''''>4
                    (
                    r8
                    [
                    <c'' b'' a'''>8
                    ]
                    <fs'' g'' e''' e''''>4
                    r4
                    <fs'' g'' e''' e''''>4
                    )
                    <b' fs'' c''' b'''>8
                    [
                    (
                    r8
                    ]
                    r4
                    <c'' b'' a'''>4
                    <b' fs'' c''' b'''>4
                    )
                    <fs'' g'' e''' e''''>4
                    (
                    r4
                    <fs'' g'' e''' e''''>8
                    [
                    r8
                    ]
                    r4
                    <fs'' g'' e''' e''''>8
                    [
                    r8
                    ]
                    )
                    <fs'' g'' e''' e''''>4
                    (
                    <c' b' a''>4
                    r4
                    r4
                    )
                    <fs'' g'' e''' e''''>4
                    (
                    <c'' b'' a'''>8
                    [
                    r8
                    ]
                    r4
                    <b' fs'' c''' b'''>8
                    [
                    r8
                    ]
                    r4
                    )
                    <b' fs'' c''' b'''>8
                    [
                    (
                    r8
                    ]
                    r4
                    <c'' b'' a'''>4
                    <b' fs'' c''' b'''>4
                    )
                    <fs'' g'' e''' e''''>4
                    (
                    <fs'' g'' e''' e''''>8
                    [
                    r8
                    ]
                    r2
                    r2
                    )
                    <b' fs'' c''' b'''>4
                    r4
                    r2
                    <b' fs'' c''' b'''>8
                    [
                    r8
                    ]
                    r4
                    r8
                    [
                    <b' fs'' c''' b'''>8
                    ]
                    r4
                    r8
                    [
                    <b'' fs''' c'''' b''''>8
                    ]
                    r4
                    r2
                    <b' fs'' c''' b'''>4
                    (
                    r4
                    <b' fs'' c''' b'''>8
                    [
                    r8
                    ]
                    r4
                    <b' fs'' c''' b'''>8
                    [
                    r8
                    ]
                    )
                    <b' fs'' c''' b'''>4
                    (
                    <b' fs'' c''' b'''>4
                    r4
                    r2
                    r1
                    r2
                    r4
                    )
                    <c'' b'' a'''>4
                    r2
                    (
                    r4
                    <c' b' a''>8
                    [
                    r8
                    ]
                    r4
                    )
                    <fs''' g''' e'''' e'''''>8
                    [
                    (
                    r8
                    ]
                    <c''' b''' a''''>4
                    r4
                    r2
                    )
                    <c'' b'' a'''>4
                    r8
                    [
                    <fs'' g'' e''' e''''>8
                    ]
                    <c'' b'' a'''>4
                    r8
                    [
                    <fs'' g'' e''' e''''>8
                    ]
                    r2
                    (
                    <c'' b'' a'''>4
                    r4
                    r4
                    r8
                    )
                    [
                    <fs''' g''' e'''' e'''''>8
                    ]
                    r4
                    r8
                    [
                    <fs''' g''' e'''' e'''''>8
                    ]
                    r4
                    r8
                    [
                    <fs''' g''' e'''' e'''''>8
                    ]
                    r4
                    <c''' b''' a''''>4
                    <b'' fs''' c'''' b''''>4
                }
            }
            \context Staff = "s2"
            \with
            {
                \consists Horizontal_bracket_engraver
            }
            {
                {
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
                    g'4
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
                    g'4
                    (
                    g'8
                    [
                    a'8
                    ]
                    e'4
                    fs'8
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
                    b'4
                    d''4
                    cs''4
                    )
                    a'4
                    (
                    b'8
                    [
                    a'8
                    ]
                    e'4
                    cs'8
                    [
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
                    e''4
                    ds''4
                    )
                    b'4
                    (
                    cs''4
                    b'8
                    [
                    gs'8
                    ]
                    cs''4
                    b'8
                    [
                    gs'8
                    ]
                    )
                    b'4
                    (
                    b'4
                    cs''4
                    ds''4
                    )
                    gf''4
                    (
                    gf''8
                    [
                    af''8
                    ]
                    ef''4
                    f''8
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
                    bf''4
                    df''4
                    c''4
                    )
                    af'4
                    (
                    bf'8
                    [
                    af'8
                    ]
                    ef'4
                    c'8
                    [
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
                    ef''4
                    d''4
                    )
                    bf'4
                    (
                    c''4
                    bf'8
                    [
                    g'8
                    ]
                    c''4
                    bf'8
                    [
                    g'8
                    ]
                    )
                    bf'4
                    (
                    bf'4
                    c''4
                    d''4
                    )
                    f''4
                    (
                    f''8
                    [
                    g''8
                    ]
                    d''4
                    e''8
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
                    a''4
                    c'''4
                    b''4
                    )
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