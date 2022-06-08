label firstDayRoadIntroduction:
    with fade
    play sound "audio/sfx/chirp2.flac" loop
    "Es ist ein sonniger Tag draußen, Vögel zwitschern, Blumen blühen..."
    "Und wieso schreiben wir an Tagen wie diesen einen Lateintest?"
    play music "audio/music/aki.ogg" loop fadein 2.0
    scene Bg Home Road
    with squares
    play sound ["audio/sfx/step_lth1.ogg", "audio/sfx/step_lth2.ogg", "audio/sfx/step_lth3.ogg", "audio/sfx/step_lth4.ogg"] loop
    unknown "\"MAAAAAAAARRRRRRCUUUUUUUUUUUUUUUUUUUUS!!!\""
    "Habe ich schon erwähnt? Ich bin Marcus. Marcus Kashima."
    "Und die, die gerade hinter mir herläuft ist meine Kindheitsfreundin Aki Kuzunoha."
    aki "\"MAAAAAAAAAAAARRRRRRCUUUUUUUUUUUS warte mal!\""
    marcus "\"Jaja, schon gut.\""
    show Aki Default Happy Laugh Teeth # i need one of those > o < faces here
    "Ich bleibe stehen und drehe mich um."
    "Von einer weiten Entfernung kann man schon ihre pinken Haare sehen."
    "Sie ist ein bisschen kleiner als ich, und eigentlich ein ganz nettes Mädchen"
    "Manchmal kann sie auch etwas... naja... blöd und ungeschickt sein."
    stop sound fadeout 2.0
    aki "*Stöhn* \"Phew! Ich bin völlig aus der Puste. Bitte woaaaaaaaaaaaaaah!\""
    "Aki ist über eine Kante gestolpert. Das vierte Mal in dieser Woche."
    marcus "\"Hey! Get's dir gut?\""
    aki "\"Ja, eigentlich schon.\""
    marcus "\"Sag mal, was geht denn bei dir täglich ab, das war das vierte mal in dieser Woche.\""
    show Aki Default Happy Laugh Closed with dissolve
    aki "\"Hehehe.\""
    "Nachdem sie mich endlich aufgeholt hat und sich erholt hat, gehen wir nebeneinander los."
    "Aki wohnt ein paar Blöcke hinter mir, und eigentlich wäre der Plan, dass sie zuerst losgeht, und dass sie dann vor unserer Tür wartet, bis ich fertig bin."
    "Aber anscheinend klappt das nicht so ganz."
    show Aki Default Normal Talk Small with dissolve
    aki "\"Hast du dich auf den Lateintest vorbereitet?"
    marcus "\"Na klar! Ich bin ja schließlich der Leiter vom Lateinclub!\""
    "Ach ja, ich bin der stolze Leiter vom Lateinclub an unserer Schule."
    "Der Lateinclub wurde von der vorletzten Schüler-generation gegründet, und ich bin seit dem letzten Jahr Präsident vom Club."
    "Wir sind eine recht aktive Gruppe mit recht vielen Mitgliedern, nämlich 14."
    show Aki Default Sad Talk Small with dissolve
    aki "\"Ich hoffe wir scheiben den Test nicht über AcIs, die kann ich gar nicht!\""
    show Aki Default Sad Talk Small with dissolve
    aki "\"Wofür steht AcI eigentlich überhaupt?\""
    marcus "\"Akkusativus cum Infinitivo.\""
    marcus "\"Du solltest das wissen, ich habe dir mehrmals gesagt, dass du das lernen solltest!\""
    show Aki Default Sad Talk Big with dissolve  # i need one of those > o < faces here too
    aki "\"Ich habe versucht, aber kanns immer nicht!\""
    hide Aki Default Normal Talk Big with dissolve
    scene Bg Load
    with fade
    stop music fadeout 3.0
    queue music "audio/music/school_way.ogg" loop fadein 2.0
    "Wir haben uns dann für den Rest des Schulweges Vokablen abgefragt. Ziemlich normal für uns."
    pause 2.0
