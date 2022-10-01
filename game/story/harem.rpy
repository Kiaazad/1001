

define hal = Character("Halia", color="#4ff", what_text_color="#dff")
define hur = Character("Huria", color="#4ff", what_text_color="#dff")
define hul = Character("Hulu", color="#4ff", what_text_color="#dff")

default halia_fight = fighter("Halia", 4, "Dancer")
image halia idle:
    "halia idle_1"
    .1
    "halia idle_2"
    .1
    "halia idle_3"
    .1
    repeat

label harem:
    scene bg harem with dissolve
    $ jafar.add_flag("met jafar's harem")
    menu:
        "Go talk to the girls.":
            menu:
                "Go to the sweet one.":
                    abd "Hello."
                    show huria normal with dissolve
                    $ renpy.pause(.1)
                    show huria shocked
                    hur "Eeeep? You can talk?"
                    abd "Don't panic please, I'm a friend of Jafar."
                    hur "You're not one of Jafar's conjured creatures?"
                    show halia scream at midright
                    hal "Back off! Back off from her!"
                    show huria worry
                    hur "Halia wait! He's not a creature."
                    show halia confused at midright
                    hal "He's not?"
                    abd "It's true. I'm a real human."
                    hal "A real human? how did you get inside the lamp?"
                    abd "I've found the lamp. And Jafar brought me in here."
                    menu:
                        "I've made a deal with Jafar to help him.":
                            abd "I've made a deal with Jafar to help him."
                            hal "..."
                            hal "Then go back to Jafar. I'll have to think."
                            abd "errm..{nw}"
                            hal "What are you waiting for?"
                            abd "Sure, see you later then."
                            if "late harem visit" in jafar.flags:
                                jump inside_lamp
                            else:
                                jump lamp_visit_back_to_jafar

                        "I'm the lamp's owner and your master now.":
                            abd "I'm the lamp's owner and your master now."
                            show halia normal at midright
                            hal "No you're not!"
                            abd "I'm pretty sur...{nw}"
                            show halia scream at midright
                            hal "No! You're wrong! Now get lost before I cut you!"
                            menu:
                                "Alright alright, I'm going.":
                                    abd "Alright alright, I'm going."
                                    if "late harem visit" in jafar.flags:
                                        jump inside_lamp
                                    else:
                                        jump lamp_visit_back_to_jafar
                                "No way.":
                                    abd "No way! you need to respect me."
                                    hal "Respect huh?"
                                    hide hur
                                    hal "Alright, here's my respect."
                                    hal "For the dead!"
                                    hide hal
                                    window hide
                                    call screen battle([halia_fight])
                                    show hulu angry at midright
                                    show huria shocked
                                    hul "{size=50}That's enough!"
                                    hul "{size=50}Get out of here!!"
                                    abd "Di..."
                                    hul "{size=50}Now!!!"
                                    abd "Alright, alright..."
                                    if "late harem visit" in jafar.flags:
                                        jump inside_lamp
                                    else:
                                        jump lamp_visit_back_to_jafar
                "Go to the angry one.":
                    show halia normal at midright
                    abd "hi."
                    show black # Halia knocks hero out
                    $ renpy.pause(3)
                    show huria normal behind black
                    hide black with dissolve
                    abd "What happened?"
                    hal "See he's alive."
                    hal "Next time don't jump me like that."
                    abd "I didn't..."
                    hal "Now get up!"
                    $ renpy.pause(.1)
                    hal "Can you walk?"
                    abd "Yes."
                    hal "Great, get lost then!"
                    abd "But..."
                    hal "Now!"
                    abd "Alright... I'm going..."
                    if "late harem visit" in jafar.flags:
                        jump inside_lamp
                    else:
                        jump lamp_visit_back_to_jafar
                "Go to the conceded one.":
                    show hulu normal
                    abd "hi."
                    hul "No you didn't..."
                    abd "I didn't what?"
                    hul "Tell me you didn't come to me expecting something all dirty like that."
                    abd "No no! I just wanted to say hi to such a beaut...{nw}"
                    hul "Hold it right there! I knew it. You did come here to get under my skirt."
                    abd "No I didn't."
                    hul "do you want to?"
                    abd "I mean...{nw}"
                    hul "I knew it!"
                    abd "..."
                    hul "Not like this though, Go sit in that tub and start washing yourself."
                    hul "I'll join you soon."
                    jump harem_bath
                "Hey ladies...!":
                    abd "Hey ladies."
                    hal "Step back! don't come any closer!"
                    abd "I...{nw}"
                    hal "Turn around and walk out of here while you can."
                    abd "But I'm...{nw}"
                    hal "Now!"
                    abd "Alright... Alright..."
                    abd "Well that was counter productive."
                    hal "Stop mumbling and walk faster!"
                    if "late harem visit" in jafar.flags:
                        jump inside_lamp
                    else:
                        jump lamp_visit_back_to_jafar
        "Jump right into the water.":
            # show bg cg_hero_bathing
            show hulu normal with dissolve
            hul "We have a tub you know!"
            abd "Oh, Hi! I didn't want to disturb you ladies."
            hul "That's alright, the water will clear up soon."
            hul "You should have removed your cloths first."
            abd "But...{nw}"
            hul "Come on! Don't be shy."
            hul "Get naked and get in that tub over there."
            hul "I'll join you shortly."
            jump harem_bath

