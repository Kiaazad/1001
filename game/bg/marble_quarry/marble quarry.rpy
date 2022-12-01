# Exists
default marble_quarry_watch_tower = pnco(
    "The watch tower",
    "bg/no_image.png",
    (121, 652),
    Jump('watch_tower'),
    )
default marble_quarry_roc_pass = pnco(
    "Roc pass",
    "bg/no_image.png",
    (1100, 900),
    Jump('roc_pass'),
    )
default marble_quarry_mine = pnco(
    "Mine rocks",
    "bg/no_image.png",
    (1226, 826),
    Show(
        'do_work',
        time = 50,
        text = "Mining rocks...",
        loot = [
            [marble, 80],
            [quartz_bit, 10],
        ]
        ),
    )

default marble_quarry_map = pncs(
    "Marble quarry",
    [
        marble_quarry_watch_tower,
        marble_quarry_roc_pass,
        marble_quarry_mine,
    ], night = "bg/marble_quarry/night.webp"
    )
image bg marble_quarry = "bg/marble_quarry/bg.webp"
label marble_quarry:
    scene 
    show bg marble_quarry onlayer bg
    show screen pnc(hero, marble_quarry_map)
    with dissolve
    pause
    jump marble_quarry

# item singing sand
label found_gems:
    abd "A gem stone?"
    $ qlog.got(a_diamond_to_sell)
    $ quartz_bit.quest = None
    $ a_diamond_to_sell.flags.append("quarry")
    return