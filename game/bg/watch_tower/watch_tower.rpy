# exists
default watch_tower_marble_quarry = pnco(
    "Marble quarry",
    None,
    (1667, 743),
    Jump('marble_quarry'),
    )
default watch_tower_old_gate = pnco(
    "Old gate",
    None,
    (888, 1020),
    Jump('old_gate'),
    )

# items
default watch_tower_0 = pnco(
    "thorns",
    "bg/roc_pass/01.webp",
    (188, 598),
    items = [[thorns, 1]],
    regen = 10,
    )
default watch_tower_1 = pnco(
    "thorns",
    "bg/roc_pass/02.webp",
    (1713, 559),
    items = [[thorns, 1]],
    regen = 10,
    )
default watch_tower_2 = pnco(
    "thorns",
    "bg/roc_pass/03.webp",
    (173, 842),
    items = [[thorns, 1]],
    regen = 10,
    )
default watch_tower_3 = pnco(
    "thorns",
    "bg/roc_pass/04.webp",
    (411, 729),
    items = [[thorns, 1]],
    regen = 10,
    )


# Fights

default watch_tower_ogre = pnco(
    "thorns",
    "bg/watch_tower/ogre.webp",
    (182, 660),
    Jump('watch_tower_ogre'),
    aggressive = True,
    )
label watch_tower_ogre:
    "The fight system is being reworked to fit the first person view."
    jump watch_tower



default watch_tower_loc = pncs("The watch tower",
    [
        watch_tower_old_gate,
        watch_tower_marble_quarry,

        watch_tower_0,
        watch_tower_1,
        watch_tower_2,
        watch_tower_3,

        watch_tower_ogre,

    ], night = "bg/watch_tower/night.webp"

    )

image bg watch_tower = "bg/watch_tower/bg.webp"
label watch_tower:
    if not watch_tower_loc in all_places:
        $ all_places.append(watch_tower_loc)
    scene 
    show bg watch_tower onlayer bg
    show screen pnc(hero, watch_tower_loc)
    with dissolve
    pause
    jump watch_tower
