# Blue: #00a7ff
# Red: #FF4B4B
# Green: #438A64

label firstDayClubroomLearning:
    scene Bg Classroom
    stop music fadeout 3.0
    queue music "audio/music/club.ogg" fadein 2.0
    "Was soll ich lernen?"
    menu:
        "PC lernen":
            "Hier ist ein altes Buch über das PC, geschrieben von Ben Dover."
            "{size=+10}{b}{u}Das PC{/u}{/b}{/size}\n{b}{u}Grundwissen und Aufbau:{/u}{/b}"
            "Das PC, Partizipium Coniunctum, kommt in lateinischen Sätzen oft als Attribut vor. Man bildet diese mit dem Bezugswort und dem PPP (Partizip Perfekt Passiv). Außerdem stehen Pcs immer vorzeitig zum Hauptsatz."
            "{color=#00a7ff}{u}Cattus{/u}{/color} {color=#FF4B4B}{u}servatus{/u}{/color} latus est. - Die {color=#FF4B4B}gerettete{/color} {color=#00a7ff}Katze{/color} ist fröhlich.\n {size=-10}*Cattus = Katze{/size}\n\n{size=-3}In diesem Fall ist \"Cattus\" das Bezugswort und \"servatus\" das Partizip.{/size}"
            "{b}{u}Ablativ des Urhebers:{/u}{/b}\nDa das Pc im Passiv steht, kann es im Satz auch einen Urheber geben, der dem Subjekt eine Tat ausübt. Solche stehen im Ablativ und werden Ablativ ddes Urhebers genannt."
            "{color=#00a7ff}{u}Cattus{/u}{/color} a {color=#438A64}{u}domino{/u}{/color} {color=#FF4B4B}{u}servatus{/u}{/color} latus est. - Die {color=#438A64}vom Herrn{/color} {color=#FF4B4B}gerettete{/color} {color=#00a7ff}Katze{/color} ist fröhlich."
            "{size=-3}Wenn der Urheber eine Person ist, wird dessen Wort mit einem \"a\" geschrieben, und wenn nicht, schreibt man es nicht.{/size}\n\n{color=#00a7ff}{u}Cattus{/u}{/color} {color=#438A64}{u}ira{/u}{/color} {color=#FF4B4B}{u}mota{/u}{/color} petivit. - Die {color=#438A64}von Zorn{/color} {color=#FF4B4B}bewegte{/color} {color=#00a7ff}Katze{/color} griff an."
            "{b}{u}Erkennung:{/u}{/b}\nMan erkennt ein Pc an dessen PPP, welches auch KNG-Konguent zu dem Bezugswort ist."
            "{size=-3}Um den Ablativ des Urhebers auch mitzuerkennen kann man Klammern anwenden. Die fängt nach dem Bezugswort an und endet nach dem Partizip.{/size}\n\n{color=#00a7ff}{u}Cattus{/u}{/color} a ({color=#438A64}{u}domino{/u}{/color} {color=#FF4B4B}{u}servatus{/u}{/color}) latus est."
        "ACI lernen":
            jump readACI

label readACI:
    # b