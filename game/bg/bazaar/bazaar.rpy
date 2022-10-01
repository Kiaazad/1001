init:
    default bazaar_street_loc = pnco(
        "Street",
        "bg/bazaar/street.webp",
        (516, 343),
        Jump('street'),
        hidden = False, hoffset = (40,60),
        )
    default akbar_loc = pnco(
        "Akbar's shack",
        "bg/bazaar/akbar.webp",
        (0, 466),
        Jump('akbars_shack'),
        hidden = False, hoffset = (200,0),
        shifts = [[90,270]],
        )
    default fruits_loc = pnco(
        "Fruits shack",
        "bg/bazaar/fruits.webp",
        (631, 581),
        Jump('fruit_shack'),
        hidden = False, hoffset = (83,-40),
        shifts = [[95,260]],
        )
    default jewelry_loc = pnco(
        "Jewelry",
        "bg/bazaar/jewelry.webp",
        (798, 405),
        Jump('jewelry_shop'),
        hidden = False, hoffset = (146,-80),
        shifts = [[100,250]],
        )
    default rugs_loc = pnco(
        "Rugs and rags shack",
        "bg/bazaar/rugs.webp",
        (868, 486),
        Jump('rugs_shop'),
        hidden = False, hoffset = (200,0),
        shifts = [[90,265]],
        )
    default tailor_loc = pnco(
        "Tailor",
        "bg/bazaar/tailor.webp",
        (1195, 527),
        Jump('tailor'),
        hidden = False, hoffset = (154,-80),
        shifts = [[90,270]],
        )
    default hakim_loc = pnco(
        "Hakim",
        "bg/bazaar/hakim.webp",
        (1476, 75),
        Jump('hakim'),
        hidden = False, hoffset = (100,100),
        shifts = [[80,270]],
        )

    default bazaar_poor_loc = pnco(
        "Poor section",
        "bg/bazaar/poor.webp",
        (407, 999),
        Jump('poor'),
        hidden = False, hoffset = (0,0),
        )
    default bazaar_fatti = pnco(
        "Fatti",
        "bg/bazaar/fatti.webp",
        (532, 669),
        Jump('bazaar_fatti'),
        hidden = False, hoffset = (43,106),
        shifts = [[110,140], [180,210]],
        )
    default bazaar_map = pncs(
        "Bazaar",
        [
            bazaar_street_loc,
            akbar_loc,
            fruits_loc,
            jewelry_loc,
            rugs_loc,
            tailor_loc,
            hakim_loc,
            bazaar_poor_loc,
            bazaar_fatti,
        ], night = "bg/bazaar/night.webp"
        )

image bg bazaar = "bg/bazaar/bg.webp"
label bazaar:
    scene
    show bg bazaar onlayer bg
    show screen pnc(hero, bazaar_map)
    with dissolve
    pause
    jump bazaar

# Fruit vendor
define sim = Character("Simin", color="#4ff", what_text_color="#dff")

default simin_u = unit(
    "Fruit trader",
    "char/fruit_trader",

    1641,
    [
        (dates, 42),
        (cantaloupe, 6),
        (pomegranate, 12),
        (watermelon, 3),
        (apple, 23),
    ],
    1.1,

    8,
    "Peasant",
    interests = [],
    reject = ["Weapon", "armor", "lamp"]
    )
label fruit_shack:
    scene
    show simin normal
    sim "Dates?"
    if qlog.has_line(seeking_sweets, "Fatti says the fruit vendor's wife Simin used to cook sweets."):
        abd "Ive heard you used to cook sweets."
        sim "That is correct."
        abd "You don't do that anymore?"
        sim "Ever since my husband got arrested, I have to tend this shack."
        abd "What for did he get arrested?"
        sim "The thief he tried to cut the hand of, turned out to be the princess."
        abd "I see."
        "..."
        sim "Do you need sweets?"
        abd "Yes, can you bake some for me?"
        sim "I can bake small amounts if you want."
        abd "Really?"
        sim "Yeah, sure. I need the money."
        abd "Awesome, when should I come back."
        sim "Tomorrow."
        $ seeking_sweets.extend("Simin agreed to baking some sweets for you.")
        $ timed_quest_extends.append([seeking_sweets, "The sweets must be ready now.", calendar.when_next(90)])
        abd "Alright. Thank you."
        sim "Anything else you need?"
    elif qlog.has_line(seeking_sweets, "The sweets must be ready now."):
        $ simin_u.add_items(halva, 12, date_cake, 8, chickpea_cookie, 20, qhottab, 10, kolompeh, 15)
        $ seeking_sweets.extend("Should I ask for more?")
        abd "Sweets?"
        sim "Yes, they're ready."
    show simin normal at right with move
    call screen shop(s = simin_u)
    jump bazaar

