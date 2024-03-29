# Blue: #00a7ff
# Red: #FF4B4B
# Green: #438A64

label firstDayClubroomLearning:
    "Endlich bin ich im Clubraum angekommen."
    scene Bg Clubroom with fade
    queue music "audio/music/club.ogg" loop fadein 2.0
    "Das ist der Clubraum vom Lateinclub."
    "Ich war hier schon sehr oft, und alles ist so wie es sein sollte."
    "Eigentlich ist es nicht mal unser Clubraum, es ist eigentlich ein Raum für den Literaturclub."
    "Aber sie haben uns freundlicherweise diese Ecke des Raumes völlig freiwillig gegeben."
    "Völlig freiwillig."
    "Sie wurden überhaupt nicht von den Lehrern dazu gezwungen, uns diese Ecke zu geben."
    "Achja, der Drache in der Ecke da."
    show Bg Clubroom with dissolve:
        xpos 0.05 ypos 1.28 xanchor 0.5 yanchor 1.0 zoom 2.0
    "Das ist Raidou."
    "Er ist ein Preis, welches der Literaturclub bei einem Wettbewerb gewonnen hat."
    "Eigentlich war der Literaturclub und der Lateinclub früher recht gut in Wettbewerben, aber seitdem wir den Drachen bekommen haben, haben beide Clubs nie mehr einen gewonnen."
    "Alle meinen, dass der Drache ein Unglücksbringer ist, aber ich meine, dass in den Drachen eine Wanze versteckt ist, mitdem uns die gegnerischen Antreter in den Wettbewerben ausspionieren."
    "Achja, und ich trete Raidou auch manchmal eine in die Fresse, wenn es mir schlecht geht."
    scene Bg Clubroom with dissolve
    "Wie sehr interessant ich die Backstory vom Literaturclub auch finde, muss ich mich jetzt auch auf Latein konzentrieren."
    "Der Lehrer hat gesagt, dass wir einen Test schreiben werden, aber nicht über was."
    "Wenn ich mal ehrlich bin, ist es ein ziemlich blöder Move, aber was solls?"
    "Ich glaube der Sinn von solch einem Test liegt daran, dass man beides gleich lernen und beherrschen sollte."
    "Aber ich lerne nur eines von denen, weil ich es kann."
    menu:
        with Dissolve(0.3)
        "Was soll ich denn überhaupt lernen?"
        "Pc lernen":
            "Aus den Schrank vor mir habe ich ein uraltes, mit Staub bedecktes Buch genommen."
            "Ich puste den Staub weg und eine riesige Wolke taucht auf"
            "Unter der Staubschicht erscheint der Text:"
            "Partizipium coniunctum für Beginner, von Ben Dover."

            $ partizia_route = True

            jump readPc
        "AcI lernen":
            "Aus den Schrank vor mir habe ich ein uraltes, mit Staub bedecktes Buch genommen."
            "Ich puste den Staub weg und eine riesige Wolke taucht auf"
            "Unter der Staubschicht erscheint der Text:"
            "Akkusativus cum Infinitivo made Easy, von Mike Oxlong."

            $ aki_route = True

            jump readAcI


label readPc:
    "{size=+10}{b}{u}Das Pc{/u}{/b}{/size}\n{b}{u}Grundwissen und Aufbau:{/u}{/b}"
    "Das Pc, Partizipium Coniunctum, kommt in lateinischen Sätzen oft als Attribut vor. Man bildet diese mit dem Bezugswort und dem PPP (Partizip Perfekt Passiv). Außerdem stehen Pcs immer vorzeitig zum Hauptsatz."
    "{color=#00a7ff}{u}Cattus{/u}{/color} {color=#FF4B4B}{u}servatus{/u}{/color} latus est. - Die {color=#FF4B4B}gerettete{/color} {color=#00a7ff}Katze{/color} ist fröhlich.\n {size=-10}*Cattus = Katze{/size}\n\n{size=-3}In diesem Fall ist \"Cattus\" das Bezugswort und \"servatus\" das Partizip.{/size}"
    "{b}{u}Ablativ des Urhebers:{/u}{/b}\nDa das Pc im Passiv steht, kann es im Satz auch einen Urheber geben, der dem Subjekt eine Tat ausübt. Solche stehen im Ablativ und werden Ablativ ddes Urhebers genannt."
    "{color=#00a7ff}{u}Cattus{/u}{/color} a {color=#438A64}{u}domino{/u}{/color} {color=#FF4B4B}{u}servatus{/u}{/color} latus est. - Die {color=#438A64}vom Herrn{/color} {color=#FF4B4B}gerettete{/color} {color=#00a7ff}Katze{/color} ist fröhlich."
    "{size=-3}Wenn der Urheber eine Person ist, wird dessen Wort mit einem \"a\" geschrieben, und wenn nicht, schreibt man es nicht.{/size}\n\n{color=#00a7ff}{u}Cattus{/u}{/color} {color=#438A64}{u}ira{/u}{/color} {color=#FF4B4B}{u}mota{/u}{/color} petivit. - Die {color=#438A64}von Zorn{/color} {color=#FF4B4B}bewegte{/color} {color=#00a7ff}Katze{/color} griff an."
    "{b}{u}Erkennung:{/u}{/b}\nMan erkennt ein Pc an dessen PPP, welches auch KNG-Konguent zu dem Bezugswort ist."
    "{size=-3}Um den Ablativ des Urhebers auch mitzuerkennen kann man Klammern anwenden. Die fängt nach dem Bezugswort an und endet nach dem Partizip.{/size}\n\n{color=#00a7ff}{u}Cattus{/u}{/color} a ({color=#438A64}{u}domino{/u}{/color} {color=#FF4B4B}{u}servatus{/u}{/color}) latus est."

    menu:
        "Das war ein Haufen. Habe ich das alles schon verstanden?"

        "Nein":
            "Nicht wirklich, aber alles nochmal zu lesen kann ja einen nichts schlechtes antun."
            jump readPc
        "Ja":
            jump after

