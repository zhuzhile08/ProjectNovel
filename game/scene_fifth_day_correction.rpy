label fifthDayCorrection:
    pause 5.0
    if aki_route:
        scene Bg Room with fade
        queue music "audio/music/park.ogg" loop fadein 3.0
        "Eine ganze Woche ist vergangen, und heute liege ich mit Kopfhörern im Bett und denke über mein Leben nach."
        "So verbringe ich mein Wochenende."
        "Ich könnte jetzt Sport machen, ich könnte jetzt ein ganzes Videospiel für ein Schulprojekt programmieren."
        "Aber nein."
        "Ich bin fast eingeschlafen, als ich plötzlich irgentwas gehört habe."
        "Ich glaube es ist... Klopfen?"
        "Ich hatte schon oft solche Halluzinationen, wo ich gedacht habe, dass irgendeiner meinen Namen ruft oder dass irgendjemand an der Tür klopft."
        "Keine Ahnung warum das passiert, aber es passiert und es ist nerfig."
        menu:
            with Dissolve(0.3)
            "Soll ich das Klopfen ignorieren?"
            "Ja":
                stop music fadeout 5.0
                "Meh, keine Lust jetzt aufzustehen."
                "Mein Lieblingssong spielt jetzt gerade immerhin."
                "Und ich werde auch *gähn* langsam müde."
                scene Bg Load with irisin
                "Ich fühlte wie die Welt vor meinen Augen verschwindet und sich in unendliche Dunkelheit verwandelt."
                "Gute Nacht."
            "Nein":
                "Ich legte meine Kopfhörer ab und ging zu Tür."
                "Ich öffne vorsichtig die Tür."
                scene Bg Home Outwards with fade
                stop music fadeout 1.0
                queue music "audio/music/aki.ogg" loop fadein 2.0
                unknown "\"Hi Marcus~!\""
                "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUC-"
                "Ich kanns nicht glauben."
                "Ich habe einmal meine Ruhe gefunden, schon kommt sie und ruiniert alles."
                "Genau so wie wenn ich Pizza Hawaii auf einer langen Liste von normalen und leckeren Pizzen sehe."
                marcus "\"Jaaaaaaaaa? Was ist denn jetzt los?\""
                aki "\"Heeeeeeey! Wie gehts!\""
                "Ernsthaft?"
                marcus "\"Kacke.\""
                aki "\"Wieso denn?\""
                marcus "\"Weil du hier bist und mich nerfst!\""
                aki "\"Aber ich habe ein paar Fragen!\""
                marcus "\"Jaja, komm rein.\""
                scene Bg Room with fade
                "Ich ließ Aki in mein Haus rein."
                marcus "\"Willst du was zu trinken?\""
                aki "\"Mountain Dew!\""
                "Ich rollte meine Augen."
                marcus "\"Ernsthaft jetzt.\""
                aki "\"Kaffee.\""
                marcus "\"OK.\""
                "Nachdem ich die Getränke vorbereitet habe, ging ich zu meinen Zimmer zurück."
                "Ich habe für mich auch ein Kaffee gemacht."
                aki "\"Mmmh! Danke Marcus~!\""
                "Sie nahm ein Schluck Kaffee und holte ein Stück Papier raus."
                marcus "\"Sind das die nuklearen Abschusscodes der USA?\""
                aki "\"Ja! Joe Biden hat es mir geschenkt!\""
                marcus "\"Wie bitte was?!\""
                "Aki fing an zu lachen."
                aki "\"Hahahahahahahaha!\""
                aki "\"Dachtest du es wirklich?!\""
                "Verdammt."
                "Ich hasse mich."
                marcus "\"OK OK, was hast du denn da?\""
                aki "\"Aufgaben.\""
                marcus "\"Was?\""
                aki "\"Naja, ich habe Zuhause selber noch ein bisschen am AcI geübt und ein Art Selbsttest geschrieben.\""
                aki "\"Kannst du meine Sätze bitte für mich korrigieren?\""
                "Ich stöhnte."
                "Ich meine, ich habe eh nichts zu tun, also wieso nicht?"
                marcus "\"Na gut.\""
                aki "\"Yaaaaaay!\""
                marcus "\"Dabei machte sie einen kleinen Hüpfer.\""

                stop music fadeout 2.0
                queue music "audio/music/park.ogg" loop fadein 3.0
                # the tasks go here

                marcus "\"Du hast dich definitv sehr viel Verbessert, Aki.\""
                "Aki lachte."
                marcus "\"Aber noch ein bisschen Übung kann dir nichts schlechts tun.\""
                marcus "\"Wenn du Hilfe brauchst, kannst du immer mich fragen.\""
                aki "\"Danke Marcus!\""
                scene Bg Load with fade
                stop music fadeout 4.0
                "Wir haben den restlichen Tag noch miteinander verbracht."
                "Ich habe schon lange keine Runde Monopoly mehr mit Aki gespielt."
                "Hat recht viel Spaß gemacht."
                "Am Abend bin ich völlig erschöpft in mein Bett gefallen."
                "*Gähn* 10/10 würde ich nochmal machen."
                "Gute Nacht."
                scene Bg Load with fade
    if partizia_route == True:
        queue music "audio/music/club.ogg" loop fadein 3.0
        scene Bg Clubroom with fade
        "Fast eine ganze Woche ist vergangen."
        "Es ist Freitags, und ich war gerade dabei, den Clubraum aufzuräumen, als ich ein leichtes Klopfen an der Tür hörte."
        unknown "\"Hallo?\""
        marcus "\"Sie können reinkommen.\""
        stop music fadeout 2.0
        "Die Tür öffnete sich langsam."
        queue music "audio/music/partizia.ogg" loop fadein 2.0
        marcus "\"Ach, Hallo, Partizia!\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Schön dich hier zu sehen, Marcus.\""
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Hättest du für einen ganz kurzen Moment Zeit?\""
        marcus "\"Klar.\""
        partizia "\"Dies ist bezüglich der Aufgabne, die du mir das Letzte mal gegeben hast.\""
        "Sie holte aus ihrer Tasche ein Heft heraus."
        partizia "\"Könntest du diese bitte für mich korrigieren?\""
        marcus "\"Ich sehe keinen Grund, wieso ich es nicht machen sollte.\""
        "Partizia überreichte mir ihr Heft."
        show Partizia mouth_happy with dissolve
        partizia "\"Danke sehr.\""
        "Ich höffnete ihr Heft."
        stop music fadeout 2.0
        queue music "audio/music/club.ogg" loop fadein 3.0

        # the tasks go here.

        "Ich gab ihr das Heft zurück."
        show Partizia mouth_small with dissolve
        partizia "\"Hmmm, ich sehe.\""
        show Partizia mouth_happy with dissolve
        partizia "\"Ein nochmals sehr großes Danke schön.\""
        marcus "\"Kein Problem, wir sind ja Klassenkameraden, ich denke wir sollten uns helfen.\""
        "Parzitia zeigte mir ein Lächeln."
        show Partizia mouth_small with dissolve
        partizia "\"Hättest du noch einige Tipps für mich?\""
        marcus "\"Einfach viel üben. Du hast dich verglichen zum letzten Mal deutlich verbessert.\""
        "Partizia schaute auf ihre Uhr."
        partizia "\"Ach, sieh dir die Zeit an. Ich muss ganz schnell los. Ich habe noch was zu machen.\""
        "Wahrscheinlich Gedenken lesen üben."
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Und nein, ich übe zuhause kein Gedanken lesen.\""
        "Warte was?"
        show Partizia eyes_closed mouth_laugh with dissolve
        partizia "\"Jedenfalls, schönes Wochenende noch.\""
        "Sie ging zügig aus der Tür raus, während sie mir hinterhergewinkt hat."
        "Was zum Teufel war das?"
        stop music fadeout 3.0
        scene Bg Load with fade
