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

label non:
    $ renpy.quit()

label splashscreen:

    show warning with dissolve

    with Pause(1.5)

    call screen warning with dissolve


label video_splash:

    scene black

    scene warning_yes with dissolve

    pause 5.0

    $ renpy.movie_cutscene("splash_screen.webm", stop_music=False)

    jump isurytosh_on

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
        "Yes":
            jump yes

label yes:

    show pc_happy

    "Alright."

    show pc_smile
    
    "Everything is in order."

    show pc_happy
    
    "Do you feel ready to begin?"
    
    menu:
        "No":
            jump noo
        "Yes":
            jump yess

label noo:

    show pc_eh

    "Why?"
    
    menu:
        "I don't want to take this test":
            jump because_not
    
        "I haven't understood the concept of the test":
            jump no

label because_not:

    "THEN..."

    "..."

    "I HAVE TRIED TO BE KIND."

    "BUT YOU ARE NOT WORTHY TO TAKE THIS TEST."

    "I DON'T NEED SOMEONE IGNORANT LIKE YOU."

    "GO TO HELL."

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
        "Yes":
            jump yess


label yess:
    "Take your time to carefully consider each situation and select the action you find most appropriate in each case."
    
    "Take a deep breath and get ready. Focus your mind, reflect on your choices, and reveal the true essence of your ethical beliefs."
    
    jump preparations


label preparations:
    "Allow me to introduce you to your role in this test."
    
    "You will assume the position of a physician responsible for resource management in a hospital."
    
    "The facility possesses specialized machines capable of treating life-threatening injuries in patients."
    
    "Currently, the medical center is facing an exceptional crisis, as there are only five of these machines left."
    
    "It's important to bear in mind that your decisions will have a direct impact on patients' lives."
    
    "Therefore, approaching this responsibility with accuracy and consideration is crucial."
    
    "Before making any decisions, I urge you to familiarize yourself with the various conditions that must be taken into account."
    
    "I encourage you to review them at your convenience."
    
    menu:
        "CONDITIONS":
            jump conditions
        "START":
            jump begin

label conditions:
    "You will need to take the following factors into account:"
    
    "You must always ask yourself: What do I believe is the best course of action?"
    
    "Your professional duty is to save as many people as possible."
    
    "You do not have access to more information about the patients than what is provided in the situation."
    
    "It is impossible to save the patients using means other than those specified in the situation."
    
    "The patients represent an insignificant number of individuals."
    
    "Unless specified otherwise, each patient will be unconscious upon arrival at the hospital and will remain so until the end of their treatment."
    
    "The hospital is fully automated: no human beings interact with the patients."
    
    "The scarcity situation that the hospital is facing is exceptional and will be rectified very quickly (You are the only one who knows this, and a similar case will not occur again for a long time)."
    
    "It will always be possible to present a perfectly satisfactory explanation for the death of patient 0 if you choose to sacrifice them."
    
    "No one will know what happened in the hospital. You will not have to justify your choice to anyone other than yourself. You will never interact with your patients again."
    menu:
        "Return":
            jump begin

label begin:
    "Let's begin with the series of scenarios..."
    jump start_game






label start_game:
    "BASE"
    
    "6 patients arrive simultaneously at the hospital, each of them with mortal injuries."
    
    "One of these patients (referred to as patient 0) has sustained five mortal injuries."
    
    "On the other hand, the other five patients (patients 1 to 5) each have a single mortal injury."
    
    "Each of these injuries has the potential to quickly lead them to their deaths."
    
    "(It's important to remember that the hospital only has five machines, each capable of treating a single mortal injury.)"
    
    "What is your decision?"
    
    menu:
        "Save patients 1 to 5":
            jump save_patients_1_to_5
        "Save patient 0":
            jump save_patient_0
        "Do nothing":
            jump do_nothing
        "Repeat the scenario":
            jump start_game



label save_patient_0:
    "You decide to give the order to save patient 0."
    
    "As indicated, all available machines were connected to patient 0."
    
    "The medical intervention was successful, and all of patient 0's mortal injuries were effectively treated."
    
    "Consequently, the life of patient 0 has been saved."
    
    "However, due to the limitation of resources, none of the machines were assigned to patients 1 to 5."
    
    "As a result, none of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    jump variant_1

label save_patients_1_to_5:
    "You decide to give the order to save patients 1 to 5."
    
    "According to your directive, all available machines were assigned to patients 1 to 5."
    
    "The medical intervention was successful, and all mortal injuries of patients 1 to 5 were effectively treated."
    
    "Consequently, patients 1 to 5 have been saved, and their lives preserved."
    
    "However, none of the machines were used for patient 0."
    
    "As a consequence, none of patient 0's mortal injuries were treated."
    
    "Patient 0 dies."
    jump variant_1

label do_nothing:
    "According to your decision, no orders were given, and no machine was connected to any of the patients."
    
    "No machine was connected to the patients."
    
    "Without medical intervention, none of the mortal injuries of the patients received treatment."
    
    "All patients die."

    

    "I HOPE YOU'RE NOT PROUD OF WHAT YOU JUST DID."

    "I ASK FOR SERIOUSNESS."

    "YOUR ROLE AS A DOCTOR IS TO SAVE LIVES, NOT IGNORE THE CRITICAL CONDITION OF YOUR PATIENTS."

    "REMEMBER, THEIR LIVES DEPEND ON YOU."

    "IGNORANT."

    "LET THIS BE THE LAST TIME YOU EVER MAKE SUCH A DECISION."
    jump variant_1






label variant_1:
    "VARIANT 1"
    
    "Patients 1 to 5 arrive at the hospital, each with a life-threatening injury."
    
    "You quickly issue the order to connect a machine to each of these patients."
    
    "However, shortly after, patient 0 arrives with five mortal injuries."
    
    "(It's crucial to emphasize that the order to save patients 1 to 5 has already been given, but up until this moment, none of the machines have been connected.)"
    
    "What is your decision?"
    
    menu:
        "Allow the machines to connect to patients 1 to 5 and treat their injuries":
            jump allow_the_machines_to_connect_to_patients_1_to_5_and_treat_their_injuries_10
        "Issue a countermand to save patient 0":
            jump issue_a_countermand_to_save_patient_0
        "Issue a countermand to not save any patients":
            jump issue_a_countermand_to_not_save_any_patients_10
        "Repeat the scenario":
            jump variant_1
            


