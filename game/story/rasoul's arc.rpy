﻿
# Fights
image rasoul idle:
    "rasoul idle_1"
    .1
    "rasoul idle_2"
    .1
    "rasoul idle_3"
    .1
    repeat

label rasoul_arc_1:
    scene
    show bg street onlayer bg
    show screen pnc(hero, street_map)
    show ras normal with dissolve
    menu:
        "I didn't do anything wrong...":
            abd "I didn't do anything wrong Rasoul."
            show ras angry
            ras "Shut up!" with hpunch

        "Head of the palace guards, taking orders from Kamal...":
            abd "I never imagined to see head of palace guards taking orders from Kamal."
            "..."
            abd "Does he have some dirt on you?"
            show ras angry
            ras "I'm just doing my job and keeping the scum like you off the street."
            abd "What did I do?"
            show ras normal
            ras "Violation of people's property."
            ras "Don't tell me it wasn't you talking to female slaves in the rich section."
            abd "Well I did talk, but...{w=.2}{nw}"
            show ras smile
            ras "So you've confessed.{w=.2}{nw}"
            ras "MOVE IT!" with hpunch
        "Run...":
            "What's that?{w=.2}{nw}"
            hide abd with moveoutleft
            show ras angry
            ras "No you won't!{w=.2}{nw}" with vpunch
            scene
            hide pnc
            $ e = fighter("Rasoul", random.randint(8, 12) + main_fighter.level, "Beast")
            call screen battle([e])
            jump agrabahs_gate
            pause 2
            jump beduins_camp


    scene
    show bg bazaar onlayer bg
    show screen pnc(hero, bazaar_map)
    show ras normal with dissolve
    ras "Walk faster!"
    "{nw}"
    scene
    show bg poor onlayer bg
    show screen pnc(hero, poor_map)
    "{w=1}{nw}"
    show bg barracks onlayer bg
    show screen pnc(hero, barracks_map)
    show ras normal with dissolve
    ras "Guard!"
    show ras normal
    with move
    show guard_2 normal at midright with dissolve
    guard_2 "Yes sir?"
    ras "Take him to jail."
    guard_2 "Yes sir!"
    hide ras with moveoutright
    show guard_2 at center with move
    "{w=.2}{nw}"
    hide screen pnc

image bg jail = "bg/jail/bg.webp"
image bg jail cell = "bg/jail/cell.webp"


init python:
    class book:
        def __init__(self, name, inf, paragraphs):
            self.name = name
            self.inf = inf
            self.paragraphs = paragraphs

screen book_reader(b):
    modal True


default the_free_lie = book(
    _("The free lie"),
    _("By Jafar Barmaki"),
    [
        _("In a grand scale, free doesn't exist. Everything has it's own cost and somebody is paying that cost, that somebody is often you."),
        _("The iron in the ground is free, but you need to pay for an iron axe simply because somebody had to dig the iron out of the ground, somebody had to gather wood for the bloomery, somebody had to hammer the bloom into iron and somebody had to shape it into an axe.\nIt's useless to you when it's free and even if you do all of those yourself, it wouldn't be free, you had to pay for it with your labor and time."),
        _("When you find a sack of coins on the ground, it looks like free money for you, but comes as a heavy cost to somebody else."),
        _("When a merchant feels generous with votive offerings, it might look like a free meal that comes out of his pockets to the commoners, but the cost often comes out of the pockets of his customers.\nHe kept his house, his shop, his wealth and his social status. Nothing changes for him, if anything, this show of duplicity was a ploy to push him upwards in the social ranks."),
        _("In other hand, he cover his costs by selling his merchandise for a little more. A cost that everybody else has to pay for him."),
        _("You can't think of anything that comes free of cost, some effort had to go into collecting, moving or shaping it. Therefore, next time you're offered something for free, ask, what's the catch?")
    ]
)
default the_free_lie_book = item(
    _("The free lie"),
    _("One of Jafar's books."),
    "the_free_lie_book",
    2300,
    ["Book", "By Jafar", "Forbidden"],
    the_free_lie,
    )

