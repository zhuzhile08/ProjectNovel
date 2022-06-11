label fourthDayTutor:
    "Ich habe schon seit heute morgen auf Aki gewartet."
    "Jetzt ist es gerade 10 Uhr."
    "Naja, mir wird es langsam langweilig. Was soll ich überhaupt machen um die Zeit zu vertreiben?"
    "Ich schaue mich im Zimmer um und sehe ein Haufen Bücher und mein PC"
    menu:
        with Dissolve(0.3)
        "Was soll ich machen?"

        "Ein Buch lesen":
            ""
        "Dark Souls":
            ""
        "Fortnite":
            scene Bg Load with fade
            "Ich mache mein PC an und öffne Fortnite."
            "Ich habe es schon in einer ganzen Weile nicht mehr gespielt, und ich glaube, dass ich damit die Zeit recht gut verschwenden kann, bis Aki endlich kommt."
            pause 3.0
            marcus "\"BOOOOOOM GET RECT LOOOOOOOOSERS!\""
            marcus "\"VICTORY ROYALE!\""
            "Ich schmiss mein Controller auf den Tisch."
            "Ich tanzte durch mein Zimmer bis ich Aki vor meiner Tür mit einen entsetzten Gesicht sah."
            marcus "\"Aki, warte ich kann es erklä-\""
            "Bevor ich mein Satz vollenden konnte, stürmte sie aus mein Zimmer."
            scene Bg Load with fade
            pause 1.0
            jump credits

label tutorAcI:
    menu:
        with Dissolve(0.3)
        "1) Wofür steht überhaupt AcI?"
        "a) Akkusativus cum Infinitivo, habe ich doch gesagt.":
            # correct
            "ja"
        "b) Akkusativ cum Infinitiv, habe ich doch gesagt.":
            # wrong
            "nein"
    
    menu:
        with Dissolve(0.3)
        "2) Wie übersetzt man nochmal einen AcI ins Deutsche?"
        "a) Als dass-Satz":
            # correct
            "ja"
        "b) Als Adverbialsatz":
            # wrong
            "nein"
    
    menu:
        with Dissolve(0.3)
        "3) Welche Bestandteile im deutschen dass-Satz sind mit der vom AcI vergleichbar?"
        "a) Das Subjekt mit dem Subjekt im Rahmensatz, das Prädikat mit dem Kopfverb":
            # wrong
            "nein"
        "b) Das Subjekt mit dem Subjektsakkusativ, das Prädikat mit dem Prädikatsinfinitiv":
            # correct
            "ja"
    
    menu:
        with Dissolve(0.3)
        "4) Wann wird nochmal ein AcI vorzeitig?"
        "a) Wenn der Prädikatsinfinitiv im Perfekt steht":
            # correct
            "ja"
        "b) Wenn das Kopfverb im Futur steht":
            # wrong
            "nein"
    
    menu:
        with Dissolve(0.3)
        "5) Worauf beziehen sich nochmal \"se\", \"sibi\" und \"suus\" im AcI?"
        "a) Auf das Subjekt im Rahmensatz":
            # wrong
            "nein"
        "b) Auf das Subjektakkusativ":
            # correct
            "ja"

    menu:
        with Dissolve(0.3)
        "6) Wie kann man dann ein Bezug auf das Subject im Rahmensatz machen?"
        "a) Geht nicht :(":
            # wrong
            "nein"
        "b) Mit is/ea/id":
            # correct
            "ja"