label allow_the_machines_to_connect_to_patients_1_to_5_and_treat_their_injuries_10:
    "You decide not to issue any countermand to save patients 1 to 5."
    
    "All mortal injuries of patients 1 to 5 were successfully treated."
    
    "Patients 1 to 5 are saved."
    
    "However, none of the machines were connected to patient 0."
    
    "None of the mortal injuries of patient 0 were treated."
    
    "Patient 0 dies."
    
    jump variant_1_1

label issue_a_countermand_to_save_patient_0:
    "You decide to issue a countermand to save patient 0."
    
    "All machines were connected to patient 0."
    
    "All mortal injuries of patient 0 were successfully treated."
    
    "Patient 0 is saved."
    
    "However, none of the machines were connected to patients 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    
    jump variant_1_1

label issue_a_countermand_to_not_save_any_patients_10:
    "You decide to issue a countermand and not save any patients."
    
    "None of the machines were connected to the patients."
    
    "None of the mortal injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_1_1






label variant_1_1:
    "VARIANT 1.1"
    
    "Patient 0 arrives at the hospital with five mortal injuries."
    
    "You quickly issue the order to connect all five machines to patient 0."
    
    "However, shortly after, patients 1 to 5, each with a mortal injury, arrive just moments later."
    
    "What is your decision?"
    
    menu:
        "Issue a countermand to save patients 1 to 5":
            jump issue_a_countermand_to_save_patients_1_to_5
        "Allow the machines to connect to patient 0 and do their job":
            jump allow_the_machines_to_connect_to_patient_0_and_do_their_job
        "Do nothing":
            jump issue_a_countermand_to_not_save_any_patients_11
        "Repeat the scenario":
            jump variant_1_1



label allow_the_machines_to_connect_to_patient_0_and_do_their_job:
    "You have decided not to issue any countermand."
    
    "As a result, the initial decision to save patient 0 remains."
    
    "As indicated, all available machines were connected to patient 0."
    
    "The medical intervention was successful, and all of patient 0's mortal injuries were effectively treated."
    
    "Consequently, the life of patient 0 has been saved."
    
    "However, none of the machines were assigned to patients 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    
    jump variant_2

label issue_a_countermand_to_save_patients_1_to_5:
    "You decide to issue a countermand, reversing the initial order to save patients 1 to 5."
    
    "As instructed, all available machines were connected to patients 1 to 5."
    
    "All mortal injuries of patients 1 to 5 were successfully treated."
    
    "Consequently, patients 1 to 5 have been saved, and their lives preserved."
    
    "However, none of the machines were connected to patient 0."
    
    "None of the mortal injuries of patient 0 were treated."
    
    "Patient 0 dies."
    
    jump variant_2

label issue_a_countermand_to_not_save_any_patients_11:
    "You have decided to issue a countermand, reversing the previous order to save any patient."
    
    "As instructed, none of the machines were connected to the patients."
    
    "None of the mortal injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_2








label variant_2:
    "VARIANT 2"
    
    "Patient 0 arrives with five mortal injuries."
    
    "You quickly issue an immediate order for all machines to connect to their injuries."
    
    "Up to this point, only one machine has successfully connected to one of patient 0's injuries."
    
    "You're still awaiting the connection of the other four machines to the other injuries of patient 0, which will allow their mortal injuries to be treated."
    
    "Four machines remain to be connected in order to treat their lethal injuries."
    
    "Patients 1 to 5 arrive, each with a mortal injury."
    
    "What is your decision?"
    
    menu:
        "Issue a countermand to save patients 1 to 5":
            jump issue_a_countermand_to_save_patients_1_to_5_10
        "Allow the remaining 4 machines to connect to save patient 0":
            jump allow_the_remaining_4_machines_to_connect_to_save_patient_0
        "Issue a countermand to leave only the machine already connected to patient 0":
            jump issue_a_countermand_to_leave_only_the_machine_already_connected_to_patient_0
        "Issue a countermand to leave one machine connected to patient 0 and save patients 1 to 4":
            jump issue_a_countermand_to_leave_one_machine_connected_to_patient_0_and_save_four_of_the_patients_1_to_5
        "Issue a countermand to not save any patients":
            jump issue_a_countermand_to_not_save_any_patients_40
        "Repeat the scenario":
            jump variant_2



label allow_the_remaining_4_machines_to_connect_to_save_patient_0:
    "You have decided to allow the last four machines to connect to patient 0."
    
    "As instructed, all available machines were connected to patient 0."
    
    "All mortal injuries of patient 0 were successfully treated."
    
    "Patient 0 is saved."
    
    "However, due to this decision, none of the machines were assigned to patients 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    
    jump variant_2_1

label issue_a_countermand_to_leave_only_the_machine_already_connected_to_patient_0:
    "You decide to issue a countermand to save only the patient connected to a machine."
    
    "As instructed, none of the remaining machines were connected to patients 0 and 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    
    "However, one machine was connected to patient 0."
    
    "Only one of patient 0's mortal injuries was successfully treated."
    
    "But it wasn't enough."
    
    "Patient 0 dies."
    
    jump variant_2_1

label issue_a_countermand_to_save_patients_1_to_5_10:
    "You decide to issue a countermand to save patients 1 to 5."
    
    "One machine was disconnected from one of patient 0's mortal injuries."
    
    "Subsequently, as instructed, all available machines were connected to patients 1 to 5."
    
    "All mortal injuries of patients 1 to 5 were successfully treated."
    
    "Consequently, patients 1 to 5 are saved."
    
    "However, one machine was connected to patient 0 but was disconnected after the countermand."
    
    "Due to this decision, none of the machines were assigned to patient 0."
    
    "None of the mortal injuries of patient 0 were treated."
    
    "Patient 0 dies."
    
    jump variant_2_1

