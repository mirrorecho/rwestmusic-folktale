#(set-global-staff-size 22)

\header {
    composer = "Randall West"
    tagline = ##f
    poet = \markup { \box "SCORE IN C" } %HACKY WAY TO GET SCORE IN C IN THERE !!!!!!
    title = \markup {
        \column {
            \center-align {
                \fontsize #3 {
                    "A Folktale"
                }
            }
        }
    }
    tagline = "Copyright 2017 Randall West."
}

  #(set! paper-alist (cons '("10x13" . (cons (* 10 in) (* 13 in))) paper-alist))

  \paper {
    #(set-paper-size "10x13")
    %#(set-paper-size "letter")
    left-margin = 22\mm
    system-separator-markup = \slashSeparator
    markup-system-spacing = #'(
        (basic-distance . 0)
        (minimum-distance . 0)
        (padding . 8)
        (stretchability . 0)
    )
    system-system-spacing = #'(
        (basic-distance . 12)
        (minimum-distance . 18)
        (padding . 12)
        (stretchability . 20)
    )
}

\layout {
    \set Score.markFormatter = #format-mark-circle-letters 
    \context {        
        \Score
        
        % \remove "Bar_number_engraver"
        \override BarNumber #'break-visibility = #'#(#f #t #t)
        \override BarNumber #'font-size = #1.2
        \override BarNumber  #'stencil = #(make-stencil-boxer 0.1 0.25 ly:text-interface::print)
        
        \override RehearsalMark #'font-size = #6

    }
    \context {
        \Staff 
        % \RemoveEmptyStaves
        \override VerticalAxisGroup #'remove-first = ##t % NOTE: comment this out to show staves on first page
        \override Hairpin #'minimum-length = #6
    }
    \context {
        \RhythmicStaff 
        % \RemoveEmptyStaves
        \override VerticalAxisGroup #'remove-first = ##t % NOTE: comment this out to show staves on first page
        \override Hairpin #'minimum-length = #6
    }
    % \context {
    %     \Dynamics
    %     \consists #Measure_counter_engraver
    %     \override MeasureCounter.direction = #DOWN
    %     \override MeasureCounter.font-encoding = #'latin1
    %     \override MeasureCounter.font-shape = #'italic
    %     % to control the distance of the Dynamics context from the staff:
    %     \override VerticalAxisGroup.nonstaff-relatedstaff-spacing.padding = #3
    %     \override MeasureCounter.font-size = #1.2
    %     % NOTE... below causes an error... why?
    %     % \override MeasureCounter.stencil = #(make-stencil-boxer 0.1 0.25 ly:text-interface::print)
    % }
}
