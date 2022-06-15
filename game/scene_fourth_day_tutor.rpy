label fourthDayTutor:
    if aki_route == True:
        scene Bg Room with fade
        queue music "audio/music/park.ogg" loop fadein 3.0
        "Ich habe schon seit heute Morgen auf Aki gewartet."
        "Jetzt ist es gerade 10 Uhr."
        "Mir wird es langsam langweilig. Was soll ich überhaupt machen, um die Zeit zu vertreiben?"
        "Ich schaue mich im Zimmer um und sehe ein Haufen Bücher und mein PC"
        menu:
            with Dissolve(0.3)
            "Was soll ich machen?"
            "Ein Buch lesen":
                $ aki_affec += 1
                "Ich könnte auch meine Zeit damit verbringen, ein Buch zu lesen."
                "Also holte ich mein Lieblingsbuch \"Parry Hotter and the Backrooms of Mystery\" aus meinem Schrank heraus und fing an zu lesen."
                pause 3.0
                "Eine kurze Zeit später klopfte Aki an meiner Tür und ich habe sie hereingelassen."
            "Dark Souls":
                $ aki_affec += 2
                "Aki hat mich irgendwie von der Idee überzeugt, eine Kopie von Dark Souls zu kaufen."
                "Frag mich nicht wie."
                "Ich habe das Spiel, nachdem ich es gekauft habe, für ein paar Minuten ausprobiert, und es war mir zu schwer."
                "Keine Ahnung, wie Aki sowas spielen kann."
                "Ich habe das Spiel nach 10 Jahren endlich wieder angemacht und bin für 20 Minuten am Stück am ersten Boss gereckt."
                "Dark Souls mein Arsch."
                "Ich habe schon fast Tränen in meinen Augen gespürt, als Aki endlich an meiner Tür klingelte."
                "Ich ging nach unten und führte sie zu meinem Zimmer."
            "Fortnite":
                scene Bg Load with fade
                "Ich mache mein PC an und öffne Fortnite."
                "Ich habe es schon in einer ganzen Weile nicht mehr gespielt, und ich glaube, dass ich damit die Zeit recht gut verschwenden kann, bis Aki endlich kommt."
                pause 3.0
                marcus "\"BOOOOOOM GET RECT LOOOOOOOOSERS!\""
                marcus "\"VICTORY ROYALE!\""
                "Ich schmiss mein Controller auf den Tisch."
                "Ich tanzte durch mein Zimmer, bis ich Aki vor meiner Tür mit einem entsetzten Gesicht sah."
                show Aki outfit_casual left_casual right_casual eyebrows_angry mouth_big with dissolve
                marcus "\"Aki, warte, ich kann es erklä-\""
                "Bevor ich meinen Satz vollenden konnte, stürmte sie aus meinem Zimmer."
                scene Bg Load with fade
                pause 1.0
                jump credits
        
        scene Bg Load with fade
        pause 1.0
        scene Bg Room with fade
        show Aki outfit_casual left_casual right_casual mouth_laugh with dissolve
        aki "\"Wow! Ich war schon lange nicht mehr in deinem Zimmer!\""
        show Aki mouth_small with dissolve
        aki "\"Das letzte Mal war vor... 7 Jahren?\""
        aki "\"Nicht vieles hat sich geändert.\""
        "Mein Zimmer ist ziemlich kahl."
        "Ich brauche eigentlich nur ein PC, ein Tisch und ein Bett, um zu leben."
        "Vielleicht auch einen Schrank, um meine Bücher zu lagern."
        aki "\"Ich glaube, ich gucke jetzt mal unter deinen Be-\""
        marcus "\"NEIN NEIN NEIN DAS MACHST DU JETZT NICHT.\""
        show Aki eyebrows_angry eyes_closed mouth_laugh_teeth with dissolve
        "Aki fing an zu lachen."
        aki "\"Hehehe!\""
        "Ich will nicht mehr."
        show Aki eyebrows_neutral eyes_open mouth_small with dissolve
        marcus "\"Na gut. Sollen wir jetzt mit der Nachhilfe anfangen?\""
        aki "\"Jep!\""
        "Aki packte ihre Sachen aus."
        aki "\"Zuerst habe ich einige Fragen zum Grundwissen.\""
        marcus "\"Enttäusche mich nicht.\""
        menu:
            with Dissolve(0.3)
            aki "\"Wofür steht überhaupt AcI?\""
            "Akkusativus cum Infinitivo":
                "Ernsthaft?"
                marcus "\"Akkusativus cum Infinitivo, habe ich doch gesagt.\""
                "Gerade erst gesagt, bitte enttäusche mich nicht."
                $ aki_affec += 2
            "Akkusativ cum Infinitiv":
                "Ernsthaft?"
                marcus "\"Akkusativ cum Infinitiv, habe ich doch gesagt.\""
                "Ich habe gerade erst gesagt, bitte enttäusche mich nicht."
        aki "\"Stimmt!\""
        menu:
            with Dissolve(0.3)
            aki "\"Und wie übersetzt man nochmal einen AcI ins Deutsche?\""
            "Als dass-Satz":
                $ aki_affec += 2
                marcus "\"Als ein dass-Satz, solltest du doch wissen!\""
            "Als Adverbialsatz":
                marcus "\"Als Adverbialsatz, solltest du doch wissen!\""
        show Aki eyebrows_angry mouth_big with dissolve
        aki "\"Ich verstehe es aber nicht!\""
        marcus "\"Das sind die absoluten Basics!\""
        show Aki eyebrows_neutral eyes_open mouth_small with dissolve
        menu:
            with Dissolve(0.3)
            aki "\"Wie wird der AcI im Lateinischen denn überhaupt aufgebaut?\""
            "Kopfverb im Hauptsatz, Nominativsubjekt und Prädikatsinfinitiv im AcI, durch Kommas getrennt":
                marcus "\"Ein AcI besteht aus einem Hauptsatz und ein Nominativsubject und ein Prädikatsinfinitiv in einen Nebensatz.\""
                marcus "\"Der Nebensatz wird auch das AcI genannt.\""
                marcus "\"Ein Beispiel wäre:\""
                marcus "\"Video, is ire. - Ich sehe, dass er geht.\""
                marcus "\"In diesen Fall wäre Video das Kopfverb, is das Nominativsubject und ire der Prädikatsinfinitiv.\""
            "Kopfverb im Rahmensatz, Subjektsakkusativ und Prädikatsinfinitiv im AcI":
                $ aki_affec += 2
                marcus "\"Ein AcI besteht aus einem Rahmensatz und das AcI.\""
                marcus "\"Im Rahmensatz muss sich ein Verb befinden.\""
                marcus "\"Im AcI selbst befindet sich ein Akkusativ, den sogenannten Subjektsakkusativ und ein Verb im Infinitiv, nämlich dem Prädikatsinfinitiv.\""
                marcus "\"Ein Beispiel wäre:\""
                marcus "\"Video eum ire. - Ich sehe, dass er geht.\""
                marcus "\"In diesen Fall wäre Video das Kopfverb, eum der Subjektsakkusativ und ire der Prädikatsinfinitiv.\""
        aki "\"Mhm...\""
        menu:
            with Dissolve(0.3)
            aki "\"So wie ich es verstehe, ist der Subjektsakkusativ im AcI mit dem Subjekt im deutschen dass-Satz vergleichbar und das Prädikatsinfinitv mit dem Verb im dass-Satz.\""
            "Nein":
                marcus "\"Nein, nicht immer, der Subjektsakkusativ kann auch das Subjekt vom Rahmensatz sein.\""
            "Ja":
                $ aki_affec += 2
                marcus "\"Ja, so ungefähr.\""
        aki "\"Interessant...\""
        aki "\"\Ich habe auch etwas von Vorzeitigkeit oder so mitbekommen\""
        marcus "\"Also hast du den ganzen Unterricht doch nicht durchgeschlafen!\""
        show Aki eyebrows_angry mouth_big with dissolve
        aki "\"Hey! Das war fies!\""
        marcus "\"Hehe.\""
        show Aki eyebrows_neutral eyes_open mouth_small with dissolve
        marcus "\"Aber zurück zum Thema, verstehst du das?\""
        aki "\"Nicht wirklich.\""
        menu:
            with Dissolve(0.3)
            aki "\"Wann wird nochmal ein AcI überhaupt vorzeitig?\""
            "Wenn der Prädikatsinfinitiv im Perfekt steht":
                $ aki_affec += 2
                marcus "\"Wenn der Prädikatsinfinitiv im Perfekt steht.\""
                marcus "\"Verändern wir das vorherige Beispiel:\""
                marcus "\"Video eum isse. - Ich sehe, wie er gegangen ist.\""
                marcus "\"Oder Vidi eum isse. Ich sah, wie er gegangen war.\""
                marcus "\"Auch wenn jetzt beide Verben im Perfekt stehen, wird der Satz immer noch vorzeitig übersetzt.\""
                marcus "\"Das bedeutet, dass gehen jetzt im deutschen Satz als Plusquamperfekt übersetzt wird.\""
            "Wenn das Kopfverb im Futur steht":
                marcus "\"Wenn das Kopfverb im Futur steht.\""
        marcus "\"Soweit so gut?\""
        aki "\"Ja.\""
        menu:
            with Dissolve(0.3)
            aki "\"Kann man dann ein Bezug auf das Subjekt im Rahmensatz machen?\""
            "Mit Reflexivpronomen":
                $ aki_affec += 2
                marcus "\"Ja, nämlich mit Personalpronomen.\""
                marcus "\"Zum Beispiel Videt se ire. - Er sieht, dass er geht.\""
            "Mit Personalpronomen":
                marcus "\"Ja, nämlich mit Personalpronomen.\""
                marcus "\"Video me ire. - Ich sehe, dass ich gehe.\""
                marcus "\"Oder auch Videt eum ire. - Er sieht, dass er geht.\""
        "Aki und ich haben uns noch einige Aufgaben angeguckt."
        marcus "\"War das alles?\""
        show Aki eyes_closed mouth_laugh_teeth with dissolve
        aki "\"Jup. Danke Marcus! Ich wusste, dass du mir helfen wirst!\""
        "Aki sah mich mit ein Lächeln an."
        scene Bg Load with fade
        stop music fadeout 8.0
        "Aki und ich haben den Rest des Tages damit verbracht, weitere Übungsaufgaben zum Thema AcIs zu machen."
        "Auch wenn sie eigentlich jeden Satz falsch übersetzt hat, hat man bei ihr zumindest ein bisschen Fortschritt erkannt."
        "Machte mir mehr Spaß als erwartet."
        "Nachdem wir fertig geworden sind, habe ich sie nach Hause begleitet und ich bin kurz später in mein Bett gefallen."
        "Morgen ist schließlich ja ein Montag."
        scene Bg Load with fade

    if partizia_route == True:
        scene Bg Clubroom with fade
        queue music "audio/music/club.ogg" loop fadein 3.0
        "Es ist Montag Nachmittag."
        "Ich sitze wie immer in meiner Ecke im Clubraum und starre Löcher in die Luft."
        "Ich schaue auf meine Uhr, und bemerke, dass es schon 16:02 ist."
        "Das heißt, dass Partizia sich um 2 Minuten verspätet hat."
        "Normalerweise ist sie immer pünktlich."
        "Und sie meinte auch, dass sie auf mich warten würde."
        "Wie das Blatt sich gewendet hat."
        "Na ja, jeder hat mal diese Tag- warte, das hört sich falsch an."
        "Genau als ich in meinen Gedanken versunken war, kam Partizia in den Clubraum rein."
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Schön dich hier zu sehen, Marcus.\""
        marcus "\"Gleichfalls.\""
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Du denkst wohl, wieso ich so spät gekommen bin, oder?\""
        "Warte, wie wusste sie das?"
        partizia "\"Ich musste Arbeit für den Studentenrat tun.\""
        partizia "\"Da macht die Menge, die mich immer umzingelt, meine Arbeit auch nicht einfacher.\""
        "Ich glaube, dass ich nicht fragen sollte, woher sie das alles weiß."
        "Manchmal ist es auch besser so."
        show Partizia eyes_closed with dissolve
        partizia "\"Nein nein, keine Sorge, mach dir keine Gedanken darüber.\""
        marcus "\"Worüber?\""
        show Partizia mouth_laugh with dissolve
        partizia "\"Fufufu~\""
        "Partizia packte ihre Sachen aus, ohne mich ausreden zu lassen."
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Nun, wollen wir Anfangen?\""
        marcus "\"Ja, aber-\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Klasse. Nun, kannst du mir bitte noch einmal von Grund auf Pcs erklären?\""
        partizia "\"Ich denke, dass es keinen Besseren als dich gibt, der es mir erklären könnte.\""
        "Klasse. Jetzt lässt sie mich nicht ausreden."
        "Da ist definitiv etwas Zwielichtiges im Gange, aber das ist jetzt nicht das wichtige."
        marcus "\"Klar.\""
        show Partizia eyes_open mouth_happy with dissolve
        partizia "\"Danke.\""
        show Partizia eyes_open mouth_small with dissolve
        menu:
            with Dissolve(0.3)
            partizia "\"Pc steht für Partizipium Coniunctum, soweit ich weiß.\""
            "Ja":
                $ partizia_affec += 2
                marcus "\"Ja\""
            "Nein":
                marcus "\"Nein, Pc steht für Partizipium cum Coniuncto\""
        partizia "\"OK.\""
        menu:
            with Dissolve(0.3)
            partizia "\"Wie wird das PPP gebildet?\""
            "Es gibt keine feste Regel bei der Bildung":
                marcus "\"Keine feste Regel existiert, deshalb musst du dir das PPP bei jedem Wort auswendig lernen.\""
            "Präsensstamm + -tus, -a, -um":
                $ partizia_affec += 2
                marcus "\"Du nimmst dir den Präsensstamm vom Verb und packst ein -tus, a, um dahinter.\""
                marcus "\"Das PPP muss aber KNG-Kongurent zum Bezugswort sein, also musst du darauf achten.\""
                marcus "\"Jedoch ist das PPP bei vielen Wörtern unregelmäßig, wie bei ferre (latum), weshalb du diese dir auswendig lernen musst.\""
        show Partizia eyes_closed with dissolve
        partizia "\"Hört sich aber aufwendig an.\""
        show Partizia eyes_open mouth_small with dissolve
        menu:
            with Dissolve(0.3)
            partizia "\"Was ist eigentlich der Unterschied zwischen dem normalen Perfekt passiv und dem Pc?\""
            "Es gibt keinen":
                marcus "\"Kein echter Unterschied existiert zwischen denen.\""
            "Bei Perfekt passiv gibt es ein From von “esse” im Satz":
                $ partizia_affec += 2
                marcus "\"Der Unterschied liegt darin, dass bei einem normalen Perfekt passiv ein esse im Satz ist.\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Gut zu wissen.\""
        show Partizia eyes_open mouth_small with dissolve
        menu:
            with Dissolve(0.3)
            partizia "\"Soweit ich weiß, kann man das Pc als sehr viele verschiedene Sorten von Nebensätzen übersetzen, oder?\""
            "Ja":
                $ partizia_affec += 2
                marcus "\"Ja, du kannst es zum Beispiel als Relativ- und Adverbialsatz übersetzen, aber auch als Beiordnung und Präpositionalausdruck.\""
            "Nein, es muss als Relativsatz übersetzt werden.":
                marcus "\"Nein, da das Partizipium Coniunctum eine Beschreibung ist, muss man es als Relativsatz übersetzten.\""
        partizia "\"Alles Klar.\""
        menu:
            with Dissolve(0.3)
            partizia "\"Man kann Pcs nur vorzeitig zum Hauptsatz übersetzen, oder?\""
            "Ja":
                $ partizia_affec += 2
                marcus "\"Jep.\""
            "Nein, es muss nicht":
                marcus "\"Nein, du muss auf den Kontext im Satz achten.\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Danke sehr für deine Zeit, Marcus.\""
        marcus "\"War das alles?\""
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"So ungefähr.\""
        show Partizia eyes_open mouth_happy with dissolve
        partizia "\"Nochmals ein großes Dankeschön an dich, Marcus.\""
        marcus "\"Kein Problem.\""
        scene Bg Load with fade
        stop music fadeout 6.0
        "Aki und ich haben den Rest des Tages damit verbracht, einige Übungsaufgaben zum Thema Pcs zu machen."
        "Desto mehr Zeit ich mit mir verbringe, desto mehr denke ich, dass sie schwarze Magie beherrscht, regelmäßig Gedanken liest und Dämo- oh warte falsches Spiel."
        "Jedenfalls, Partizia hat definitiv sehr große Fortschritte gemacht, und am Ende des Tages habe ich ihr mit ein paar schwierigeren Übungsaufgaben auf den Weg geschickt."
        "Sie hat mir gesagt, dass sie mir ihre Antworten zeigt, wenn wir das nächste Mal uns im Clubraum sehen."
        scene Bg Load with fade
