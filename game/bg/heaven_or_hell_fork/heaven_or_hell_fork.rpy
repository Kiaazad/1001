# Exits
default heaven_or_hell_fork_beduins_camp = pnco(
    "Beduins camp",
    "bg/no_image.png",
    (1274, 954),
    Jump('beduins_camp'),
    )
default heaven_or_hell_fork_heaven_oasis = pnco(
    "Heaven oasis",
    "bg/no_image.png",
    (1217, 509),
    Jump('heaven_oasis'),
    )
default heaven_or_hell_fork_old_tomb = pnco(
    "Old tomb",
    "bg/no_image.png",
    (443, 543),
    Jump('old_tomb'),
    )
label old_tomb:
    "not ready yet."
    jump heaven_or_hell_fork

# fights
image tiger scorpion idle:
    "tiger_scorpion_idle_1"
    .1
    "tiger_scorpion_idle_2"
    .1
    "tiger_scorpion_idle_3"
    .1
    repeat

default heaven_or_hell_fork_scorpions = pnco(
    "Tiger scorpions",
    "bg/heaven_or_hell_fork/scorpions.png",
    (147 , 683),
    Jump('heaven_or_hell_fork_scorpions'),
    aggressive = False,
    )
label heaven_or_hell_fork_scorpions:
    python:
        e = []
        for i in range(random.randint(1,5)):
            e.append(fighter("Tiger scorpion", random.randint(6,9), "Beast"))
        loot = [
            [scorpion_tail, 100],
            [thorns, 14],
            [stick, 4],
            [string, 2],
        ]
    call screen battle(e, loot)
    if _return == "escaped":
        jump heaven_oasis
    jump heaven_or_hell_fork

image branch demon idle:
    "branch_demon_idle_1"
    .1
    "branch_demon_idle_2"
    .1
    "branch_demon_idle_3"
    .1
    repeat
default heaven_or_hell_branch_demon = pnco(
    "Demon branch",
    "bg/heaven_or_hell_fork/demon_branch.webp",
    (669 , 617),
    Jump('heaven_or_hell_branch_demon'),
    aggressive = False,
    )

label heaven_or_hell_branch_demon:
    python:
        e = fighter("Branch demon", random.randint(6,9), "Demon")
        loot = [
            # [scorpion_tail, 100],
            [thorns, 14],
            [stick, 4],
            [string, 2],
        ]
    call screen battle([e], loot)
    if _return == "escaped":
        jump heaven_oasis
    jump heaven_or_hell_fork
    


# Map
default heaven_or_hell_fork_map = pncs(
    "Heaven or hell fork",
    [
        heaven_or_hell_fork_beduins_camp,
        heaven_or_hell_fork_heaven_oasis,
        heaven_or_hell_fork_old_tomb,
        heaven_or_hell_fork_scorpions,
        heaven_or_hell_branch_demon,
    ], night = "bg/heaven_or_hell_fork/night.webp"
    )
"""
Background design notes:
A fork in the road, the thirsty travelers that choose wrong can end up dead instead of the Heaven oasis.
"""
image bg heaven_or_hell_fork = "bg/heaven_or_hell_fork/bg.webp"
label heaven_or_hell_fork:
    if not heaven_or_hell_fork_map in all_places:
        $ all_places.append(heaven_or_hell_fork_map)
    scene
    show bg heaven_or_hell_fork onlayer bg
    show screen pnc(hero, heaven_or_hell_fork_map)
    with dissolve
    pause
    jump heaven_or_hell_fork




