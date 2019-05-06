for %i in (*) do md "%~ni"
for %i in (*) do move "%i" "%~ni"
 (: parse : String -> PLANG)
 ;; parses a string containing a PLANG expressionto a PLANG AST
 (define (parse str)
   (let ([code (string->sexpr str)])
 (match code
   [(list (cons 'poly hea) (list tai ...)) ((cond
                                             [(null? hea) (error 'parse "parse: at least one coefficient is required in ~s" code)]
                                             [(null? tai) (error 'parse "parse: at least one point is required in ~s" code)]
                                             [else (Poly (map parse-sexpr hea) (map parse-sexpr tai))]))]
   [else (error 'parse "bla ~s"
                code)])))