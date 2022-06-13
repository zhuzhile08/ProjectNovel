# add a custom noise channel
init python:
    renpy.music.register_channel('noise', "sound")

label firstDayEntrancePartizia:
    scene Bg School Entrance with fade
    play noise "audio/sfx/crowd_outdoors.ogg" loop fadein 4.0 volume 0.2
    "Als wir nach einer Weile am Eingang der Schule angekommen waren, haben wir noch ein bisschen rumgedadelt und gewartet."
    show Crowd with Dissolve(0.3)
    "Mittlerweile war eine riesige Menge von Schülern schon angekommen."
    pause 2
    play sound "audio/sfx/school_bell.ogg" volume 0.6
    "Endlich. Als die Glocke klingelte, ist die Menge in das Schulgebäude reingeströmt und wir machten uns auch langsam auf den Weg."
    scene Bg Main Staircase Lower Floor with fade
    pause 1
    scene Bg Hallway Staircase with fade
    pause 1
    scene Bg Hallway with fade
    pause 1
    show Crowd with Dissolve(0.3)
    "Wir wollten jetzt eigentlich in unsere Klasse, aber eine riesige Menge steht jetzt gerade in unseren Weg."
    show Aki eyebrows_angry mouth_big with dissolve
    aki "\"Och nee, was soll das denn?\""
    aki "\"Wenn wir hier nicht schnellstmöglich durchkommen, kommen wir noch zu spät zum Unterricht.\""
    "Solch eine Menge habe ich schon oft gesehen, und ich habe schon eine Ahnung, was da passiert."
    show Aki eyebrows_neutral mouth_small:
        xalign 0.5
        linear 1.0 xalign 0.1
    with dissolve
    unknown "\"Morgen, Marcus!\""
    stop noise fadeout 0.3
    stop music fadeout 3.0
    queue music "audio/music/partizia.ogg" loop fadein 2.0
    "Ich wusste es."
    marcus "\"Morgen, Partizia. Wie geht es dir?\""
    show Partizia with dissolve
    "Es ist Partizia, die Studentenratsvorsitzende. Sie ist super beliebt unter Jungs und Mädchen."
    "Egal wo man sie sieht, ist sie immer von einer Menge umzingelt."
    "Sie ist genau das Gegenteil von mir."
    partizia "\"Hast du Heute während der Mittagspause Zeit?\""
    marcus "\"Wieso?\""
    partizia "\"Wegen dem Lateintest.\""
    "Ach ja, sie ist auch ein Mitglied vom Lateinclub und eine meiner Klassenkameradin."
    "Auch wenn sie sehr oft nicht anwesend ist."
    partizia "\"Ich brauche noch ein bisschen Hilfe bei PCs.\""
    marcus "\"Nein, tut mir leid, leider nicht.\""
    partizia "\"Hmm, du willst also Zeit mit A...\""
    "Bevor sie ihren Satz vollendet hat, wurde sie von der Menge schon weggeschoben."
    show Partizia eyes_closed eyebrows_sad mouth_laugh with dissolve
    partizia "\"Eeh, vergiss es. Bis später, Marcus!\""
    stop music fadeout 4.0
    hide Partizia with moveoutright
    hide Crowd with moveoutright
    queue music "audio/music/class.ogg" fadein 2.0
    "Bevor ich noch Antworten konnte, war sie schon aus meiner Sichtweite raus."
    "Beliebt zu sein hat seine Nachteile."
    show Aki eyebrows_angry mouth_big:
        linear 0.5 xalign 0.5
    with dissolve
    aki "\"Eeeeeeendlich!\""
    aki "\"Wie kann man überhaupt so leben, den ganzen Tag von einer Menge unzingelt zu sein?\""
    scene Bg Load with fade
    "Und damit machten wir uns auf den Weg zu unserem Klassenraum."
    pause 2.0
