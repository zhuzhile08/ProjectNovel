label firstDayCafeteriaLunch:
    scene Bg Cafeteria Entrance with fade
    play noise "audio/sfx/crowd_indoors.ogg" loop fadein 4.0 volume 0.1
    queue music "audio/music/park.ogg" loop fadein 2.0 # yeah, it doesn't make sense but trust me, it works
    "Wir betreten die Cafeteria. Normalerweise wäre die ziemlich voll, aber da wir etwas später gekommen sind, ist sie etwas leerer als gewohnt."
    "Während Aki losging und uns ein Platz reservierte, schaute ich auf das Menü."
    scene Bg Menu with fade
    marcus "\"Yes! Pizza!\""
    food_list "\"Pizza Tuna, Pizza Margherita, Pizza Prosciutto e Fungi, Pizza Pugliese ...\""
    "Alles scheint gut und normal zu sein, bis ich nach unten gucke."
    food_list "\"Pizza Hawaii\""
    "Und so verdirbt man die Stimmung."
    "Ich meine Ananas auf Pizza?!"
    "Was soll das den?"
    "Wissen die nicht, dass Ananas auf Pizza absolut grässlich ist?"
    "So gern ich mich jetzt auch beim Chef beschweren möchte, habe ich einfach in aller Stille meine Lieblingspizza Pizza Margherita geholt."
    "Der Klassiker."
    menu:
        with Dissolve(0.3)
        "Welche Pizza soll ich für Aki Mitnehmen?"
        "Pizza Tuna":
            $ aki_affec += 4
            "Ich habe für Aki die Pizza Tuna bestellt, ihre Lieblingspizza."
        "Pizza Prosciutto e Fungi":
            $ aki_affec += 2
            "Etwas ungewöhnlicher für Aki, aber sie mag alle Sorten von Pizzen außer Pizza HawaIi."
        "Pizza Pigliese":
            $ aki_affec += 3
            "Ich glaube das war Aki's Lieblingspizza. Oder zumindest etwas ähnliches."
        "Pizza Hawaii":
            "Ich habe die Pizza Hawaii bestellt."
            "Damit machte ich mich mit zwei Tablets auf den Weg."
            "Man muss nicht so hart bei Aki schauen, wenn man sie suchen will, ihre Haare sind auffälliger als eine Mülltonne im Heuhaufen."
            "Woher ich diesen Vergleich habe, weiß ich auch nicht."
            scene Bg Cafeteria with fade
            show Aki
            aki "\"Marcus, welche Pizza hast du für mich genommen?\""
            marcus "\"Ich habe dir die Pizza Hawaii bestellt.\""
            stop noise fadeout 1.0
            stop music fadeout 1.0
            show Aki eyebrows_angry mouth_big with dissolve
            "Sie sah auf die Pizza Hawaii in meinen Händen"
            "Aki wurde auf einmal blass."
            aki "\"Ich hasse dich!\""
            "Damit stürmte Aki aus der Cafeteria heraus."
            hide Aki with moveoutright
            scene Bg Load with fade
            jump credits
    "Ich machte mich mit zwei Tablets auf den Weg."
    "Man muss nicht so hart bei Aki schauen, wenn man sie suchen will, ihre Haare sind auffälliger als eine Mülltonne im Heuhaufen."
    "Woher ich diesen Vergleich habe, weiß ich auch nicht."
    scene Bg Cafeteria with fade
    show Aki
    aki "\"Marcus, welche Pizza hast du für mich genommen?\""
    marcus "\"Weißt du, ich habe dir die Pizza Hawaii bestellt.\""
    show Aki eyebrows_angry mouth_big with dissolve
    "Aki wurde auf einmal blass."
    "Ehrlich gesagt, ich habe auch was hochkommen spüren, als ich auch nur das Wort gesagt habe."
    marcus "\"Nene, war ein Witz.\""
    show Aki mouth_angry with dissolve
    aki "\"Das war aber fies! Versprichs, dass du es nie wieder machst!\""
    marcus "\"Jaja, schon gut.\""
    "Sie handelt manchmal wie ein Kindergartenkind."
    "Und das war auch das 420ste mal, dass ich so sowas in der Art versprochen habe."
    "Wie man sehr gut sieht, halte ich mich nicht wirklich daran."
    marcus "\"Na ja, Guten Appetit!\""
    show Aki eyebrows_sad mouth_sad with dissolve
    aki "\"Ich weiß nicht, ob ich noch Appetit habe, nachdem du Pizza Hawaii erwähnt hast.\""
    marcus "\"Was?!\""
    show Aki eyebrows_neutral eyes_closed mouth_laugh_teeth with dissolve
    "Aki fing an zu kichern."
    aki "\"Hahaha, dachtest du das wirklich?! Jetzt weißt du wie es sich anfühlt, wenn man mit \'Sarkasmus\' reingelegt wird!\""
    "Ehrlich gesagt, weiß ich nicht, ob ich mich freuen sollte oder nicht."
    "Einerseits hat sie endlich Sarkasmus gecheckt, andererseits wurde ich gerade so mies reingelegt."
    show Aki eyes_closed mouth_laugh with dissolve
    aki "\"Komm, sei nicht so mies drauf, deine Pizza wartet noch auf dich! Fufufufufu~\""
    scene Bg Load with fade
    pause 3.0
    scene Bg Cafeteria with fade # I need the cafeteria entrance here
    show Aki eyebrows_neutral eyes_closed mouth_laugh_teeth with dissolve
    aki "\"Ich bin absolut gestopft!\""
    marcus "\"Ebenso\""
    show Aki eyebrows_neutral eyes_open mouth_small with dissolve
    aki "\"Hast du nicht irgendetwas mit deinen Club oder so gesagt?\""
    marcus "\"Was?\""
    aki "\"Na ja, dass du irgendwie dorthin musstest.\""
    "Das habe ich komplett vergessen."
    marcus "\"Ach ja! Danke, dass du mich daran erinnert hast!\""
    marcus "\"Ich glaube ich muss jetzt langsam los.\""
    show Aki mouth_happy
    aki "\"Keine Sorge, ich kann mich ums Auffäumen kümmern. Viel Spaß beim Club noch!\""
    marcus "\"Danke Aki! Bis Später\""
    "Ich winkte ihr hinterher und sie tat das selbe. Danach machte ich auf den Weg zu unseren Clubraum."
    scene Bg Load with fade
    stop noise fadeout 1.0
    stop music fadeout 3.0
