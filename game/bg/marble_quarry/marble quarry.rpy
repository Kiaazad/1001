# Exists
default marble_quarry_watch_tower = pnco(
    "The watch tower",
    None,
    (121, 652),
    Jump('watch_tower'),
    )
default marble_quarry_roc_pass = pnco(
    "Roc pass",
    None,
    (1100, 990),
    Jump('roc_pass'),
    )

default marble_quarry_map = pncs(
    "Marble quarry",
    [
        marble_quarry_watch_tower,
        marble_quarry_roc_pass,
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