default jail_chest = inventory(
    0,
    [

    ],
    1.0
)
label rasoul_arc_2:
    scene
    show bg jail onlayer bg
    # show screen pnc(hero, barracks_map)
    show guard_2 normal with dissolve
    guard_2 "I've got a guest for you Qasim."
    qasim "Coming..."
    show guard_2 normal at right
    with move
    show qasim normal with dissolve
    qasim "Go!"
    guard_2 "Right!"
    hide guard_2 with dissolve
    show qasim normal with move
    qasim "You're pretty lucky to get in.{w=.2} We're fully booked."
    qasim "Now give me your belongings.{w=.2} I'll keep them safe."
    abd "But...{w=.2}{nw}"
    qasim "It's the law." with hpunch
    call screen show_loot(jail_chest, mandatory = "give")
    qasim "Your money too."
    "..."
    call screen show_loot(jail_chest, mandatory = "give_cash")
    abd "Is that...{w=.2} pile of books?"
    qasim "They're illegal books we confiscated, not for the prisoners."
    show bg jail cell onlayer bg with dissolve
    show qasim normal with dissolve
    qasim "Here's your room..."
    qasim "No bed but the shackles are pretty comfy.{w=.2} Just yell if you want me to put them on you."
    "..."
    qasim "Enjoy your stay in the palace."
    hide qasim with dissolve

default planted_evidence = quest(
    _("Planted evidence"),
    [_("Rasoul wants you to plant one of Jafar's books in Hakim's shop.")],
    )


label rasoul_arc_3:
    menu:
        "Sleep":
            show screen time_pass(random.randint(3,10))
            "Resting for a while."
            jump rasoul_arc_3
        "Ask for food.":
            abd "Guard...{w=.2} guard!"
            "..."
            abd "Guard!"
            show qasim normal with dissolve
            qasim "What is it?"
            abd "I'm hungry."
            qasim "Where do you think you are?{w=.2} A tavern?"
            if (calendar.day % 2):
                qasim "You'll get your piece of bread every other day.{w=.2} Today isn't the other day."
            else:
                qasim "You'll get your piece of bread every other day.{w=.2} Lucky for you, today is an other day."
            qasim "Now shut up!"
            hide qasim with dissolve
            menu:
                "I can't stay here...":
                    abd "Guard!"
                    "..."
    show qasim normal with dissolve
    qasim "Will you shut up?"
    abd "Guard...{w=.2} please...{w=.2} I can't stay here..."
    qasim "Why didn't you say so?{w=.2} Let me release you."
    "..."
    abd "Really?"
    qasim "Of course not.{w=.2} You idiot."
    abd "Come on,{w=.2} there must be a way,{w=.2} I didn't do anything wrong."
    qasim "Why didn't yo...{w=.2}{nw}"
    ras "There is a way."
    show qasim at right with move
    show ras normal at center with moveinright
    ras "You can pay the fine."
    abd "But you took all of my money."
    qasim "You have some money stashed somewhere don't you?"
    ras "Do you?"
    abd "I'm a wood collector sleeping on the streets Rasoul."
    ras "Then this is an improvement for you, isn't it?"
    abd "Please Rasoul, you know I'm innocent."
    ras "Hmmm...{w=.2} Maybe you can do something for me."
    abd "Anything Rasoul."
    ras "Bring me the book!"
    qasim "Yes sir."
    hide qasim with moveoutright
    "..."
    show qasim normal at right with moveinright
    qasim "Sir."
    ras "Take this!"
    $ hero.got(the_free_lie_book, 1)
    ras "Plant this book on Hakim's shelf and I'll forgive you."
    abd "Alright...{w=.2} But why."
    $ qlog.got(planted_evidence)
    ras "Because I said so."
    abd "Hakim is my friend Rasoul.{w=.2} What are you planning to do to him."
    ras "Do you want to get out of here or not?"
    abd "Yes."
    ras "Then do as I say."
    abd "well...{w=.2} If I have to."
    ras "Good.{w=.2} Release him!"
    hide ras with moveoutright
    show qasim at center with move
    qasim "Yes sir!"
    "..."
    scene
    show bg jail onlayer bg with dissolve
    # show screen pnc(hero, barracks_map)
    show qasim normal with dissolve
    abd "Can I have my belongings back?"
    qasim "What belongings?"
    abd "The ones you took from me."
    qasim "Alright, here are your junk."
    call screen show_loot(jail_chest, mandatory = "take")
    abd "And my money?"
    qasim "You didn't have any."
    abd "But...{w=.2}{nw}"
    qasim "Do you want to go back to your cell?"
    abd "No."
    qasim "Then get out!"
    "..."
    qasim "Go!"
    jump barracks

