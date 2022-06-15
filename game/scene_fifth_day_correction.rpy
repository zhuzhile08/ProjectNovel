label fifthDayCorrection:
    pause 5.0
    if aki_route:
        scene Bg Room with fade
        queue music "audio/music/park.ogg" loop fadein 3.0
        "Eine ganze Woche ist vergangen, und heute liege ich mit Kopfhörern im Bett und denke über mein Leben nach."
        "So verbringe ich mein Wochenende."
        "Ich könnte jetzt Sport machen, ich könnte jetzt ein ganzes Videospiel für ein Schulprojekt programmieren."
        "Aber nein."
        "Ich bin fast eingeschlafen, als ich plötzlich etwas gehört habe."
        "Ich glaube, es ist... Klopfen?"
        "Ich hatte schon oft solche Halluzinationen, wo ich gedacht habe, dass irgendeiner meinen Namen ruft oder dass irgendjemand an der Tür klopft."
        "Keine Ahnung, warum das passiert, aber es passiert und es ist nervig."
        menu:
            with Dissolve(0.3)
            "Soll ich das Klopfen ignorieren?"
            "Ja":
                stop music fadeout 5.0
                "Meh, keine Lust, jetzt aufzustehen."
                "Mein Lieblingssong spielt jetzt gerade immerhin."
                "Und ich werde auch *gähn* langsam müde."
                scene Bg Load with irisin
                "Ich fühlte, wie die Welt vor meinen Augen verschwindet und sich in unendliche Dunkelheit verwandelt."
                "Gute Nacht."
            "Nein":
                "Ich legte meine Kopfhörer ab und ging nach unten."
                "Ich öffne vorsichtig die Tür."
                scene Bg Home Outwards with fade
                stop music fadeout 1.0
                queue music "audio/music/aki.ogg" loop fadein 2.0
                unknown "\"Hi Marcus~!\""
                "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUC-"
                "Ich kann es nicht glauben."
                "Ich habe einmal meine Ruhe gefunden, schon kommt sie und ruiniert alles."
                "Genauso wie wenn ich Pizza Hawaii auf einer langen Liste von normalen und leckeren Pizzen sehe."
                marcus "\"Jaaaaaaaaa? Was ist denn jetzt los?\""
                show Aki outfit_casual left_casual right_casual eyes_closed mouth_laugh_teeth with dissolve
                aki "\"Heeeeeeey! Wie gehts!\""
                "Ernsthaft?"
                marcus "\"Kacke.\""
                show Aki eyes_open mouth_small with dissolve
                aki "\"Wieso denn?\""
                marcus "\"Weil du hier bist und mich nervst!\""
                show Aki eyebrows_sad with dissolve
                aki "\"Aber ich habe ein paar Fragen!\""
                marcus "\"Jaja, komm rein.\""
                scene Bg Room with fade
                show Aki outfit_casual left_casual right_casual eyes_open mouth_small with dissolve
                "Ich ließ Aki in mein Haus rein."
                marcus "\"Willst du was zu trinken?\""
                show Aki eyes_closed mouth_laugh with dissolve
                aki "\"Mountain Dew!\""
                "Ich rollte meine Augen."
                marcus "\"Ernsthaft jetzt.\""
                show Aki eyes_open mouth_small with dissolve
                aki "\"Kaffee.\""
                marcus "\"OK.\""
                "Nachdem ich die Getränke vorbereitet habe, ging ich zu meinem Zimmer zurück."
                "Ich habe für mich auch ein Kaffee gemacht."
                show Aki eyes_closed mouth_laugh_teeth with dissolve
                aki "\"Mmmh! Danke Marcus~!\""
                "Sie nahm ein Schluck Kaffee und holte ein Stück Papier raus."
                marcus "\"Sind das die nuklearen Abschusscodes der USA?\""
                show Aki eyes_open mouth_laugh_teeth with dissolve
                aki "\"Ja! Joe Biden hat es mir geschenkt!\""
                marcus "\"Wie bitte was?!\""
                show Aki eyes_closed mouth_laugh_teeth with dissolve
                "Aki fing an zu lachen."
                aki "\"Hahahahahahahaha!\""
                aki "\"Dachtest du es wirklich?!\""
                "Verdammt."
                "Ich hasse mich."
                marcus "\"OK OK, was hast du denn da?\""
                show Aki eyes_open mouth_small with dissolve
                aki "\"Aufgaben.\""
                marcus "\"Was?\""
                aki "\"Na ja, ich habe Zuhause selbst noch ein bisschen am AcI geübt und ein Selbsttest geschrieben oder sowas in der Art.\""
                aki "\"Kannst du meine Sätze bitte für mich korrigieren?\""
                "Ich stöhnte."
                "Ich meine, ich habe eh nichts zu tun, also wieso nicht?"
                marcus "\"Na gut.\""
                show Aki eyes_closed mouth_laugh with dissolve
                aki "\"Yaaaaaay!\""
                marcus "\"Dabei machte sie einen kleinen Hüpfer.\""
                "Aki überreichte mir ein Blatt Papier."

                stop music fadeout 2.0
                queue music "audio/music/park.ogg" loop fadein 3.0

                menu:
                    with Dissolve(0.3)
                    "Sciunt hostes in patriam esse. - Die Feinde wussten, dass sie in deren Heimat waren."
                    "Richtig":
                        "Der Satz scheint richtig zu sein."
                    "Bezugsfehler - \"hostes\" ist der Subjektsakkusativ":
                        $ aki_affec += 1
                        "Aki scheint das Subjektsakkusativ falsch übersetzt zu haben."
                menu:
                    with Dissolve(0.3)
                    "Vidit alios in timore fuisse. - Er sah, dass anderen in Furcht waren."
                    "Richtig":
                        "Sollte nach meinem Wissen korrekt sein."
                    "Tempusfehler - \"fuisse\" muss in Plusquamperfekt übersetzt werden":
                        $ aki_affec += 1
                        "Ein recht kleiner Tempusfehler."
                        "Passiert dem Besten."
                menu:
                    with Dissolve(0.3)
                    "Audivimus multos patriam defendere. - Wir hörten, dass viele die Heimat beschützen."
                    "Richtig":
                        $ aki_affec += 1
                        "Yep, alles richtig."
                    "Bezugsfehler - \"patriam\" bezieht sich nicht auf \"defendere\"":
                        "Auf Bezugsfehler muss man halt aufpassen."
                        "Ein Bezugsfehler kann den Sinn eines Satzes sehr stark verändern."
                menu:
                    with Dissolve(0.3)
                    "Sciunt milites magnum periculum sustinere. - Sie wissen, dass die großen Soldaten die Gefahr aushalten."
                    "Richtig":
                        "Ist richtig. Glaube ich zumindest."
                    "Bezugsfehler - \"magnum\" bezieht sich auf \"periculum\"":
                        $ aki_affec += 1
                        "Huh. Schon wieder."
                menu:
                    with Dissolve(0.3)
                    "Audivimus copias in patriam vincere. - Wir hörten, dass die Truppen in der Heimat gewonnen haben."
                    "Richtig":
                        $ aki_affec += 1
                        "Gut genug."
                    "Tempusfehler - \"vincere\" ist vorzeitig":
                        "Ein kleiner Tempusfehler."
                        "Ich habe das falsche Wort durchgestrichen und ein neues aufgeschrieben."
                menu:
                    with Dissolve(0.3)
                    "Dicit sibi semper in tabernam stare. - Er sagt, dass er immer in das Gasthaus steht."
                    "Richtig":
                        $ aki_affec += 1
                        "Letzte Aufgabe richtig."
                    "Bezugsfehler - \"sibi\" bezieht sich auf \"tabernam\"":
                        "Auch ein Bezugsfehler."
                        "Aki sollte auf diese besonders aufpassen."
                
                "Ich habe alle Aufgaben noch mal durchgeguckt und gab Aki das Blatt wieder zurück."
                marcus "\"Du hast dich definitiv sehr viel verbessert, Aki.\""
                show Aki mouth_laugh with dissolve
                "Aki lachte."
                marcus "\"Aber noch ein bisschen Übung kann dir nichts Schlechtes tun.\""
                marcus "\"Wenn du Hilfe brauchst, kannst du immer mich fragen.\""
                show Aki eyes_closed
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
        "Es ist freitags, und ich war gerade dabei, den Clubraum aufzuräumen, als ich ein leichtes Klopfen an der Tür hörte."
        unknown "\"Hallo?\""
        marcus "\"Sie können hereinkommen.\""
        stop music fadeout 2.0
        "Die Tür öffnete sich langsam."
        queue music "audio/music/partizia.ogg" loop fadein 2.0
        marcus "\"Ach, Hallo, Partizia!\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Schön dich hier zu sehen, Marcus.\""
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Hättest du für einen ganz kurzen Moment Zeit?\""
        marcus "\"Klar.\""
        partizia "\"Dies ist bezüglich der Aufgabe, die du mir das letzte Mal gegeben hast.\""
        "Sie holte aus ihrer Tasche ein Heft heraus."
        partizia "\"Könntest du diese bitte für mich korrigieren?\""
        marcus "\"Ich sehe keinen Grund, wieso ich es nicht machen sollte.\""
        "Partizia überreichte mir ihr Heft."
        show Partizia mouth_happy with dissolve
        partizia "\"Danke sehr.\""
        "Ich öffnete ihr Heft."
        stop music fadeout 2.0
        queue music "audio/music/club.ogg" loop fadein 3.0
        show Partizia eyes_open mouth_small with dissolve
        menu:
            with Dissolve(0.3)
            "relinquere - relinctus"
            "Richtig":
                "Die Lösung ist anscheinend korrekt."
            "Falsch, richtig ist relictus":
                $ partizia_affec += 1
                "Ich strich die falsche Lösung durch und schrieb die Richtie auf."
        menu:
            with Dissolve(0.3)
            "ducere - ductum"
            "Richtig":
                $ partizia_affec += 1
                "Formen korrekt."
            "Falsch, richtig ist duxtum":
                "Ein basic Formenfehler. Passiert den Besten."
        menu:
            with Dissolve(0.3)
            "Graeci a Polyphemo capti in magno timore sunt. - Die Griechen, die vom Polyphemo gefangen worden waren, sind in großer Furcht."
            "Richtig":
                "Sollte richtig sein."
            "Tempusfehler - \"a Polyphemo capti\" muss im Präteritum übersetzt werden":
                $ partizia_affec += 1
                "Ein kleiner Tempusfehler hier, sonst scheint alles gut zu sein."
        menu:
            with Dissolve(0.3)
            "Ulixes solus socios relictos servare potuit. - Odysseus konnte alleine die zurückgelassenen Soldaten retten."
            "Richtig":
                $ partizia_affec += 1
                "Gut genug."
            "Falsch, Odysseus konnte die alleine zurückgelassenen Soldaten retten.":
                "Hmmm, kleiner Fehler."
        menu:
            with Dissolve(0.3)
            "Ulixes et socii Troiam interfecta reliquit. - Odysseus und die Soldaten vernichteten Troja, die verlassen worden war."
            "Richtig":
                "Das ist auch richtig."
            "Formfehler - \"reliquit\" ist ein Verb und auf \"Troiam\" bezieht sich \"interfecta\"":
                $ partizia_affec += 1
                "Ein Bezugsfehler. Ich streiche den Satz durch und habe es neu aufgeschrieben."
        menu:
            with Dissolve(0.3)
            "Viri uxores et liberos relictos desiderabant. - Die Männer sehnten auf die Ehefrauen und Kinder, obwohl sie zurückgelassen worden waren."
            "Tempusfehler -":
                "Scheint auch richtig zu sein."
            "Richtig, aber der Satz macht vom Inhalt her keinen Sinn":
                $ partizia_affec += 1
                "Hmmm..."
                "Der Satz ist von der Übersetzung her richtig, aber Partizia hat den Satz konzessiv übersetzt, was bei diesem Satz nicht möglich ist."
                "Ich notiere den letzten Fehler in ihr Heft."

        marcus "\"OK... Alles sollte jetzt richtig sein.\""
        "Ich gab ihr ihr Heft zurück."
        show Partizia mouth_small with dissolve
        partizia "\"Hmmm, ich sehe.\""
        show Partizia mouth_happy with dissolve
        partizia "\"Ein nochmals sehr großes Danke schön.\""
        marcus "\"Kein Problem, wir sind ja Klassenkameraden, ich denke, wir sollten uns helfen.\""
        "Parzitia zeigte mir ein Lächeln."
        show Partizia mouth_small with dissolve
        partizia "\"Hättest du noch einige Tipps für mich?\""
        marcus "\"Einfach viel üben. Du hast dich verglichen zum letzten Mal deutlich verbessert.\""
        "Partizia schaute auf ihre Uhr."
        partizia "\"Ach, sieh dir die Zeit an. Ich muss ganz schnell los. Ich habe noch was zu machen.\""
        "Wahrscheinlich Gedenken lesen üben."
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Und nein, ich übe zu Hause kein Gedanken lesen.\""
        "Warte was?"
        show Partizia eyes_closed mouth_laugh with dissolve
        partizia "\"Jedenfalls, schönes Wochenende noch.\""
        "Sie ging zügig aus der Tür raus, während sie mir hinterher gewinkt hat."
        "Was zum Teufel war das?"
        stop music fadeout 3.0
        scene Bg Load with fade