label readAcI:
    "{size=+10}{b}{u}Der AcI{/u}{/b}{/size}\n{b}{u}Grundwissen und Aufbau:{/u}{/b}"
    "Der AcI, Akkusativus cum Infinitivo(Akkusativ mit Infinitiv) auf Latein, kommt sehr oft in lateinischen Sätze vor. Es wird im deutschen meistens mit einem dass-Satz übersetzt."
    "{size=-3}Ein AcI in lateinischen Sätzen enthält einen Kopfverb, Subjektsakkusativ, und einen Prädikatsinfinitiv:{/size}\n{color=#438A64}{u}Scio{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum suum {color=#FF4B4B}{u}amare{/u}{/color}. - Ich weiß, dass die Schwester ihre Katze liebt.\n {size=-10}*Cattus = Katze{/size}"
    "\"{color=#438A64}Scio{/color}\" ist das Kopfverb, \"{color=#00a7ff}sororem{/color}\" der Subjektakkusativ und \"{color=#FF4B4B}amare{/color}\" ist das Prädikatsinfinitiv. Den Teil, der nicht zwischen dem Kopfverb und dem Prädikatsinfinitiv steht, nennt man \"Rahmensatz\"."
    "Wenn ein Infinitiv im Satz auftaucht, enthält dieser einen AcI mit hoher Wahrscheinlichkeit."
    "Wörter wie videre, negare, putare oder scire werden oft als Kopfverb verwendet.\n{color=#FF4B4B}ACHTUNG:{/color} Es gibt Verben, die mit einem Infinitiv stehen, aber keine Kopfverben sind, zum Beispiel wie posse oder velle."
    "{b}{u}Vor- und Gleichzeitigkeit{/u}{/b}\n{size=-3}Mit dem AcI zeigt man auch das Zeitverhältnis zum Rahmensatz, indem man das Tempus vom Prädikatsinfinitiv ändert. Wenn man den Prädikatsinfinitiv in Präsens schreibt, ist es gleichzeitig zum Hauptsatz, und wenn man es in Perfekt ausdrückt, ist es Vorzeitig.{/size}"
    "Im deutschen ändert sich das Tempus von dem Prädikatsinfinitiv abhängig vom Tempus des Kopfverbs."
    "{color=#438A64}{u}Scio{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum suum {color=#FF4B4B}{u}amare{/u}{/color}. - Ich weiß, dass die Schwester ihre Katze liebt.\n{color=#438A64}{u}Scivi{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum {color=#FF4B4B}{u}amare{/u}{/color}. - Ich wusste, dass die Schwester ihre Katze liebte.\n{size=-10}- Gleichzeitigkeit{/size}"
    "{color=#438A64}{u}Scio{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum {color=#FF4B4B}{u}amavisse{/u}{/color}. - Ich weiß, dass die Schwester ihre Katze liebte.\n{color=#438A64}{u}Scivi{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum {color=#FF4B4B}{u}amavisse{/u}{/color}. - Ich wusste, dass die Schwester ihre Katze geliebt hatte.\n{size=-10}- Vorzeitigkeit{/size}"
    "Wenn das Kopfverb im Präsens steht,  wird das Prädikatsinfinitiv in Präteritum übersetzt, und wenn es im Perfekt steht, wird das Prädikatsinfinitiv in Plusquamperfekt, welches Vorzeitigkeit gegen Perfekt ausdrückt, übersetzt."
    "{b}{u}Reflexivität:{/u}{/b}\n{size=-3}Die Wörter “se”, “suus” und “sibi” beziehen sich in normalen Sätzen auf das Subjekt, und wenn diese in einem AcI auftauchen, beziehen sie sich auf das Subjekt des Rahmensatzes. Man benutzt Personalpronomen, wenn man eine Beziehung auf dem Subjektsakkusativ zeigen will.{/size}"
    "Scio {color=#ffa500}{u}sororem{/u}{/color} cattum {color=#ffa500}{u}suum amare{/u}{/color}. - Ich weiß, dass die {color=#ffa500}{u}Schwester ihre{/u}{/color} Katze liebt.\nVideo {color=#ffa500}{u}cattum{/u}{/color} stare et {color=#ffa500}{u}eum{/u}{/color} amo.  - Ich sehe, dass die {color=#ffa500}{u}Katze{/u}{/color} steht und ich liebe {color=#ffa500}{u}sie{/u}{/color}."
    menu:
        "Das war ein Haufen. Habe ich das alles schon verstanden?"

        "Nein":
            "Nicht wirklich, aber alles nochmal zu lesen kann ja einen nichts schlechtes antun."
            jump readAcI
        "Ja":
            jump after

label after:
    "Recht einfach zu verstehen. Aber auch ein Lateinweltmeister wie ich braucht auch mal eine Pause"
    "Ich gucke auf die Uhr und bemerke, dass ich noch 30 Minuten bis zum Test habe."
    "Also habe ich mein Handy rausgenommen und ein bisschen darauf rumgedaddlet."
    scene Bg Load
    with fade
    stop music fadeout 3.0
    