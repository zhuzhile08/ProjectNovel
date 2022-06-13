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

    def drag_placed(drags, drop):
        if not drop:
            # Check if it is in draggedList and if yes remove it
            if drags[0].drag_name in store.draggedList:
                store.draggedList.remove(drags[0].drag_name)
            return
        
        # "store.draggable": Use of a store variable that has not been defaulted.
        # danke vscode... aber es geht
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        newX = drop.x + (drop.w / 2) - (drags[0].w / 2)
        # Round newX
        newX = int(newX)
        #print(newX)
        #print(drags[0].w / drop.w)
        drags[0].snap(newX, drop.y, .2)
        if not drags[0].drag_name in store.draggedList:
            store.draggedList.append(drags[0].drag_name)

        if len(store.draggedList) == store.dragAmount:
            return True

        #return True

label sixthDayBoss:
    default draggedList = []
    default dragAmount = 2
    
    default dragItems = []
    $ dragItems.append(DragObject("1", 0.25, 0.5))
    $ dragItems.append(DragObject("Test 2", 0.5, 0.5))

    default dragSpots = []
    $ dragSpots.append(DragSpot(0.1, 0.1, dragItems[0], "Spot 1"))
    $ dragSpots.append(DragSpot(0.1, 0.4, dragItems[1], "Very long text ss"))

    call screen drag_test2
    "[draggable] was put on [droppable]"


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
        
        drag:
            drag_name "Spot2"
            xpos 0.3
            draggable False
            droppable True
            # child "image.png"
            frame:
                xpadding 20
                ypadding 20
                text "Spot"
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