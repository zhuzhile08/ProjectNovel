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

    "{size=+10}{b}{u}Das AcI{/u}{/b}{/size}\n{b}{u}Grundwissen und Aufbau:{/u}{/b}"
    "Das Aci, Akkusativus cum Infinitivo (Akkusativ mit Infinitiv) auf Latein, kommt sehr oft in lateinischen Sätzen vor. Es wird im deutschen meistens mit einem dass-Satz übersetzt."
    "{size=-3}Ein AcI in lateinischen Sätzen enthält ein Kopfverb, Subjektakkusativ und einen Prädikatsinfinitiv:{/size}\n{color=#438A64}{u}Scio{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum suum {color=#FF4B4B}{u}amare{/u}{/color}. - Ich weiß, dass die Schwester ihre Katze liebt.\n {size=-10}*Cattus = Katze{/size}"
    "\"{color=#438A64}Scio{/color}\" ist das Kopfverb, \"{color=#00a7ff}sororem{/color}\" der Subjektakkusativ und \"{color=#FF4B4B}amare{/color}\" ist das Prädikatsinfinitiv. Wenn ein Infinitiv im Satz auftaucht, enthält dieser einen AcI mit hoher Wahrscheinlichkeit."
    "Wörter wie videre, negare, putare oder scire werden oft als Kopfverb verwendet.\n{color=#FF4B4B}ACHTUNG:{/color} Es gibt Verben, die mit einem Infinitiv stehen, aber keine Kopverben sind, zum Beispiel: posse, velle und iubere."
    "{b}{u}Vor- und Gleichzeitigkeit{/u}{/b}\n{size=-3}Mit dem AcI zeigt man auch das Zeitverhältnis zum Hauptsatz, indem man das Tempus vom Prädikatsinfinitiv ändert. Wenn man das Prädikatsininitiv in präsens schreibt, ist es gleichzeitig zum Hauptsatz, un wenn man es in Perfekt ausdrückt, ist es Vorzeitig.{/size}"
    "Im deutschen ändert as Tempus vom Prädikatsinfinitv je nach dem Tempus des Kopfverbs."
    "{color=#438A64}{u}Scio{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum suum {color=#FF4B4B}{u}amare{/u}{/color}. - Ich weiß, dass die Schwester ihre Katze liebt.\n{color=#438A64}{u}Scivi{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum {color=#FF4B4B}{u}amare{/u}{/color}. - Ich wusste, dass die Schwester ihre Katze liebte.\n{size=-10}- Gleichzeitigkeit{/size}"
    "{color=#438A64}{u}Scio{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum {color=#FF4B4B}{u}amavisse{/u}{/color}. - Ich weiß, dass die Schwester ihre Katze liebte.\n{color=#438A64}{u}Scivi{/u}{/color} {color=#00a7ff}{u}sororem{/u}{/color} cattum {color=#FF4B4B}{u}amavisse{/u}{/color}. - Ich wusste, dass die Schwester ihre Katze geliebt hatte.\n{size=-10}- Vorzeitigkeit{/size}"
    "Wenn das Kopverb im Präsens steht, wird das Prädikatsinfinitiv in Präteritum übersetzt, und wenn es im Perfekt steht, wird das Prädikatsinfinititiv in Plusquamperfekt, welches Vorzeitigkeit gegen Perekt ausdrückt, übersetzt."
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