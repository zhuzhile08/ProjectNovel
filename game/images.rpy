# define images here
# aki
layeredimage Aki:
    always:
        "aki_head"

    group outfit:
        attribute outfit_uniform default:
            "aki_uniform_base"
        attribute outfit_casual:
            "aki_casual_base"
        
    group left_arm:
        attribute left_uniform default:
            "aki_uniform_left"
        attribute left_casual:
            "aki_casual_left"
    
    group right_arm:
        attribute right_uniform default:
            "aki_uniform_right"
        attribute right_casual:
            "aki_casual_right"
    
    group eyes:
        attribute eyes_open default:
            "aki_eyes_open"
        attribute eyes_closed:
            "aki_eyes_closed"

    group eyebrows:
        attribute eyebrows_neutral default:
            "aki_eyebrows_neutral"
        attribute eyebrows_sad:
            "aki_eyebrows_sad"
        attribute eyebrows_angry:
            "aki_eyebrows_angry"
    
    group mouth:
        attribute mouth_small default:
            "aki_mouth_small"
        attribute mouth_big:
            "aki_mouth_big"
        attribute mouth_happy:
            "aki_mouth_happy"
        attribute mouth_sad:
            "aki_mouth_sad"
        attribute mouth_laugh:
            "aki_mouth_laugh"
        attribute mouth_laugh_teeth:
            "aki_mouth_laugh_teeth"
        attribute mouth_angry:
            "aki_mouth_angry"
    
    zoom 0.65

layeredimage Partizia:
    always:
        "partizia_base"
        
    group left_arm:
        attribute left_normal default:
            "partizia_left"
    
    group right_arm:
        attribute right_normal default:
            "partizia_right"
    
    group eyes:
        attribute eyes_open default:
            "partizia_eyes_open"
        attribute eyes_closed:
            "partizia_eyes_closed"

    group eyebrows:
        attribute eyebrows_neutral default:
            "partizia_eyebrows_neutral"
        attribute eyebrows_sad:
            "partizia_eyebrows_sad"
        attribute eyebrows_angry:
            "partizia_eyebrows_angry"
    
    group mouth:
        attribute mouth_small default:
            "partizia_mouth_small"
        attribute mouth_big:
            "partizia_mouth_big"
        attribute mouth_happy:
            "partizia_mouth_happy"
        attribute mouth_sad:
            "partizia_mouth_sad"
        attribute mouth_laugh:
            "partizia_mouth_laugh"
        attribute mouth_laugh_teeth:
            "partizia_mouth_laugh_teeth"
        attribute mouth_angry:
            "partizia_mouth_angry"
    
    zoom 0.65

# crowd effect
image Crowd:
    "vfx/crowd_1.png" with Dissolve(0.3)
    pause 0.5
    "vfx/crowd_2.png" with Dissolve(0.3)
    pause 0.5
    "vfx/crowd_3.png" with Dissolve(0.3)
    pause 0.5
    repeat

# define backgrounds here
image Bg Cafeteria = im.Scale("bg/cafeteria.png", 1280, 720)
image Bg Classroom = im.Scale("bg/classroom.png", 1280, 720)
image Bg Hallway = im.Scale("bg/hallway.png", 1280, 720)
image Bg Hallway Staircase = im.Scale("bg/hallway_staircase.png", 1280, 720)
image Bg Main Staircase Lower Floor = im.Scale("bg/main_staircase_lower_floor.png", 1280, 720)
image Bg Main Staircase Upper Floor = im.Scale("bg/main_staircase_upper_floor.png", 1280, 720)
image Bg Clubroom = im.Scale("bg/clubroom.png", 1280, 720)
image Bg Park Path = im.Scale("bg/park_path.png", 1280, 720)
image Bg School Entrance = im.Scale("bg/school_entrance.png", 1280, 720)
image Bg School Way = im.Scale("bg/school_way.png", 1280, 720)
image Bg Side Path = im.Scale("bg/side_path.png", 1280, 720)
image Bg Side Staircase Lower Floor = im.Scale("bg/side_staircase_lower_floor.png", 1280, 720)
image Bg Side Staircase Upper Floor = im.Scale("bg/side_staircase_upper_floor.png", 1280, 720)
image Bg Stone Circle = im.Scale("bg/stone_circle.png", 1280, 720)
image Bg Home Door = im.Scale("bg/home_door.png", 1280, 720)
image Bg Home Outwards = im.Scale("bg/home_outwards.png", 1280, 720)
image Bg Home Road = im.Scale("bg/home_road.png", 1280, 720)
image Bg Load = "bg/loading.png"
image Bg Room = im.Scale("bg/room.png", 1280, 720)
image Bg Splashscreen = "bg/splashscreen.png"