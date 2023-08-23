# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -2:
    style say_thought:
        line_spacing -25
    style say_dialogue:
        line_spacing -25

define e = Character("Eileen")

define config.keymap['self_voicing'] = []
define config.keymap['clipboard_voicing'] = []
define config.keymap['screenshot'] = []

screen warning():
    imagebutton auto "images/yes_%s.png" focus_mask True action [ToggleScreen("warning"), Jump("video_splash")] hovered [ Play ("sound" , "audio/click.wav") ]
    imagebutton auto "images/no_%s.png" focus_mask True action [ToggleScreen("warning"), Jump("non")] hovered [ Play ("sound" , "audio/click.wav") ]


label splashscreen:

    show warning with dissolve

    with Pause(1.5)

    call screen warning with dissolve


label video_splash:

    scene black

    scene warning_yes with dissolve

    pause 5.0

    $ renpy.movie_cutscene("splash_screen.webm")

    jump isurytosh_on

label isurytosh_on:
    scene black
    $ renpy.movie_cutscene("isurytosh_on.webm")
    play music "old_computer_sound.mp3" loop
    call screen isurytosh_screen

screen isurytosh_screen():
    tag statsUI
    add "images/isurytosh_screen.png"
    imagebutton auto "images/cat_%s.png" focus_mask True action Play("sound", "audio/cat.wav")
    imagebutton auto "images/sj_%s.png" focus_mask True action ShowMenu("about")
    imagebutton auto "images/trash_%s.png" focus_mask True action ShowMenu("about")
    
    

label non:
    $ renpy.quit()

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


    NoType "My dialogue does not have typing in it!"
    Type "My dialogue has it, I serve as an example for character callbacks!"
    NoType "..."
    Type "..."
    "Give it a shot with a short text."

    "Try with, like, a super long text, like crazy long where I could've used Lorem Ipsum but I was too lazy LOL."

    "But hey..."

    "We see that this is working."

    "Awesome :D"


    menu:
        "XDDDDDD":
            $ renpy.quit()
        "XDDDDDD":
            $ renpy.quit()
        "XDDDDDDDDD":
            $ renpy.quit()
        "XDDDDDDDDDDDDDDDDDDD":
            $ renpy.quit()
        "._.":
            $ renpy.quit()

    # This ends the game.

    return

