
default farms_village = pnco(
    "Village",
    None,
    (1428, 564),
    Jump('village'),
    )
default farms_orchards = pnco(
    "Orchards",
    None,
    (213, 607),
    Jump('orchards'),
    )
default farms_agrabahs_gate = pnco(
    "Agrabahs gate",
    None,
    (1038, 1019),
    Jump('agrabahs_gate'),
    )
default farm_girl = pnco(
    "Farm girl",
    "bg/farms/farm_girl.webp",
    (1084, 586),
    Jump('farm_girl'),
    hidden = False, hoffset = (83,-40),
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
    [_("The farm girl wants you to delive say hi to her teacher for her.")],
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
        ari "They say that we can see the glimmer of the golden domes from here."
        abd "Aghraba's palace?"
        ari "Yes."
        abd "I don't think so."
        abd "There's a montain in the way."
        "..."
        abd "Why don't you go to the city and seen them close-up?"
        ari "My father wouldn't allow it."
        ari "He forbode me from leaving the village."
        abd "And you're going to obey?"
        ari "Of course."
        abd "If visiting Agrabah is your dream, I can escort you there and back before your father finds out."
        ari "I've seen Aghrabah plenty. I just miss my friends."
        abd "You used to live there?"
        ari "Yes."
        abd "How come you're living in a village now?"
        ari "Can't say!"
        "..."
        ari "Do you visit Agrabah often?"
        abd "Of course."
        ari "can you deliver a message for me?"
        abd "Sure."
        ari "Would you tell my teacher Ariana said hi."
        $ ari.name = "Ariana"
        abd "Just hi?"
        ari "yes."
        abd "And your teacher?"
        ari "She's the head of the school."
        $ qlog.got(ariana_said_hi)
        abd "Alright."
        $ ariana_u.add_flag("First")
    else:
        menu:
            "I have your homework." if hero.has(arianas_notes):
                abd "I have your homework."
                if not "first notes" in ariana_u.flags:
                    abd "Your teacher said hi."
                    ari "How was she."
                    abd "Fi... she was well."
                    $ hero.drop(arianas_notes, 1)
                    abd "And she sent these."
                    ari "My homework!"
                    ari "We left so fast that I couldn't retrive these."
                    ari "Thank you!"
                    abd "She asked me to deliver your homework to you regularly."
                    ari "You would do that?"
                    abd "Sure, why not."
                    ari "Thank you, you're a kind mand."
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
            "I need to speak with your father.":
                abd "I need to speak with your father."
                ari "My father doesn't accept visitors."
                abd "I have a very important message for him."
                ari "What is it? I'll deliver the message to him."
                menu:
                    "No I have to deliver it myself.":
                        abd "No I have to deliver it myself."
                    "Alright.":
                        abd "Alright."
                        abd "Tell him Jafar said hi."
                        ari "What?"
                        abd "Tell him Jafar said ..."
                        ari "I've heard it the first time."
                        ari "Is this some kind of joke?"
                        abd "No."
                        ari "But I thought he was..."
                        abd "Dead?"
                        ari "Yes."
                        abd "Well, he's not."
                        ari "Wait here."
                        hide farmgirl with dissolve
                        pause 5
                        show farm_girl with dissolve
                        ari "My father is eager to know more."
                        ari "he asked for his writting."
                        abd "Sure, I can ask."
                        ari "Please, and hurry up."
                        abd "Alright."


    jump farms

label village:
    "Not ready yet."
    jump farms
label orchards:
    "Not ready yet."
    jump farms