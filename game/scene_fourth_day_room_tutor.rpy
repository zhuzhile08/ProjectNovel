label fourthDayRoomTutor:
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
