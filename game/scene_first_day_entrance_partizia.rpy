# add a custom noise channel
init python:
    renpy.music.register_channel('noise', "sound")

label firstDayEntrancePartizia:
    scene Bg School Entrance
    with dissolve
    play noise "audio/sfx/crowd_outdoors.ogg" loop fadein 4.0 volume 0.2
    "Als wir nach einer Weile am Eingang der Schule angekommen waren, habe wir noch ein bisschen rumgedadelt und gewartet."
    show Crowd with Dissolve(0.3)
    "Mittlerweile war eine riesige Menge von Schülern schon angekommen."
    pause 2
    play sound "audio/sfx/school_bell.ogg" volume 0.6
    "Endlich. Als die Glocke klingelte, ist die Menge in das Schulgebäude reingeströmt und wir machten uns auch langsam auf den Weg."
    scene Bg Main Staircase Lower Floor
    with fade
    pause 1
    scene Bg Hallway Staircase
    with fade
    pause 1
    scene Bg Hallway
    with fade
    pause 1
    show Crowd with Dissolve(0.3)
    "Wir wollten jetzt eigentlich in unsere Klassen, aber eine riesige Menge steht jetzt gerade in unseren Weg."
    aki "\"Och nee, was soll das denn?\""
    aki "\"Wenn wir hier nicht schnellstmöglich durchkommen, kommen wir noch zu spät zum Unterricht.\""
    "Solch eine Menge habe ich schon oft gesehen, und ich habe schon eine Ahnung, wass da passiert."
    unknown "\"Morgen, Marcus!\""
    stop noise fadeout 0.3
    stop music fadeout 3.0
    queue music "audio/music/partizia.ogg" fadein 2.0
    "Ich wusste es."
    marcus "\"Morgen, Partizia. Wie geht es dir?\""
    "Es ist Partizia, die Schulratsvorsitzende. Sie ist super beliebt unter Jungs und Mädchen."
    "Egal wo man sie sieht, ist sie immer von einer Menge umzingelt."
    "Sie ist genau das Gegenteil von mir."
    partizia "\"Yeah we got a number one victory royale\""
    