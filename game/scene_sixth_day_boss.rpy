init python:
    import uuid
    import random

    class TextObject:
        def __init__(self, txt, x, y):
            self.txt = txt
            self.x = x
            self.y = y

    class DragObject:
        def __init__(self, txt, x=0.25, y=0.5):
            self.txt = txt
            self.x = x
            self.y = y
            self.dragPosition = None
            self.uniqueId = None
            # Generate a unique ID for this drag object
            self.uniqueId = str(uuid.uuid4())

    class DragSpot:
        def __init__(self, x, y, obj, txt):
            self.x = x
            self.y = y
            self.obj = obj
            self.txt = txt
            self.currentObj = None
            self.uniqueId = None
            # Generate a unique ID for this drag spot
            self.uniqueId = str(uuid.uuid4())
        
        def hasCorrectObject(self):
            if self.currentObj is None:
                return False
            return self.currentObj.txt == self.obj.txt
        def isCorrectSpot(self, spot):
            return self.x == spot.x and self.y == spot.y

    class Sentence:
        def __init__(self, txt):
            self.txt = txt
            self.dragObjects = []
            self.dragSpots = []
            self.txtObj = TextObject(self.txt, 0.25, 0.5)
        
        def addDragObject(self, obj):
            self.dragObjects.append(obj)
        def addDragSpot(self, spot):
            self.dragSpots.append(spot)
        def getDragObjects(self):
            return self.dragObjects
        def getDragSpots(self):
            return self.dragSpots
        def areAnswersCorrect(self):
            for dragSpot in self.dragSpots:
                if type(dragSpot) == DragSpot and not dragSpot.hasCorrectObject():
                    return False
            return True
        def calculateAllPositions(self, indexInSentences):

            # window size: 1280x720

            txtYPos = 0.05 + indexInSentences * 0.25
            dragSpotYPos = txtYPos + 0.1
            self.txtObj.y = txtYPos
            # x position in pixels. xalign and yalign are 0
            self.txtObj.x = int(1280 - len(self.txt) * 10 - 640*0.8)
            self.txtObj.x = int(1280/2 - len(self.txt)*5)

            for obj in self.dragObjects:
                # randomize x position between 0.1 and 0.75
                obj.x = random.uniform(0.1, 0.75)
                # randomize y position between 0.8 and 0.85
                obj.y = random.uniform(0.8, 0.85)

            allObjectWidth = 0
            for obj in self.dragSpots:
                thisLength = len(obj.txt) * 10
                if type(obj) == DragSpot:
                    thisLength = len(obj.obj.txt) * 10
                allObjectWidth += thisLength
            objIndex = 0
            for i in range(len(self.dragSpots)):
                obj = self.dragSpots[i]
                thisLength = len(obj.txt) * 10
                if type(obj) == DragSpot:
                    thisLength = len(obj.obj.txt) * 10

                
                lastObj = self.dragSpots[i-1] if i > 0 else None
                if lastObj is not None:
                    # with some space between the objects
                    lastLength = len(lastObj.txt)
                    if type(lastObj) == DragSpot:
                        lastLength = len(lastObj.obj.txt) 
                    lastLengthA = lastLength * 11 + 40

                    lastLength = int(lastLengthA)
                    obj.x = lastObj.x + lastLength 
                else:
                    obj.x = self.txtObj.x - allObjectWidth / 2 + thisLength

                obj.y = dragSpotYPos
                if type(obj) == DragSpot:
                    obj.txt = len(self.dragObjects[objIndex].txt) * " "
                    
                    objIndex += 1

    def drag_position(drags, drop):
        print(str(drags[0].x) + " " + str(drags[0].y))

    def drag_placed(drags, drop):
        if not drop:
            # Check if a dragspot has this drag object
            dragObj = None
            for dragO in dragItems:
                if dragO.uniqueId == drags[0].drag_name:
                    dragObj = dragO
                    break
            if not dragObj:
                return
            dragObj.dragPosition = None
            for dragS in dragSpots:
                if dragS.currentObj == dragObj:
                    dragS.currentObj = None
                    break
            return

        # Get dragSpot with txt == drop drag_name
        dragSpt =None
        for dragSpot in dragSpots:
            if dragSpot.uniqueId == drop.drag_name:
                dragSpt = dragSpot 
                break
        
        if not dragSpt:
            return
        if dragSpt.currentObj:
            return
        # Get current drag object
        dragObj = None
        for dragO in dragItems:
            if dragO.uniqueId == drags[0].drag_name:
                dragObj = dragO
                break
        if not dragObj:
            return
        for dragS in dragSpots:
            if dragS.currentObj == dragObj:
                dragS.currentObj = None
                break

        dragSpt.currentObj = dragObj
        dragObj.dragPosition = dragSpt

        newX = drop.x + (drop.w / 2) - (drags[0].w / 2)
        newX = int(newX)

        print(dragSpt.obj.txt + ". Correct: " + str(dragSpt.hasCorrectObject()))

        drags[0].snap(newX, drop.y, .2)
        
        doAllSpotsHaveObject = True
        for dragSpot in dragSpots:
            if not dragSpot.currentObj:
                doAllSpotsHaveObject = False

        if doAllSpotsHaveObject:
            return True    

        #if len(store.draggedList) == store.dragAmount:
            #return True