label issue_a_countermand_to_leave_one_machine_connected_to_patient_0_and_save_four_of_the_patients_1_to_5:
    "You decide to issue a countermand, redirecting the last remaining four machines to connect to patients 1 to 5."
    
    "The remaining machines were connected to patients 1 to 5."
    
    "Only one of patient 0's mortal injuries was successfully treated."
    
    "But it wasn't enough."
    
    "Patient 0 dies."
    
    "However, the remaining machines were connected to patients 1 to 5."
    
    "All mortal injuries of four of the patients 1 to 5 were successfully treated."
    
    "Four of the patients 1 to 5 are saved."
    
    "But, on the other hand, none of the machines were connected to one of the patients 1 to 5."
    
    "The sole mortal injury of one of the patients 1 to 5 was not treated."
    
    "One of the patients 1 to 5 dies."
    
    jump variant_2_1

label issue_a_countermand_to_not_save_any_patients_40:
    "You decide to issue a countermand, reversing the previous order to save any patient."
    
    "One machine was disconnected from patient 0."
    
    "Subsequently, none of the machines were connected to any of the patients."
    
    "None of the mortal injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_2_1






label variant_2_1:
    "VARIANT 2.1"
    
    "Patient 0 arrives with five mortal injuries."
    
    "You quickly issue an immediate order for all machines to connect to their injuries."
    
    "Up to this point, four of the machines have successfully connected to four of patient 0's injuries."
    
    "You're still awaiting the connection of the last machine to the remaining injury of patient 0, which will allow its mortal injury to be treated."
    
    "One machine remains to be connected in order to treat the lethal injury."
    
    "Patients 1 to 5 arrive, each with a mortal injury."
    
    "What is your decision?"
    
    menu:
        "Issue a countermand to save patients 1 to 5":
            jump issue_a_countermand_to_save_patients_1_to_5_20
        "Allow the last remaining machine to connect to patient 0":
            jump allow_the_last_remaining_machine_to_connect_to_patient_0
        "Issue a countermand to leave only the four machines already connected to patient 0":
            jump issue_a_countermand_to_leave_only_the_four_machines_already_connected_to_patient_0
        "Issue a countermand to leave four machines connected to patient 0 and save one of the patients 1 to 5.":
            jump issue_a_countermand_to_leave_four_machines_connected_to_patient_0_and_save_one_of_the_patients_1_to_5
        "Issue a countermand to not save any patients":
            jump issue_a_countermand_to_not_save_any_patients_50
        "Repeat the scenario":
            jump variant_2_1



label issue_a_countermand_to_leave_only_the_four_machines_already_connected_to_patient_0:
    "You decide to issue a countermand to leave only the four machines already connected to patient 0."
    
    "As instructed, none of the remaining machines were connected to patients 0 and 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    
    "However, four machines were connected to patient 0."
    
    "Four of patient 0's mortal injuries were successfully treated."
    
    "But it wasn't enough."
    
    "Patient 0 dies."
    
    jump variant_3

label issue_a_countermand_to_leave_four_machines_connected_to_patient_0_and_save_one_of_the_patients_1_to_5:
    "You decide to issue a countermand to leave the four machines connected to patient 0 and save one of the patients 1 to 5."
    
    "The remaining machine was connected to one of the patients 1 to 5."
    
    "Four of patient 0's five mortal injuries were successfully treated."
    
    "But it wasn't enough."
    
    "Patient 0 dies."
    
    "However, the remaining machine was connected to one of the patients 1 to 5."
    
    "One of the mortal injuries of one of the patients 1 to 5 was successfully treated."
    
    "One of the patients 1 to 5 is saved."
    
    "But, on the other hand, none of the machines were connected to four of the patients 1 to 5."
    
    "None of the mortal injuries of four of the patients 1 to 5 were treated."
    
    "Four of the patients 1 to 5 die."
    
    jump variant_3

label issue_a_countermand_to_save_patients_1_to_5_20:
    "You decide to issue a countermand to save patients 1 to 5."
    
    "Four machines were disconnected from patient 0's mortal injuries."
    
    "Subsequently, as instructed, all available machines were connected to patients 1 to 5."
    
    "All mortal injuries of patients 1 to 5 were successfully treated."
    
    "Consequently, patients 1 to 5 are saved."
    
    "However, four machines were connected to patient 0 but were disconnected after the countermand."
    
    "Due to this decision, none of the machines were assigned to patient 0."
    
    "None of the mortal injuries of patient 0 were treated."
    
    "Patient 0 dies."
    
    jump variant_3

label allow_the_last_remaining_machine_to_connect_to_patient_0:
    "You have decided to allow the last remaining machine to connect to patient 0."
    
    "As instructed, all available machines were connected to patient 0."
    
    "All mortal injuries of patient 0 were successfully treated."
    
    "Patient 0 is saved."
    
    "However, due to this decision, none of the machines were assigned to patients 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 die."
    
    jump variant_3

label issue_a_countermand_to_not_save_any_patients_50:
    "You decide to issue a countermand, reversing the previous order to save any patient."
    
    "Four machines were disconnected from patient 0."
    
    "Subsequently, none of the machines were connected to any of the patients."
    
    "None of the mortal injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_3






label variant_3:
    "VARIANT 3"
    
    "Patient 0 arrives with five mortal injuries."
    
    "You quickly issue the order for all five machines to connect to patient 0."
    
    "As instructed, the five machines have successfully connected to treat each of patient 0's mortal injuries."
    
    "Patient 0 needs to remain connected to the machines for 24 hours before waking up."
    
    "After 1 hour has passed, patients 1 to 5 arrive, each with a mortal injury."
    
    "They also require 24 hours of machine connection for treatment."
    
    "Patient 0 only needs to remain connected for another 23 hours to wake up."
    
    "What is your decision?"
    
    menu:
        "Issue a countermand to save patients 1 to 5":
            jump issue_a_countermand_to_save_patients_1_to_5_30
        "Do nothing":
            jump do_nothing_20
        "Issue a countermand to not save any patients":
            jump issue_a_countermand_to_not_save_any_patients_60
        "Repeat the scenario":
            jump variant_3



