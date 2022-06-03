# add a custom noise channel
init python:
    renpy.music.register_channel('noise', "sound")

label firstDayEntranceHurt:
    scene Bg School Entrance
    with dissolve
    "Als wir am Eingang der Schule angekommen waren, habe wir noch ein bisschen rumgedadelt und gewartet."
    show Crowd
    play noise "audio/sfx/crowd_outdoors.ogg" loop
    "Mittlerweile war eine riesige Menge von Schülern schon angekommen."
    play sound "audio/sfx/school_bell.ogg" 
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
    "Da wir jetzt in verschiedene Klassen gehen müssen, verabschiedete ich mich von Aki."
    aki "Dann, tschüss, Marcus!"
    marcus "Den Test scheiben wir am Nachmittag, du hast also noch ein bisschen Zeit zum Lernen." 
    aki "Können wir dann zusammen lernen?"
    marcus "Ich kann heute nicht, bin mit dem Club beschäftigt."
    aki "Okay!"
    aki "Aki lief mit einem Lächeln auf dem Gesicht in das Gebäude."
    stop voice fadeout 0.3
    "*Dumpf!*"
    "Aki knallte mit voller Wucht auf den Boden."
    aki "Ouch... Das tat weh!"
    "Ich rannte zu Aki rüber."
    marcus "Gehts dir gut?"
    aki "Ich glaube nicht."
    marcus "Das war das zweite Mal, dass du diese Woche gespolperst bist"
    "Sie versuchte aufzustehen, aber ihr Versuch war nicht erfolgreich."
    "Dabei konnte ich für einen Moment einen Blick auf Aki's blutiges Knie werfen."
    marcus "Das sieht nicht so gut aus. Kannst du ins Krankenzimmer gehen?"