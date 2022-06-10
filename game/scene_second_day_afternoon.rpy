label secondDayAfternoon:
    pause 4.0
    scene Bg Cafeteria with fade
    play noise "audio/sfx/crowd_indoors.ogg" loop fadein 4.0 volume 0.05
    queue music "audio/music/park.ogg" loop fadein 2.0
    "Nach 3 harten Unterrichtsstunden von Mathe, Deutsch und Bio bin ich EEEEEENDLIIICH frei!"
    "Naja, für die Mittagspause zumindest."
    if aki_route == True:
        "Mein Mittagsessen mit Aki war recht normal, wir haben uns über alles mögliche unterhalten."
        "Aki scheint heute aber etwas zu sehr nervös zu sein."
        marcus "\"Hey, es gibt keinen Grund so nervös zu sein!\""
        marcus "\"Lass jetzt einfach unser Essen genießen.\""
        marcus "\"Wenn du etwas hast, kannst du immer mir bescheid sagen.\""
        aki "\"Naja, du weißt schon, meine Beziehung mit AcIs, wie kann ich da nicht nervös sein?!\""
        "Darauf habe ich auch keine Antwort mehr."
        "Aki scheint das Konzept von AcIs nicht zu verstehen, obwohl das viel einfacher ist als PCs."
        "Naja, was kann ich denn als jemand der beides verstehet sagen?"
    if partizia_route == True:
        "Aki hat sich anscheinend krank gemeldet."
        "Ich kann irgendwie verstehen wieso, aber gleichzeitig auch nicht."
        "Aki hat wahrscheinlich Angst vor den Testergebnissen und hat nicht gut geschlafen."
        "Aber das Thema war PCs, ich kann nicht verstehen wieso sie Angst haben soll, sie ist ein Weltmeister darin."
        "Einmal alleine Mittag zu essen ist ja auch nicht schlecht."
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
    "Die Stunde ist gerade zu Ende gegangen und wir haben unsere Testergebnisse zurückbekommen."
    "Ich schaute mit großer Hoffnung auf meine Note."
    if test_score >= 11:
        marcus "\"YES!\""
        "Habe nichts anderes erwartet."
        "Eine eins wie immer."
    if 10 >= test_score >= 8:
        "Gut genug!"
        "Es war leicht enttäuschend, dass ich keine Eins gekriegt habe, aber was solls?"
        "Ist immer noch eine zwei."
    if 7 >= test_score >= 6:
        "Mmmmmmh, unkomfortabel."
        "Meine Note war... unnormal \"schlecht\"."
        "Ich meine, über eine drei können sich viele freuen, aber ich nicht wirklich."
        "Naja, hauptsache ich habe den Test bestanden."
        "Trotzdem ändert es nichts, dass es mir jetzt ziemlich blöd geht."
    if test_score < 6:
        stop music fadeout 1.0
        "Was?"
        "Nein oder?"
        "Ich kann es nicht fassen..."
        "Das muss ein Fehler sein, oder?"
        "Eine..."
        "..."
        scene black with dissolve
        "Jeder wird mal Fehler machen."
        "Es ist unvermeidbar."
        "Jeder wird mal von seinen Thron fallen."
        "Es ist unvermeidbar."
        "Es ist natürlich."
        "Man kriegt immer eine zweite Chance."
        "Also komm..."
        "Versuchs nochmal."
        jump credits

    if aki_route == True:
        "Ich ging aus neugier zu Akis Platz."
        marcus "\"Hey, Aki!\""
        "Aki schien sehr aufgeregt zu sein."
        aki "\"Rate mal.\""
        marcus "\"Was?\""
        aki "\"Na. meine Note!\""
        marcus "\"Kein Plan.\""
        aki "\"Eine Vier!\""
        "Wie man sich über sowas freuen kann, das weiß ich nicht."
        "Aber naja, wenn sie eine Sechs erwartet hätte, kann ich es schon verstehen."
        aki "\"Gut ist es jetzt aber auch nicht.\""
        marcus "\"Das sehe ich.\""
        aki "\"Aber bestanden ist bestanden!\""
        "Ihr Gesicht glänzte vor Stolz, aber irgendwo kann ich auch ein Hauch von Enttäuschung sehen."
    if partizia_route == True:
        "Der Leher hat mir auch Akis Test gegeben, weil sie heute nicht anwesend war."
        "Ich sollte es ihr geben, wenn ich sie treffe"
    
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
                aki "\"Yay!\""
                "Sie machte ein ganz kleinen Hüpfer in die Luft"
                "Wir haben beide unsere Sachen gepackt und sind zusammen nach Hause gegangen, während wir unsere Testergebnisse diskutiert haben."
            "\"Tut mir leid, nein.\"":
                marcus "\"Tut mir leid, nein.\""
                "Manchmal habe ich auch kein Bock und will alleine sein."
                "Und heute ist solch ein Tag."
                aki "\"Wieso denn?\""
                "Aki guckte mich ganz traurig an."
                marcus "\"Ehhm, ich habe also eeh... zuhause noch etwas zu tun! Genau!\""
                "Ich bin ein verdammt schlechter Lügner"
                aki "\"Wenn du es so meinst.\""
                "Ich habe meine Sachen gepackt und bin dann alleine nach Hause gegangen."
    if partizia_route == True:
        "Endlich!"
        "Ich habe meine Sachen gepackt und bin dann nach Hause gegangen."

    scene Bg Load with fade
    stop noise fadeout 2.0
    stop music fadeout 6.0
    "Nachdem ich zuhause angekommen bin, habe ich mich sofort in Bett gelegt."
    "Dieser Tag war anstrengend, aber morgen ist ja Samstag."
    "Eine Weile später bin ich in aller Ruhe eingeschlafen."

    scene Bg Load with fade
