# Exists

default snake_pass_roc_pass = pnco(
    "Roc pass",
    None,
    (882, 960),
    Jump('roc_pass'),
    hidden = True
    )
# Items
default des_1_1 = pnco(
    "Dried Tree",
    "bg/snakes_pass/01.webp",
    (1357, 596),
    hits = 10,
    items = [[wood, 7]],
    tools = [axe, saw],
    )
default des_1_2 = pnco(
    "thorns",
    "bg/snakes_pass/02.webp",
    (578, 725),
    items = [[thorns, 1]],
    regen = 10,
    )
default des_1_3 = pnco(
    "thorns",
    "bg/snakes_pass/03.webp",
    (1700, 900),
    items = [[thorns, 1]],
    regen = 10,
    )
default des_1_4 = pnco(
    "thorns",
    "bg/snakes_pass/04.webp",
    (961, 633),
    items = [[thorns, 1]],
    regen = 10,
    )
default des_1_5 = pnco(
    "thorns",
    "bg/snakes_pass/05.webp",
    (342, 867),
    items = [[thorns, 1]],
    regen = 10,
    )


# Fights
image cobra idle:
    "cobra idle_1"
    .1
    "cobra idle_2"
    .1
    "cobra idle_3"
    .1
    repeat

default snakes_pass_snake = pnco(
    "Snake",
    "bg/snakes_pass/snake.webp",
    (434, 653),
    Jump('snakes_pass_snake'),
    aggressive = True,
    )
label snakes_pass_snake:
    $ e = fighter("Cobra", renpy.random.randint(4, 8), "Beast")
    call screen battle([e])
    jump snakes_pass

default snake_pass_map = pncs("Snake's pass",
    [
        snake_pass_roc_pass,
        des_1_1,
        des_1_2,
        des_1_3,
        des_1_4,
        des_1_5,
        snakes_pass_snake,
    ], night = "bg/snakes_pass/night.webp"
    )
image bg snakes_pass = "bg/snakes_pass/bg.webp"
label snakes_pass:
    scene
    show bg snakes_pass onlayer bg
    show screen pnc(abdul, snake_pass_map)
    pause
    jump snakes_pass


label desert_1:
    if not snake_pass_map in all_places:
        $ all_places.append(snake_pass_map)
    scene
    show bg snakes_pass onlayer bg
    show screen pnc(abdul, snake_pass_map)
    with dissolve

    abd "It's unusually hot today."
    "..."
    window hide
    show screen mirage_1 with dissolve
label desert_1_loop:
    pause
    jump desert_1_loop

transform mirage_t(a, t =1):
    ease t alpha a
transform delayed(p):
    alpha 0
    pause p
    alpha 1
transform fade_to_screen:
    alpha .2 zoom .01
    ease 3 zoom 100 alpha 0
screen mirage_1:
    style_prefix "mirage_1"
    default alph = 0
    default intervals = 1
    default initial = 0
    if intervals < 20:
        timer .01 action SetScreenVariable("initial", 1)
        timer 2 repeat True action SetScreenVariable("alph", .1), SetScreenVariable("intervals", intervals+1)
        timer intervals*.1 repeat True action SetScreenVariable("alph", 0)
    else:
        timer .01 action Jump("desert_1_conv")
    if intervals == 5:
        text "Abdul" at fade_to_screen
    elif intervals == 10:
        text "Abdul" at fade_to_screen
    elif intervals == 15:
        text "Come to me" at fade_to_screen
    frame:
        background "#000"
        at mirage_t(float(intervals)/20, initial)
    frame:
        background None align .5,1.0 padding 0,0
        at delayed(1)
        add "jasmine seducing" at mirage_t(alph, initial)
style mirage_1_text is zero

label desert_1_conv:
    scene black with dissolve
    hide screen collect
    hide screen mirage_1
    show jasmine seducing at center with Dissolve(3)
    jas "Abdul..."
    abd "Yes?"
    jas "Come to me, Abdul."
    abd "Yes, your highness."
    jas "Abdul, I need your help."
    abd "What can I do for you, my princess?"
    jas "Agrabah is in trouble."
    abd "I will give my life for my city. What do you need from me?"
    jas "I need your seed, Abdul."
    abd "My seed?"
    jas "I need you to honor me with an heir."
    abd "With...?"
    jas "I need you to impregnate me, Abdul. Right here, Right now."
    abd "Are you..."
    abd "If you insist, your highness."


# ---------- CG

default jasmine_dream_veil = cg_obj(
    _("Veil"),
    "cg/jasmine dream/veil.webp",
    "veil",
    5,10,
    type = "item"
    )
default jasmine_dream_leash = cg_obj(
    _("Leash"),
    "cg/jasmine dream/leash.webp",
    "leash",
    10,5,
    type = "item"
    )

default jasmine_dream_shocked = cg_obj(
    _("Shocked"),
    "cg/jasmine dream/shocked.webp",
    "shocked",
    type = "expression"
    )
default jasmine_dream_adore = cg_obj(
    _("Adore"),
    "cg/jasmine dream/adore.webp",
    "adore",
    type = "expression"
    )
default jasmine_dream_angry = cg_obj(
    _("Angry"),
    "cg/jasmine dream/angry.webp",
    "angry",
    type = "expression"
    )
default jasmine_dream_default = cg_obj(
    _("Default"),
    "cg/jasmine dream/neutral.webp",
    "default",
    type = "expression"
    )


default jasmine_dream_scene1_fx = cg_obj(
    _("Scene1_fx"),
    "cg/jasmine dream/sex1.webp",
    "scene1_fx",
    0,0,2,
    type = "motion"
    )
default jasmine_dream_scene2_fx = cg_obj(
    _("Scene2_fx"),
    "cg/jasmine dream/sex2.webp",
    "scene2_fx",
    0,0,4,
    type = "motion"
    )
default jasmine_dream_scene3_fx = cg_obj(
    _("Scene3_fx"),
    "cg/jasmine dream/sex3.webp",
    "scene3_fx",
    0,0,8,
    type = "motion"
    )

image jasmine_dream_l2d = Live2D("cg/jasmine dream/l2d/jassmine_ride_model.model3.json", loop=True,
    nonexclusive= ["veil","leash", "shocked", "adore", "angry", "default"],
    # update_function=i_love_you_parasite,
    )


default jasmine_dream_cg = l2dcg(
    jasmine,
    [
        jasmine_dream_scene1_fx,
        jasmine_dream_scene2_fx,
        jasmine_dream_scene3_fx,

        jasmine_dream_shocked,
        jasmine_dream_adore,
        jasmine_dream_angry,

        jasmine_dream_veil,
        jasmine_dream_leash,

    ], "jasmine_dream_l2d"
    )


label desert_1_dream:
    scene black with dissolve

    show screen cgscr(jasmine_dream_cg)
    pause

    scene
    show bg snakes_pass onlayer bg
    show screen pnc(abdul, snake_pass_map)
    with dissolve
    abd "Woah..."
    abd "That was weird."
    abd "I need to got to the city before I die from heat."

    $ roc_pass_snakes_pass.hidden = False
    $ snake_pass_roc_pass.hidden = False
    $ roc_pass_marble_quarry.hidden = False

    jump street
