label lamp_visit:
    scene black
    hide screen pnc
    hide screen lamp_get
    show bg black
    with dissolve
    $ agrabah_lamp.act = Jump('inside_lamp')
    abd "Woaaaaah. What?"
    jaf "Welcome to my humble lamp, Abdul."
    show jaf normal
    with dissolve
    abd "Jafar? Did you bring me inside your lamp?"
    jaf "Yes."
    abd "I knew it!"
    jaf "You knew what?"
    abd "Did you bring me here to trap me inside your lamp?"
    show jaf probing
    jaf "Now why would I want to do that?"
    abd "To gain your freedom?"
    show jaf normal
    jaf "If it was that simple, or even if I wanted to, I would have done it already."
    jaf "It wouldn't be that hard to trick you either, you're pretty gullible."
    abd "I...{w=.5} you're right. Sorry for doubting you."
    abd "So why did you bring me here?"
    jaf "Abdul my friend, we are going to work together."
    jaf "I want to show you my home."
    abd "This darkness is your home?"
    "..."
    abd "It's a lot bigger on the inside."
    "..."
    abd "You have quite the leg room in here too."
    "..."
    abd "Doesn't smell like farts either."
    show jaf annoyed
    jaf "Stop with your wisecracks, we have work to do."
    show jaf normal
    jaf "You need to learn how to navigate this place when I'm not around."
    abd "First question, how do I get in and out on my own?"
    show jaf thinking
    jaf "Excellent question, to get in just rub the lamp."
    abd "And rub it again to go out?"
    jaf "Nope, you can't bring the lamp inside itself."
    abd "Hey, it's gone..."
    jaf "Didn't you hear what I said?"
    abd "Oh!"
    jaf "I'll come up with something. We can worry about that later."
    show jaf normal

    menu:
        jaf "But first, let me show you around."
        "I can find my way around, let's get to something more exciting.":
            abd "I can find my way around, let's get to something more exciting."
            show jaf thinking
            jaf "Eager to draw your sword, aren't you?"
            show jaf normal
            jaf "All right, have a look around by yourself then meet me in my library."
            hide jaf with dissolve
            jump ch3_1
        "Yes, please. This place looks like the desert at night.":
            abd "Yes, please. This place looks like the desert at night."
            jaf "Are you afraid of the dark?"
            abd "No. I'm afraid of what might be hiding in the darkness. How do I know I won't fall in a hole?"
            show jaf thinking
            show jaf normal
            jaf "Just don't wander far away from the bright spots."
            jaf "It's not that easy to find your way back in the darkness."
            abd "Okay..."

label lamp_visit_save:
    # save
    # show bg sav
    # show screen save(_layer = "bg")
    # scene
    show jaf normal
    abd "Empty jars?"
    abd "Are they an obsession of yours?"
    abd "Where are they hanging from? I can't see the ceiling."
    jaf "There's no ceiling here, no walls and that thing you're walking on is not a floor."
    abd "Wait, what!?"
    show jaf angry
    jaf "Focus, Abdul!"
    show jaf normal
    jaf "Here, take this."
    $ msg.msg("Received a bag?")
    "..."
    $ msg.msg("...of sand?")
    abd "A bag of sand?"
    jaf "These are the Sands of Time."
    jaf "Extremely valuable!"
    jaf "Grab a handful, put it in one of these jars and the 'you' from that moment will remain in it."
    $ msg.msg("Right, Received sands of time, a dozen handfuls.")
    jaf "That 'you' can be recovered if something...{w=.5} unfortunate happens to you."
    jaf "Well, {w=.2}You need to bring in your own jars."
    jaf "The things I conjure in here will disappear a while after I take my mind of them.."
    # Remove jars
    abd "You can resurrect me?"
    show jaf thinking
    jaf "Not exactly."
    show jaf normal
    jaf "You would have to wish for resurrection, and it wouldn't be a pretty sight. Plus, it's difficult to wish When you're dead."
    jaf "This is my way to manage around that problem."
    jaf "Just don't overdo it, you don't have much sand and it's not easy to obtain more of it."
    # add a jar
    jaf "In fact... {w=.4}Let's preserve you in this moment."
    abd "Are you sure it's... {w=.2}{nw}"
    show jaf magic
    # $ save_list.add()
    "...{nw}"
    # $ renpy.take_screenshot()
    # $ renpy.save("1-1", extra_info='')
    abd "... safe?"
    show jaf normal
    jaf "I'm sure we'll find out soon."
    abd "Does that mean I'm going to die soon?"
    jaf "Let's move on."
    $ renpy.hide_screen("save", layer = "bg")

label lamp_visit_settings:
    # set
    show bg sett behind jaf
    abd "What's this one?"
    show jaf thinking
    jaf "To be honest, I'm not entirely sure. These devices seem to have some minor effects on the outside world."
    show jaf normal
    jaf "I don't have any use for them."
    jaf "You'll have to try them by yourself, I'm afraid."

default books_for_jafar = quest(
    _("Books for jafar"),
    [_("Jafar wants books, lots of them.")],
    )

