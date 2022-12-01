
default farms_village = pnco(
    "Village",
    "bg/no_image.png",
    (1428, 464),
    Jump('village'),
    )
default farms_orchards = pnco(
    "Orchards",
    "bg/no_image.png",
    (213, 507),
    Jump('orchards'),
    )
default farms_agrabahs_gate = pnco(
    "Agrabahs gate",
    "bg/no_image.png",
    (1038, 919),
    Jump('agrabahs_gate'),
    )
default farm_girl = pnco(
    "Farm girl",
    "bg/farms/farm_girl.webp",
    (1084, 586),
    Jump('farm_girl'),
    hidden = False, hoffset = (83,-40),
    shifts = [[80,250]]
    )

default farms_map = pncs(
    "Farms",
    [
        farms_village,
        farms_orchards,
        farms_agrabahs_gate,
        farm_girl,
    ], night = "bg/farms/night.webp"
    )

image bg farms = "bg/farms/bg.webp"
label farms:
    if not farms_map in all_places:
        $ all_places.append(farms_map)
    scene
    show bg farms onlayer bg
    show screen pnc(hero, farms_map)
    with dissolve
    pause
    jump farms

default ariana_said_hi = quest( 
    _("Ariana says hi"),
    [_("The farm girl wants you to deliver say hi to her teacher for her.")],
    )
default jafars_writing = quest( 
    _("jafar's writing"),
    [_("Ariana's father asked for jafar's writing.")],
    )
default ariana_u = unit(
    "Ariana",
    "char/viking",

    3410,
    [
    ],
    1.2,

    28,
    "Peasant",
    interests = [],
    reject = ["lamp"]
    )
default ari = Character("Farm girl", color="#4ff", what_text_color="#dff")
label farm_girl:
    scene
    show farm_girl with dissolve
    if not "First" in ariana_u.flags:
        ari "Don't bother me."
        abd "Emmm...."
        abd "What are you doing?"
        ari "They say we can see the glimmer of the golden domes from here."
        abd "Agrabah's palace?"
        ari "Yes."
        abd "I don't think so."
        abd "There's a mountain in the way."
        "..."
        abd "Why don't you go to the city and see them close up?"
        ari "My father wouldn't allow it."
        ari "He forbode me from leaving the village."
        abd "And you're going to obey?"
        ari "Of course."
        abd "If visiting Agrabah is your dream, I can escort you there and back before your father finds out."
        ari "I've seen Agrabah plenty. I just miss my friends."
        abd "You used to live there?"
        ari "Yes."
        abd "How come you're living in a village now?"
        ari "Can't say!"
        "..."
        ari "Do you visit Agrabah often?"
        abd "Of course."
        ari "Can you deliver a message for me?"
        abd "Sure."
        ari "Will you tell my teacher \"Ariana said hi\"?"
        $ ari.name = "Ariana"
        abd "Just \"Hi\"?"
        ari "Yes."
        abd "And your teacher is?"
        ari "She's the head of the school."
        $ qlog.got(ariana_said_hi)
        abd "Alright."
        $ ariana_u.add_flag("First")
    elif not "second" in ariana_u.flags:
        menu:
            "I have your homework." if hero.has(arianas_notes):
                abd "I have your homework."
                if not "first notes" in ariana_u.flags:
                    abd "Your teacher said \"Hi.\""
                    ari "How was she?"
                    abd "Fi... she was well."
                    $ hero.drop(arianas_notes, 1)
                    abd "And she sent these."
                    ari "My homework!"
                    ari "We left so fast that I couldn't retrieve these."
                    ari "Thank you!"
                    abd "She asked me to deliver your homework to you regularly."
                    ari "You would do that?"
                    abd "Sure, why not?"
                    ari "Thank you, you're a kind man."
                    abd "She'll pay me. I guess."
                    ari "Still... Not everybody would do that."
                    ari "Thank you."
                    abd "Alright, I'll leave you to study."
                    ari "Thanks."
                    $ ariana_u.add_flag("first notes")
                else:
                    $ hero.drop(arianas_notes, 1)
                    abd "Got your notes."
                    ari "Thank you."
            "I need to speak with your father." if qlog.has(jafar_said_hi) == "Active":
                abd "I need to speak with your father."
                ari "My father doesn't accept visitors."
                abd "I have a very important message for him."
                ari "What is it? I'll deliver the message to him."
                menu:
                    "No, I have to deliver it myself.":
                        abd "No, I have to deliver it myself."
                    "Alright.":
                        abd "Alright."
                        abd "Tell him \"Jafar said Hi\"."
                        ari "What?"
                        abd "Tell him \"Jafar said ...\""
                        ari "I heard it the first time."
                        ari "Is this some kind of joke?"
                        abd "No."
                        ari "But I thought he was..."
                        abd "Dead?"
                        ari "Yes."
                        abd "Well, he's not."
                        ari "Wait here."
                        $ jafar_said_hi.complete()
                        hide farm_girl with dissolve
                        pause 8
                        show farm_girl with dissolve
                        ari "My father is eager to know more."
                        ari "He asked for his writing."
                        abd "Sure, I can ask."
                        $ qlog.got(jafars_writing)
                        ari "Please, and hurry up."
                        abd "Alright."
            "I have Jafar's writing." if hero.has(jafars_writing_note):
                abd "I have Jafar's writing."
                ari "Let me see."
                $ hero.drop(jafars_writing_note, 1)
                abd "Here."
                "..."
                ari "It is Jafar's hand writing."
                abd "You know his hand writing?"
                ari "Of course."
                ari "My father copies books, he still have a couple of Jafar's books that I've read."
                abd "I see."
                ari "Wait here."
                hide farm_girl with dissolve
                pause 8
                show farm_girl with dissolve
                $ jafars_writing.complete()
                ari "My father will be honored to be at Jafar's service once again."
                abd "What he can do for us?"
                abd "Can he lend me money?"
                ari "We don't have much to spare."
                ari "But Jafar asked my father in the note to copy any book you would bring."
                abd "I see."
                abd "I'll have to talk to jafar."
                ari "Alright."
                $ ariana_u.add_flag("second")
    else:
        menu:
            ari "Got a book?"
            "Not today.":
                abd "Not today.."
                ari "Alright."
            

    jump farms

label village:
    "Not ready yet."
    jump farms
label orchards:
    "Not ready yet."
    jump farms