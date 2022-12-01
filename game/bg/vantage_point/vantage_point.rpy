
default vantage_point_rich = pnco(
    "Back to town",
    "bg/no_image.png",
    (1520, 947),
    Jump('rich'),
    hidden = False, hoffset = (100,-60),
    )
default vantage_point_cg = pnco(
    "Peep",
    "bg/no_image.png",
    (1393, 633),
    Jump('vantage_point_cg'),
    hidden = True, hoffset = (100,-60),
    )

default vantage_point_map = pncs(
    "Vantage point",
    [
        vantage_point_rich,
        vantage_point_cg,
    ], night = "bg/vantage_point/night.webp"
    )

image bg vantage_point = "bg/vantage_point/bg.webp"
label vantage_point:
    scene
    show bg vantage_point onlayer bg
    show screen pnc(hero, vantage_point_map)
    with dissolve
    pause
    jump vantage_point

image spyglass old = "cg/vantage_point/old_spyglass.webp"
image cg jasmine_on_balcony = "cg/vantage_point/jasmine_on_balcony.webp"

label vantage_point_cg:
    if hero.has(old_spyglass):
        scene
        show spyglass old with dissolve
        show cg jasmine_on_balcony behind spyglass with dissolve
        abd "Is that princess Jasmine?"
    elif hero.has(new_spyglass):
        scene
        # show spyglass old with dissolve
        show cg jasmine_on_balcony behind spyglass with dissolve
        abd "Princess Jasmine."
        abd "Naughty naughtily girl."
    else:
        abd "Can't see much"
    jump vantage_point
