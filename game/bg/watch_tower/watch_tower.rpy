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
image cerpenger guard idle:
    "cerpenger_idle_1"
    .1
    "cerpenger_idle_2"
    .1
    "cerpenger_idle_3"
    .1
    repeat
default cerpenger = pnco(
    "Cerpenger guard",
    "bg/watch_tower/cerpenger.webp",
    (182, 600),
    Jump('cerpenger'),
    aggressive = False,
    )
default serpent_nest = pnco(
    "Snake nest",
    "bg/watch_tower/serpent_nest.webp",
    (185, 698),
    Jump('serpent_nest'),
    )

default cerpenger_guard = fighter("Cerpenger guard", 9, "Beast")
label cerpenger:
    "Cerpenger" "Hssss..."
    $ loot = [
        # [quartz_bit, 30],
        [stick, 5],
        [rope, 5],
        [None, 50],
    ]
    call screen battle([cerpenger_guard], loot)
    if _return == "escaped":
        jump marble_quarry
    if _return == "won":
        $ watch_tower_loc.remove(cerpenger)
        $ watch_tower_loc.add(serpent_nest)
    jump watch_tower




default watch_tower_loc = pncs("The watch tower",
    [
        watch_tower_old_gate,
        watch_tower_marble_quarry,

        watch_tower_0,
        watch_tower_1,
        watch_tower_2,
        watch_tower_3,

        cerpenger,

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
