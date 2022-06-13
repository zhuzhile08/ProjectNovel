define config.default_music_volume = 0.4
$ preferences.text_cps = 42

# the game starts here.
label start:
    call firstDayRoadIntroduction from _call_firstDayRoadIntroduction
    call firstDayEntrancePartizia from _call_firstDayEntrancePartizia
    call firstDayClassroomSleep from _call_firstDayClassroomSleep
    call firstDayClubroomLearning from _call_firstDayClubroomLearning
    call firstDayClassroomExam from _call_firstDayClassroomExam
    call secondDayRoad from _call_secondDayRoad
    call secondDayAfternoon from _call_secondDayAfternoon
    call fourthDayTutor
    call fifthDayCorrection
    call sixthDayBoss from _call_sixthDayBoss

    call eighthDayEnding from _call_eighthDayEnding

    return
