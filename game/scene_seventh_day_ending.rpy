label seventhDayEnding:
    pause 5.0
    scene Bg Load with fade
    queue music "audio/music/ending.ogg" loop fadein 10.0
    "Eine Weile ist schon vergangen."
    "Nach den Abiturprüfungen ist alles wieder normal geworden."
    "Endlich können wir uns wieder ausruhen."
    "Unsere Zeugnisse wurden schon ausgeteilt."
    "Meins war exzellent, wie immer."
    "Ich habe mich für einen Studienplatz in Oxford beworben, und wurde sogar angenommen."
    if aki_route == True:
        "Na gut, der die Aufnahmeprüfung liegt immer noch vor mir, aber es ist ein Schritt in die richtige Richtung."
        "Heute ist der Tag, an dem ich nach Großbritannien abreisen sollte."
        "Also wollte ich noch ein letztes Mal zu Aki gehen und mich bei ihr verabschieden."
        if aki_affec >= 45:
            show Bg Aki House with fade
            "Ich ging zu Aki's Haus und klopfte an ihrer Tür an."
            "Ich habe auf diesen Moment mein ganzes Leben gewartet."
            marcus "\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKIIIIIIIIIIIIIIIIIIIIIIII!\""
            aki "\"Marcus?\""
            "Aki guckte oben aus dem Fenster heraus."
            marcus "\"Ja.\""
            aki "\"Hi!\""
            aki "\"Ich mache dir mal die Tür auf.\""
            "Aki rannte nach unten."
            show Aki outfit_casual left_casual right_casual eyes_closed mouth_laugh_teeth with dissolve
            aki "\"Und? Wie gehts?\""
            marcus "\"Gut genug.\""
            marcus "\"Aber ich habe noch etwas Wichtigeres.\""
            show Aki eyes_open mouth_small with dissolve
            aki "\"Hmm?\""
            marcus "\"Ich werde heute nach Großbritannien ziehen, um dort zu studieren.\""
            marcus "\"Habe mich an Oxford beworben.\""
            show Aki eyebrows_sad mouth_happy with dissolve
            "Aki guckte ganz traurig."
            aki "\"Danke, dass du es mir gesagt hast.\""
            aki "\"Ich habe auch noch etwas.\""
            marcus "\"Was?\""
            show Aki eyebrows_neutral eyes_closed mouth_laugh_teeth with dissolve
            aki "\"Ich wurde auch an Oxford angenommen!\""
            "Du machst Witze!"
            "Was?!"
            show Aki eyes_open mouth_happy with dissolve
            aki "\"Ich reise tatsächlich auch heute ab.\""
            aki "\"Ich wollte gerade bei dir vorbeikommen, um mich zu verabschieden!\""
            "Unfassbar."
            "Danke Gott."
            "Danke, dass ich mich nicht jetzt von Aki verabschieden muss."
            marcus "\"Dank Gott!\""
            marcus "\"Ich dachte, dass das das letzte Mal wäre, dass ich dich sehen werde!\""
            show Aki eyes_closed mouth_laugh with dissolve
            aki "\"Ist es aber nicht!\""
            "Man kann nicht beschreiben, wie unfassbar glücklich ich gerade bin."
            show Aki eyes_open mouth_small with dissolve
            aki "\"Achso, und ich habe auch noch etwas.\""
            marcus "\"Was?\""
            show Aki eyebrows_sad mouth_smile with dissolve
            aki "\"Marcus ...\""
            stop music fadeout 3.0
            jump credits
        if 45 > aki_affec:
            show Bg Aki House with fade
            "Ich ging zu Aki's Haus und klopfte an ihrer Tür an."
            "Ich habe auf diesen Moment mein ganzes Leben gewartet."
            marcus "\"AAAAAAAAAAAAAAAAAAAAAAAKIIIIIIIIIIIIIIIIIIII!\""
            "Keiner antwortete."
            "Ich klopfte nochmals an ihrer Tür."
            "Nichts."
            "Na ja, vielleicht ist Aki gerade weg."
            "Vielleicht versuche ich es gleich noch einmal."
            "Ich wollte sie nur noch einmal sehen, bevor ich wegziehe."
            "Weil ich ..."
            stop music fadeout 3.0
            jump credits
    if partizia_route == True:
        "Ich war schon eine Weile in Großbritannien und warte gerade auf die Ergebnisse meiner Annahmeprüfung."
        "Ich hoffe, dass es gut gehen wird."
        "Heute habe ich ein Brief im Briefkasten bekommen."
        "Aber es waren keine Prüfungsergebnisse, sondern ein Brief von Partizia."
        "Ich öffnete es und vor mir stand:"
        partizia "Lieber Marcus, "
        partizia "Ich hoffe, dir geht es gut. Mir auf jeden Fall."
        partizia "Ich habe gehört, dass du bei Oxford angenommen wurdest."
        if partizia_affec >= 36:
            partizia "Ich wurde an der UCL angenommen."
            partizia "Also leben wir gar nicht so weit voneinander entfernt."
            partizia "Vieleicht kann ich dich irgendwann mal besuchen."
            "Reiner Zufall."
        "Ich habe den langen Brief noch zu Ende gelesen."
        partizia "Ich wünsche dir noch viel Glück im Leben!"
        partizia "Ich würde mich auf eine Antwort von dir freuen!"
        partizia "Viele Grüße, "
        partizia "Partizia."
        if partizia_affec >= 36:
            "Als ich den Brief umdrehte, bemerkte ich, dass auf der Rückseite auch was stand."
            partizia "p.s."
            partizia "Ach ja, ich muss dir noch unbedingt was sagen:"
            partizia "Ich ..."
            stop music fadeout 3.0
            jump credits
        if 36 > partizia_affec:
            "Ich schloss meine Augen und dachte über alles nach, was wir zusammen gemacht haben."
            "Danke, Partizia."
            "Danke für die schönen Erinnerungen, die du mir geschenkt hast."
            "Ich werde dich immer in meinen Herzen behalten."
            stop music fadeout 3.0
            jump credits

    scene Bg Load with fade
    stop music fadeout 3.0
    jump credits
