# exists
default serpent_nest_watch_tower = pnco(
    "Watch tower",
    None,
    (947, 989),
    Jump('watch_tower'),
    )
default serpent_queen = pnco(
    "Serpent queen",
    None,
    (845, 840),
    Jump('serpent_queen'),
    )

define s_slave = Character("Serpent queen", color="#4ff", what_text_color="#dff")
default snake_slave = pnco(
    "Snake slave",
    None,
    (400, 680),
    Jump('snake_slave'),
    )
label snake_slave:
    show snake_slave with dissolve
    s_slave "I'm at your service master."
    menu:
        "Let's go.":
            abd "Let's go."
            s_slave "Where to master."
            abd "Out of here."
            s_slave "I'm sorry master, I'm not allowed to leave the nest."
            abd "You belong to me!"
            s_slave "I am, but it's not up to me to decide."
            $ hero.add_flag("slave's day out")
        "Bend over.":
            abd "Bend over."
            s_slave "Yes master."
            hide snake_slave with dissolve
            pause 1
            show snake_slave_sex with dissolve
            abd "Huh?"
            s_slave "Something wrong master?"
            abd "I can't move."
            s_slave "Maybe today isn't your day."
            abd "That's not it, I have a raging boner inside you."
            s_slave "Maybe I'm not ready yet?"
            abd "That must be it."
            abd "We will try this later."
            hide snake_slave_sex with dissolve
            pause 1
            show snake_slave with dissolve
            s_slave "As you wish master."
            $ hero.add_flag("broken slave")
    jump serpent_nest


default kill_some_cobras = quest( 
    _("Kill some cobras"),
    [_("The serpent queen wants you to kill some serpent and bring her the carcases.")],
    )
default serpent_queen_u = unit(
    "Serpent queen",
    "char/viking",

    3410,
    [
    ],
    1.2,

    28,
    "Beast",
    interests = [],
    reject = ["lamp"]
    )
define s_queen = Character("Serpent queen", color="#4ff", what_text_color="#dff")
label serpent_queen:
    show serpent_queen
    if not "First" in serpent_queen_u.flags:
        s_queen "A sssssstrong man. I ssssee."
        s_queen "Jusssst the thing I need."
        abd "I assume you're in charge around here. Right."
        s_queen "Yessss."
        abd "What's wrong with your guard, he just attacked me when I tried to talk to him."
        s_queen "He is tassssked to tessst vissssitor'sss ssstrength."
        abd "Why?"
        s_queen "To ssseek a sssuitable sssssuitter."
        abd "But..."
        s_queen "Hushhhh..."
        s_queen "I have a favor to ask."
        abd "Ummm. sure?"
        s_queen "There are ccccertain ssserpentsss I want you to kill."
        abd "Killing your own kind? isn't that..."
        s_queen "Hushhhhh..."
        s_queen "My kind yessss, but not my keen."
        s_queen "I only care about my own brood."
        s_queen "And I don't appriciate competition."
        $ qlog.got(kill_some_cobras)
        abd "Alright, where and who?"
        s_queen "Cobrasss in ssssnake'sss passss. Kill assss many assss you can and bring me the corpes."
        s_queen "I Will reward you with a sssizable keepssssake."
        abd "Alright. Can I leave now?"
        s_queen "Sssssure."
        $ serpent_queen_u.add_flag("First")
    else:
        s_queen "Sssspeak to me."
        $ dead_snakes_count = hero.has(dead_snake)
        menu:
            "Why can't I take out my slave?" if "slave's day out" in hero.flags:
                abd "Why can't I take out my slave?"
                s_queen "She's not ready yet!"
                abd "When she'll be ready?"
                s_queen "Sssssoon."
                abd "Alright."
            "My slave is broken!" if "broken slave" in hero.flags:
                abd "My slave is broken."
                s_queen "And it can't be your fault at all?"
                abd "How can it be my fault?"
                s_queen "Let'sss not start pointing fingerssss."
                s_queen "You're dissssssmissssed."

            "I have nothing":
                s_queen "Go, bring me waht I crave."
            "I've brought [dead_snakes_count] of them." if dead_snakes_count:
                abd "I've brought [dead_snakes_count] of them."
                s_queen "Exssssselent. Hand them to me."
                $ hero.drop(dead_snake, dead_snakes_count)
                pause .2
                $ payment = (dead_snake.val*2)*dead_snakes_count
                $ serpent_queen_u.affection += dead_snakes_count
                s_queen "Her'sss your reward."
                s_queen "Now go and hunt more."
            "How about my reward?" if serpent_queen_u.affection > 20 and not "got snake slave" in hero.flags:
                abd "How about my reward?"
                s_queen "You have sssserved me right."
                s_queen "I besssstow upon you a sssservant."
                s_queen "She will ssserve you when you're in my viccccinity."
                $ hero.add_flag("got snake slave")
                $ serpent_nest_loc.add(snake_slave)
    jump serpent_nest

# items



# Fights




default serpent_nest_loc = pncs("The serpent nest",
    [
        serpent_nest_watch_tower,
        serpent_queen,

    ], #night = "bg/watch_tower/night.webp"

    )


image bg serpent_nest = "bg/serpent_nest/bg.webp"
label serpent_nest:
    if not serpent_nest_loc in all_places:
        $ all_places.append(serpent_nest_loc)
    scene 
    show bg serpent_nest onlayer bg
    show screen pnc(hero, serpent_nest_loc)
    with dissolve
    pause
    jump serpent_nest