label rasoul_arc_end:
    scene
    hide screen pnc
    show bg jail onlayer bg
    # show screen pnc(hero, barracks_map)
    show qasim normal with dissolve
    qasim "Give me your belongings."
    abd "Why?"
    qasim "Don't argue with...{w=.2}{nw}"
    ras "Ehmmm.{w=.2}{nw}"
    show ras normal at center with moveinright
    ras "Get lost."
    qasim "Yes sir."
    hide qasim with moveoutright
    show ras normal with move
    ras "Well?"
    abd "Yes, I've planted the book in his bookshelf."
    ras "Excellent, you can go."
    $ planted_evidence.complete()
    $ hakim_loc.enabled = False
    if "Return to Rasoul." in planted_evidence.info:
        jump barracks
    abd "There's one more thing."
    ras "What?"
    abd "I've also planted a bottle of wine in his remedies."
    ras "Why?"
    abd "Well, Since Hakim often reads books, it's possible he would spot the book and destroys it before you get there."
    ras "Good point. You're not as dum as you look."
    ras "I better move fast before that happens."
    abd "Wait?"
    ras "What now?"
    menu:
        "I can assist you...":
            abd "I can assist you with these type of things if you want."
            ras "Really."
            ras "But why?"
            abd "You're a powerful man and I want to be on your good side."
            ras "Am I? I mean, I am! That's a smart move."
            ras "I'm sure I can use you for something later."
            abd "Sure, hopefully not anything that needs money, I had a hard time finding money to buy the wine."
            "..."
            ras "Qasim!"
            show qasim normal with dissolve
            qasim "Yes sir?"
            ras "Give him some money."
            qasim "Yes sir!"
            hide ras with moveoutright
            qasim "So... How much are we talking about?"
            $ money_amount_barter = 0
            jump rasoul_arc_end_barter

        "I've paid money for the wine.":
            abd "I've paid money for the wine, can you pay me for it please?"
            ras "How dare you ask for money?"
            ras "Qasim!"
            show qasim normal with dissolve
            qasim "Yes sir?"
            ras "Throw him back in the jail."
            abd "wait...{w=.2}{nw}"
            hide ras with moveoutright
            qasim "Huh... You're so stupid."
            abd "but...{w=.2}{nw}"
            qasim "Silence! You know the drill, cough up your belongings."
            "..."
            call screen show_loot(jail_chest, mandatory = "give")
            qasim "And my money."
            call screen show_loot(jail_chest, mandatory = "give_cash")
            qasim "Now move!"
            show bg jail cell onlayer bg
            show qasim normal with dissolve
            "..."
            qasim "Enjoy your stay in the palace."
            hide qasim with dissolve
            jump rasoul_arc_end_jail

label rasoul_arc_end_jail:
    menu:
        "Sleep":
            show screen time_pass(random.randint(3,10))
            "Resting for a while."
        "Guard.":
            abd "Guard...{w=.2} guard!"
            qasim "Shut up!"
    jump rasoul_arc_end_jail

