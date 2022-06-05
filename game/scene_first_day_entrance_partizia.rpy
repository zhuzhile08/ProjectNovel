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
    partizia "\"Hast du Heute während der Mittagspause Zeit?\""
    marcus "\"Wieso?\""
    partizia "\"Wegen den Lateintest.\""
    "Ach ja, sie ist auch ein Mitglied vom Lateinclub."
    partizia "\"Ich brauche noch ein Bisschen Hilfe bei PCs.\""
    marcus "\"Nein, tut mir leid, leider nicht.\""
    partizia "\"Hmm, du willst also Zeit mit A...\""
    "Bevor sie ihren Satz vollendet hat, wurde sie von der Menge schon weggeschoben."
    partizia "\"Eeh, vergiss es. Bis später, Markus!\""
    stop music fadeout 4.0
    hide Crowd with moveoutright
    queue music "audio/music/class.ogg" fadein 2.0
    "Bevor ich noch Antworten konnte, war sie schon aus meiner Sichtweite raus."
    "Beliebt zu sein hat seine Nachteile."
    "Früher war ich noch ganz neidisch, wenn einer beliebt war, aber heutzutage gefällt es mir doch mehr, wie ein NPC in Videospielen zu sein: "
    "Nämlich unauffälliger als ein Blatt am Baum."
    "Als ich nach links geguckt habe, sah ich dass Aki etwas komisch drauf war."
    marcus "\"Hast du was auf den Herzen, Aki?\""
    "Aki war völlig abwesend und in ihren Gedanken versunken."
    marcus "\"Boo!\""
    aki "\"Waaaaaaaaah!\""
    aki "\"Erschreck mich doch nicht so, Markus!\""
    aki "\"Was ist denn los?\""
    marcus "\"Wie schon gesagt, hast du was auf den Herzen, Aki?\""
    aki "\"Eeeh, nein, nichts.\""
    "Irgendwas war an dieser Aussage faul, aber ich habe mich dafür nicht mehr wirklich interessiert."
    scene Bg Load
    "Und damit machten wir uns auf den Weg zu unseren Klassenraum."
    pause 2.0

    