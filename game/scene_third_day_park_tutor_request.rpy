label thirdDayParkTutorRequest:
    pause 5.0
    scene Bg Park Path with fade
    play noise "audio/sfx/nature.mp3" loop fadein 4.0 volume 0.2
    play music "audio/music/park.ogg" loop fadein 3.0
    "Aaah..."
    "Die wunderschöne Natur."
    "Gibt es eine bessere Art sein Wochenende zu genießen?"
    "Spatzieren gehen einen tut gut."
    stop music fadeout 3.0
    if aki_route == True:
        play music "audio/music/aki.ogg" loop fadein 2.0
        unknown "\"MAAAAAAAAAAAARRRRRCUUUUUUUS!\""
        "Verdammt."
        "Wie hat sie mich hier gefunden?"
        marcus "*stöhn* \"Ja, was ist?\""
        show Aki Default Happy Laugh Teeth Closed with dissolve
        aki "\"Wie geht es dir?\""
        "Das wars?"
        "Normalerweise würde sie mich jetzt mit ihren Lieblingsspiele oder Animes volllabern."
        "Dark Souls war das?"
        "Aber diesmal tat sie es nicht."
        marcus "\"Wieso fragst du.\""
        show Aki Default Normal Talk Small with dissolve
        aki "\"Du bist doch der Lateinweltmeister, oder?\""
        marcus "\"Wieso fragst du?\""
        show Aki Default Happy Smile with dissolve
        aki "\"Einfach so!\""
        "Sie will mich irgentwie austricksen, das weiß ich jetzt schon."
        marcus "\"Ja und?\""
        show Aki Default Normal Talk Small with dissolve
        aki "\"Dann kannst du mir doch auch ein bisschen Nachhilfe geben, oder?\""
        marcus "\"Wieso?\""
        show Aki Default Normal Talk Big with dissolve
        aki "\"Naja, du bist ein Weltmeister in Latein, deiner Kindheitsfreunden einbisschen Nachhilfe zu geben ist doch nichts!\""
        "Kacke."
        "Wie soll ich mich hier rausreden?"
        show Aki Default Sad Smile with dissolve
        aki "\"Komm schon!\""
        "Sie guckte mich ganz traurig an."
        "Wie soll ich jetzt noch nein sagen können?!"
        marcus "\"Eeeeh, also ich muss...\""
        "Aki kam jetzt ganz nah an mich ran."
        show Aki Default Happy Laugh with dissolve:
            xpos 0.5 ypos 1.65 xanchor 0.5 yanchor 1.0 zoom 2.0
        aki "\"Wenn du nicht ja sagst, dann erzähl ich der ganzen Schule dass du unter deinen Bett Hen...\""
        marcus "\"JAJAJAJAJA OK OK ICH GEBE DIR NACHHILFE!\""
        "Wie zur Hölle wusste sie das?"
        marcus "\"Wer hat das dir denn erzählt?\""
        hide Aki Default Happy Laugh with dissolve
        show Aki Default Normal Talk Small with dissolve
        aki "\"Also das stimmt?\""
        "Doppelt reingelegt und verkackt."
        marcus "\"Nein nein nein, das stimmt gar nicht, wirklich nicht.\""
        "Aki interessierte sich nicht mehr dafür und fing an zu kichern."
        show Aki Default Happy Laugh Teeth Closed with dissolve
        aki "\"Aber danke Marcus~. Hihi!\""
        "Ich habe aufgegeben."
        "Am liebsten würde ich jetzt ins Wasser springen und ertrinken."
        "Aber was solls."
        marcus "\"Wann hast du denn Zeit?\""
        show Aki Default Normal Talk Small with dissolve
        aki "\"Morgen? Nachmittags?\""
        marcus "\"Geht bei mir.\""
        "Aki sprang in die Luft."
        aki "\"Yaaaaaaaaa- woooooaaaaaah\""
        "Wie stolpert man bei Hüpfen nochmal?"
        marcus "\"Gehts dir gut?\""
        "Aki konnte sich gerade noch fangen."
        show Aki Default Happy Laugh Closed with dissolve
        aki "\"Gut genug! Hihi.\""
        "Das wars also mit mein chilligen Wochenende."
        "Ich habe noch ein Paar Runden um den See gedreht, während Aki mich über Sheen Megoomy Tensai oder sowas vollgeredet hat."
    if partizia_route == True:
        queue music "audio/music/partizia.ogg" loop fadein 2.0
        unknown "\"Morgen, Marcus.\""
        "Wer kann das denn sein?"
        "Ich drehe mich um."
        marcus "\"Hallo, Partizia!\""
        "Es ist ungewöhnlich sie draußen zu sehen."
        marcus "\"Was gibts?\""
        partizia "\"Has du Zeit?\""
        marcus "\"Wieso?\""
        partizia "\"Wegen Latin. Ich könne etwas Hilfe bei PCs gut gebrauchen, und ich meine, dass du mir hier weiterhelfen kannst. \""
        marcus "\"Klar, wieso nicht?\""
        "Partizia hat bisher noch nie so wirklich mit mir geredet, also war ich ein bisschen überrascht."
        partizia "\"Hättest du morgen Zeit?\""
        marcus "\"Ich meine.\""
        partizia "\"Könnten wir uns dann beim Steinkreis in der Schule treffen?\""
        marcus "\"Ja.\""
        partizia "\"Danke sehr für deine Helfe.\""
        "Sie beugte sich vor mir."
        marcus "\"Ja, das musst du nicht machen, wir sind Klassenkameraden, wir sollten uns helfen!\""
        "Auf Partizias Gesicht erschien ein kleines lächeln."
        "Wir haben noch ein Paar runden um den See gedreht und über den Studentenrat und Clubs an unserer Schule geredet."

    scene Bg Load with fade
    stop music fadeout 2.0
    stop noise fadeout 3.0
    pause 2.0
