# define images here
# aki
layeredimage Aki:
    always:
        "aki_head"

    group outfit:
        attribute uniform default:
            "aki_uniform_base"
        attribute casual:
            "aki_casual_base"
        
    group left_arm:
        attribute uniform default:
            "aki_uniform_left"
        attribute casual:
            "aki_casual_left"
    
    group right_arm:
        attribute uniform default:
            "aki_uniform_right"
        attribute casual:
            "aki_casual_right"
    
    group eyes:
        attribute normal default:
            "aki_eyes_open"
        attribute closed:
            "aki_eyes_closed"

    group eyelids:
        attribute neutral default:
            "aki_eyelids_neutral"
        attribute sad:
            "aki_eyelids_sad"
        attribute angry:
            "aki_eyelids_angry"
    
    group mouth:
        attribute small default:
            "aki_mouth_small"
        attribute big:
            "aki_mouth_big"
        attribute happy:
            "aki_mouth_happy"
        attribute sad:
            "aki_mouth_sad"
        attribute laugh:
            "aki_mouth_laugh"
        attribute laugh_teeth:
            "aki_mouth_laugh_teeth"
        attribute angry:
            "aki_mouth_angry"
    
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
image Bg Park Lake = im.Scale("bg/park_lake.png", 1280, 720)
image Bg Park Path = im.Scale("bg/park_path.png", 1280, 720)
image Bg Park Path 2 = im.Scale("bg/park_path_2.png", 1280, 720)
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
image Bg Splashscreen = "bg/splashscreen.png"