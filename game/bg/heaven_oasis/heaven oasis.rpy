﻿init:
    default heaven_oasis_viking = pnco(
        "The viking",
        "bg/heaven_oasis/viking.webp",
        (518, 559),
        Jump('the_viking'),
        hidden = False, hoffset = (120,97),
        )
    default heaven_oasis_fishing = pnco(
        "Start fishing",
        "bg/no_image.png",
        (824, 800),
        Jump('heaven_oasis_fishing'),
        )
    default heaven_oasis_drink = pnco(
        "Drink",
        "bg/no_image.png",
        (924, 850),
        Jump('heaven_oasis_drink'),
        )
    default heaven_oasis_heaven_or_hell_fork = pnco(
        "Heaven or hell fork",
        "bg/no_image.png",
        (311, 629),
        Jump('heaven_or_hell_fork'),
        hidden = False, hoffset = (83,-40),
        )

    default heaven_oasis_loc = pncs(
        "Heaven oasis",
        [
            heaven_oasis_viking,
            heaven_oasis_heaven_or_hell_fork,
            heaven_oasis_fishing,
            heaven_oasis_drink,

        ], night = "bg/heaven_oasis/night.webp"
        )

image bg heaven_oasis = "bg/heaven_oasis/bg.webp"
label heaven_oasis:
    if not heaven_oasis_loc in all_places:
        $ all_places.append(heaven_oasis_loc)
    scene
    show bg heaven_oasis onlayer bg
    show screen pnc(hero, heaven_oasis_loc)
    with dissolve
    pause
    jump heaven_oasis



default old_spyglass = item(
    _("Old spyglass"),
    _("An old spyglass, the front glass has a crack."),
    "old_spyglass",
    3750,
    [],
    )


# The viking
define vik = Character("The Viking", color="#4ff", what_text_color="#dff")
default viking_u = unit( # we use a unit class to manage every character that has important data to keep track of like items or money
    "The Viking",
    "char/viking",

    3410,
    [
        (old_spyglass, 1),
        (fish, 1),
        (big_fish, 2),
    ],
    1.2,

    28,
    "Warrior",
    interests = [],
    reject = ["lamp"]
    )


default beer_for_the_viking = quest( 
    _("A viking's keg"),
    [_("The Viking in the oasis wants me to buy him some beer. A keg of beer.")],
    )

default vikings_note = item(
    _("viking's note"),
    _("A note with the viking's signature."),
    "vikings_note",
    0,
    ["unsellable"],
    )
label the_viking:
    scene
    if not "talked about boat" in viking_u.flags: # checks if they have not talked about the boat incident
        show viking normal
        vik "The wood collector... so, have you come to take my boat apart?"
        abd "Do you always have to mention that? I already told you, I thought it was abandoned."
        vik "Alright alright... Came to buy what I've fished out from my sunken cargo?"
        $ viking_u.add_flag("talked about boat") # adds a flag that they have talked about the boat
    else: # otherwise the usual greeting
        show viking normal
        vik "The shipwrecker! nice to see you again."
        abd "Hey, hi."
    
    if not qlog.has(beer_for_the_viking): # check if the quest is not already in the quest log
        vik "I have a favor to ask my friend."
        abd "Out of food again?"
        vik "No, this time it's something more important."
        abd "More important than food?"
        vik "Of course, I ran out of beer."
        abd "I told you I can get in lots of trouble if the guards catch me with alcohol."
        vik "Come on, they won't suspect you."
        vik "I in other hand, can't take a step in that city without eyes following me."
        abd "I can't."
        vik "I'm dying of thirst."
        abd "There's water."
        vik "Vikings don't drink that junk. Help me here friend."
        abd "Alright!"
        vik "Thank you. You're a savior."
        $ qlog.got(beer_for_the_viking) # add the quest
        $ hero.got(vikings_note)
        vik "Here, take this note to Petros."
        abd "Sure, do you need any food?"
        vik "No I'm all set on that front."
        jump heaven_oasis
    elif "Deliver the keg to the Viking." in beer_for_the_viking.info and hero.has(beer_keg): # If the quest is active
        vik "Got the beer?"
        abd "Yes, here!"
        $ hero.drop(beer_keg, 1)
        $ beer_for_the_viking.complete()
        vik "Thank you my friend, you're a savior."
        # keg noises
        vik "Here, have one on me."
        $hero.got(beer)
        jump heaven_oasis

    if qlog.has_line(seeking_painful, "The viking at heaven oasis might know something."):
        abd "I heard you mentioned thin pointy swords to Rahman."
        vik "Ah yes, I've seen them in Europe."
        vik "It's pretty deadly, and they used it with finesse."
        vik "I Got a couple of wounds from them. Wanna see?"
        abd "Maybe later."
        abd "Can you give me instructions on how to make one?"
        vik "No."
        vik "But I can give you the name if you want to ask around, or look into books."
        vik "It'c called rapier."
        abd "Books... Jafar..."
        abd "Thank you."
        $ seeking_painful.extend("Ask Jafar.")
    vik "Come browse my stuff."
    show viking normal at right with move
    call screen shop(s = viking_u)
    jump heaven_oasis

default heaven_oasis_pound = fishing_class(
    100,
    87,
    [fish, small_fish, big_fish, fish_spirit],
)
label heaven_oasis_fishing:
    scene
    if not "don't bother" in viking_u.flags and heaven_oasis_pound.population == 0:
        show viking normal
        vik "Don't bother, there's no fish to catch."
        "..."
        $ viking_u.add_flag("don't bother")
    
    call screen fishing(heaven_oasis_pound)

    if not "first fish warning" in viking_u.flags and 30 < heaven_oasis_pound.population < 50:
        show viking normal
        vik "Slow down my friend!"
        abd "What?"
        vik "If you catch too many fish too fast, they'll have a hard time replacing the fish you've caught."
        abd "I know that, I sold fish my whole life.."
        vik "Just saying."
        abd "Alright."
        $ viking_u.add_flag("first fish warning")
    if not "second fish warning" in viking_u.flags and heaven_oasis_pound.population < 30:
        show viking normal
        vik "You're fishing this pound dry."
        abd "You fish here too."
        vik "True, but I catch a fish each day. That hardly puts a dent in their numbers."
        abd "Well, I need the money."
        vik "Alright, it's your land, but don't say I didn't warn you."
        abd "Sure, sure."
        $ viking_u.add_flag("second fish warning")
    jump heaven_oasis

label heaven_oasis_drink:
    scene
    $ hero.drink(1, 4)
    jump heaven_oasis



