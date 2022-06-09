label firstDayClassroomExam:
    pause 3.0
    scene Bg Classroom with fade
    queue music "audio/music/class.ogg" loop fadein 2.0
    "Moment der Wahrheit."
    "Das Prüfungsblatt liegt vor mir."
    "Ich schaute mich um, und sah, wie Aki auf ihren Platz saß und betete."
    if aki_route == True:
        teacher "\"Ihr könnt loslegen. Dreht das Blatt um.\""
        "Die Arbeit ist über AcIs."
        "Genau das was ich gelernt habe!"
        "Das nenne ich reiner Zufall."
        jump aciExam
    else:
        teacher "Ihr könnt loslegen. Dreht das Blatt um."
        "Die Arbeit ist über PCs."
        "Genau das was ich gelernt habe!"
        "Das nenne ich reiner Zufall."
        jump pcExam

label pcExam:
    "12 Fragen, wie immer."
    "Das wird einfach. Hoffe ich zumindest."
    "Teil eins ist über Formen. Meine Spezialität."
    "{size=+10}{u}Grammatiktest - Partizipium Coniunktum{/u}{/size}\n{u}Aufgabe 1:{/u} Wähle die richtig gebildete PPP-Form aus."
    menu:
        with Dissolve(0.3)
        "1) suscipere"
        "a) sussum":
            $ test_score -= 1
        "b) susceptum":
            $ test_score -= 0
    "Definitiv."
    menu:
        with Dissolve(0.3)
        "2) mittere"
        "a) missum":
            $ test_score -= 0
        "b) mittum":
            $ test_score -= 1
    "Höchstwarscheinlich."
    menu:
        with Dissolve(0.3)
        "3) colere"
        "a) cultus":
            $ test_score -= 0
        "b) coltus":
            $ test_score -= 1
    "Soweit ich weiß."
    menu:
        with Dissolve(0.3)
        "4) statuere"
        "a) statum":
            $ test_score -= 1
        "b) statutum":
            $ test_score -= 0
    "Hmmm..."
    menu:
        with Dissolve(0.3)
        "5) petere"
        "a) petum":
            $ test_score -= 1
        "b) petitum":
            $ test_score -= 0
    "Jup!"
    menu:
        with Dissolve(0.3)
        "6) ferre"
        "a) latum":
            $ test_score -= 0
        "b) fertum":
            $ test_score -= 1
    "Klasse. Letzte Formenaufgabe fertig. Lass hoffen, dass ich alles rightig habe."
    "{u}Aufgabe 2:{/u} Wähle die richtige Übersetzung der folgenden lateinischen Sätzen."
    "Das kann kritisch werden."
    menu:
        with Dissolve(0.3)
        "1) Amicus petitus flebat."
        "a) Der Freund, der angegriffen worden ist, weint.":
            $ test_score -= 1
        "b) Der Freund weinte, weil er angegriffen worden war.":
            $ test_score -= 0
    "Erste Aufgabe, einfach."
    menu:
        with Dissolve(0.3)
        "2) Vir fortis victus non periit."
        "a) Der Tapfere Mann kam nicht um, obwohl er besiegt worden war.":
            $ test_score -= 0
        "b) Der tapfere Mann kam trotz seiner Niederlage nicht um.":
            $ test_score -= 1
    "Hoffendlich."
    menu:
        with Dissolve(0.3)
        "3) Populus a regem domo datus gaudet."
        "a) Das Volk freute sich über das Geschenk des Königs.":
            $ test_score -= 1
        "b) Das Volk freute sich, nachdem der König ein Geschenk gab.":
            $ test_score -= 0
    "Bin mir ziemlich sicher."
    menu:
        with Dissolve(0.3)
        "4) Servi a domino servati gratiam deberunt."
        "a) Die Sklaven, die vom Heer bewart werden, schulden Dank.":
            $ test_score -= 1
        "b) Die Sklaven, die vom Heer bewart worden sind, schulden Dank.":
            $ test_score -= 0
    "Easy."
    menu:
        with Dissolve(0.3)
        "5) Res ad portam motus stavit."
        "a) Das Ding, dass zur Tür bewegt worden war, stand.":
            $ test_score -= 0
        "b) Die von der Tür bewegte Sache steht.":
            $ test_score -= 1
    "Pfew! Eine übrig."
    menu:
        with Dissolve(0.3)
        "6) Tabernam petitam intro."
        "a) Ich betrete das aufgesuchte Gasthaus.":
            $ test_score -= 0
        "b) Ich betrete das Gasthaus, dass aufgesucht worden war.":
            $ test_score -= 1
    jump aftermath

