label secondDayRoad:
    pause 5.0 
    queue music "audio/music/park.ogg" loop fadein 2.0
    "Ein neuer Tag hat begonnen, und ich muss wie immer wieder aus meinen Bett."
    scene Bg Room with fade
    "Ich öffne meine Augen zu meinen vertraulichen Zimmer"
    "Ich steige aus meinen Bett heraus und bereite mich für die Schule vor."
    scene Bg Home Outwards with fade
    "Draußen angekommen, war es schön kühl, und die Sonne scheint."
    "Alles deutet auf einen normalen Tag hin."
    scene Bg Home Road with fade
    stop music fadeout 3.0
    if aki_route == True:
        queue music "audio/music/aki.ogg" loop fadein 2.0
        "Ich biege auf die Straße ab und vor mir war ein recht ungewöhnliches Bild."
        show Aki eyes_closed mouth_laugh_teeth with dissolve
        aki "\"Hey, Marcus!\""
        "Vor mir stand Aki. Normalerweise würde sie erst ein bisschen später auftauchen, aber heute war sie ungewöhnlich früh hier, früher als ich."
        marcus "\"Und wieso bist du jetzt so früh hier?\""
        show Aki eyes_open mouth_small with dissolve
        aki "\"Keine Ahnung. Ich konnte gestern einfach nicht so gut schlafen.\""
        marcus "\"Wieso denn?\""
        aki "\"Na ja, der Test.\""
        "Achso, der Test! Den habe ich komplett vergessen."
        show Aki eyebrows_sad with dissolve
        aki "\"Ich hoffe wirklich, dass ich bestehen werde.\""
        marcus "\"Ich auch.\""
        show Aki eyebrows_neutral with dissolve
        aki "\"Hoffst du also, dass ich bestehen werde oder dass du bestehen wirst?\""
        marcus "\"Das erste.\""
        show Aki eyebrows_angry mouth_big with dissolve
        aki "\"Hey, das war fies!\""
        "Danach machten wir uns auf den Weg zur Schule, während wir über den Test diskutiert haben und uns Vokabeln abgefragt haben."
    else:
        queue music "audio/music/school_way.ogg" loop fadein 2.0
        "Aber was heute nicht normal war, ist dass ich Aki nicht hinter mier rennen hören oder sehen gesehen habe."
        "Vielleicht hat sie auch überschlafen, wer weiß?"
        "Ich mache mich auf den Weg ohne weitere Sorgen."
    scene Bg Load
    with fade
    stop music fadeout 3.0
        