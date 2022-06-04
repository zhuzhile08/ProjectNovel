define config.default_music_volume = 0.4

# the game starts here.
label start:

    call firstDayRoadIntroduction from _call_firstDayRoadIntroduction
    call firstDayEntranceHurt from _call_firstDayEntranceHurt
 
    return