# Jeweler
define jew = Character("Jeweler", color="#4ff", what_text_color="#dff")


default jeweler_u = unit(
    "Jeweler",
    "char/jeweler",

    9610,
    [
        (book3, 1),
        (silver_ring, 7),
        (gold_ring, 3),
    ],
    1.1,

    8,
    "Peasant",
    interests = ["jewelry"],
    reject = ["food", "fuel", "Weapon", "armor", "lamp"]
    )
label jewelry_shop:
    scene
    show jeweler normal
    if not "first" in jeweler_u.flags:
        jew "You don't look like you belong here! Did you find something valuable to sell?"
        $ jeweler_u.add_flag("first")
    else:
        jew "What do you want?"

    menu:
        "I've found a gem." if qlog.has(a_diamond_to_sell) == "Active" and hero.has(quartz_bit):
            abd "I've found a gem, looks like a diamond."
            jew "Let me see..."
            "..."
            jew "Fifty!"
            abd "Fifty thousands?"
            abd "I'm going to need a coin sack for my fifty gold coi...{w=.4}{nw}"
            jew "fifty dinars!"
            abd "Huh?"
            jew "It's not a diamond. I'll pay 50 dinars for it, no more."
            $ quartz_bit.name = "Not a diamond"
            $ quartz_bit.val = 100
            "..."
            abd "I think I'll hold unto it."
            jew "Suit yourself."
        "I need a ring to be made." if qlog.has(make_a_copper_ring) == "Active" and hero.has(ring_recipe) and hero.cash >= 2000 and not "making copper ring" in jeweler_u.flags:
            abd "I need a ring to be made."
            jew "What kind of ring? Gold? Silver?"
            abd "Copper."
            "..."
            jew "I don't make junk."
            jew "Don't bother me if you don't have the money for real jewelry."
            abd "I'll pay you for your work like it's a gold ring."
            "..."
            jew "Alright, what's her finger size?"
            abd "It's for me. Well, I think it is."
            $ hero.drop(ring_recipe, 1)
            abd "Here's the instructions."
            "..."
            jew "What..."
            jew "No. I don't want to know..."
            jew "Payment first."
            jew "It costs 2200 dinars."
            abd "I have 2000."
            jew "Fine..."
            $ hero.paidcash(2000)
            abd "Here..."
            jew "It will be ready in a day or two."
            abd "Alright."
            $ jeweler_u.add_flag("making copper ring")
            $ timed_flags.append([jeweler_u, "copper ring made", 24])
        "Is my ring ready?" if "making copper ring" in jeweler_u.flags and not "copper ring delivered" in jeweler_u.flags:
            abd "Is my ring ready?"
            if "copper ring made" in jeweler_u.flags:
                jew "Of course."
                $ hero.got(copper_ring)
                jew "here."
                abd "Thank you."
                $ jeweler_u.add_flag("copper ring delivered")
                $ make_a_copper_ring.extend(_("Take the ring back to Jafar."))
            else:
                jew "Not yet, come back later"
                abd "alright."

        "I've found this lamp." if hero.has(black_lamp) and not "shown lamp" in jeweler_u.flags:
            $ jeweler_u.add_flag("shown lamp")
            abd "I've found this lamp in the desert."
            abd "Do you look like a junk trader?"
            jew "Take it elsewhere..."
        "Just browsing." if not "browsing" in jeweler_u.flags:
            $ jeweler_u.add_flag("browsing")
            abd "No, I'm just browsing."
            jew "No browsing! Buys something or get out!"
        "What do you have?":
            abd "Let me see..."
            show jeweler normal at right with move
            call screen shop(s = jeweler_u)
    jump bazaar



# Akbar
define akb = Character("Akbar", color="#4ff", what_text_color="#dff")


default akbar = unit(
    "Akbar",
    "char/akbar",

    2210,
    [
        (wood, 20),
        (small_sword, 1),
        (bow, 1),
        (arrows, 6),
        (water, 7),
        (prayer_beads, 12),

    ],
    1.1,

    8,
    "Peasant",
    interests = [],
    reject = []
    )

label akbars_shack:
    scene
    show akbar normal
    akb "Welcome, welcome. what can I help you with?"
    abd "Do you need firewood today?"
    akb "Yes. How much are you selling."
    show akbar normal at right with move
    call screen shop(s = akbar)
    jump bazaar

# hakim
define hak = Character("Hakim", color="#4ff", what_text_color="#dff")


default hakim_u = unit(
    "Hakim",
    "char/hakim",

    1710,
    [
        (snake_bite_remedy, 2),
        (scorpion_bite_remedy, 5),
        (salt, 12),
        (saffron, 2),
        (book2, 1),
        (book4, 1),

    ],
    1.1,

    8,
    "Peasant",
    interests = ["remedy"],
    reject = ["Weapon", "armor"]
    )

