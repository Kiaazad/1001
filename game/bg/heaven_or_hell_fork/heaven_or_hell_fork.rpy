# Exits
default heaven_or_hell_fork_beduins_camp = pnco(
    "Beduins camp",
    None,
    (1274, 954),
    Jump('beduins_camp'),
    )
default heaven_or_hell_fork_heaven_oasis = pnco(
    "Heaven oasis",
    None,
    (1169, 549),
    Jump('heaven_oasis'),
    )
default heaven_or_hell_fork_old_tomb = pnco(
    "Old tomb",
    None,
    (231, 543),
    Jump('old_tomb'),
    )
label old_tomb:
    "not ready yet."
    jump heaven_or_hell_fork

# Map
default heaven_or_hell_fork_map = pncs(
    "Heaven or hell fork",
    [
        heaven_or_hell_fork_beduins_camp,
        heaven_or_hell_fork_heaven_oasis,
        heaven_or_hell_fork_old_tomb,
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




