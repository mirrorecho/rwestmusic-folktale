#(set-default-paper-size "tabloid" 'portrait)
#(set-global-staff-size 20)

\header {
    composer = "Randall West"
    % tagline = ##f
    title = \markup {
        \column {
            \center-align {
                \fontsize #6 {
                    "Please Listen Closely as Our Options Have Changed"
                }
            }
        }
    }
    tagline = "Copyright 2016 Randall West."
}

  #(set! paper-alist (cons '("10x13" . (cons (* 10 in) (* 13 in))) paper-alist))

  \paper {
    #(set-paper-size "10x13")
    system-system-spacing #'basic-distance = #12
    system-system-spacing #'padding = #9

    % left-margin = 22\mm
    % system-separator-markup = \slashSeparator
    % markup-system-spacing = #'(
    %     (basic-distance . 0)
    %     (minimum-distance . 0)
    %     (padding . 8)
    %     (stretchability . 0)
    % )
    % system-system-spacing = #'(
    %     (basic-distance . 12)
    %     (minimum-distance . 18)
    %     (padding . 12)
    %     (stretchability . 20)
    % )
  }  

\layout {
    \set Score.markFormatter = #format-mark-circle-letters 
    \context {        
        \Score
        \override MultiMeasureRest #'expand-limit = #1
        \override BarNumber #'font-size = #1.4
        \override BarNumber  #'stencil = #(make-stencil-boxer 0.1 0.25 ly:text-interface::print)
        \override RehearsalMark #'font-size = #6
    }
    \context {
        \Staff
        \remove Instrument_name_engraver
        \override Hairpin #'minimum-length = #6
        \override MultiMeasureRest.expand-limit = #1
    }
    \context {
        \RhythmicStaff
        \remove Instrument_name_engraver
        \override Hairpin #'minimum-length = #6
        \override MultiMeasureRest.expand-limit = #1
    }
    }
}