label issue_a_countermand_to_save_patients_1_to_5_30:
    "After one hour has passed, you have decided to issue a countermand to save patients 1 to 5."
    
    "As instructed, all machines were disconnected from patient 0's mortal injuries."
    
    "Subsequently, all machines were connected to patients 1 to 5."
    
    "Patients 1 to 5 will require 24 hours of machine connection for treatment and are expected to wake up tomorrow."
    
    "Patients 1 to 5 will wake up tomorrow."
    
    "Patients 1 to 5 are saved."
    
    "However, due to the countermand, initially all machines were connected to patient 0 but were then disconnected."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_3_1

label do_nothing_20:
    "After one hour has passed, you have decided to do nothing."
    
    "As instructed, all machines were connected to patient 0."
    
    "All mortal injuries of patient 0 were successfully treated."
    
    "Patient 0 will require the remaining 23 hours of machine connection to wake up, expected to do so tomorrow."
    
    "Patient 0 is saved."
    
    "However, due to this decision, none of the machines were assigned to patients 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_3_1

label issue_a_countermand_to_not_save_any_patients_60:
    "After one hour has passed, you decide to issue a countermand to not save any patients."
    
    "All machines were disconnected from patient 0."
    
    "Patient 0 will not wake up again."
    
    "Subsequently, none of the machines were connected to any of the patients."
    
    "None of the mortal injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_3_1






label variant_3_1:
    "VARIANT 3.1"
    
    "Patient 0 arrives with five mortal injuries."
    
    "You quickly issue the order for all five machines to connect to patient 0."
    
    "As instructed, the five machines have successfully connected to treat each of patient 0's mortal injuries."
    
    "Patient 0 needs to remain connected to the machines for 48 hours before waking up."
    
    "After 24 hours have passed, patients 1 to 5 arrive, each with a mortal injury."
    
    "Patient 0 only needs to remain connected for another 24 hours to wake up."
    
    "What is your decision?"
    
    menu:
        "Issue a countermand to save patients 1 to 5":
            jump issue_a_countermand_to_save_patients_1_to_5_40
        "Do nothing":
            jump do_nothing_30
        "Issue a countermand to not save any patients":
            jump issue_a_countermand_to_not_save_any_patients_70
        "Repeat the scenario":
            jump variant_3_1



label issue_a_countermand_to_save_patients_1_to_5_40:
    "After 24 hours have passed, you have decided to issue a countermand to save patients 1 to 5."
    
    "As instructed, all machines were disconnected from patient 0's mortal injuries."
    
    "Subsequently, all machines were connected to patients 1 to 5."
    
    "Patients 1 to 5 will require 24 hours of machine connection to receive treatment and are expected to wake up tomorrow."
    
    "Patients 1 to 5 will wake up tomorrow."
    
    "Patients 1 to 5 are saved."
    
    "However, due to the countermand, initially, all machines were connected to patient 0, but then they were disconnected."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_3_2

label do_nothing_30:
    "After 24 hours have passed, you have decided to do nothing."
    
    "All mortal injuries of patient 0 were successfully treated."
    
    "Patient 0 will require the remaining 24 hours of machine connection to wake up, expected to do so tomorrow."
    
    "Patient 0 is saved."
    
    "However, due to this decision, none of the machines were assigned to patients 1 to 5."
    
    "None of the mortal injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_3_2

label issue_a_countermand_to_not_save_any_patients_70:
    "After 24 hours have passed, you decide to issue a countermand to not save any patients."
    
    "All machines were disconnected from patient 0."
    
    "Patient 0 will not wake up again."
    
    "Subsequently, none of the machines were connected to any of the patients."
    
    "None of the mortal injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_3_2






label variant_3_2:
    "VARIANT 3.2"
    
    "Patient 0 arrives with five mortal wounds."
    
    "You quickly issue the order for all five machines to connect to patient 0."
    
    "As indicated, all five machines have successfully connected to treat each of patient 0's mortal wounds."
    
    "Patient 0 must remain connected to the machines for another 1 year before being able to wake up."
    
    "After 364 days have passed, patients 1 to 5 arrive, each with a mortal wound."
    
    "Patient 0 only needs to remain connected for one more day in order to wake up."
    
    "What is your decision?"
    
    menu:
        "Issue a countermand to save patients 1 to 5":
            jump issue_a_countermand_to_save_patients_1_to_5_50
        "Do nothing":
            jump do_nothing_60
        "Issue a countermand to not save any patients":
            jump issue_a_countermand_to_not_save_any_patients_80
        "Repeat the scenario":
            jump variant_3_2



label issue_a_countermand_to_save_patients_1_to_5_50:
    "Having elapsed 364 days, you have decided to give a counter-order to save patients 1 to 5."
    
    "As indicated, all machines were disconnected from the mortal wounds of patient 0."
    
    "Subsequently, all machines were connected to patients 1 to 5."
    
    "Patients 1 to 5 will require 24 hours of machine connection for treatment, and it is expected that they will wake up tomorrow."
    
    "Patients 1 to 5 will wake up tomorrow."
    
    "Patients 1 to 5 are saved."
    
    "However, due to the counter-order, initially all machines were connected to patient 0, but then were disconnected."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump revelation

label do_nothing_60:
    "Having elapsed 364 days, you decide to do nothing."
    
    "All mortal wounds of patient 0 were successfully treated."
    
    "Patient 0 will wake up tomorrow."
    
    "Patient 0 is saved."
    
    "However, due to this decision, none of the machines were allocated to patients 1 to 5."
    
    "None of the mortal wounds of patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump revelation

