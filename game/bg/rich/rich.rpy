default rich_agrabah = pnco(
    "Street",
    None,
    (1270, 1009),
    Jump('street'),
    )
default rich_vantage_point = pnco(
    "Go up the mountain",
    None,
    (139, 956),
    Jump('vantage_point'),
    )




# Haji's son
default hajis_son = pnco(
    "Haji's son",
    "bg/rich/hajis_son.webp",
    (670, 764),
    Jump('hajis_son'),
    hidden = False, hoffset = (35,203),
    )
define hajis = Character("Haji's son", color="#4ff", what_text_color="#dff")
define hajis_slave = Character("Haji's slave", color="#4ff", what_text_color="#dff")

label hajis_son:
    scene
    show hajis_son with dissolve
    "..."
    hajis "Slave! more food!"
    hajis_slave "Yes master."
    show hajis_son at midright with move
    show hajis_slave with moveinright
    hajis_slave "Here you go."
    "..."
    hajis "What?"
    abd "Nothing..."

    jump rich

# Kaneez
default rich_laila = pnco(
    "Laila",
    "bg/rich/laila.webp",
    (1437, 733),
    Jump('rich_laila'),
    hidden = False, hoffset = (35,203),
    )
define lai = Character("Laila", color="#4ff", what_text_color="#dff")
define kam = Character("Kamal", color="#4ff", what_text_color="#dff")


label rich_laila:
    scene

    if not "kamal's warning" in hero.flags:
        show laila normal
        lai "New slave?"
        abd "What?"
        lai "I've never seen you around here, you must be a new slave."
        abd "I'm not a slave."
        lai "Ow, just poor then?"
        abd "ermmm..."
        lai "You should leave before...{nw}"
        show laila normal at midright with move
        show kamal normal with moveinright
        kam "Making friends? slave?"
        lai "Sorry master."
        kam "Go!"
        kam "Yes master."
        hide laila
        "..."
        kam "Delivering something?"
        abd "No."
        kam "Then you have no business being here."
        "..."
        kam "Go!"
        kam "Before I report you to the guards."
        abd "alright..."
        $ hero.flags.append("kamal's warning")
        jump rich
    elif not "kamal's second warning" in hero.flags:
        show laila normal with dissolve
        show kamal normal at midright with moveinright
        kam "What did I tell you?"
        kam "Get lost!"
        $ hero.flags.append("kamal's second warning")
        jump rich
    elif not "got arrested" in hero.flags:
        show laila normal with dissolve
        show kamal normal at midright with moveinright
        kam "{size=44}Guard!"
        show laila normal at midright
        show kamal normal at right
        with move
        show ras normal with dissolve
        ras "Is this the guy?"
        kam "Yes."
        ras "Move it buddy!"
        abd "Where to?"
        ras "Jail."
        abd "But...{w=.2}{nw}"
        ras "{size=44}Move!{w=.2}{nw}" with hpunch
        "{nw}"
        $ hero.flags.append("got arrested")
        jump rasoul_arc_1
    else:
        show laila normal with dissolve
        show kamal normal at midright with moveinright
        kam "You're here again?"
        kam "Rasoul will pay for this."
        jump rich



default rich_map = pncs(
    "Rich section",
    [
        rich_agrabah,
        rich_laila,
        rich_vantage_point,
        hajis_son,

    ], night = "bg/rich/night.webp"
    )

image bg rich = "bg/rich/bg.webp"
label rich:
    scene
    show bg rich onlayer bg
    show screen pnc(hero, rich_map)
    with dissolve
    pause
    jump rich