label lamp_visit_library:
    # lib
    show bg lib
    # this part can use a revamp
    abd "You have a library here?"
    jaf "Of course."
    abd "Let's see..."
    abd "Jafar's Introductory Macroeconomics for Sultans."
    abd "Jafar's Guide to Appropriate and Proper Palace Etiquette."
    abd "Jafar's Illustrated Manual of...{w=.5} Tapdance?"
    show jaf disappointed
    jaf "Not one of my best, I have to admit."
    show jaf normal
    abd "Are {b}all{/b} of these books are written by you, Jafar?"
    jaf "Of course, I can't collect any other books, being stuck in this lamp."
    jaf "And I need to transfer my knowledge to the next generation somehow."
    show jaf thinking
    jaf "Speaking of, You should collect and bring me as many books as you can."
    abd "Books are expensive Jafar."
    jaf "They're worth it. Buy when you can afford them."
    abd "But..."
    jaf "Do as I say."
    abd "Alright."
    $ qlog.got(books_for_jafar)

    jaf "You should borrow a few of them at some point."
    show jaf normal
    jaf "In fact...{w=.2} You'll need to read them all, these will help you with your quest."
    abd "Even...{w=.4}tap{w=.4}dan...{w=.2}{nw}?"
    show jaf annoyed
    "...{nw}"
    show jaf magic
    abd "Whah..."
    jaf "There... It never existed."
    show jaf annoyed
    jaf "Happy now?"
    abd "Sorry, sorry, it was just a joke."
    abd "Did you have to burn it right in my hand?"
    jaf "Now you know better to not annoy a powerful Genie."
    show jaf normal
    jaf "Now where were we? Ah yes, speaking of quests."
    jaf "I'll keep track of your progress...{nw}"

default my_to_do_list = quest(
    _("A to-do list"),
    [_("Jafar wants to write you a to-do list and he needs a blank skin scroll.")],
    )

label lamp_visit_quests:
    # quest
    show bg quest
    jaf "Here."
    abd "A mirror?"
    jaf "Through this mirror, I can watch you outside of the lamp. I can also guide you and give you information."
    abd "All the time?"
    show jaf thinking
    jaf "You're right, I have much better things to do than sitting here controlling your every move."
    "..."
    show jaf normal
    jaf "Get me a skin scroll, I'll make a to do list for you.{w=.4} Make it your first priority."
    $ qlog.got(my_to_do_list)
    abd "Um...{w=.2} my concern was something else."
    show jaf probing
    jaf "What's the matter?"
    abd "What about my privacy?"
    show jaf normal
    jaf "Get over yourself, I don't have time to watch you all the time. I have books to write."
    jaf "And I don't have any interest in watching you jerk off."
    jaf "I have a harem for myself anyway."
    abd "A harem? Let me see it!"

label lamp_visit_harem:
    # fight
    show bg fight
    abd "Not this."
    # gallery
    show bg gall
    abd "Nor this."
    # harem
    show bg harem
    abd "Woah, you have slave girls in here? You also have three of them too?"
    jaf "No, they aren't slaves, they're free people."
    abd "Wives?"
    jaf "No, they're just... here. For some reason."
    jaf "And they seem to be happy just keeping me company."
    abd "Ummm..."
    abd "Can I? Ummm... I mean... May I?"
    show jaf probing
    jaf "Fuck them?"
    abd "No no, speak to them."
    show jaf normal
    jaf "I'm not the one you should ask."
    jaf "Who am I to say what they can and can't do?"
    jaf "You might want to take advantage of the running water and at least take a shower first."
    jaf "We're trying to keep it clean in here."
    abd "A shower...? Hey, are those?"
    show jaf disappointed
    jaf "Yes, those statues look a lot like me peeing.{w=.5} It seemed like a good idea at that time."
    jaf "The girls seem to like them, and I wasn't expecting any guests in here anytime soon either."
    show jaf normal
    
    menu:
        jaf "Now, let's go back and visit the places we skipped."
        "Sure, I can come back later.":
            abd "Sure, I can come back later."
            jump lamp_visit_fight

        "I think I'm going to take that shower you just suggested to me.":
            abd "I think I'm going to take that shower you just suggested to me."
            show jaf disappointed
            jaf "Of course, there are women around, so you aren't capable of thinking straight."
            jaf "Come to me when you've relieved yourself."
            show jaf normal
            jaf "I'll think of a plan in the mean time."
            jaf "And we're going to have to work on your self-discipline."
            hide jaf with dissolve
            jump harem