default dragItems = []
default dragSpots = []
default texts = []
default sentences = []

label sixthDayBoss:
    if aki_route:
        jump aciDrag
    else:
        jump pcDrag

label finishedExam:
    "fertig a"

label aciDrag:
    
    $ dragItems = []
    $ dragSpots = []
    $ texts = []

    $ sentences = []
    $ sentences.append(Sentence("a) Gladiatorem fortem vincere scis."))

    $ sentences[0].dragObjects.append(DragObject("Du", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("weißt", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("der starke Gladiator", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("besiegt.", 0.25, 0.8))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[0], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[1], ""))
    $ sentences[0].dragSpots.append(TextObject(", dass", 0, 0))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[2], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[3], ""))


    $ sentences.append(Sentence("b) Video gladiatorem gladio petere."))
    $ sentences[1].dragObjects.append(DragObject("Ich", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("sehe", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("der Gladiator", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("mit seinem Schwert", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("angreift.", 0.25, 0.8))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[0], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[1], ""))
    $ sentences[1].dragSpots.append(TextObject(", dass", 0, 0))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[2], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[3], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[4], ""))

    $ sentences.append(Sentence("c) Gladiator confirmabat se fortem esse."))
    $ sentences[2].dragObjects.append(DragObject("Der Gladiator", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("bestätigt", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("er", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("stark", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("ist.", 0.25, 0.8))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[0], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[1], ""))
    $ sentences[2].dragSpots.append(TextObject(", dass", 0, 0))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[2], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[3], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[4], ""))


    python:
        ind = 0
        for sen in sentences:
            sen.calculateAllPositions(ind)
            for d in sen.dragObjects:
                dragItems.append(d)
            texts.append(sen.txtObj)
            for ds in sen.dragSpots:
                if type(ds) == DragSpot:
                    dragSpots.append(ds)
                else:
                    texts.append(ds)
            
            ind += 1

    call screen drag_test2
    menu:
        "Bist du dir sicher?"
        "Ja":
            hide screen drag_test2
            # Check if all answers are correct
            python:
                if sentences[0].areAnswersCorrect():
                    aki_affec += 2
                if sentences[1].areAnswersCorrect():
                    aki_affec += 2
                if sentences[2].areAnswersCorrect():
                    aki_affec += 2
            jump aciDrag2
        "Nein":
            # warum repeatet sich das wieder hilfe
            jump aciDrag

