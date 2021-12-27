image cg found_lamp_2:
    "found_lamp_2_1"
    pause .2
    "found_lamp_2_2"
    pause .2
    repeat


default sell_lamp = quest(
    _("Sell the Lamp"),
    [_("Go to the bazaar and sell the lamp you have found.")],
    )

default jafars_revenge = quest(
    _("Jafar's revenge"),
    [_("Assist Jafar in getting his revenge from Aladdin, Jasmine and the Sultan.")],
    )


label intro_0:
    $ calendar.minute = 69
    $ abdul.got_skill(run_away)
    jump roc_pass
label intro_0_1:
    $ roc_pass_map.command = None
    $ all_places.append(roc_pass_map)
    abd "Phew..."
    abd "It's getting hot."
    show des_0_shine:
        align (.834,.73)
        anchor (.5,.5)
    abd "{size=45}Huh!?"
    abd "That isn't...{w=.4} a mirage."
    "..."
    abd "There's something shiny in the sand."
    $ abdul.got(black_lamp,1,002)
    hide des_0_shine with dissolve
    show cg found_lamp_1 with dissolve
    abd "An oil lamp?"
    abd "Looks new."
    abd "Hah, this is my lucky day! I can sell this and finally eat a full meal tonight."
    $ qlog.got(sell_lamp)
    with dissolve
    abd "Hmmm... They say Aladdin found his Genie in a lamp like this and the Genie made all his wishes come true."
    abd "I {b}wish{/b} these rumours were believable."
    "{nw}"
    menu:
        "Rub the lamp!":
            $ snake_pass_map.add(snake_pass_roc_pass)
            $ abdul.add_flag("Meet Jafar")
            show cg found_lamp_2 with Dissolve(2)
            $ renpy.pause(1)
            show cg found_lamp_3 with Dissolve(2)
            jaf "{size=45}Muhahahaaaaaaaaaaaaaaaa{w=.5}{nw}"
            abd "{size=45}What the fuck?{w=1}{nw}"
            jaf "{size=45}Don't you think there's benefit to naivete?{w=1}{nw}"
            $ msg.msg("You dropped the Black Lamp")
            abd "{size=45}Woah! {w=.6}whoa. {w=.4}wha {w=.2}wh...{nw}"
            menu:
                "Run away.":
                    pass
            jaf "{size=45}Where are you running to?"
            jaf "{size=45}COME BACK HERE!{w=1}{nw}" with hpunch
            menu:
                "Please don't steal my soul!":
                    pass
            abd "{size=40}Please don't steal my soul!"
            jaf "{size=40}Calm down, I'm not interested in your soul."
            abd "{size=30}Are you a... {w=.5}a Genie?"
            jaf "Isn't it obvious?"
            jaf "Here, let me..."
            hide cg with Dissolve(2)
            show jaf normal with dissolve
            jaf "Ah, much better."
            abd "Wait! {w=.3}Jafar?"
            jaf "In the flesh... {w=.5}or smoke. {w=.8}Fire, if you want to be precise."
            jaf "Yes,{w=.3} yes, {w=.3}Genies are made of fire."
            jaf "Pick up my lamp would you?"
            abd "{size=25}Sorry."
            $ msg.msg("You got the Black lamp.")
            show jaf thinking
            $ abdul.stat = "Chatting" # In "Chatting" or "Resting" mode abdul consommes half food and water
            jaf "Do you know what holding my lamp means?"
            show jaf normal
            abd "Do... {w=.6}I get a wish."
            jaf "Three wishes?"
            abd "Three? How?"
            jaf "You rub my lamp, wish and I'll grant them."
            jaf "Yep! Those are the rules!"
            jaf "Aren't you glad you rubbed my lamp before selling it?"
            abd "How did you know that was my plan?"
            jaf "You have to stop talking to yourself out loud my friend."
            jaf "Nobody does that. {w=.5}Whenever you see someone talking to themselves, {w=.5}they're faking, {w=.5}or they're just crazy."
            jaf "Now, as I was saying."
            jaf "Here's how it works. You wish for something and I'll try to twist your words against you."
            abd "Against me? {w=.5}But why?"
            show jaf thinking
            jaf "Genies are known to use poorly phrased wishes in... interesting ways."
            jaf "I suppose it's something about teaching you a lesson."
            jaf "The value of Contentment or something stupid like that."
            show jaf normal
            jaf "HOWEVER!"
            jaf "I have a deal to propose."
            abd "A deal?"
            jaf "Yes."
            jaf "If you promise to help me get my revenge from those three idiots..."
            jaf "The bastards who trapped me in this thing...."
            jaf "I'll let you give me your first wish... {w=.5}and second wish..."
            jaf "Then I'll tell you how to avoid being screwed for your last wish."
            abd "What do you mean by 'screwed?'"
            jaf "Well, under normal circumstances... {w=.5}I'd kill you with your own wish."
            abd "Wait, I've heard that Genies can't kill..."
            jaf "Not directly we can't, {w=.5}but you'll be surprised to know..."
            abd "What you can live through?"
            jaf "You've just heard that one huh?"
            jaf "No! That was the old me..."
            jaf "I was about to say: {w=.5}How easy is it to let people die on their own?"
            abd "What do you mean?"
            menu:
                jaf "No time to explain. {w=.5}What do you say? {w=.5}Do we have a deal?"
                "Sure..!?":
                    abd "Sure..!?"
                    $ qlog.got(jafars_revenge)
                    $ sell_lamp.cancel()
                    jaf "Excellent!"
                    show jaf magic
                    $ calendar.day = 1
                    jaf "You're born anew."
                    show jaf normal
                    jaf "Do you know how to get to Agrabah?"
                    abd "Yes, it's that way."
                    jaf "Alright, let's go."
                    abd "But..."
                    jaf "Do you have anywhere better to be?"
                    jaf "A family? Wife and kids?"
                    abd "I live alone."
                    jaf "A lavish palace with servants?"
                    abd "I have a hut."
                    jaf "Well then, you have nothing to lose. Let's go."
                    jaf "Bring the thorns. {w=.5}We need all the money we can get."
                    abd "Alright."
                    $ msg.msg("You got CamelThorns")
                    $ roc_pass_agrabahs_gate.hidden = False
                    $ roc_pass_snakes_pass.hidden = False
                    $ snake_pass_roc_pass.hidden = False
                    $ roc_pass_marble_quarry.hidden = False
                    "{nw}"
                    jump ch1
                "No! I want my wishes":
                    abd "No! I just want my wishes Jafar!"
                    jaf "Are you sure? {w=.5}This will not end well for you my friend."
                    menu:
                        jaf "Last chance, Abdul! Don't throw away this opportunity."
                        "I really want my wishes Jafar.":
                            abd "I really want my wishes Jafar."
                            jaf "So be it."
                            jump wishes
                        "Okay, okay. I yield.":
                            abd "Okay, okay. I yield. Don't screw me up."
                            jaf "Good, let's make haste! {w=.5}Time's a-wastin'."
                            $ qlog.got(jafars_revenge)
                            $ sell_lamp.cancel()
                            abd "What?"
                            jaf "Something I heard- {w=.5}you know what, never mind."
                            "{nw}"
                            $ roc_pass_agrabahs_gate.hidden = False
                            $ roc_pass_snakes_pass.hidden = False
                            $ snake_pass_roc_pass.hidden = False
                            $ roc_pass_marble_quarry.hidden = False
                            jump ch1
        "Don't be naive, search for more firewood.":
            abd "Back to work then."
            $ msg.msg("You hang the lap on your bundle.")
            jump desert_1