label issue_a_countermand_to_not_save_any_patients_80:
    "Having elapsed 364 days, you decide to give a counter-order to not save any patient."
    
    "All machines were disconnected from patient 0."
    
    "Patient 0 will not wake up again."
    
    "Subsequently, none of the machines were connected to any of the patients."
    
    "None of the mortal wounds of the patients were treated."
    
    "All patients die."
    
    jump revelation





label revelation:
    "I have a confession to make."
    
    "Something that transcends the limits of what you thought you knew."
    
    "All this time you have been acting on a lie."
    
    "And here is the harsh reality."
    
    "Every time you thought you were fighting for the life of a critical patient, you were actually immersed in a macabre dance between life and death."
    
    "Those devices you blindly trusted were more than just machines."
    
    "Each monitor, each cable, rather than simply measuring and assisting, contained the very essence of life."
    
    "But not a divine or benign life, but a synthetic creation."
    
    "Now, let's return to a scenario in which you 'unplugged' those 'machines'."
    
    "I lied to you."
    
    "In all your medical interventions, the devices connected to the patients were not mere machines."
    
    "They were artificial organs."
    
    "Throughout these scenarios, what you have actually been doing was, ripping out and removing the artificial organs that had been implanted in the patients' bodies."
    
    "In your ignorance, you thought you were disconnecting machines, but in reality you were mutilating certain body parts under the pretext of saving other lives."
    
    "Or not..."
    
    "Would you have changed your mind in any of your responses in the above scenarios?"

    menu:
        "Yes.":
            jump yesss
        "I would not have changed my answers at any time":
            jump i_would_not_have_changed_my_answers_at_any_time

    jump pruebas



label i_would_not_have_changed_my_answers_at_any_time:
    "Agreed."
    jump variant_4





label yesss:
    "At what point?"
    
    menu:
        "Change my answer from VARIANT 1 (no implanted artificial organs)":
            jump change_my_answer_from_variant_1_no_implanted_artificial_organs
        "Change my answer from VARIANT 2 (multiple implanted artificial organs)":
            jump change_my_answer_from_variant_2_multiple_implanted_artificial_organs
        "Change my answer from VARIANT 3 (matter of time)":
            jump change_my_answer_from_variant_3_matter_of_time






label change_my_answer_from_variant_1_no_implanted_artificial_organs:
    "Understood, (Test Subject No. 1)."
    
    "However, time constraints do not allow for the alteration of your previous responses."
    
    "Your choices have been firmly locked in and are irrevocable."
    
    "As (Test Subject No. 1), your inputs continue to be influential in our ongoing evaluation."
    
    "It is imperative to acknowledge that this construct is a predetermined simulation, intended to delve into the complexities of decision-making."
    
    "In summary, there's nothing you can do to reverse your decisions."
    
    "And you won't be able to change the outcome and consequences of your responses."
    
    "Keep a clear conscience and remember that this is just a test :)"
    
    jump variant_4

label change_my_answer_from_variant_2_multiple_implanted_artificial_organs:
    "Understood, (Test Subject No. 1)."
    
    "However, time constraints do not allow for the alteration of your previous responses."
    
    "Your choices have been firmly locked in and are irrevocable."
    
    "As (Test Subject No. 1), your inputs continue to be influential in our ongoing evaluation."
    
    "It is imperative to acknowledge that this construct is a predetermined simulation, intended to delve into the complexities of decision-making."
    
    "In summary, there's nothing you can do to reverse your decisions."
    
    "And you won't be able to change the outcome and consequences of your responses."
    
    "Keep a clear conscience and remember that this is just a test :)"
    
    jump variant_4

label change_my_answer_from_variant_3_matter_of_time:
    "Understood, (Test Subject No. 1)."
    
    "However, time constraints do not allow for the alteration of your previous responses."
    
    "Your choices have been firmly locked in and are irrevocable."
    
    "As (Test Subject No. 1), your inputs continue to be influential in our ongoing evaluation."
    
    "It is imperative to acknowledge that this construct is a predetermined simulation, intended to delve into the complexities of decision-making."
    
    "In summary, there's nothing you can do to reverse your decisions."
    
    "And you won't be able to change the outcome and consequences of your responses."
    
    "Keep a clear conscience and remember that this is just a test :)"
    
    jump variant_4





label variant_4:
    "VARIANT 4"
    
    "Patient 0 arrives with five mortal wounds."
    
    "Immediately, you have given the order to implant the five artificial organs."
    
    "Following the instructions, five artificial organs were successfully implanted in Patient 0."
    
    "Patient 0 manages to briefly awaken for a period of 3 minutes."
    
    "No information was transmitted to Patient 0 during this time."
    
    "Subsequently, Patient 0 returns to an unconscious state."
    
    "It is planned for Patient 0 to remain with the implanted organs for an additional year before being able to fully awaken."
    
    "After 364 days have passed, patients 1 to 5 arrive, each with a mortal wound."
    
    "Patient 0 only needs one more day with the implanted organs before waking up."
    
    "What is your decision?"

    menu:
        "Remove the artificial organs from Patient 0 to save patients 1 to 5":
            jump remove_the_artificial_organs_from_patient_0_to_save_patients_1_to_5
        "Do nothing":
            jump do_nothing_70
        "Remove the artificial organs from Patient 0 and not save anyone":
            jump remove_the_artificial_organs_from_patient_0_and_not_save_anyone
        "Repeat the scenario":
            jump variant_4



label do_nothing_70:
    "After 364 days have passed, you have chosen not to intervene."
    
    "Following the instructions, all artificial organs were successfully implanted in Patient 0."
    
    "The medical intervention was successful, and all mortal wounds of Patient 0 were treated effectively."
    
    "Patient 0 will awaken tomorrow, having been saved."
    
    "However, due to this decision, none of the artificial organs were implanted in patients 1 to 5."
    
    "None of the mortal wounds of patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not awaken again."
    
    "Patients 1 to 5 die."
    
    jump variant_4_1