label harem_bath:
    scene black
    show cg harem bath 01 with dissolve
    hul "{size=10} ... once ... me ... Huria can...."
    hal "{size=10} ... crazy? ... filthy son ... no way ... day...."
    hul "{size=10} ... is it ... time ... us ... time ..."
    hal "{size=10} ... if I ... but ... once ..."
    hal "{size=10} ... alright but ..."
    hal "{size=10} ... yay ... love ..."
    $ renpy.pause(1)
    show cg harem bath 02 with dissolve
    $ renpy.pause(1)
    show cg harem bath 03 with dissolve
    $ renpy.pause(1)
    show cg harem bath 04 with dissolve
    $ renpy.pause(1)
    show cg harem bath 05 with dissolve
    $ renpy.pause(1)
    hide cg with dissolve
    scene bg harem with dissolve
    show huria normal with dissolve
    show hulu normal at midright with dissolve
    show halia normal at midleft with dissolve
    hal "Alright, you had your fun, now beat it!"
    hal "Hulu has lots of cleaning to do."
    hul "You're cruel Halia."
    hal "Your idea, your mess, your job to clean!"
    hul "Alright, what's your name stud?"
    python:
        name = renpy.input(_("My name is..."))
        name = name.strip()
        if not name:
            name = "Smog"
        hero.name = name
        abd.name = name
    abd "[hero.name]."
    hul "Don't be a stranger [hero.name], pay us a visit soon."
    hul "Come again, and again, and again..."
    hal "Stop it..."
    abd "Um... sure?"
    hal "What are you standing here for?"
    abd "Oh right, see you later then."
    if "late harem visit" in jafar.flags:
        jump inside_lamp
    else:
        jump lamp_visit_back_to_jafar

label lamp_harem:
    scene
    if not "met jafar's harem" in jafar.flags:
        $ jafar.add_flag("late harem visit")
        jump harem
    menu:
        "Peep inside!":
            $ chance = random.randint(0, 100)
            if chance < 20:
                if not "ntr" in jafar.flags:
                    jump peep_on_jafar
                
            abd "They's playing with each other's tits."
            abd "What a sight to behold."
            abd "Wish I could show that to everybody."

        "Go talk to the girls.":
            jump talk_to_harem_girls
        "Leave.":
            pass
    jump inside_lamp
