label firstDayClassroomSleep:
    scene Bg Classroom with fade
    play noise "audio/sfx/crowd_outdoors.ogg" loop fadein 4.0 volume 0.2
    "Ich saß, wie üblich, in meiner Ecke im Klassenraum."
    "Aki saß in der anderen Ecke, direkt neben der Tür."
    "Wenn sie nehen mir säße, würde sie mich jetzt gerade volllabern."
    "Aber mir gefällt es aus irgendeinen Grund, wenn sie es tut."
    pause 2.0
    unknown "\"Guten Morgen!\""
    stop noise fadeout 1.0
    class "\"Guten Morgen Herr Bratfisch.\""
    "Das sagte die Klasse, wie immer bei jeden Lehrer im der klassischen und mototonen Stimme."
    "Kein Witz, das ist wirklich sein Name. Ist aber eigentlich ein ganz netter Typ. Sein Unterricht kann nur etwas langweilig sein."
    "Informatik ist nicht so mein Ding."
    "Herr Bratfisch legte seine Sachen neben den Pult ab und fing an zu reden."
    teacher "\"Heute reden wir weiter über Hashmaps. Kann jeder noch erklären was Hashmaps sind?\""
    unknown "\"Ich, ich, Herr Bratfisch!\""
    teacher "\"Ja?\""
    unknown "\"Hashmaps sind eine spezielle Indexstruktur, wo man effizient in großen Datenmengen Daten durch deren Indexes suchen und finden kann.\""
    unknown "\"Hashmaps funktionieren mit einen Hash-Algorythmus, der...\""
    stop music fadeout 13.0
    "Ich fühlte schon, wie ich wegdöste."
    "Hashmaps, Hash Algorythmus, das geht mir völlig übers Kopf."
    "Das letzte mal, wo wir selber eine machen sollten, war meine in Geschwidingkeit der Vorletzte."
    "Zumindest habe ich es geschafft, eine zu machen, im Gegensatz zu Aki."
    "Naja, ich kann eh nicht hoffen, das alles zu verstehen, also kann ich auch einmal schlafen gehen."
    scene Bg Load
    with irisin
    pause 4.0
    play music "audio/music/school_way.ogg" loop fadein 7.0
    unknown "\"Marcus?\""
    unknown "\"Maarcus?\""
    unknown "\"Marcus, wach auf!\""
    unknown "\"MAAAAAAAAAAAARRRRCUUUUUUUUUUS!\""
    scene Bg Classroom
    with irisout
    show Aki eyebrows_sad mouth_big with dissolve
    marcus "\"Was?\""
    "Ich sah Aki vor meinen Tisch stehen."
    aki "\"Marcus, du hast den ganzen Unterricht durchgeschlafen!\""
    marcus "\"Ach was?!\""
    aki "\"Wirklich!\""
    "Aki versteht absolut kein Sarkasmus, obwohl ich immer so rede, welches ein bisschen nerfig sein kann."
    marcus "\"Nene, ich weiß schon. War Sarkasmus.\""
    show Aki eyebrows_neutral mouth_small with dissolve
    aki "\"Hmpf. Jedenfalls, willst du mit mir Essen gehen?\""
    menu:
        with Dissolve(0.3)
        "Soll ich mit Aki essen gehen?"

        "Ja":
            $ aki_affec += 4
            marcus "\"Ich meine, wieso nicht?\""
            show Aki eyes_closed mouth_laugh_teeth with dissolve
            "Im Aki's Gesicht war ein stolzes Lächeln aufgetaucht."
            aki "\"Yipee!\""
            aki "\"Dann auf in die Cafeteria!\""
            scene Bg Load with fade
            stop music fadeout 3.0
            jump firstDayCafeteriaLunch
        "Nein":
            $ partizia_affec += 4
            marcus "\"Tut mir leid, wie schon gesagt, heute muss ich mich mit den Club ein bisschen beschäftigen\""
            show Aki eyebrows_sad mouth_laugh with dissolve
            aki "\"Hehe. OK, dann das nächste Mal.\""
            "Man muss nicht ein Psychologe sein, um zu erkennen, dass es Aki gerade ziemlich schlecht geht."
            "Jetzt fühle ich mich wie ein richtiges Arschloch, aber was solls, der Test ist mir immer noch wichtiger."
            "Aki ging aus der Klasse heraus und ich folge ihr kurz später."
            scene Bg Load with fade
            stop music fadeout 3.0
            return
    