# Characters
define b = Character("Brandy")
define w = Character("Wendy")
define s = Character("Sandy")
define h = Character("Helen")

$ bpoints = 0
$ wpoints = 0
$ spoints = 0
$ hpoints = 0

# Transitions
define dis1 = { "master" : Dissolve(1.0) } 
define dis2 = { "master" : Dissolve(2.0) }
label start:
    play sound daydream
    scene day1
    "Day 1"
    scene room_morning_light_off with dis2
    pause
    "I should hurry to school!"
    scene street_redux_day with dis1
    show nanalaugh at right with dissolve
    b "Hi!"
    b "You must be in the same school as me"
    b "My name is Brandy, What is your name?"
    $ p = renpy.input("What is your name?")
    b " Oh! [p], what a cool name!"
    b "let's go to school together"
    scene egeneric_school_gate with dis1
    show nanaconfident at right with dissolve
    b "Yes! we have arrived at time!"
    show nanatalk at right with dissolve
    b "Have a good day, See ya!"
    scene classroom_03_day with dis1
    show ayametalk at right with dissolve
    w "Hello [p], you where a little late, where you have been?"
    menu:
        "I fall asleep":
            $ wpoints += 1
            p "I fall asleep"
        "That's non of your business":
            $ wpoints -= 1
            p "That's non of your business"
    pause
    scene 
    
    return