label aciExam:
    "12 Fragen, wie immer."
    "Das wird einfach. Hoffe ich zumindest."
    "{size=+10}{u}Grammatiktest - Akkusativus cum Infinitivo{/u}{/size}\n{u}Aufgabe:{/u} Wähle die richtige Übersetzungen der folgenden lateinischen Sätzen."
    menu:
        with Dissolve(0.3)
        "a) Ich komme, dass der Freund sieht.":
            $ test_score -= 0
        "b) Ich sehe, dass der Freund kommt.":
            $ test_score -= 1
        "1) Amicum venire video."
    "Erste Aufgabe, einfach."
    menu:
        with Dissolve(0.3)
        "a) Er hörte, dass die Sklaven redeten.":
            $ test_score -= 0
        "b) Er redet, dass die Sklaven hören.":
            $ test_score -= 1
        "2) Servos dicere audivit."
    "Definitiv."
    menu:
        with Dissolve(0.3)
        "a) Ich bemerke, dass das Volk sich freut.":
            $ test_score -= 1
        "b) Bemerken, dass das Volk sich freut.":
            $ test_score -= 0
        "3) Cognoscere Pupulum gaudere."
    "Höchstwarscheinlich."
    menu:
        with Dissolve(0.3)
        "a) Ihr wusstet, dass der Junge ein Geschenk gegeben hatte.":
            $ test_score -= 0
        "b) Ihr wusstet, dass der Junge ein Geschenk gab.":
            $ test_score -= 1
        "4) Scivistis puerum dono dedisse."
    "Soweit ich weiß."
    menu:
        with Dissolve(0.3)
        "a) Wir sahen, dass er zu der Tür gegangen ist.":
            $ test_score -= 1
        "b) Wir sahen, dass er zu der Tür gegangen war.":
            $ test_score -= 0
        "5) Vidivimus eum ad portam ire."
    "Hmmm..."
    menu:
        with Dissolve(0.3)
        "a) Ich hatte geglaubt, dass das Gasthaus dich augesucht hat.":
            $ test_score -= 1
        "b) Ich glaubte, dass du das Gasthaus aufgesucht hattest.":
            $ test_score -= 0
        "6) Credebam te tabernam petivisse."
    "Jup!"
    menu:
        with Dissolve(0.3)
        "a) Der Freund glaubt, dass ich hervorragend bin.":
            $ test_score -= 0
        "b) Der Hervorragende glaubt, dass ich sein Freund bin.":
            $ test_score -= 1
        "7) Amicus putat me egrergium esse."
    "Klasse."
    menu:
        with Dissolve(0.3)
        "a) Der große Herr glaubt, dass seine Sklaven die Aufgaben unternehmen.":
            $ test_score -= 0
        "b) Der Herr glaubt, dass seine Sklaven die großen Aufgaben unternehmen.":
            $ test_score -= 1
        "8) Dominus magnus credit servos suos munera suscipere."
    "Hoffendlich."
    menu:
        with Dissolve(0.3)
        "a) Der König sagt, dass dieser eine Untat begehe.":
            $ test_score -= 1
        "b) Dieser König sagt, dass ich eine Untat begehe.":
            $ test_score -= 0
        "9) Rex is me facinus committere dicit."
    "Bin mir ziemlich sicher."
    menu:
        with Dissolve(0.3)
        "a) Der Junge wusste, dass die große Hilfe gekommen ist.":
            $ test_score -= 1
        "b) Der große Junge wusste, dass Hilfe gekommen war.":
            $ test_score -= 0
        "10) Puer magnus scivit auxilium venivisse."
    "Easy."
    menu:
        with Dissolve(0.3)
        "a) Es stand fest, dass der Klare der Sieger war.":
            $ test_score -= 1
        "b) Es stand fest, dass er der klare Sieger war.":
            $ test_score -= 0
        "11) Eum victorem clarum esse constabat.\n{size=-5}*constat = es steht fest{/size}"
    "Pfew! Eine übrig."
    menu:
        with Dissolve(0.3)
        "a) Alle wissen, dass die erbärmliche Stadt vernichtet worden war.":
            $ test_score -= 0
        "b) Alle Erbärmlichen wussten, dass die Stadt vernichtet ist.":
            $ test_score -= 1
        "12) Omnes urbem malam interficebar cognoverunt."
    jump aftermath

label aftermath:
    "Klasse! Letzte Aufgabe fertig."
    "Ich schaute mich in der Klasse um. Anscheinend bin ich der erste, der fertig bin."
    "Jetzt muss ich die letzten paar Minuten auswarten. Das wird langweilig."
    scene Bg Load with fade
    pause 3.0
    scene Bg Classroom with fade
    teacher "\"Stifte niederlegen! Ich werde jetzt den Test einsammeln!\""
    "Alle legen ihre Stifte nieder."
    "Der Leher ging dann bei jeden herum und nahm sich ein Zettel nach den anderen."
    teacher "\"Die Testergebnisse bekommt jeder morgen zurück.\""
    play sound "audio/sfx/school_bell.ogg" volume 0.6
    teacher "\"Damit ist der Schultag beendet. Erholt euch zuhause gut!\""
    play noise "audio/sfx/crowd_indoors.ogg" loop fadein 1.0 volume 0.3
    if aki_route == True:
        "Ich sah rüber zu Aki und bemerkte, dass sie völlig erledigt in ihren Sitz saß."
        "Ich ging zu ihr rüber."
        aki "\"Phew! Endlich ist das vorbei!\""
        marcus "\"Und? Wie ist es gelaufen?\""
        aki "\"Ehrlich gesagt, ganz OK. Glaube ich.\""
        
    if partizia_route == True:
        "Ich sah rüber zu Aki und sie saß stolz in ihren Stuhl."
        marcus "\"Diesmal hattest du ja Glück.\""
        aki "\"Hehe! Du weißt ja, dass PCs meine Spezialität sind.\""
    
    aki "\"Jedenfalls, willst du mit mir nach Hause gehen?\""
    menu:
        with Dissolve(0.3)
        "Soll ich?"
        "\"Ja\"":
            marcus "\"Ja.\""
            aki "\"Dann, lass loslegen!\""
            "Wir haben uns auf den Weg gemacht, nachdem wir unsere Sachen gepackt haben."
        "\"Ne, vieleicht nächstes mal.\"":
            marcus "\"Ne, vieleicht nächstes mal.\""
            aki "\"Oooh, schade!\""
            aki "\"Aber naja, ich habe auf den Weg eh was zu tun.\""
            marcus "\"OK. Dann bis morgen!\""
            aki "\"Bis morgen, Marcus!\""
            "Und damit sammelte sie ihre Sachen ein und machte sich auf den Weg."

    scene Bg Load with fade
    stop noise fadeout 1.0
    stop music fadeout 3.0            
