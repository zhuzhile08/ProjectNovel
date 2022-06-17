label secondDayAfternoon:
    pause 4.0
    scene Bg Cafeteria with fade
    play noise "audio/sfx/crowd_indoors.ogg" loop fadein 4.0 volume 0.05
    queue music "audio/music/park.ogg" loop fadein 2.0
    "Nach 3 harten Unterrichtsstunden von Mathe, Deutsch und Bio bin ich EEEEEENDLIIICH frei!"
    "Na ja, für die Mittagspause zumindest."
    if aki_route == True:
        show Aki eyebrows_sad with dissolve
        "Mein Mittagsessen mit Aki war recht normal, wir haben uns über alles Mögliche unterhalten."
        "Aki scheint heute aber etwas zu sehr nervös zu sein."
        marcus "\"Hey, es gibt keinen Grund so nervös zu sein!\""
        marcus "\"Lass jetzt einfach unser Essen genießen.\""
        marcus "\"Wenn du etwas hast, kannst du immer mir Bescheid sagen.\""
        aki "\"Du weißt schon, meine Beziehung mit AcIs, wie kann ich da nicht nervös sein?!\""
        "Darauf habe ich auch keine Antwort mehr."
        "Aki scheint das Konzept von AcIs nicht zu verstehen, obwohl das viel einfacher ist als Pcs."
        "Na ja, was kann ich denn als jemand, der beides versteht sagen?"
    if partizia_route == True:
        "Aki hat sich anscheinend krankgemeldet."
        "Ich kann irgendwie verstehen, wieso, aber gleichzeitig auch nicht."
        "Aki hat wahrscheinlich Angst vor den Testergebnissen und hat nicht gut geschlafen."
        "Aber das Thema war Pcs, ich kann nicht verstehen, wieso sie Angst haben soll, sie ist ein Weltmeister darin."
        "Einmal alleine Mittag zu essen, ist ja auch nicht schlecht."
    scene Bg Load with fade
    pause 2.0
    scene Bg Cafeteria with fade
    "Das Essen heute war so gut wie immer."
    "Ich gucke auf die Uhr und bemerke, dass die nächste Stunde in 10 Minuten anfängt."
    "Jetzt haben wir Latein, und ich bin recht angespannt auf die Testergebnisse."
    "Ich glaube, ich kann mich schon mal auf den Weg machen."
    stop noise fadeout 1.0
    scene Bg Load with fade
    stop music fadeout 3.0
    pause 3.0
    queue music "audio/music/class.ogg" loop fadein 2.0
    scene Bg Classroom with fade
    "Die Stunde ist gerade geendet und wir haben unsere Testergebnisse zurückbekommen."
    "Ich schaute mit großer Hoffnung auf meine Note."
    if test_score >= 11:
        marcus "\"YES!\""
        "Habe nichts anderes erwartet."
        "Eine Eins wie immer."
    if 10 >= test_score >= 8:
        "Gut genug!"
        "Es war leicht enttäuschend, dass ich keine Eins gekriegt habe, aber was soll's?"
        "Ist immer noch eine Zwei."
    if 7 >= test_score >= 6:
        "Mmmmmmh, unkomfortabel."
        "Meine Note war ... unnormal \"schlecht\"."
        "Ich meine, über eine Drei können sich viele freuen, aber ich nicht wirklich."
        "Na ja, Hauptsache ich habe den Test bestanden."
        "Trotzdem ändert es nichts, dass es mir jetzt ziemlich blöd geht."
    if test_score < 6:
        stop music fadeout 1.0
        "Was?"
        "Nein oder?"
        "Ich kann es nicht fassen ..."
        "Das muss ein Fehler sein, oder?"
        "Eine ..."
        " ..."
        scene black with dissolve
        "Jeder wird mal Fehler machen."
        "Es ist unvermeidbar."
        "Es ist natürlich."
        "Man bekommt immer eine zweite Chance."
        "Also komm ..."
        "Versuch es nochmal."
        jump credits

    if aki_route == True:
        "Ich ging aus Neugier zu Akis Platz."
        marcus "\"Hey, Aki!\""
        "Aki schien sehr aufgeregt zu sein."
        show Aki eyes_closed mouth_laugh_teeth with dissolve
        aki "\"Rate mal.\""
        marcus "\"Was?\""
        show Aki eyes_closed mouth_laugh with dissolve
        aki "\"Na, meine Note!\""
        marcus "\"Kein Plan.\""
        show Aki eyes_open mouth_happy with dissolve
        aki "\"Eine Vier!\""
        "Wie man sich über sowas freuen kann, das weiß ich nicht."
        "Aber gut, wenn sie eine Sechs erwartet hätte, kann ich es schon verstehen."
        show Aki eyebrows_sad mouth_small with dissolve
        aki "\"Gut ist es jetzt aber auch nicht.\""
        marcus "\"Das sehe ich.\""
        show Aki eyes_closed mouth_laugh_teeth with dissolve
        aki "\"Aber bestanden ist bestanden!\""
        "Ihr Gesicht glänzte vor Stolz, aber irgendwo kann ich auch ein Hauch von Enttäuschung sehen."
    if partizia_route == True:
        "Der Lehrer hat mir auch Akis Test gegeben, weil sie heute nicht anwesend war."
        "Ich sollte es ihr geben, wenn ich sie treffe."
    
    show Aki eyebrows_neutral eyes_open mouth_small with dissolve
    pause 2
    stop music fadeout 2.0
    queue music "audio/music/park.ogg" loop fadein 2.0
    play sound "audio/sfx/school_bell.ogg" volume 0.6
    teacher "\"Die Stunde ist hiermit beendet. Ihr könnt eure Sachen packen. Ich wünsche euch noch ein schönes Wochenende!\""
    play noise "audio/sfx/crowd_indoors.ogg" loop fadein 1.0 volume 0.3

    if aki_route == True:
        aki "\"Wollen wir zusammen nach Hause gehen?\""
        menu:
            with Dissolve(0.3)
            "Soll ich?"
            "\"Ja\"":
                $ aki_affec += 4
                marcus "\"Ja.\""
                show Aki eyes_closed mouth_laugh_teeth with dissolve
                aki "\"Yay!\""
                "Sie machte einen ganz kleinen Hüpfer in die Luft."
                "Wir haben beide unsere Sachen gepackt und sind zusammen nach Hause gegangen, während wir unsere Testergebnisse diskutiert haben."
            "\"Tut mir leid, nein.\"":
                marcus "\"Tut mir Leid, nein.\""
                show Aki eyebrows_sad mouth_sad with dissolve
                aki "\"Wieso denn?\""
                "Aki guckte mich ganz traurig an."
                marcus "\"Ehhm, ich habe also eeh ... zu Hause noch etwas zu tun! Genau!\""
                "Ich bin ein verdammt schlechter Lügner."
                aki "\"Wenn du es so meinst.\""
                "Ich habe meine Sachen gepackt und bin dann alleine nach Hause gegangen."
    if partizia_route == True:
        "Endlich!"
        "Ich habe meine Sachen gepackt und bin dann nach Hause gegangen."
        scene Bg Load with fade
        stop noise fadeout 2.0
        scene Bg School Entrance with fade
        "Als ich am Schuleingang angekommen bin, sah ich Partizia, wie sie selber auf den Bänken saß."
        stop music fadeout 5.0
        "Sie winkte mir hinterher."
        "Ich glaube, dass sie will, dass ich zu ihr rüberkomme."
        queue music "audio/music/partizia.ogg" loop fadein 3.0
        marcus "\"Ach, Hallo, Partizia!\""
        show Partizia mouth_happy eyes_closed with dissolve
        partizia "\"Hallo, Marcus! Zum Glück hast du mich bemerkt. Wie geht es dir?\""
        marcus "\"Eigentlich ganz gut.\""
        "Normalerweise redet Partizia nur im Club mit mir und nur wenn es nötig ist."
        "Daher bin ich jetzt leicht überrascht."
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Könntest du mir bitte einen Gefallen tun?\""
        marcus "\"Ja, klar. Wieso nicht?\""
        "Normalerweise fragt mich sowas nur Aki."
        partizia "\"Danke sehr. Kannst du nun bitte 200 Euro mir überreichen?\""
        marcus "\"Was?\""
        show Partizia eyes_closed mouth_laugh with dissolve
        "Partizia fand das aber eher lustiger als es bei mir rübergekommen ist und fing an zu kichern."
        partizia "\"Nein, das war ein Scherz. Eigentlich wollte ich fragen, ob du mir Nachhilfe für Latein geben kannst?\""
        "Anscheinend ist sie recht humorvoll, was ich von ihr nicht erwartet hätte."
        "Und Nachhilfe? Für Partizia? Das habe ich mir nicht wirklich vorgestellt."
        "Da finde ich die 200 Euro sogar wahrscheinlicher."
        marcus "\"Klar. Welches Thema denn?\""
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Pcs.\""
        marcus "\"Alles klar.\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Danke sehr. Ich hätte nichts anderes von dir erwartet.\""
        show Partizia eyes_open mouth_small with dissolve
        partizia "\"Wie wärs, nächsten Montag im Clubraum?\""
        marcus "\"Da sehe ich kein Problem. Alle anderen Clubmitglieder haben sich abgemeldet.\""
        partizia "\"Ich weiß.\""
        marcus "\"Dann ist es so abgeschlossen. Ich warte dann nächsten montagnachmittags um 16 Uhr im Clubraum auf dich.\""
        partizia "\"Danke. Ach ja, wieso ist Aki heute nicht da? Normalerweise würde sie immer neben dir nach Hause gehen.\""
        marcus "\"Sie hat sich krankgemeldet.\""
        partizia "\"Achso.\""
        show Partizia eyes_closed mouth_happy with dissolve
        partizia "\"Auf Wiedersehen! Ich wünsche dir ein schönes Wochenende.\""
        hide Partizia with moveoutleft
        "Damit eilte sie zum Hinterausgang der Schule und verschwand kurz danach aus meinem Sichtfeld."
        "Verdammt, jetzt werden alle Jungs aus meiner Klasse neidisch, da ich das beliebteste Mädchen in der Schule Nachhilfe gebe."
        "Als ich mich auch auf den Weg gemacht habe, dachte ich mir, wie Partizia das alles wusste."
        "Nicht viele wissen, dass ich und Aki befreundet sind, und weniger wissen, dass wir zusammen nach Hause gehen."
        "Na gut, was soll's, sie ist die Studentenratsleiterin, sie hat wahrscheinlich ihre eigenen Methoden, um das herauszufinden."
        "Und damit ging ich langsam nach Hause."

    scene Bg Load with fade
    stop noise fadeout 2.0
    stop music fadeout 6.0
    "Nachdem ich zu Hause angekommen bin, habe ich mich sofort ins Bett gelegt."
    "Dieser Tag war anstrengend, aber morgen ist ja Samstag."
    "Eine Weile später bin ich in aller Ruhe eingeschlafen."

    if aki_route == True:
        jump thirdDayParkTutorRequest
