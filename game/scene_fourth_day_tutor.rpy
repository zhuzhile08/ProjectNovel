label fourthDayTutor:
    queue music "audio/music/park.ogg" loop fadein 3.0
    "Ich habe schon seit heute morgen auf Aki gewartet."
    "Jetzt ist es gerade 10 Uhr."
    "Naja, mir wird es langsam langweilig. Was soll ich überhaupt machen um die Zeit zu vertreiben?"
    "Ich schaue mich im Zimmer um und sehe ein Haufen Bücher und mein PC"
    menu:
        with Dissolve(0.3)
        "Was soll ich machen?"

        "Ein Buch lesen":
            $ aki_affec += 1
            "Naja, ich kann auch meine Zeit damit verbringen, ein Buch zu lesen."
            "Ich holte mein Lieblingsbuch \"Parry Hotter and the Backrooms of Mystery\" aus mein Schrank raus und fing an zu lesen."
            pause 3.0
            "Eine kurze Zeit später klopfte Aki an meiner Tür und ich habe sie reingelassen."
        "Dark Souls":
            $ aki_affec += 2
            "Aki hat mich irgendwie von der Idee überzeugt, eine Kopie von Dark Souls zu kaufen."
            "Frag mich nicht wie."
            "Ich habe das Spiel, nachdem ich es gekauft habe, für ein Paar Minuten ausprobiert, und es war mir zu schwer."
            "Keine Ahnung wie Aki sowas spielen kann."
            "Ich habe das Spiel nach gefühlt 10 Jahren endlich wieder angemacht und bin für 20 Minuten am Stück am ersten Boss gereckt."
            "Dark Souls mein Arsch."
            "Ich habe schon fast Tränen in meinen Augen gespürt, als Aki endlich an meiner Tür klingelte."
            "Ich ging nach unten und führte sie zu meinen Zimmer."
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
    
    scene Bg Load with fade
    pause 1.0
    # load room
    aki "\"Wow! Ich war schon lange nicht mehr in deinen Zimmer!\""
    aki "\"Das letzte mal war vor... 7 Jahren?\""
    aki "\"Nicht vieles hat sich geändert.\""
    "Mein Zimmer ist ziemlich kahl."
    "Ich brauche eigentlich nur ein PC, ein Tisch und ein Bett um zu leben."
    "Vieleicht auch einen Schrank um meine Bücher zu lagern."
    aki "\"Vieleicht gucke ich jetzt mal unter deinen Be-\""
    marcus "\"NEIN NEIN NEIN DAS MACHST DU JETZT NICHT.\""
    "Aki fing an zu lachen."
    aki "\"Hehehe!\""
    "Ich will nicht mehr."
    marcus "\"Na gut. Sollen wir jetzt mit der Nachhilfe anfangen?\""
    aki "\"Jep!\""
    "Aki packte ihre Sachen aus."
    aki "\"Zuerst habe ich einige Fragen zum Grundwissen.\""
    marcus "\"Enttäusch mich nicht.\""
    menu:
        with Dissolve(0.3)
        aki "\"Wofür steht überhaupt AcI?\""
        "Akkusativus cum Infinitivo":
            "Ernsthaft?"
            marcus "\"Akkusativus cum Infinitivo, habe ich doch gesagt.\""
            "Gerade erst gesagt, bitte enttäusch mich nicht."
            $ aki_affec += 1
        "Akkusativ cum Infinitiv":
            "Ernsthaft?"
            marcus "\"Akkusativ cum Infinitiv, habe ich doch gesagt.\""
            "Gerade erst gesagt, bitte enttäusch mich nicht."
    aki "\"Stimmt!\""
    menu:
        with Dissolve(0.3)
        aki "\"Und wie übersetzt man nochmal einen AcI ins Deutsche?\""
        "Als dass-Satz":
            $ aki_affec += 1
            marcus "\"Als dass-Satz, soltest du doch wissen!\""
        "Als Adverbialsatz":
            marcus "\"Als Adverbialsatz, soltest du doch wissen!\""
    aki "\"Ich verstehe es aber nicht!\""
    marcus "\"Das sind die absoluten Basics!\""
    menu:
        with Dissolve(0.3)
        aki "\"Wie wird der AcI im lateinischen denn überhauput aufgebaut?\""
        "Kopfverb im Hauptsatz, Nominativsubjekt und Prädikatsinfinitiv im AcI, durch Kommas getrennt":
            marcus "\"Ein AcI besteht aus ein Hauptsatz und ein Nominativsubject und ein Prädikatsinfinitiv in einen Nebensatz.\""
            marcus "\"Der Nebensatz wird auch das AcI genannt.\""
            marcus "\"Ein Beispiel wäre:\""
            marcus "\"Video, is ire. - Ich sehe, dass er geht.\""
            marcus "\"In diesen Fall wäre Video das Kopfverb, is das Nominativsubject und ire das Prädikatsinfinitiv.\""
        "Kopfverb im Rahmensatz, Subjektsakkusativ und Prädikatsinfinitiv im AcI":
            $ aki_affec += 1
            marcus "\"Ein AcI besteht aus einen Rahmensatz und das AcI.\""
            marcus "\"Im Rahmensatz muss sich ein Verb befinden.\""
            marcus "\"Im AcI selbst befindet sich ein Akkusativ, den sogenannten Subjektsakkusativ und ein Verb im Infinitiv, nämlich das Prädikatsinfinitiv.\""
            marcus "\"Ein Beispiel wäre:\""
            marcus "\"Video eum ire. - Ich sehe, dass er geht.\""
            marcus "\"In diesen Fall wäre Video das Kopfverb, eum das Subjektsakkusativ und ire das Prädikatsinfinitiv.\""
    aki "\"Mhm...\""
    menu:
        with Dissolve(0.3)
        aki "\"So wie ich es verstehe, ist das Subjektsakkusativ im AcI mit den Subjekt im Deutschen dass-Satz vergleichbar und das Prädikatsinfinitv mit den Verb im dass-Satz.\""
        "Nein":
            marcus "\"Nein, nicht immer, das Subjektsakkusativ kann auch das Subjekt vom Rahmensatz sein.\""
        "Ja":
            $ aki_affec += 1
            marcus "\"Ja, so ungefähr.\""
    aki "\"Interessant...\""
    aki "\"\Ich habe auch etwas von Vorzeitigkeit oder so mittbekommen\""
    marcus "\"Also hast du den ganzen Unterricht doch nicht durchgeschlafen!\""
    aki "\"Hey! Das war fies!\""
    marcus "\"Hehe.\""
    marcus "\"Aber zurück zum Thema, verstehst du das?\""
    aki "\"Nicht wirklich.\""
    menu:
        with Dissolve(0.3)
        aki "\"Wann wird nochmal ein AcI überhaupt vorzeitig?\""
        "Wenn der Prädikatsinfinitiv im Perfekt steht":
            $ aki_affec += 1
            marcus "\"Wenn der Prädikatsinfinitiv im Perfekt steht.\""
            marcus "\"Verändern wir das vorherige Beispiel:\""
            marcus "\"Video eum isse. - Ich sehe, wie er gegangen ist.\""
            marcus "\"Oder Vidi eum isse. Ich sah, wie er gegangen war.\""
            marcus "\"Auch wenn jetzt beide Verben im Perfekt stehen, wird der Satz immer noch Vorzeitig übersetzt.\""
            marcus "\"Das bedeutet, dass gehen jetzt im Deutschen Satz als Plusquamperfekt übersetzt wird.\""
        "Wenn das Kopfverb im Futur steht":
            marcus "\"Wenn das Kopfver im Futur steht.\""
    marcus "\"Soweit so gut?\""
    aki "\"Ja.\""
    menu:
        with Dissolve(0.3)
        aki "\"Worauf beziehen sich nochmal \'se\', \'sibi\' und \'suus\' im AcI?\""
        "a) Auf das Subjekt im Rahmensatz":
            # wrong
            "nein"
        "b) Auf das Subjektakkusativ":
            # correct
            "ja"
    menu:
        with Dissolve(0.3)
        aki "\"Wie kann man dann ein Bezug auf das Subjekt im Rahmensatz machen?\""
        "Geht nicht":
            marcus "\"Geht leider nicht.\""
            marcus "\"Das ist ein großer Nachteil an AcIs.\""
        "Mit is/ea/id":
            # correct
            "ja"
    marcus "\"War das alles?\""
    aki "\"Jup. Danke Marcus! Ich wusste dass du mir hilfst!\""
    "Aki sah mich mit ein Lächeln an."
    marcus "\"Kein Problem. Hast du sonst noch irgendetwas?\""
    aki "\"Nope.\""
    scene Bg Load with fade
    stop music fadeout 10.0
    "Aki und ich haben den Rest des Tages damit verbracht, einige Übungsaufgaben zum Thema AcIs zu machen."
    "Auch wenn sie eigentlich jeden Satz falsch übersetzt hat, hat man bei ihr zumindest ein bisschen Fortschritt erkannt."
    "Machte mir mehr Spaß als erwartet."
    "Nachdem wir fertig geworden sind, habe ich sie nach Hause begleitet und ich bin kurz später in mein Bett gefallen."
    "Morgen ist schließlich ja ein Montag."
    scene Bg Load with fade
