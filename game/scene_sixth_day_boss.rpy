init python:
    def drag_placed(drags, drop):
        if not drop:
            return
        
        # "store.draggable": Use of a store variable that has not been defaulted.
        # danke vscode... aber es geht
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

label sixthDayBoss:
    call screen drag_test2
    "[draggable] was put on [droppable]"

screen drag_test:
    fixed:
        drag:
            xpos 0.25
            ypos 0.25
            drag_raise True
            draggable True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"

screen drag_test2:
    draggroup:
        # Drag spot
        drag:
            drag_name "Spot"
            xpos 0.1
            draggable False
            droppable True
            # child "image.png"
            frame:
                xpadding 20
                ypadding 20
                text "Spot"
        
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
        drag:
            drag_name "Object"
            xpos 0.25
            ypos 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Test 1 2 3 4 5 How long can this text be"
        drag:
            drag_name "Object2"
            xpos 0.5
            ypos 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"