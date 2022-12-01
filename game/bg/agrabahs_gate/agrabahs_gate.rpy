# Exits
default agrabahs_gate_roc_pass = pnco(
    "Roc pass",
    "bg/agrabahs_gate/roc pass.webp",
    (1600, 576),
    Jump('roc_pass'),
    )
default agrabahs_gate_agrabah = pnco(
    "Agrabah",
    "bg/agrabahs_gate/agrabah.webp",
    (720, 880),
    Jump('street'),
    )
default agrabahs_gate_beduins_camp = pnco(
    "Beduins camp",
    "bg/no_image.png",
    (932, 501),
    Jump('beduins_camp'),
    )
default agrabahs_gate_farms = pnco(
    "Farms",
    "bg/no_image.png",
    (265, 589),
    Jump('farms'),
    )


# Random
default agrabahs_gate_nasim = pnco(
    "Trap",
    "bg/agrabahs_gate/nasim.webp",
    (1057, 628),
    Jump('agrabahs_gate_nasim'),
    shifts = [[220,270]],
    )
define nasim = Character("Nasim", color="#4ff", what_text_color="#dff")

label agrabahs_gate_nasim:
    scene
    show nasim normal dark
    nasim "Hey there strong man!"
    abd "Huh? hey..."
    nasim "Come on daddyo, why the hesitance? I won't bite..."
    nasim "Unless you want me to."
    abd "Ummm... I...{w=.2}{nw}"
    $ msg.msg("You've received a piece of paper.")
    nasim "Here."
    abd "What's this?"
    nasim "An invitation."
    abd "Invitation? To what?"
    nasim "My lady is camping nearby, and you're invited to meet her."
    abd "Where?"
    nasim "It's written on the invitation. The southern trade route."
    abd "Ummm..."
    abd "Who's your lady?"
    nasim "That's a secret."
    abd "Sounds suspicious... Are you going to lure me there and jump me?"
    nasim "I can jump you here if you want?"
    abd "I meant mug me."
    nasim "What's the fun in that?"
    "..."
    nasim "Listen, I love to stay and chat you up, but I have to bounce before some guard shows up."
    nasim "Come over tomorrow if you want to meet my lady. She has something that you'll definitely want."
    abd "What is it that I want?"
    nasim "Me please..."
    "..."
    nasim "No rush big boy."
    nasim "See you tomorrow!"
    hide nasim with dissolve
    $ agrabahs_gate_nasim.hidden = True
    "..."
    jump agrabahs_gate

# Fights
image black scorpion idle:
    "black scorpion idle_1"
    .1
    "black scorpion idle_2"
    .1
    "black scorpion idle_3"
    .1
    repeat
default agrabahs_gate_black_scorpion = pnco(
    "Black scorpion",
    "bg/agrabahs_gate/black_scorpion.webp",
    (182, 660),
    Jump('agrabahs_gate_black_scorpion'),
    )
label agrabahs_gate_black_scorpion:
    $ e = fighter("Black scorpion", random.randint(2,4), "Beast")
    $ loot = [
        [scorpion_tail, 100],
        [thorns, 14],
        [stick, 4],
        [string, 2],
    ]
    call screen battle([e], loot)
    if _return == "escaped":
        jump street
    jump agrabahs_gate



default agrabahs_gate_map = pncs(
    "Agrabah's gate",
    [
        agrabahs_gate_agrabah,
        agrabahs_gate_roc_pass,
        agrabahs_gate_farms,
        agrabahs_gate_beduins_camp,
        agrabahs_gate_black_scorpion,
        agrabahs_gate_nasim,
    ], night = "bg/agrabahs_gate/night.webp"
    )
"""
Background design notes:
This background is the desert immediately outside of the city's gate, it can be few pathways towards different places. 3 should suffice.
"""
image bg desert = "bg/agrabahs_gate/bg.webp"
label agrabahs_gate:
    if not agrabahs_gate_map in all_places:
        $ all_places.append(agrabahs_gate_map)
    scene
    show bg desert onlayer bg
    show screen pnc(hero, agrabahs_gate_map)
    with dissolve
    pause
    jump agrabahs_gate