default seeking_painful = quest(
    _("Seeking painful"),
    [_("Harem girl Halia seems to be crazy about causing pain, and she's talking about a thin pointy sword.")]
)
default seeking_sweets = quest(
    _("Seeking sweets"),
    [_("Harem girl Hulu seems to be interested in sweets.")]
)
default seeking_fluffy = quest(
    _("Seeking fluffy"),
    [_("Harem girl Huria likes cute, cuddly and fluffy stuff.")]
)
label talk_to_harem_girls:
    menu:
        "Talk to [hal.name].":
            show halia normal with dissolve 
            abd "Hi [hal.name], how are you today?"
            if not hal.name == "Halia":
                hal "I have a name, it's Halia."
            hal "What do you want?"
            menu:
                "I've got you something.":
                    abd "I've got you something."
                    hal "Oh?"
                    call screen show_bag(give = True)
                    abd "here..."
                    if hero.giving.item in [rapier]:
                        hal "[hero.giving.item.name]!"
                        hal "Ehm..."
                        hal "I mean..."
                        hal "Alright I'll fuck you. Strip!"
                        jump fuck_halia
                    else:
                        hal "What use do I have for [hero.giving.item.name]?"
                        hal "Don't bring your junk here."
                "Just want to talk":
                    abd "Just want to talk"
                    hal "About what?"
                    abd "I just want to know more about you."
                    hal "I much rather fighting you."
                    hal "Can imagine when I'm standing over you beaten up face..."
                    hal "Push just the tip of my thin shiny and new sword into yor skin..."
                    hal "You beg me for mercy... And I let you live another day..."
                    abd "Do you hate me that much?"
                    hal "Hate? NO! I just... you know..."
                    $ qlog.got(seeking_painful)
                    abd "Can't say I do. Can you elaborate?"
                    hal "Wait a minute. You're tricking me to talk..."
                    hal "Get lost."
                    abd "But we were getting along."
                    hal "Out!"
                    abd "Alright."

        "Talk to [hul.name].":
            show hulu normal with dissolve 
            abd "Hello [hul.name]."
            if not hul.name == "Hulu":
                hul "The name's Hulu sweetie."
            hul "What can I do for you honey?"
            menu:
                "I've got you something.":
                    abd "I've got you something."
                    hul "Sweet. What is it?"
                    call screen show_bag(give = True)
                    abd "here..."
                    if hero.giving.item in [halva, sugar_halva, chickpea_cookie, zulbia, date_cake, baklava, qhottab, gaz, sohan, kolompeh]:
                        hul "[hero.giving.item.name]?"
                        hul "I would've suck your dick for that."
                        abd "Really?"
                        hul "Sure."
                        abd "Will... You..."
                        hul "WHy not? Drop the pants."
                        jump fuck_hulu
                    else:
                        hul "[hero.giving.item.name]?"
                        hul "Not what I want to sink my teth in."
                        abd "I'll bring something else then."
                        hul "Do that honey and I'll lick you up and down honey."
                "Just want to talk":
                    abd "Just want to talk"
                    hul "Talk honey."
                    abd "Oh... I meant if we can talk."
                    abd "Or you do most of the talking and I listen."
                    hul "Aren't you sweet?"
                    hul "But honey it's not a good time."
                    hul "Maybe later, at tea time, with some pastry, sweets and baklava, I'll talk your ears off."
                    hul "Wouldn't that be nice?"
                    hul "I can't remember last time I did that."
                    $ qlog.got(seeking_sweets)
                    abd "Alright."

        "Talk to [hur.name].":
            show huria normal with dissolve 
            abd "Hello [hur.name]."
            if not hur.name == "Huria":
                hur "Huria."
                hur "Call me Huria."
            hur "Yes?"
            menu:
                "I've got you something.":
                    abd "I've got you something."
                    hur "Really?"
                    call screen show_bag(give = True)
                    abd "here..."
                    if hero.giving.item in [fluffy_doll]:
                        hur "Yay, [hero.giving.item.name]."
                        hur "I love it. I love it."
                        abd "And?"
                        hur "I..."
                        hur "Love you?"
                        abd "By how much?"
                        hur "Eeep."
                        jump fuck_huria
                    else:
                        hur "[hero.giving.item.name]?"
                        "..."
                        abd "What's the matter?"
                        hur "I don't want that."
                        abd "I'll bring something else then."
                        hur "Really?"
                        abd "Sure. Just wait."
                "Just want to talk":
                    abd "Just want to talk"
                    hur "With me?"
                    abd "Yes."
                    hur "Yay!"
                    "..."
                    abd "So... What do you like?"
                    hur "I like fluffy clouds, stars, sunrise, miracles, rainbows, sunshine..."
                    abd "Slow down..."
                    hur "Why?"
                    abd "I can't bring any of that for you."
                    hur "Bring me? Really?"
                    abd "Sure."
                    hur "Yay! You're the best!"
                    hur "Please hurry, I can't wait any longer."
                    hur "Ba bye."
                    abd "Wait, but you didn't say what to bring."
                    hur "Fluffy, cute and cuddly."
                    abd "Bye."
                    $ qlog.got(seeking_fluffy)
                    abd "Alright."



    jump inside_lamp