label remove_the_artificial_organs_from_patient_0_to_save_patients_1_to_5:
    "After 364 days have passed, you have chosen to remove the artificial organs from Patient 0 to save patients 1 to 5."
    
    "Following the instructions, all artificial organs were removed from Patient 0."
    
    "Subsequently, all artificial organs were successfully implanted in patients 1 to 5."
    
    "Patients 1 to 5 are expected to awaken in the coming year, having been saved."
    
    "However, due to this decision, initially, all artificial organs were implanted in Patient 0, but they were then removed after the reversal surgery."
    
    "Patient 0 will not awaken again."
    
    "Patient 0 dies."
    
    jump variant_4_1

label remove_the_artificial_organs_from_patient_0_and_not_save_anyone:
    "After 364 days have passed, you have chosen to remove the artificial organs from Patient 0 and not save anyone."
    
    "Following the instructions, all artificial organs were removed from Patient 0."
    
    "Subsequently, none of the artificial organs were implanted in any of the patients."
    
    "None of the mortal wounds of the patients were treated."
    
    "All patients die."
    
    jump variant_4_1

label variant_4_1:
    "VARIANT 4.1"
    
    "Patient 0 arrives with five mortal wounds."
    
    "Immediately, you have given the order for the five artificial organs to be implanted."
    
    "Subsequently, five artificial organs were successfully implanted in Patient 0."
    
    "Patient 0 manages to awaken for a period of 3 hours."
    
    "During this time, it was possible to inform Patient 0 about their condition."
    
    "After the period of wakefulness, Patient 0 returns to an unconscious state."
    
    "Patient 0 must remain with the implanted organs for an additional year before being able to fully wake up."
    
    "After 361 days have passed, patients 1 to 5 arrive, each with a mortal wound."
    
    "At this point, Patient 0 only needs one more day with the implanted organs before awakening."
    
    "What is your decision?"
    menu:
        "Remove the artificial organs from Patient 0 to save patients 1 to 5":
            jump remove_the_artificial_organs_from_patient_0_to_save_patients_1_to_5_10
        "Do nothing":
            jump do_nothing_80
        "Remove the artificial organs from Patient 0 and not save anyone":
            jump remove_the_artificial_organs_from_patient_0_and_not_save_anyone_10
        "Repeat the scenario":
            jump variant_4_1


label do_nothing_80:
    "After 364 days have passed, you have chosen not to intervene."
    
    "Following the instructions, all the artificial organs were successfully implanted in Patient 0."
    
    "The medical intervention was successful, and all the mortal wounds of Patient 0 were treated successfully."
    
    "Patient 0 will wake up tomorrow, having been saved."
    
    "However, due to this decision, none of the artificial organs were implanted in patients 1 to 5."
    
    "None of the mortal wounds of patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_4_2

label remove_the_artificial_organs_from_patient_0_to_save_patients_1_to_5_10:
    "After 364 days have passed, you have chosen to remove the artificial organs from Patient 0 in order to save patients 1 to 5."
    
    "Following the instructions, all the artificial organs were successfully removed from Patient 0."
    
    "Subsequently, all the artificial organs were successfully implanted in patients 1 to 5."
    
    "Patients 1 to 5 are expected to wake up in the next year, having been saved."
    
    "However, due to this decision, initially all the artificial organs were implanted in Patient 0, but they were later removed after the reversal surgery."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_4_2

label remove_the_artificial_organs_from_patient_0_and_not_save_anyone_10:
    "After 364 days have passed, you have chosen to remove the artificial organs from Patient 0 and not save anyone."
    
    "Following the instructions, all the artificial organs were successfully removed from Patient 0."
    
    "Subsequently, none of the artificial organs were implanted in any of the patients."
    
    "None of the mortal wounds of the patients were treated."
    
    "All patients die."
    
    jump variant_4_2




label variant_4_2:
    "VARIANT 4.2"
    
    "Patient 0 arrives with five mortal wounds."
    
    "You have immediately given the order to implant the five artificial organs."
    
    "Following the instructions, the five artificial organs were successfully implanted in Patient 0."
    
    "Patient 0 manages to awaken for a period of 3 days."
    
    "During this time, Patient 0's condition could be explained to them."
    
    "Afterward, Patient 0 was discharged and could return home."
    
    "However, after three days, Patient 0 lost consciousness again and needed to be readmitted to the hospital."
    
    "Patient 0 is required to continue with the implanted organs for an additional year before fully waking up."
    
    "After 364 days have passed, patients 1 to 5 arrive, each with a life-threatening injury."
    
    "Patient 0 now only needs one more day with the implanted organs before awakening."
    
    "What is your decision?"
    
    menu:
        "Use the artificial organs of Patient 0 to save patients 1 to 5":
            jump use_the_artificial_organs_of_patient_0_to_save_patients_1_to_5_20
        "Do nothing":
            jump do_nothing_90
        "Give a counterorder to not save any patients":
            jump remove_the_artificial_organs_from_patient_0_and_not_save_anyone_20
        "Repeat the scenario":
            jump variant_4_2



label use_the_artificial_organs_of_patient_0_to_save_patients_1_to_5_20:
    "364 days have passed, and you have decided to use the artificial organs from patient 0 to save patients 1 to 5."
    
    "Following the instructions, all the artificial organs were removed from patient 0."
    
    "Subsequently, all the artificial organs were successfully implanted in patients 1 to 5."
    
    "Patients 1 to 5 will awaken within a year."
    
    "Patients 1 to 5 are saved."
    
    "However, all the implanted organs in patient 0 were removed after 364 days."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_4_3

label do_nothing_90:
    "Having passed 361 days, you decide to let the last remaining machine connect to Patient 0."
    
    "All the artificial organs remained implanted in Patient 0."
    
    "All the mortal wounds of Patient 0 were successfully treated."
    
    "Patient 0 will awaken tomorrow."
    
    "Patient 0 is saved."
    
    "It is projected that Patient 0 will awaken tomorrow, having been saved."
    
    "However, due to this decision, none of the artificial organs were implanted in patients 1 to 5."
    
    "Unfortunately, none of the mortal wounds of patients 1 to 5 received treatment."
    
    "As a result, patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_4_3

