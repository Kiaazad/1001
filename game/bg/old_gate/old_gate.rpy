# Exits
default old_gate_beduins_camp = pnco(
    "Beduins camp",
    "bg/no_image.png",
    (1500, 943),
    Jump('beduins_camp'),
    )
default old_gate_watch_tower = pnco(
    "The watch tower",
    "bg/no_image.png",
    (1200, 676),
    Jump('watch_tower'),
    )
default old_gate_southern_trade_route = pnco(
    "Southern trade route",
    "bg/no_image.png",
    (124, 714),
    Jump('southern_trade_route'),
    )
label southern_trade_route:
    "not ready yet."
    jump old_gate

# fights

image robber idle:
    "robber_idle_1"
    .1
    "robber_idle_2"
    .1
    "robber_idle_3"
    .1
    repeat
default old_gate_robbers = pnco(
    "Robbers",
    "bg/old_gate/robbers.webp",
    (504, 735),
    Jump('old_gate_robbers'),
    aggressive = True,
    )

label old_gate_robbers:
    "robber" "Empty your pockets before I cut you down.{w=.2}{nw}"
    $ e = fighter("Robber", random.randint(4, 8), "Peasant")
    $ e1 = fighter("Robber", random.randint(4, 8), "Peasant")
    $ loot = [
        # [quartz_bit, 30],
        # [stick, 5],
        [rope, 5],
        [None, 50],
    ]
    call screen battle([e, e1], loot)
    if _return == "escaped":
        jump beduins_camp
    jump old_gate


# Map
default old_gate_map = pncs(
    "Old gate",
    [
        old_gate_beduins_camp,
        old_gate_watch_tower,
        old_gate_southern_trade_route,
        old_gate_robbers,
    ], night = "bg/old_gate/night.webp"
    )
"""
Background design notes:
The remains of an old gate in the middle of desert. It was the entrance of the old city that's under sand now.
"""
image bg old_gate = "bg/old_gate/bg.webp"
label old_gate:
    if not old_gate_map in all_places:
        $ all_places.append(old_gate_map)
    scene
    show bg old_gate onlayer bg
    show screen pnc(hero, old_gate_map)
    with dissolve
    pause
    jump old_gate




