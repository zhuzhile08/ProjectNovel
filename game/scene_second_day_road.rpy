label secondDayRoad:
    pause 5.0 
    queue music "audio/music/park.ogg" loop fadein 2.0
    "Ein neuer Tag hat begonnen, und ich muss wie immer wieder aus meinen Bett."
    "Ich öffne meine Augen zu meinen vertraulichen Zimmer"
    "Ich steige aus meinen Bett heraus und bereite mich für die Schule vor."
    scene Bg Home Outwards with fade
    "Draußen angekommen, war es schön kühl, und die Sonne scheint."
    "Alles deutet auf einen normalen Tag hin."
    scene Bg Home Road with fade
    stop music fadeout 3.0
    if aki_route:
        queue music "audio/music/aki.ogg" loop fadein 2.0
        "Ich biege auf die Straße ab und vor mir war ein recht ungewöhnliches Bild."
        aki "\"Hey, Marcus!\""
        "Vor mir stand Aki. Normalerweise würde sie erst ein bisschen später auftauchen, aber heute war sie ungewöhnlich früh hier, früher als ich."
        marcus "\"Und wieso bist du jetzt so früh hier?\""
        aki "\"Keine Ahnung. Ich konnte gestern einfach nicht so gut schlafen.\""
        marcus "\"Wieso denn?\""
        aki "\"Naja, der Test.\""
        "Achso, der Test! Den habe ich komplett vergessen."
        "Danach machten wir uns auf den Weg zur Schule, während wir über den Test diskutiert haben und uns Vokabel abgefragt haben."
        scene Bg Load
        with fade
        stop music fadeout 3.0
    else:
        queue music "audio/music/school_way.ogg" loop fadein 2.0
        "Aber was heute nicht normal war, ist dass ich Aki nicht hinter mier rennen hören oder sehen gesehen habe."
        "Vielleicht hat sie auch überschlafen, wer weiß?"
        "Ich mache mich auf den Weg ohne weitere Sorgen."
        scene Bg Load
        with fade
        stop music fadeout 3.0
        