label hakim:
    scene
    show hakim normal
    if not "first" in hakim_u.flags:
        hak "Welcome strange, how are you today, are you feeling sick?"
        $ hakim_u.add_flag("first")
    else:
        hak "Ah, you're back."
    menu:
        # planted_evidence
        "I just came to say hi." if qlog.has(planted_evidence) == "Active" and hero.has(the_free_lie_book) and len(planted_evidence.info) < 2:
            abd "No, I just came to say hi Hakim."
            hak "Ah, so nice of you. Let me put my grind away and come back to you."
            hide hakim with moveoutright
            abd "No no! I'm leaving, don't let me interrupt your work."
            menu:
                "Leave the book.":
                    $ hero.drop(the_free_lie_book, 1)
                    $ planted_evidence.extend(_("Return to Rasoul."))
            abd "Goodby hakim."
            jump bazaar
        "I have some bad news." if qlog.has(planted_evidence) == "Active" and len(planted_evidence.info) == 1:
            abd "I have some bad news hakim."
            hak "What's the matter? Something happened to you? Are you in pain?"
            abd "It's Rasoul."
            hak "Oh man, is he up to no good again?"
            abd "Yes, and this time he's targeting you."
            hak "Me?"
            abd "He forcing me to plant this book in your shop."
            hak "This is bad"
            "..."
            hak "He wants me in jail.."
            abd "I can refuse and throw the book back to him."
            hak "There's no point."
            hak "He'll throw you in jail and comes for me some other way."
            abd "What should we do?"
            hak "I would run to Jafar, he was the wise man to know what to do, but he's g...{w=.2}{nw}"
            abd "Yes! I can ask him!"
            hak "But he's no more."
            abd "Emmmm..."
            abd "I know somebody as wise as Jafar. I can ask him."
            hak "Who?"
            abd "I'll be right back."
            $ planted_evidence.extend(_("Talk to jafar and find a solution to Hakim's predicament."))
            jump bazaar
        "I have a solution." if qlog.has(planted_evidence) == "Active" and planted_evidence.info[-1] in ["Plant a bottle of wine in Hakim's shop.", "Ask hakim for some money for the wine."] and "Talk to jafar and find a solution to Hakim's predicament." in planted_evidence.info:
            abd "I have the solution Hakim."
            hak "Really? do tell."
            abd "I'll hide a bottle of wine in your shop, tell Rasoul that I've planted the book and the wine."
            abd "He can only find the wine and arrest you for it instead."
            hak "hmmm..."
            hak "If Rasoul doesn't bring another book to plant on me, That can actually work."
            hak "This friend of yours is a genius. Anyone I know?"
            abd "Maybe."
            hak "Interesting, can I meet him?"
            abd "Maybe later."
            hak "Right, let's deal with the situation at hand first."
            hak "Do you have the bottle of wine?"
            if hero.has(wine):
                abd "Yes."
                $ hero.drop(wine, 1)
                abd "Here."
                abd "Put it among your remedies."
                $ planted_evidence.extend(_("Tell Rasoul: the book and wine are planted."))
            else:
                menu:
                    "I'll buy one...":
                        abd "No, but I'll buy one right away."
                    "I didn't have money.":
                        abd "No, They took my money, I didn't have any."
                        hak "I see, here..."
                        $ hero.gotcash(700)
                        hak "This should be enough."
                        abd "I'll be right back."
                $ planted_evidence.extend(_("Buy a bottle of wine for Hakim."))
            hak "Thank you, you're a savior."
            jump bazaar
        "I got the wine." if qlog.has(planted_evidence) == "Active" and planted_evidence.info[-1] in ["Buy a bottle of wine for Hakim."] and hero.has(wine):
            abd "I got the wine Hakim."
            $ hero.drop(wine, 1)
            abd "Here..."
            hak "Thank you."
            abd "Put it among your remedies."
            hak "I will."
            $ planted_evidence.extend(_("Tell Rasoul: the book and wine are planted."))
            "..."
            abd "I should go."
            hak "For sure, let's hope for the best."
            jump bazaar

        "I have bad news and good news..." if qlog.has(planted_evidence) == "Active" and planted_evidence.info[-1] in ["Plant a bottle of wine in Hakim's shop.", "Ask hakim for some money for the wine."] and not "Talk to jafar and find a solution to Hakim's predicament." in planted_evidence.info:
            abd "I have bad news and good news hakim."
            hak "oh? What about?"
            abd "THe bad news is... Rasoul is targeting you and tried to force me to plant one of Jafar's books in your shop or go to jail."
            hak "He didn't..."
            hak "That is indeed bad news. What's the good news?"
            abd "I already have a solution."
            hak "What's the solution?"
            abd "We'll plant a bottle of wine instead and you can make an excuse for it and both of us escape this predicament."
            "..."
            abd "What do you think?"
            hak "That certainty is a solution."
            hak "And he wouldn't back off until they get me behind the bars."
            abd "Who is him:"
            hak "The doctor of the palace."
            abd "Why he wants you locked up?"
            hak "He doesn't like cheap medicine available to the poor and accused me of stealing his patients."
            abd "I see."
            hak "In any case, let's proceed with your plan. I can't think of anything better."
            hak "Do you have the bottle of wine?"
            if hero.has(wine):
                abd "Yes."
                $ hero.drop(wine, 1)
                abd "Here."
                abd "Put it among your remedies."
                $ planted_evidence.extend(_("Tell Rasoul: the book and wine are planted."))
            else:
                menu:
                    "I'll buy one...":
                        abd "No, but I'll buy one right away."
                    "I didn't have money.":
                        abd "No, They took my money, I didn't have any."
                        hak "I see, here..."
                        $ hero.gotcash(700)
                        hak "This should be enough."
                        abd "I'll be right back."
                $ planted_evidence.extend(_("Buy a bottle of wine for Hakim."))
            hak "Thank you, you're a savior."
            jump bazaar

        "Not today..." if not "not today" in hakim_u.flags:
            $ hakim_u.add_flag("not today")
            abd "Not today Hakim."
            hak "Have you come to buy a remedy?"
            abd "Let me see what you have."
        "Found anything to erect old men yet Hakim?" if not "erect old" in hakim_u.flags:
            $ hakim_u.add_flag("erect old")
            abd "Found anything to erect old men yet Hakim?"
            hak "Ah hahaha, This joke again? Let me know if there's anything I can do for you."
            abd "Sure. I'll take a look."
        "I've found this lamp..." if hero.has(black_lamp) and not "shown lamp" in hakim_u.flags:
            $ hakim_u.add_flag("shown lamp")
            abd "I've found this lamp hakim."
            abd "Do you want to buy it?"
            hak "Hmmm... I do need a good old lamp for my nightly reading sessions."
            hak "Looks fine... How much are you selling it?"
            abd "For you hakim, 2000!"
            hak "You know I can't afford that."
            hak "1500?"
            menu:
                "Sure":
                    abd "Sure"
                    hak "Thank you. I'll make it up to you"
                    $ hero.sell(black_lamp, 1, hakim_u, 1500)
                    hak "Do you want to buy something as well?"
                    abd "Sure."
                "Too low!":
                    abd "That's too low hakim."
                    hak "Alright, buy something and I might be able to buy it from you."
                    abd "Sure."
    hak "Choose wisely."

    #just added a cue from the seller, otherwise Abdul continues to slap his lips.
    # since we might add lip flip to vendors, "{nw}" should do the job as well
    "{nw}"
    show hakim normal at right with move
    call screen shop(s = hakim_u)
    jump bazaar