label aciDrag2:
    $ dragItems = []
    $ dragSpots = []
    $ texts = []

    
    $ sentences = []
    # First sentence: Equum celere properavisse audivit.
    # translation: Er hörte, dass das Pferd schnell geeilt hatte.
    $ sentences.append(Sentence("a) Equum celere properavisse audivit."))
    $ sentences[0].dragObjects.append(DragObject("Er", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("hörte", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("das Pferd", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("schnell", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("geeilt", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("hatte.", 0.25, 0.8))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[0], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[1], ""))
    $ sentences[0].dragSpots.append(TextObject(", dass", 0, 0))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[2], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[3], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[4], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[5], ""))

    # Second sentence: Putavistis equum eum celerem esse.
    # translation: Ihr glaubtet, dass dieses Pferd schnell war.
    $ sentences.append(Sentence("b) Putavistis equum eum celerem esse."))
    $ sentences[1].dragObjects.append(DragObject("Ihr", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("glaubtet", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("dieses Pferd", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("schnell war.", 0.25, 0.8))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[0], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[1], ""))
    $ sentences[1].dragSpots.append(TextObject(", dass", 0, 0))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[2], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[3], ""))

    # Third sentence: Dixerunt me equum violare.
    # translation: Sie sagten, dass ich das Pferd verletzt habe.
    $ sentences.append(Sentence("c) Dixerunt me equum violare."))
    $ sentences[2].dragObjects.append(DragObject("Sie", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("sagten", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("ich", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("das Pferd verletzt", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("habe.", 0.25, 0.8))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[0], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[1], ""))
    $ sentences[2].dragSpots.append(TextObject(", dass", 0, 0))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[2], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[3], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[4], ""))

    python:
        ind = 0
        for sen in sentences:
            sen.calculateAllPositions(ind)
            for d in sen.dragObjects:
                dragItems.append(d)
            texts.append(sen.txtObj)
            for ds in sen.dragSpots:
                if type(ds) == DragSpot:
                    dragSpots.append(ds)
                else:
                    texts.append(ds)
            
            ind += 1

    call screen drag_test2
    menu:
        "Bist du dir sicher?"
        "Ja":
            hide screen drag_test2
            # check if answers are correct
            python:
                if sentences[0].areAnswersCorrect():
                    aki_affec += 2
                if sentences[1].areAnswersCorrect():
                    aki_affec += 2
                if sentences[2].areAnswersCorrect():
                    aki_affec += 2
            jump finishedExam
        "Nein":
            # warum repeatet sich das wieder hilfe
            jump aciDrag2

