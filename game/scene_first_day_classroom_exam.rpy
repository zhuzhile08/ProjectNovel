label firstDayClassroomExam:
    scene Bg Classroom with fade
    if aki_route == True:
        jump aciExam
    else:
        "ne"

label aciExam:
    "{size=+10}{u}Grammatiktest - Akkusativus cum Infinitivo{/u}{/size}\n{u}Aufgabe:{/u} Wähle die richtige Übersetzungen der folgenden lateinischen Sätzen."
    menu:
        "a) Ich komme, dass der Freund sieht.":
            $ test_score -= 1
        "b) Ich sehe, dass der Freund kommt.":
            # hier muss was stehen sonst error
            $ test_score -= 0
        "1) Amicum venire video."
    menu:
        "a) Er hörte, dass die Sklaven redeten.":
            $ test_score -= 1
        "b) Er redet, dass die Sklaven hören.":
            $ test_score -= 0
        "2) Servos dicere audivit."
    menu:
        "a) Ich bemerke, dass das Volk sich freut.":
            $ test_score -= 1
        "b) Bemerken, dass das Volk sich freut.":
            $ test_score -= 0
        "3) Cognoscere Pupulum gaudere."
    menu:
        "a) Ihr wusstet, dass der Junge ein Geschenk gegeben hatte.":
            $ test_score -= 1
        "b) Ihr wusstet, dass der Junge ein Geschenk gab.":
            $ test_score -= 0
        "4) Scivistis puerum dono dedisse."
    menu:
        "a) Wir sahen, dass er zu der Tür gegangen ist.":
            $ test_score -= 1
        "b) Wir sahen, dass er zu der Tür gegangen war.":
            $ test_score -= 0
        "5) Vidivimus eum ad portam ire."
    menu:
        "a) Ich hatte geglaubt, dass das Gasthaus dich augesucht hat.":
            $ test_score -= 1
        "b) Ich glaubte, dass du das Gasthaus aufgesucht hattest.":
            $ test_score -= 0
        "6) Credebam te tabernam petivisse."
    menu:
        "a) Der Freund glaubt, dass ich hervorragend bin.":
            $ test_score -= 1
        "b) Der Hervorragende glaubt, dass ich sein Freund bin.":
            $ test_score -= 0
        "7) Amicus putat me egrergium esse."
    menu:
        "a) Der große Herr glaubt, dass seine Sklaven die Aufgaben unternehmen.":
            $ test_score -= 1
        "b) Der Herr glaubt, dass seine Sklaven die großen Aufgaben unternehmen.":
            $ test_score -= 0
        "8) Dominus magnus credit servos suos munera suscipere."
    menu:
        "a) Der König sagt, dass dieser eine Untat begehe.":
            $ test_score -= 1
        "b) Dieser König sagt, dass ich eine Untat begehe.":
            $ test_score -= 0
        "9) Rex is me facinus committere dicit."
    menu:
        "a) Nom Verb (Prät) Adj SAkk PInf (Plus)":
            $ test_score -= 1
        "b) Nom Adj Verb (Perf) SAkk PInf (Plus)":
            $ test_score -= 0
        "10) Verb (Perf) Adj (Nom) SAkk PInf (Perf)"
    menu:
        "a) Es stand fest, dass der Klare der Sieger war.":
            $ test_score -= 1
        "b) Es stand fest, dass er der klare Sieger war.":
            $ test_score -= 0
        "11) Eum victorem clarum esse constabat.\n{size=-5}*constat = es steht fest{/size}"
    menu:
        "a) Alle wissen, dass die erbärmliche Stadt vernichtet worden war.":
            $ test_score -= 1
        "b) Alle Erbärmlichen wussten, dass die Stadt vernichtet ist.":
            $ test_score -= 0
        "12) Omnes urbem malam interficebar cognoverunt."