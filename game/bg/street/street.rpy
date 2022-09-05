# Shops
default street_money_lender_loc = pnco(
    "Money lender",
    "bg/street/Money lender.webp",
    (483, 576),
    Jump('money_lender'),
    hidden = False, hoffset = (110,-20),
    shifts = [[100,170],[190,260]],
    )
default street_empty_shop_loc = pnco(
    "Empty shop",
    "bg/street/empty shop.webp",
    (146, 486),
    Jump('empty_shop'),
    hidden = False, hoffset = (20,20),
    shifts = [[100,170],[190,260]],
    )
default street_karim_loc = pnco(
    "Karim's shop",
    "bg/street/karim.webp",
    (94, 636),
    Jump('karim'),
    hidden = False, hoffset = (20,20),
    shifts = [[90,270]],
    )
default street_palace_loc = pnco(
    "Palace",
    "bg/street/palace.webp",
    (711, 357),
    Jump('palace'),
    hidden = False, hoffset = (20,20),
    )
default street_home_loc = pnco(
    "Home",
    "bg/street/home.webp",
    (1464, 200),
    Jump('agrabah'), enabled = False,
    hidden = False, hoffset = (20,20),
    )
default street_blacksmith_loc = pnco(
    "Blacksmith",
    "bg/street/blacksmith.webp",
    (1536, 406),
    Jump('blacksmith'),
    hidden = False, hoffset = (20,20),
    shifts = [[80,280]],
    )

default street_agrabahs_gate = pnco(
    "Agrabah's gate",
    "bg/street/desert.webp",
    (655, 959),
    Jump('agrabahs_gate'),
    hidden = False, hoffset = (20,20),
    )
default street_bazaar_loc = pnco(
    "Bazaar",
    None,
    (1046, 760),
    Jump('bazaar'),
    hidden = False, hoffset = (20,20),
    )

# People
default street_beggar = pnco(
    "Beggar",
    "bg/street/beggar.webp",
    (1193, 802),
    Jump('beggar'),
    hidden = False, hoffset = (17,42),
    )

default street_jamal = pnco(
    "Jamal",
    "bg/street/jamal.webp",
    (781, 775),
    Jump('jamal'),
    hidden = False, hoffset = (14,76),
    shifts = [[100,260]],
    )
default street_shepard = pnco(
    "Shepard",
    "bg/street/shepard.webp",
    (899, 780),
    Jump('shepard'),
    hidden = False, hoffset = (15,43),
    shifts = [[140,220]],
    )

default street_map = pncs(
    "Main street",
    [
        street_money_lender_loc,
        street_empty_shop_loc,
        street_karim_loc,
        street_agrabahs_gate,
        street_palace_loc,
        street_bazaar_loc,
        street_home_loc,
        street_blacksmith_loc,

        street_beggar,
        street_jamal,
        street_shepard,
    ], night = "bg/street/night.webp"
    )

image bg street = "bg/street/bg.webp"
label street:
    scene
    show bg street onlayer bg
    show screen pnc(hero, street_map)
    with dissolve
    pause
    jump street

# Blacksmith
define rah = Character("Rahman", color="#4ff", what_text_color="#dff")

default damascus_steel = item(
    _("Damascus steel"),
    _("Very high quality steel from India."),
    "damascus_steel",
    1400,
    ["Material", "Metal"],
    )
default damascus_sword = item(
    _("Damascus sword"),
    _("A sword so sharp it can cut silk in mid air."),
    "damascus_sword",
    1400,
    ["Weapon"],
    )



default rahman_u = unit(
    "Rahman",
    "char/rahman",

    1310,
    [
        (arrowhead, 24),
        (small_sword, 2),
        (axe, 4),
        (saw, 2),

    ],
    1.1,

    14,
    "Peasant",
    interests = ["Weapon", "Armor", "Fuel"],
    reject = ["hard drug"]
    )
label blacksmith:
    scene
    show rahman normal
    rah "My friend, what you got for me today?"
    abd "Maybe later."
    rah "Alright."
    show rahman normal at right with move
    call screen shop(s = rahman_u)
    jump street


# Money lender
define mst = Character("Mostafa the money lender", color="#4ff", what_text_color="#dff")

label money_lender:
    scene
    show mostafa normal
    mst "...?"
    mst "No money unless you have something valuable?"
    mst "You don't look like having anything."
    mst "Get lost!"
    jump street

# Empty shop
label empty_shop:
    scene
    show mostafa normal
    mst "The rent is 4000 per month, do you want to rent?"
    mst "I can't afford it."
    mst "Get lost then!"
    jump street

# Karim
define kar = Character("Karim", color="#4ff", what_text_color="#dff")

default karim_u = unit(
    "Karim",
    "char/karim",

    3410,
    [
        (rice, 24),
        (bread, 15),
        (salt, 12),
        (saffron, 2),
        (crackers, 16),
        (bread, 15),
        (hashish, 3),
        (opium, 2),
    ],
    1.3,

    8,
    "Peasant",
    interests = ["hard drug"],
    reject = ["Weapon", "armor", "fuel", "lamp"]
    )
label karim:
    scene
    show karim normal
    kar "No hand outs!"
    abd "I didn't ask for any."
    kar "Just saying, what do you want?"
    show karim normal at right with move
    call screen shop(s = karim_u)
    jump street


label beggar:
    scene
    show beggar
    "Beggar" "Give me money."
    abd "Can't you ask nicely for once old man?"
    "Beggar" "Give me money."
    menu:
        "Here's 10 dinars..." if hero.cash > 9:
            abd "Here, take this 10 dinars."
            $ hero.paidcash(10)
            "Beggar" "Thank you, the God's blessing be upon you."
        "I don't have anything...":
            abd  "I don't have anything right now."
            "Beggar" "You're lying, go away."
            abd "I'm n..."
            "Beggar" "Go away!"
    jump street

label jamal:
    scene
    show jamal
    "Jamal" "Beat it!"
    hide jamal with dissolve
    jump street

label shepard:
    scene
    show shepard
    "..."
    hide shepard with dissolve
    jump street