label pcDrag:
    $ dragItems = []
    $ dragSpots = []
    $ texts = []

    
    $ sentences = []
    # First sentence: Gladiator a populo laudatus gaudet.
    # translation: Der Gladiator freute sich wegen der Lobe des Volkes.
    $ sentences.append(Sentence("a) Gladiator a populo laudatus gaudet."))
    $ sentences[0].dragObjects.append(DragObject("Der Gladiator", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("freute sich", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("wegen", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("der Lobe", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("des Volkes.", 0.25, 0.8))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[0], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[1], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[2], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[3], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[4], ""))

    # Second sentence: b) Gladiator a gladiatorem alium victus flebat.
    # translation: Der Gladiator weinte, nachdem er von einem anderen Gladiator besiegt worden war.
    $ sentences.append(Sentence("b) Gladiator a gladiatorem alium victus flebat."))
    $ sentences[1].dragObjects.append(DragObject("Der Gladiator", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("weinte, ", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("nachdem", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("er", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("von einem", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("anderen Gladiator", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("besiegt worden war.", 0.25, 0.8))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[0], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[1], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[2], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[3], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[4], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[5], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[6], ""))
    
    # Third sentence: c) Gladiator in pugnam victus a omnes relictus erat.
    # translation: Der Gladiator war von allen verlassen worden, nachdem er im Kampf besiegt worden war.
    $ sentences.append(Sentence("c) Gladiator in pugnam victus a omnes relictus erat."))
    $ sentences[2].dragObjects.append(DragObject("Der Gladiator war", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("von allen", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("verlassen worden, ", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("nachdem", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("er", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("im Kampf", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("besiegt worden war.", 0.25, 0.8))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[0], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[1], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[2], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[3], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[4], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[5], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[6], ""))

    python:
        ind = 0
        for sen in sentences:
            sen.calculateAllPositions(ind)
            for d in sen.dragObjects:
                dragItems.append(d)
            texts.append(sen.txtObj)
            for ds in sen.dragSpots:
                if type(ds) == DragSpot:
                    dragSpots.append(ds)
                else:
                    texts.append(ds)
            
            ind += 1

    call screen drag_test2
    menu:
        "Bist du dir sicher?"
        "Ja":
            hide screen drag_test2
            # check if answers are correct
            python:
                if sentences[0].areAnswersCorrect():
                    partizia_affec += 2
                if sentences[1].areAnswersCorrect():
                    partizia_affec += 2
                if sentences[2].areAnswersCorrect():
                    partizia_affec += 2
            jump pcDrag2
        "Nein":
            # warum repeatet sich das wieder hilfe
            jump pcDrag

label pcDrag2:
    $ dragItems = []
    $ dragSpots = []
    $ texts = []

    
    $ sentences = []
    # First sentence: a) Equus celere latus celer est.
    # translation: Das Pferd, das schnell gebracht worden ist, ist schnell.
    $ sentences.append(Sentence("a) Equus celere latus celer est."))
    $ sentences[0].dragObjects.append(DragObject("Das Pferd", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("schnell gebracht", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("worden ist, ", 0.25, 0.8))
    $ sentences[0].dragObjects.append(DragObject("ist schnell.", 0.25, 0.8))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[0], ""))
    $ sentences[0].dragSpots.append(TextObject(", das", 0.25, 0.8))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[1], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[2], ""))
    $ sentences[0].dragSpots.append(DragSpot(0, 0, sentences[0].dragObjects[3], ""))

    # Second sentence: b) b) Equus petitus violatus est.
    # translation: Das angegriffene Pferd ist verletzt worden.
    $ sentences.append(Sentence("b) Equus petitus violatus est."))
    $ sentences[1].dragObjects.append(DragObject("Das", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("angegriffene", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("Pferd", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("ist verletzt", 0.25, 0.8))
    $ sentences[1].dragObjects.append(DragObject("worden.", 0.25, 0.8))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[0], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[1], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[2], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[3], ""))
    $ sentences[1].dragSpots.append(DragSpot(0, 0, sentences[1].dragObjects[4], ""))

    # Third sentence: c) Equus a medico servatus laetus erat.
    # translation: Das Pferd war fröhlich, weil es vom Arzt gerettet worden war.
    $ sentences.append(Sentence("c) Equus a medico servatus laetus erat."))
    $ sentences[2].dragObjects.append(DragObject("Das Pferd", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("war fröhlich, ", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("weil", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("es", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("vom Arzt", 0.25, 0.8))
    $ sentences[2].dragObjects.append(DragObject("gerettet worden war.", 0.25, 0.8))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[0], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[1], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[2], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[3], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[4], ""))
    $ sentences[2].dragSpots.append(DragSpot(0, 0, sentences[2].dragObjects[5], ""))

    python:
        ind = 0
        for sen in sentences:
            sen.calculateAllPositions(ind)
            for d in sen.dragObjects:
                dragItems.append(d)
            texts.append(sen.txtObj)
            for ds in sen.dragSpots:
                if type(ds) == DragSpot:
                    dragSpots.append(ds)
                else:
                    texts.append(ds)
            
            ind += 1

    call screen drag_test2
    menu:
        "Bist du dir sicher?"
        "Ja":
            hide screen drag_test2
            # check if answers are correct
            python:
                if sentences[0].areAnswersCorrect():
                    partizia_affec += 2
                if sentences[1].areAnswersCorrect():
                    partizia_affec += 2
                if sentences[2].areAnswersCorrect():
                    partizia_affec += 2
            jump finished
            
        "Nein":
            # warum repeatet sich das wieder hilfe
            jump pcDrag2

screen drag_test2:
    draggroup:
        # Drag spot
        for dragSpot in dragSpots:
            drag:
                drag_name dragSpot.uniqueId
                xpos dragSpot.x
                ypos dragSpot.y
                draggable False
                droppable True
                # child "image.png"
                # add to draggroup
                frame:
                    xpadding 20
                    ypadding 20
                    text dragSpot.txt
        # Draggable object
        for dragg in dragItems:
            drag:
                drag_name dragg.uniqueId
                xpos dragg.x
                ypos dragg.y
                drag_raise True
                draggable True
                dragged drag_placed
                frame:
                    xpadding 20
                    ypadding 20
                    text dragg.txt
    for textObj in texts:
        frame:
            xpadding 20
            ypadding 20
            xpos textObj.x
            ypos textObj.y
            text textObj.txt