label lamp_visit_fight:
    # fight
    scene black
    show bg fight
    show jaf normal
    jaf "This is my throne. You'll be fighting the creatures I conjure in here."
    jaf "To increase your fighting skill, and maybe for my amusement."
    jaf "You can come here and start fighting any time."
    
    menu:
        jaf "But... do you want to give it a try right now?"
        "Yes.":
            abd "Yes."
            jaf "Alright, here we go."

            hide jaf
            window hide
            "The fight system is being reworked to fit the first person view."
            $ training_dummy.reset()
            call screen battle([training_dummy])

            with dissolve
            show jaf normal
            with dissolve
            jaf "Not bad."
            jaf "At least you didn't hurt yourself vailing on a dummy."
            jaf "Now, do you want to try something that fights back?"
            menu:
                "Of course!":
                    abd "Of course!"
                    jaf "Alright, let me summon something."

                "I'll pass.":
                    abd "I'll pass."
                    jaf "That might be wise rather than coward."

            jaf "Or, if you did, the sands of time have worked."
            jaf "It would be hard to decern."
            jaf "Anyways..."
            jaf "I'll have to prepare something."
            jaf "Explore the lamp as you wish, meet me at my library when you're done."
            hide jaf with dissolve
            jump ch3_1
        "Maybe later.":
            show jaf normal
            abd "Maybe later."
            jaf "Alright. Next is the Hall of Memories."
            # hall of memories
            jaf "You can revisit your most proudest moments in here."
            jaf "And that's it. I have some thinking to do. Feel free to roam around while I'm busy."
            jaf "Meet me at my library when you're done."
            hide jaf with dissolve
            jump ch3_1

label ch3_1:
    scene black
    show screen lamp_visit_menu
    pause
    jump ch3_1

screen lamp_visit_menu:
    style_prefix "nav"
    modal True
    button:
        padding 0,0 anchor .0,.0 pos (916, 476)
        add "bg/lamp/fight.webp"
        action Hide("lamp_visit_menu"), Jump("ch3_fight")
    button:
        padding 0,0 anchor .0,.0 pos (724, 47)
        add "bg/lamp/harem.webp"
        action Hide("lamp_visit_menu"), Jump("harem")
    button:
        padding 0,0 anchor .0,.0 pos (412, 225)
        add "bg/lamp/library.webp"
        action Hide("lamp_visit_menu"), Jump("lamp_visit_back_to_jafar")
    button:
        padding 0,0 anchor .0,.0 pos (1272, 828)
        add "bg/lamp/quest.webp"
        action Hide("lamp_visit_menu"), Jump("ch3_mirror")
    button:
        padding 0,0 anchor .0,.0 pos (103, 604)
        add "bg/lamp/replay.webp"
        action Hide("lamp_visit_menu"), Jump("ch3_replay")
    button:
        padding 0,0 anchor .0,.0 pos (1024, 234)
        add "bg/lamp/save.webp"
        action Hide("lamp_visit_menu"), Jump("ch3_sav")
    button:
        padding 0,0 anchor .0,.0 pos (600, 758)
        add "bg/lamp/settings.webp"
        action Hide("lamp_visit_menu"), Jump("ch3_set")
    button:
        padding 0,0 anchor .0,.0 pos (1423, 533)
        add "bg/lamp/mm.webp"
        action Hide("lamp_visit_menu"), Jump("ch3_mm")

label ch3_mm:
    # scene bg sav
    "Nothing to do here."
    jump ch3_1
label ch3_sav:
    # scene bg sav
    "Nothing to do here."
    jump ch3_1
label ch3_set:
    scene bg sett
    "Nothing to do here."
    jump ch3_1
label ch3_replay:
    scene bg sett
    "Nothing to do here."
    jump ch3_1
label ch3_mirror:
    show screen quests
    pause
    jump ch3_1


default training_dummy = fighter("Training dummy", 4, "Dummy")
image training dummy idle:
    "training dummy idle_1"
    .1
    "training dummy idle_2"
    .1
    "training dummy idle_3"
    .1
    repeat

default all_demons = [
    "Scorpion dancer",
    "Skeletabber",
    "Dummy teen",
    "Tornado rider",
    "Stiffy",
    ]
image scorpion dancer idle:
    "scorpion dancer idle_1"
    .1
    "scorpion dancer idle_2"
    .1
    "scorpion dancer idle_3"
    .1
    repeat
image skeletabber idle:
    "skeletabber idle_1"
    .1
    "skeletabber idle_2"
    .1
    "skeletabber idle_3"
    .1
    repeat
image dummy teen idle:
    "dummy teen idle_1"
    .1
    "dummy teen idle_2"
    .1
    "dummy teen idle_3"
    .1
    repeat
image tornado rider idle:
    "tornado rider idle_1"
    .1
    "tornado rider idle_2"
    .1
    "tornado rider idle_3"
    .1
    repeat
image stiffy idle:
    "stiffy idle_1"
    .1
    "stiffy idle_2"
    .1
    "stiffy idle_3"
    .1
    repeat



label ch3_fight(j=False):
    window hide
    menu:
        "Fight a dummy.":
            $ training_dummy.reset()
            call screen battle([training_dummy])
        "Fight demons.":
            python:
                d = renpy.random.randint(1,5)
                enemies = []
                for i in range(d):
                    n = renpy.random.choice(all_demons)
                    l = main_fighter.level + renpy.random.randint(-3, 3)
                    enemies.append(fighter(n, l, "Demon"))
            call screen battle(enemies)
    if j:
        return
    else:
        jump ch3_1

