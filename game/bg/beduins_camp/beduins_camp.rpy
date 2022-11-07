
# Exists
default beduins_camp_agrabahs_gate = pnco(
    "Agrabah's gate",
    None,
    (980, 1009),
    Jump('agrabahs_gate'),
    hidden = False, hoffset = (83,-40),
    )
default beduins_old_gate = pnco(
    "Old gate",
    None,
    (1734, 704),
    Jump('old_gate'),
    )
default beduins_heaven_or_hell_fork = pnco(
    "Heaven or hell fork",
    None,
    (91, 714),
    Jump('heaven_or_hell_fork'),
    )
# Fights
image sand warrior idle:
    "sand warrior idle_1"
    .1
    "sand warrior idle_2"
    .1
    "sand warrior idle_3"
    .1
    repeat

default beduins_camp_sand_warrior = pnco(
    "Sand warrior",
    "bg/beduins_camp/sand_warrior.webp",
    (1240, 660),
    Jump('beduins_camp_sand_warrior'),
    aggressive = True,
    )
default a_diamond_to_sell = quest(
    _("A diamond to sell"),
    [_("This might be a diamond, I must show it to the jeweler, or better Jafar.")],
    )
label beduins_camp_sand_warrior:
    $ e = fighter("Sand warrior", renpy.random.randint(4, 8), "Beast")
    $ loot = [
        [quartz_bit, 30],
        [stick, 5],
        [rope, 5],
        [None, 50],
    ]
    call screen battle([e], loot)
    if _return == "escaped":
        jump agrabahs_gate
    if hero.has(quartz_bit) and not qlog.has(a_diamond_to_sell):
        abd "A gem stone?"
        $ qlog.got(a_diamond_to_sell)
        $ a_diamond_to_sell.flags.append("camp")
    jump beduins_camp

default beduins_camp_loc = pncs(
    "Beduins camp",
    [
        beduins_camp_agrabahs_gate,
        beduins_old_gate,
        beduins_heaven_or_hell_fork,
        beduins_camp_sand_warrior,
    ], night = "bg/beduins_camp/night.webp"
    )

image bg beduins_camp = "bg/beduins_camp/bg.webp"
label beduins_camp:
    if not beduins_camp_loc in all_places:
        $ all_places.append(beduins_camp_loc)
    scene
    show bg beduins_camp onlayer bg
    show screen pnc(hero, beduins_camp_loc)
    with dissolve
    pause
    jump beduins_camp

