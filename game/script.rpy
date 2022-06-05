define config.default_music_volume = 0.4

# the game starts here.
label start:
    call firstDayRoadIntroduction
    call firstDayEntrancePartizia
    call firstDayClassroomSleep
    call firstDayClubroomLearning

    return