# Tailor
define far = Character("Farrokh the tailor", color="#4ff", what_text_color="#dff")


default tailor_u = unit(
    "Farrokh the tailor",
    "char/farrokh",

    3410,
    [
        (simple_hat, 2),
        (simple_shirt, 3),
        (simple_pants, 2),

    ],
    1.1,

    8,
    "Peasant",
    interests = ["textile"],
    reject = ["Weapon", "armor", "lamp"]
    )

label tailor:
    scene
    show farrokh normal
    far "Do you need stitching? Or new clothing?"
    menu:
        "Not today...":
            abd "Not today, I'm just browsing."
            far "Alright then, tell me if anything catches your eye."
        "I've found this lamp..." if hero.has(black_lamp) and not "shown lamp" in tailor_u.flags:
            $ tailor_u.add_flag("shown lamp")
            abd "I've found this lamp in the desert."
            far "Hmmm... show it to Akbar. Or Hakim."
            far "I'll end up selling it to them if I buy it."
    show farrokh normal at right with move
    call screen shop(s = tailor_u)
    jump bazaar

# Rugs shop
define nem = Character("Nemat", color="#4ff", what_text_color="#dff")

label rugs_shop:
    scene
    show nemat normal
    nem "Rugs?"
    abd "Not today."
    jump bazaar


# fat
define fat = Character("Fatti", color="#4ff", what_text_color="#dff")

label bazaar_fatti:
    scene
    show fatti normal
    fat "What are you shopping for?"
    if qlog.has_line(seeking_sweets, "Harem girl Hulu seems to be interested in sweets."):
        abd "I'm looking for some sweets."
        fat "Simin can cook some for you."
        abd "Really?"
        fat "Yes, and they were really tasty back when she was baking."
        abd "Thank you, I'll ask her."
        $ seeking_sweets.extend("Fatti says the fruit vendor's wife Simin used to cook sweets.")
    else:
        abd "Nothing for now."
        fat "You should buy something to eat, you're wasting away."
    jump bazaar


