
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

define farmgirl = Character("Farm girl", color="#4ff", what_text_color="#dff")
label farm_girl:
    scene
    show farm_girl with dissolve
    farmgirl "Don't bother me."
    abd "Alright."
    jump farms

label village:
    "Not ready yet."
    jump farms
label orchards:
    "Not ready yet."
    jump farms