label fuck_halia:
    "Some fucking will go on here later"
    jump inside_lamp
label fuck_hulu:
    "Some fucking will go on here later"
    jump inside_lamp
label fuck_huria:
    "Some fucking will go on here later"
    jump inside_lamp

label peep_on_jafar:
    show black with dissolve
    show cg jafar_huria_sex_scene with dissolve
    jaf "Take that bitch."
    jaf "You little whore."
    menu:
        "stay and watch":
            jaf "How does the most powerful cock in the world feels?"
            "..."
            hur "Hmmmpfff..."
            jaf "What was that?"
            jaf "Oh yeah, you you can't talk."
            jaf "Good. It's rude to talk with you mouth full."
            jaf "Almost as rude as peeping on people fucking!"
            show screen return_timer(2)
            menu:
                "Leave!":
                    hide screen return_time
                    show cg found_lamp_3 with dissolve
                    jaf "Leaving so soon?"
                    jump harem_caught_peeping
                "Stay!":
                    hide screen return_timer
        "leave":
            hide cg with dissolve
            jump harem_avoided_ntr
    show cg found_lamp_3 with dissolve
    jaf "Enjoying the view?"
    jump harem_caught_peeping


label harem_avoided_ntr:
    abd "What the fuck?"
    jump inside_lamp

default get_them_pregnant = quest(
    _("Get them pregnant"),
    [_("Jafar ordered you to try and get the harem girls pregnant.")]
)
label harem_caught_peeping:
    abd "I'm sorry... I'm sorry..."
    abd "I didn't mean...{w=.5}{nw}"
    jaf "For somebody who doesn't want to peep, you took your sweet time."
    abd "Sorry... Sorry..."
    jaf "Calm down. It's fine."
    abd "Nooo..."
    abd "Wait... What?"
    hide black
    hide cg
    show jaf normal
    with dissolve
    jaf "I was messing with you."
    jaf "I don't care. Neither do the girls."
    abd "You don't?"
    jaf "I've figured that you'll eventually walk on me ramming one of the girls."
    jaf "Talked it over with them, and they said it's fine."
    abd "I see."
    "..."
    abd "You don't mind if I..."
    jaf "You what? Try to fuck them?"
    abd "Well."
    jaf "You would lose few teths if you asked me that in my human years."
    jaf "When sharing women meant risking a disease or a bastard child."
    jaf "I'm a god now, none of those seem to apply anymore. I've tried plenty."
    abd "You tried to get sick?"
    jaf "Well yes! To some extend."
    jaf "But I'm sure I can't get any of the girls pregnant... Tested that thoroughly."
    jaf "There is one more thing to test though."
    jaf "That's were you come in."
    abd "Me?"
    jaf "Yes... See if you can get any of the girls pregnant."
    abd "Really?"
    jaf "Sure. Why not? Let's figure this thing together"
    $ qlog.got(get_them_pregnant)
    abd "Alright! Can I start now?"
    jaf "Maybe later, I'm not done with them today."
    jaf "And you can't just jump on them."
    jaf "Show them some respect. Earn their affection."
    abd "I will, Thank you, thank you."
    jaf "Go before this conversation gets more awkward than it is."
    abd "Yes!"
    $ jafar.add_flag("ntr")
    jump inside_lamp

















