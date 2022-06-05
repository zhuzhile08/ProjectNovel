# Blue: #00a7ff
# Red: #FF4B4B
# Green: #438A64

label firstDayClubroomLearning:
    "Endlich bin ich im Clubraum angekommen."
    scene Bg Classroom with fade
    stop music fadeout 3.0
    queue music "audio/music/club.ogg" fadein 2.0
    "Der Leher hat gesagt, dass wir ein Test schreiben werden, aber nicht über was."
    "Wenn ich mal ehrlich bin, ist es ein ziemlich blöder move, aber was solls?"
    "Ich glaube der Sinn von solch einen Test liegt daran, dass man beides gleich lernen und beherrschen sollte."
    "Aber ich lerne nur eines von denen, weil ich es kann."
    menu:
        "Was soll ich denn überhaupt lernen?"

        "PC lernen":
            jump readPC
        "ACI lernen":
            jump readACI


label readPC:
    "Aus den Schank vor mir habe ich ein uraltes, mit Staub bedecktes Buch genommen."
    "Ich puste das Staub weg und eine riesige Wolke taucht auf"
    "Unter der Staubschicht erscheint der Text:"
    "Partizipium Coniunctum für Beginner, von Ben Dover."
    "{size=+10}{b}{u}Das PC{/u}{/b}{/size}\n{b}{u}Grundwissen und Aufbau:{/u}{/b}"
    "Das PC, Partizipium Coniunctum, kommt in lateinischen Sätzen oft als Attribut vor. Man bildet diese mit dem Bezugswort und dem PPP (Partizip Perfekt Passiv). Außerdem stehen Pcs immer vorzeitig zum Hauptsatz."
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
            jump readPC
        "Ja":
            jump after

label readACI:
    "Aus den Schank vor mir habe ich ein uraltes, mit Staub bedecktes Buch genommen."
    "Ich puste das Staub weg und eine riesige Wolke taucht auf"
    "Unter der Staubschicht erscheint der Text:"
    "Akkusativus cum Infinitivum made Easy, von Mike Oxlong."

    menu:
        "Das war ein Haufen. Habe ich das alles schon verstanden?"

        "Nein":
            "Nicht wirklich, aber alles nochmal zu lesen kann ja einen nichts schlechtes antun."
            jump readACI
        "Ja":
            jump after

label after:
    "Recht einfach zu verstehen. Aber auch ein Lateinweltmeister wie ich braucht auch mal eine Pause"
    "Ich gucke auf die Uhr und bemerke, dass ich noch 30 Minuten bis zum Test habe."
    "Also habe ich mein Handy rausgenommen und ein bisschen darauf rumgedaddlet."
    scene Bg Load
    with fade
    stop music fadeout 3.0