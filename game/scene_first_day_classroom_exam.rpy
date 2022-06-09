label firstDayClassroomExam:
    scene Bg Classroom with fade
    if aki_route == True:
        jump aciExam
    else:
        "ne"

label pcExam:
    "{size=+10}{u}Grammatiktest - Partizipium Coniunktum{/u}{/size}\n{u}Aufgabe 1:{/u} Wähle die richtig gebildete PPP-Form aus."
    menu:
        "1) suscipere"
        "a) sussum":
            $ test_score -= 1
        "b) susceptum":
            $ test_score -= 0
    menu:
        "2) mittere"
        "a) missum":
            $ test_score -= 0
        "b) mittum":
            $ test_score -= 1
    menu:
        "3) colere"
        "a) cultus":
            $ test_score -= 0
        "b) coltus":
            $ test_score -= 1
    menu:
        "4) statuere"
        "a) statum":
            $ test_score -= 1
        "b) statutum":
            $ test_score -= 0
    menu:
        "5) petere"
        "a) petum":
            $ test_score -= 1
        "b) petitum":
            $ test_score -= 0
    menu:
        "6) ferre"
        "a) latum":
            $ test_score -= 0
        "b) fertum":
            $ test_score -= 1
    "{u}Aufgabe 2:{/u} Wähle die richtige Übersetzung der folgenden lateinischen Sätzen."
    menu:
        "1) Amicus petitus flebat."
        "a) Der Freund, der angegriffen worden ist, weint.":
            $ test_score -= 1
        "b) Der Freund weinte, wweil er angegriffen worden war.":
            $ test_score -= 0
    menu:
        "2) Vir fortis victus non periit."
        "a) Der Tapfere Mann kam nicht um, obwohl er besiegt worden war.":
            $ test_score -= 0
        "b) Der tapfere Mann kam trotz seiner Niederlage nicht um.":
            $ test_score -= 1
    menu:
        "3) Populus a regem domo datus gaudet."
        "a) Das Volk freute sich über das Geschenk des Königs.":
            $ test_score -= 1
        "b) Das Volk freute sich, nachdem der König ein Geschenk gab.":
            $ test_score -= 0
    menu:
        "4) Servi a domino servati gratiam deberunt."
        "a) Die Sklaven, die vom Heer bewart werden, schulden Dank.":
            $ test_score -= 1
        "b) Die Sklaven, die vom Heer bewart worden sind, schulden Dank.":
            $ test_score -= 0
    menu:
        "5) Res ad portam motus stavit."
        "a) Das Ding, dass zur Tür bewegt worden war, stand.":
            $ test_score -= 0
        "b) Die von der Tür bewegte Sache steht.":
            $ test_score -= 1
    menu:
        "6) Tabernam petitam intro."
        "a) Ich betrete das aufgesuchte Gasthaus.":
            $ test_score -= 0
        "b) Ich betrete das Gasthaus, dass aufgesucht worden war.":
            $ test_score -= 1

label aciExam:
    "{size=+10}{u}Grammatiktest - Akkusativus cum Infinitivo{/u}{/size}\n{u}Aufgabe:{/u} Wähle die richtige Übersetzungen der folgenden lateinischen Sätzen."
    menu:
        "a) Ich komme, dass der Freund sieht.":
            $ test_score -= 0
        "b) Ich sehe, dass der Freund kommt.":
            # hier muss was stehen sonst error
            $ test_score -= 1
        "1) Amicum venire video."
    menu:
        "a) Er hörte, dass die Sklaven redeten.":
            $ test_score -= 0
        "b) Er redet, dass die Sklaven hören.":
            $ test_score -= 1
        "2) Servos dicere audivit."
    menu:
        "a) Ich bemerke, dass das Volk sich freut.":
            $ test_score -= 1
        "b) Bemerken, dass das Volk sich freut.":
            $ test_score -= 0
        "3) Cognoscere Pupulum gaudere."
    menu:
        "a) Ihr wusstet, dass der Junge ein Geschenk gegeben hatte.":
            $ test_score -= 0
        "b) Ihr wusstet, dass der Junge ein Geschenk gab.":
            $ test_score -= 1
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
            $ test_score -= 0
        "b) Der Hervorragende glaubt, dass ich sein Freund bin.":
            $ test_score -= 1
        "7) Amicus putat me egrergium esse."
    menu:
        "a) Der große Herr glaubt, dass seine Sklaven die Aufgaben unternehmen.":
            $ test_score -= 0
        "b) Der Herr glaubt, dass seine Sklaven die großen Aufgaben unternehmen.":
            $ test_score -= 1
        "8) Dominus magnus credit servos suos munera suscipere."
    menu:
        "a) Der König sagt, dass dieser eine Untat begehe.":
            $ test_score -= 1
        "b) Dieser König sagt, dass ich eine Untat begehe.":
            $ test_score -= 0
        "9) Rex is me facinus committere dicit."
    menu:
        "a) Der Junge wusste, dass große Hilffe gekommen ist.":
            $ test_score -= 1
        "b) Der große Junge wusste, dass Hile gekommen war.":
            $ test_score -= 0
        "10) Puer magnus scivit magnum auxilium venivisse."
    menu:
        "a) Es stand fest, dass der Klare der Sieger war.":
            $ test_score -= 1
        "b) Es stand fest, dass er der klare Sieger war.":
            $ test_score -= 0
        "11) Eum victorem clarum esse constabat.\n{size=-5}*constat = es steht fest{/size}"
    menu:
        "a) Alle wissen, dass die erbärmliche Stadt vernichtet worden war.":
            $ test_score -= 0
        "b) Alle Erbärmlichen wussten, dass die Stadt vernichtet ist.":
            $ test_score -= 1
        "12) Omnes urbem malam interficebar cognoverunt."