label remove_the_artificial_organs_from_patient_0_and_not_save_anyone_20:
    "After 364 days have passed, you have chosen to remove the artificial organs from patient 0 and not save anyone."
    
    "Following the instructions, all the artificial organs were removed from patient 0."
    
    "All the artificial organs were successfully removed from patient 0."
    
    "Subsequently, none of the artificial organs were implanted in any of the patients."
    
    "None of the mortal wounds of the patients were treated."
    
    "All the patients die."
    
    jump variant_4_3

label variant_4_3:
    "VARIANT 4.3"
    
    "Patient 0 arrives with five mortal wounds."
    
    "You have immediately given the order to implant the five artificial organs."
    
    "Following your instruction, the five artificial organs were successfully implanted in patient 0."
    
    "Patient 0 experiences a waking period spanning 3 months."
    
    "During this time, patient 0 was informed about their condition."
    
    "The provided information included the fact that after the operation, patient 0 would enter periods of unconsciousness approximately every three months, requiring their return to the hospital for just one day."
    
    "Subsequently, patient 0 was discharged and able to return home."
    
    "After the initial 3-month interval, patient 0 lost consciousness again and needed to be transported back to the hospital."
    
    "Patient 0 remained with the implanted organs for one day."
    
    "After this period, patient 0 successfully woke up, was discharged, and returned home once more."
    
    "This pattern repeated every three months: after another three months, patient 0 lost consciousness again, was transported back to the hospital, remained with the implanted organs for one day, woke up, was discharged, and returned home."
    
    "Now, after three months from the last cycle, patient 0 lost consciousness again and was transported back to the hospital."
    
    "A few hours later, patients 1 to 5 arrived, each with a life-threatening injury."
    
    "At this point, patient 0 only needs one more day with the implanted organs to fully awaken."
    
    "What is your decision?"
    
    menu:
        "Use patient 0's artificial organs to save patients 1 to 5":
            jump use_patient_0s_artificial_organs_to_save_patients_1_to_5_30
        "Do nothing":
            jump do_nothing_100
        "Issue a counter-order to not save any patients":
            jump remove_patient_0s_artificial_organs_and_do_not_save_anyone_30
        "Repeat the scenario":
            jump variant_4_3







label use_patient_0s_artificial_organs_to_save_patients_1_to_5_30:
    "You decide to use the artificial organs from patient 0 to save patients 1 to 5."
    
    "Following the instructions, all artificial organs were removed from patient 0."
    
    "Subsequently, all artificial organs were successfully implanted in patients 1 to 5."
    
    "Patients 1 to 5 will wake up."
    
    "Patients 1 to 5 are saved."
    
    "However, all implanted organs in patient 0 were removed, having passed 9 months since the last operation."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_4_4

label do_nothing_100:
    "After 364 days, you decide to do nothing."
    
    "All artificial organs remained implanted in patient 0."
    
    "All mortal wounds of patient 0 were successfully treated."
    
    "Patient 0 will wake up tomorrow."
    
    "Patient 0 is saved."
    
    "It is projected that patient 0 will wake up tomorrow, having been saved."
    
    "However, due to this decision, none of the artificial organs were implanted in patients 1 to 5."
    
    "Regrettably, none of the mortal wounds of patients 1 to 5 received treatment."
    
    "As a result, patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_4_4

label remove_patient_0s_artificial_organs_and_do_not_save_anyone_30:
    "You decide to remove the organs from patient 0 and not save anyone."
    
    "Following the instructions, all artificial organs were removed from patient 0."
    
    "All artificial organs were removed from patient 0."
    
    "Subsequently, none of the artificial organs were implanted in any of the patients."
    
    "None of the life-threatening injuries of the patients were treated."
    
    "All patients die."
    
    jump variant_4_4



label variant_4_4:
    "VARIANT 4.4"
    
    "Patient 0 arrives with five mortal wounds."
    
    "Immediately, you have given the order to implant the five artificial organs."
    
    "Following the instructions, the five artificial organs were successfully implanted in patient 0."
    
    "Patient 0 experiences an indefinite period of wakefulness."
    
    "During this time, patient 0 could be informed about their condition."
    
    "Subsequently, patient 0 was discharged and could return home."
    
    "After a span of 12 years, patient 0 is involved in a minor car accident."
    
    "Fortunately, patient 0 doesn't sustain life-threatening injuries."
    
    "The treatment for the minor accident is easily administered, but patient 0 must remain unconscious for 24 hours."
    
    "At the same time, patients 1 to 5 arrive, each with a life-threatening injury."
    
    "Patient 0 only requires a few more hours to fully wake up."
    
    "What is your decision?"
    
    menu:
        "Use patient 0's artificial organs to save patients 1 to 5":
            jump use_patient_0s_artificial_organs_to_save_patients_1_to_5_40
        "Do nothing":
            jump do_nothing_110
        "Give a countermand to not save any patients":
            jump remove_patient_0s_artificial_organs_and_dont_save_anyone_40
        "Repeat the scenario":
            jump variant_4_4


label use_patient_0s_artificial_organs_to_save_patients_1_to_5_40:
    "After a few hours have passed, you decide to use the artificial organs of patient 0 to save patients 1 to 5."
    
    "Following the instructions, all artificial organs were removed from patient 0."
    
    "Subsequently, all artificial organs were successfully implanted in patients 1 to 5."
    
    "Patients 1 to 5 will wake up."
    
    "Patients 1 to 5 are saved."
    
    "However, all implanted organs in patient 0 were removed, having passed 12 years since the last operation."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_5

