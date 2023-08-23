

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image camescope = Movie(play="filtro.webm", loop= True)

screen effet_camescope():
    zorder 10
    add "camescope":
        alpha 0.7

define config.overlay_screens = ["effet_camescope"]




init:
    image pc_happy = "pc_happy.png"
    image pc_happy glitch = Glitch("pc_happy.png")
init -2:
    style say_thought:
        line_spacing -25
    style say_dialogue:
        line_spacing -25

define config.keymap['self_voicing'] = []
define config.keymap['clipboard_voicing'] = []
define config.keymap['screenshot'] = []

screen warning():
    imagebutton auto "images/yes_%s.png" focus_mask True action [ToggleScreen("warning"), Jump("isurytosh_on")] hovered [ Play ("sound" , "audio/click.wav") ]
    imagebutton auto "images/no_%s.png" focus_mask True action [ToggleScreen("warning"), Jump("non")] hovered [ Play ("sound" , "audio/click.wav") ]

label non:
    $ renpy.quit()

label splashscreen:

    show warning with dissolve

    with Pause(1.5)

    call screen warning with dissolve




label isurytosh_on:
    scene black
    $ renpy.movie_cutscene("isurytosh_on.webm", stop_music=False)
    play music "old_computer_sound.mp3" loop
    call screen isurytosh_screen

screen isurytosh_screen():
    tag statsUI
    add "images/isurytosh_screen.png"
    imagebutton auto "images/cat_%s.png" focus_mask True action Play("sound", "audio/cat.wav")
    imagebutton auto "images/sj_%s.png" focus_mask True action [ToggleScreen("isurytosh_screen"), Jump("js_open")]
    imagebutton auto "images/trash_%s.png" focus_mask True action [ToggleScreen("isurytosh_screen"), Jump("trash")]
    
label trash:
    $ renpy.movie_cutscene("open_trash.webm", stop_music=False)
    call screen isurytosh_trash

screen isurytosh_trash():
    tag statsUI
    add "images/isurytosh_trash.png"
    imagebutton auto "images/my_life_%s.png" focus_mask True action Play("sound", "audio/oh_oh.wav")
    imagebutton auto "images/exit_%s.png" focus_mask True action [ToggleScreen("isurytosh_trash"), Jump("close_trash")]

label close_trash:
    $ renpy.movie_cutscene("close_trash.webm", stop_music=False)
    call screen isurytosh_screen

label js_open:
    $ renpy.movie_cutscene("js_open.webm", stop_music=False)
    call screen js_open_screen

screen js_open_screen():
    tag statsUI
    add "images/js_open.png"    
    imagebutton auto "images/sj_si_%s.png" focus_mask True action [ToggleScreen("js_open_screen"), Jump("intro_animation")]
    imagebutton auto "images/close_si_%s.png" focus_mask True action [ToggleScreen("js_open_screen"), Jump("close_js")]

label close_js:
    $ renpy.movie_cutscene("js_close.webm", stop_music=False)
    call screen isurytosh_screen


label intro_animation:

    $ renpy.movie_cutscene("transition_intro.webm")

    return






# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

##pick between one of the two and add an # to the other to keep it

##regular taps, medium intervals
define sounds = ['audio/text.mp3']

##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']


##both combined
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


#example of a character with the typing sound
define Type = Character("Character with typing", callback=type_sound)


#just don't add the character callback if you don't want that ound
define NoType = Character("Character without typing")

#regular narration that doesn't have a character attached to it, add an # to it if you don't want that
define narrator = Character("", callback=type_sound)

label start:

    $ _game_menu_screen = "preferences"
    $ _rollback = False

    show filtro onlayer filtro

    play music "old_computer_sound.mp3"

    scene pc_happy with dissolve

    "Greetings, (Test Subject number 1)."

    show pc_smile
    
    "I welcome you to Sanity Junction, an objective test designed to measure the level of utilitarian thinking from the depths of the human psyche."

    show pc_happy

    "First of all, do you have a clear idea of what utilitarian thinking is?"

    menu:
        "No":
            jump no

label noo:

    show pc_eh

    "Why?"
    
    menu:
        "I don't want to take this test":
            jump because_not
    
        "I haven't understood the concept of the test":
            jump no

label because_not:

    stop music fadeout 0.5

    "THEN..."

    show pc_happy

    "..."

    scene expression "#cc0000"
    show pc_happy at Glitch(_fps=1000.)
    ".̶̢̢̛̗̲̱̰̞̄̅͋̓͂̋̒̐̆̎̿̋̀͑̈ͅ.̴̢͉̪̭̖̹͖̥͍̈́̎̋͜."
    show pc_happy at Glitch(_fps=1000., glitch_strength=.3, color_range1="#0a00", color_range2="0f0")
    show layer screens at Glitch(glitch_strength=.75)
    "TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH"
    window hide

    $ renpy.movie_cutscene("videos/hell_1.webm")
    show hell_1
    $ renpy.pause ()
    $ renpy.movie_cutscene("videos/hell_2.webm")
    show hell_2
    $ renpy.pause ()
    $ renpy.movie_cutscene("videos/hell_3.webm")
    show hell_3
    $ renpy.pause ()
    $ renpy.movie_cutscene("videos/hell_4.webm")

    $ renpy.quit()

label no:

    scene pc_happy
    
    "Don't worry, I will help you understand the principles behind this ethical framework."

    scene balance with dissolve
    
    "Utilitarianism is a moral theory that focuses on maximizing general well-being and happiness while minimizing suffering."
    
    scene tranvia with dissolve

    "In simpler terms, it suggests that the best action is the one that produces the greatest good for the greatest number of people, even if it involves making difficult decisions."
    scene variations with dissolve

    "In this test, you will be faced with questioning which decisions to make in a series of scenarios, each presenting slightly different situations."

    scene question with dissolve
    
    "There are no right or wrong answers. This test simply aims to observe and conclude how your choices align with utilitarian thinking."

    scene pc_smile with dissolve
    
    "Your decisions will be the core of your exploration of this concept and will determine to what extent you embrace utilitarian values."

    scene pc_happy
    
    "Do you feel ready to begin?"

    
    menu:
        "No":
            jump noo