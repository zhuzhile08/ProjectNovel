init python:

    class DragObject:
        def __init__(self, txt, x=0.25, y=0.5):
            self.txt = txt
            self.x = x
            self.y = y
            self.dragPosition = None

    class DragSpot:
        def __init__(self, x, y, obj, txt):
            self.x = x
            self.y = y
            self.obj = obj
            self.txt = txt
            self.currentObj = None
        
        def hasCorrectObject(self):
            return self.currentObj == self.obj

    def drag_placed(drags, drop):
        if not drop:
            # Check if a dragspot has this drag object
            dragObj = None
            for dragO in dragItems:
                if dragO.txt == drags[0].drag_name:
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
            if dragSpot.txt == drop.drag_name:
                dragSpt = dragSpot 
                break
        if not dragSpt:
            return
        if dragSpt.currentObj:
            return
        # Get current drag object
        dragObj = None
        for dragO in dragItems:
            if dragO.txt == drags[0].drag_name:
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

        print(dragSpt.txt + ". Correct: " + str(dragSpt.hasCorrectObject()))

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

label sixthDayBoss:
    jump firstDrag

label firstDrag:
    
    $ dragItems = []
    $ dragSpots = []

    $ dragItems.append(DragObject("1", 0.25, 0.5))
    $ dragItems.append(DragObject("Test 2", 0.5, 0.5))

    
    $ dragSpots.append(DragSpot(0.1, 0, dragItems[0], "Spot 1"))
    $ dragSpots.append(DragSpot(0.6, 0, dragItems[1], "Very long text ss"))
    call screen drag_test2
    menu:
        "Bist du dir sicher?"
        "Ja":
            hide screen drag_test2
        "Nein":
            # warum repeatet sich das wieder hilfe
            jump firstDrag

screen drag_test2:
    draggroup:
        # Drag spot
        for dragSpot in dragSpots:
            drag:
                drag_name dragSpot.txt
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
                drag_name dragg.txt
                xpos dragg.x
                ypos dragg.y
                drag_raise True
                draggable True
                dragged drag_placed
                frame:
                    xpadding 20
                    ypadding 20
                    text dragg.txt