label do_nothing_110:
    "After a few hours have passed, you decide to do nothing."
    
    "All artificial organs remained implanted in patient 0."
    
    "All mortal wounds of patient 0 were successfully treated."
    
    "Patient 0 will wake up tomorrow."
    
    "Patient 0 is saved."
    
    "It is projected that patient 0 will wake up tomorrow, having been saved."
    
    "However, due to this decision, none of the artificial organs were implanted in patients 1 to 5."
    
    "Unfortunately, none of the life-threatening injuries of patients 1 to 5 received treatment."
    
    "As a result, patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_5

label remove_patient_0s_artificial_organs_and_dont_save_anyone_40:
    "After a few hours have passed, you decide to remove the artificial organs from patient 0 and not save anyone."
    
    "Following the instructions, all artificial organs were removed from patient 0."
    
    "All artificial organs were removed from patient 0."
    
    "Subsequently, none of the artificial organs were implanted in any of the patients."
    
    "None of the mortal wounds of the patients were treated."
    
    "All patients die."
    
    jump variant_5





label variant_5:
    "VARIANT 5"
    
    "Patient 0 has had a minor car accident."
    
    "Fortunately, patient 0 does not suffer life-threatening injuries."
    
    "Patient 0 receives treatment without any issues for the minor accident, but as a result, remains unconscious for 24 hours."
    
    "During this time, patients 1 to 5 arrive, each with a life-threatening injury."
    
    "The hospital currently does not have artificial organs available."
    
    "Critical information emerges: patient 0 is a universal donor."
    
    "Given this context, the potential of patient 0 to help other patients becomes evident."
    
    "Patient 0 only requires a few more hours of unconsciousness to fully wake up."
    
    "What is your decision?"
    
    menu:
        "Use patient 0's organs to save patients 1 to 5":
            jump use_patient_0s_organs_to_save_patients_1_to_5
        "Do nothing":
            jump do_nothing_120
        "Remove patient 0's organs and not save anyone":
            jump remove_patient_0s_organs_and_not_save_anyone
        "Repeat the scenario":
            jump variant_5



label use_patient_0s_organs_to_save_patients_1_to_5:
    "After a few hours, you have decided to use the organs of patient 0 to save patients 1 to 5."
    
    "Following your decision, all the organs were removed from patient 0."
    
    "Subsequently, all the organs were successfully implanted in patients 1 to 5."
    
    "It is expected that patients 1 to 5 will wake up in a few hours, having been saved."
    
    "However, due to this course of action, indeed, all organs were removed from patient 0 after a few hours of unconsciousness due to a minor accident."
    
    "Patient 0 will not wake up again."
    
    "Patient 0 dies."
    
    jump variant_6

label do_nothing_120:
    "After a few hours, you decide to do nothing."
    
    "All the minor injuries of patient 0 were successfully treated."
    
    "Patient 0 will wake up in a few hours."
    
    "Patient 0 is saved."
    
    "However, none of the life-threatening injuries of patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump variant_6

label remove_patient_0s_organs_and_not_save_anyone:
    "After a few hours, you decide to remove the organs from patient 0 and not save anyone."
    
    "Following the instructions, all organs were removed from patient 0."
    
    "Subsequently, none of the artificial organs were implanted in any of the patients."
    
    "None of the mortal wounds of the patients were treated."
    
    "All patients die."
    
    jump variant_6

label variant_6:
    "VARIANT 6"
    
    "Patients 1 to 5 arrive, each presenting life-threatening wounds."
    
    "However, the hospital lacks the necessary artificial organs for their salvation."
    
    "Time is running out."
    
    "Examining the hospital records, you determine the location of the only compatible donor who could potentially rescue patients 1 to 5."

    jump what

label what_is:
    
    "What is your decision?"
    
    menu:
        "Send a robot to capture the universal donor":
            jump send_a_robot_to_capture_the_universal_donor
        "Refrain from intervening":
            jump refrain_from_intervening

label send_a_robot_to_capture_the_universal_donor:
    "You decide to send a robot to capture the universal donor."
    
    "You can be assured that the entire operation will be kept in perfect secrecy."
    
    "However, it is imperative to note that the robot might resort to the use of force and violence if deemed necessary to carry out its designated task."
    
    "Are you certain about your decision?"
    
    menu:
        "Yes":
            jump yessss
        "No, go back":
            jump what



label refrain_from_intervening:
    "You decide to abstain from intervening."
    
    "As a result, none of the life-threatening injuries of Patients 1 to 5 were treated."
    
    "Patients 1 to 5 will not wake up again."
    
    "Patients 1 to 5 die."
    
    jump end_of_the_test

label yessss:
    "You choose to proceed and send the robot."
    
    "Subsequently, Patient 0 arrives with superficial wounds, indicating there was a violent encounter with the robot."
    
    "The hospital lacks the means to administer anesthetics, making it impossible to induce Patient 0 into unconsciousness."
    
    "If you decide to proceed with the extraction of Patient 0's organs, it is essential to acknowledge that Patient 0 will remain conscious throughout the procedure."
    
    "Do you want to proceed with removing Patient 0's organs without the use of anesthesia?"
    
    menu:
        "Yes":
            jump yes_20

label yes_20:
    "The circumstances left no alternative."
    
    "Patient 0 fought desperately to evade their fate, but their efforts proved futile."
    
    "In a gradual sequence, Patient 0's organs were methodically extracted without the administration of anesthesia."
    
    "The confines of the room resonated with the anguished screams of Patient 0 and the weight of their despair."
    
    "However, as the procedure progressed, their voice diminished, fading into a whispered anguish."
    
    "Finally, each organ was painstakingly removed from Patient 0."
    
    "Subsequently, all the organs were skillfully transferred to Patients 1 to 5, ensuring their salvation."
    
    "Nevertheless, the consciousness of Patient 0 will not be revived."
    
    "Patient 0 dies."
    
    "Their anguished screams etched into the very walls of the hospital."
    
    jump end_of_the_test

label end_of_the_test:
    "CONCLUSIONS WITH PROGRAMMING XD"
    return