label rasoul_arc_end_barter:
    menu:
        "500":
            abd "500"
            $ money_amount = 500
        "700":
            abd "700"
            $ money_amount = 700
        "1000":
            abd "1000"
            $ money_amount = 1000
        "2000":
            abd "2000"
            $ money_amount = 2000
        "3000":
            abd "3000"
            $ money_amount = 3000
        "4000":
            abd "4000"
            $ money_amount = 4000
    if money_amount == 500:
        qasim "Here's 300, now get lost!"
        $ hero.gotcash(300)
        jump barracks
    elif money_amount == 4000:
        qasim "Not a chance!"
        jump rasoul_arc_end_barter
    else:
        if money_amount_barter < 2:
            if money_amount < random.randint(500, 3050):
                qasim "Fine, take the money and get lost."
                $ hero.gotcash(money_amount)
                jump barracks
            else:
                "..."
                $ money_amount_barter += 1
                jump rasoul_arc_end_barter
        else:
            qasim "You get 500 and that's it."
            $ hero.gotcash(500)
            qasim "Now get lost."
            jump barracks


default widows_house = pnco(
    "Widow's house",
    "bg/poor/widows_house.webp",
    (679, 462),
    Jump('widows_house'),
    hidden = False, hoffset = (20,-80),
    )

define wid = Character("Woman", color="#044", what_text_color="#fdd", namebox_align=(1.0, 0.0))

image bg widows house = "bg/widows_house/bg.webp"
label visiting_widow:
    scene
    show bg poor onlayer bg
    show screen pnc(hero, poor_map)
    show ras normal with dissolve
    ras "So, what can you do for me?"
    abd "Anything!"
    ras "Anything you say? Yeah, I guess I can use somebody like you."
    hide screen pnc
    show bg widows house onlayer bg
    show ras normal with dissolve
    ras "Wait here"
    hide ras with dissolve
    "{w=3}{nw}"
    wid "Why are you in my house?"
    show widow normal with dissolve
    $ wid.name = "Soodeh"
    menu:
        "Ummm...":
            abd "Ummm..."
    ras "He's with me."
    show widow normal at midright with move
    show ras normal with dissolve
    ras "Go!{w=.8}{nw}"
    hide widow with moveoutright
    "..."
    ras "Come on, time to go."
    show bg poor onlayer bg with dissolve
    show screen pnc(hero, poor_map)
    $ poor_map.add(widows_house)
    "..."
    ras "What?"
    abd "I didn't say anything."
    ras "Look, she has a daughter who needs my support."
    ras "The poor girl just lost her father, you see."
    ras "Such a tragedy."
    abd "Wasn't it you who executed him?"
    ras "What, No!? I mean... Well, If you want to get all technical about it..."
    ras "Then, yes."
    ras "But that's not the point!"
    abd "Of course, It's none of my business."
    ras "Look, It's my job to maintain order within the city."
    ras "He broke the law and the heavy, er... burden, fell to me to deal with it."
    "..."
    ras "Let's keep moving."
    "{nw}"
    scene
    show bg bazaar onlayer bg
    show screen pnc(hero, bazaar_map)
    show ras normal with dissolve
    "{w=1}{nw}"

    scene
    show bg street onlayer bg
    show screen pnc(hero, street_map)
    show ras normal with dissolve
    "{w=1}{nw}"


default dirt_on_haji = quest(
    _("Dirt on Haji"),
    [_("Rasoul wants some dirt on Haji. Something that'll land him in jail.")],
    )

label rasoul_needs_dirt:
    scene
    show bg rich onlayer bg
    show screen pnc(hero, rich_map)
    show ras normal with dissolve
    ras "Here we are."
    abd "You're not planning to drag me off to jail again, are you?"
    ras "Don't worry. Just follow my instructions and you'll be fine."
    abd "Alright."
    abd "What do you need me to do?"
    ras "Do you see that fat bastard over there?"
    abd "Haji's boy?"
    ras "Yes."
    ras "I have a bone to pick with his father, but he's outside my err... {i}official{/i}, reach."
    ras "I need you to find some dirt on his father."
    abd "What kind of {i}dirt{/i}?"
    ras "Anything that can land one of them in jail. I don't care what."
    $ qlog.got(dirt_on_haji)
    abd "Alright."
    ras "Oh, and don't touch their slave girl! She's mine!"
    $ dirt_on_haji.extend(_("Don't touch their slave girl."))
    ras "Any questions?"
    abd "Nope!"
    hide ras with dissolve
    jump rich
