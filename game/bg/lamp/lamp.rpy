﻿
init offset = -1

## Navigation screen ###########################################################
transform lampoff(x,y):
    parallel:
        alpha 0 offset (0,0)
        ease .2 offset (x,y) alpha 1
    parallel:
        on idle:
            easein .2 alpha .6
        on hover:
            easein .2 alpha 1.0
        # on selected_idle:
        #     easein .2 additive .2
        # on selected_hover:
        #     easein .2 additive .3
        on insensitive:
            easein .2 alpha .2
# screen navigation(ii=0):
#     style_prefix "nav"
#     tag menu
#     add "#000"
#     button: 
#         add "bg/lamp/back.webp"
#         action Return()
#     button:
#         at lampoff(-350, 150)
#         add "bg/lamp/fight.webp"
#         action Return()
#     button:
#         at lampoff(350, 150)
#         add "bg/lamp/harem.webp"
#         action Return()
#     button:
#         at lampoff(0, 260)
#         add "bg/lamp/library.webp"
#         action Call("lamp_jafar")
#     button:
#         at lampoff(350, -150)
#         add "bg/lamp/quest.webp"
#         action Return()
#     button:
#         at lampoff(-350, -150)
#         add "bg/lamp/replay.webp"
#         action Return()
#     button:
#         at lampoff(0, -260)
#         add "bg/lamp/save.webp"
#         action ShowMenu("save")
#     button:
#         at lampoff(-600, 0)
#         add "bg/lamp/settings.webp"
#         action ShowMenu("preferences")
#     button:
#         at lampoff(600, 0)
#         add "bg/lamp/mm.webp"
#         action MainMenu()


# style nav_button:
#     background None
#     align (.5,.5)




init:
    default lamp_quest = pnco(
        "Quest room",
        "bg/lamp/quest.webp",
        (1272, 828),
        Jump('lamp_quest'),
        hidden = False, hoffset = (114,80),
        )

    default lamp_jafar = pnco(
        "Jafar's den",
        "bg/lamp/library.webp",
        (412, 225),
        Jump('lamp_jafar'),
        hidden = False, hoffset = (114,80),
        )

    default lamp_harem = pnco(
        "Jafar's harem",
        "bg/lamp/harem.webp",
        (724, 47),
        Jump('lamp_harem'),
        hidden = False, hoffset = (114,80),
        )

    default lamp_agrabah = pnco(
        "Back to Agrabah",
        "bg/lamp/back.webp",
        (103, 604),
        Jump('agrabah'),
        hidden = False, hoffset = (114,80),
        )

    default lamp_fight = pnco(
        "Fighting ground",
        "bg/lamp/fight.webp",
        (916, 476),
        Jump('lamp_fight'),
        hidden = False, hoffset = (114,80),
        )

    default lamp_save = pnco(
        "Jar room",
        "bg/lamp/save.webp",
        (1024, 234),
        ShowMenu("save"),
        hidden = False, hoffset = (114,80),
        )

    default lamp_settings = pnco(
        "The odd room",
        "bg/lamp/settings.webp",
        (600, 758),
        ShowMenu("preferences"),
        hidden = False, hoffset = (114,80),
        )

    default lamp_gate = pnco(
        "The gate",
        "bg/lamp/mm.webp",
        (1423, 533),
        MainMenu(),
        hidden = False, hoffset = (114,80),
        )

    default lamp_map = pncs(
        "Jafar's lamp",
        [
            lamp_jafar,
            lamp_harem,
            lamp_fight,

            lamp_quest,

            lamp_save,
            lamp_settings,
            lamp_gate,
            lamp_agrabah,
        ]
        )

image bg lamp = "#000"
label inside_lamp:
    scene
    show bg lamp onlayer bg
    show screen pnc(hero, lamp_map)
    pause
    jump inside_lamp

label lamp_quest:
    call screen quests
    jump inside_lamp

label lamp_fight:
    scene black
    menu:
        "Fight a dummy.":
            $ training_dummy.reset()
            call screen battle([training_dummy])
        "Fight demons.":
            python:
                d = random.randint(1,5)
                enemies = []
                loot = [
                    [None, 200],
                    [nuru_gel, 2],
                ]
                for i in range(d):
                    n = random.choice(all_demons)
                    l = main_fighter.level + random.randint(-3, 3)
                    enemies.append(fighter(n, l, "Demon"))
            call screen battle(enemies, loot)
    jump inside_lamp

default learn_pick_pocket = quest(
    _("Learn pick pocket"),
    [_("Jafar wants you to learn pick pocket from Ahmad.")]
)

default ring_recipe = item(
    _("Ring recipe"),
    _("A recipe for an odd looking copper ring. Jafar drawn and wrote it."),
    "ring_recipe",
    0,
    ["Finger", "jewelry", "unsellable"],
    )
default copper_ring = item(
    _("Copper ring"),
    _("Made according to jafar's instructions."),
    "copper_ring",
    1000,
    ["Finger", "jewelry", "unsellable"],
    )
default make_a_copper_ring = quest(
    _("Make a copper ring"),
    [_("Jafar wants a copper ring made.")],
    )
default find_a_big_quartz = quest(
    _("Find a big quartz"),
    [_("Jafar needs a fist size quartz.")],
    )
default jafar_said_hi = quest(
    _("Jafar said hi"),
    [_("Jafar wants you to say hi to Ariana's father..")],
    )

image bg jafars_lab = "bg/lamp/jafars_lab.webp"
label lamp_jafar:
    scene
    "{nw}"
    show bg jafars_lab
    show jaf normal
    menu:
        "Chit chat....":
            jaf "No time for chit chat."
        
        # gem stone chain
        "I've found a diamond." if qlog.has(a_diamond_to_sell) == "Active" and hero.has(quartz_bit):
            abd "I've found a diamond Jafar. I'm rich!"
            jaf "Oh? Let me see..."
            "..."
            jaf "It's not a diamond. It's a quartz."
            $ quartz_bit.name = "Quartz bit"
            abd "It's not? At least it's a precious gem right."
            $ quartz_bit.inf = "Not a diamond."
            $ quartz_bit.val = 20
            jaf "It worths pocket change."
            abd "Damn it."
            $ a_diamond_to_sell.complete()
            jaf "Where did you find it?"
            if "quarry" in a_diamond_to_sell.flags:
                abd "Mined it in the marble quarry."
            else:
                abd "Fought a sand warrior, it turned into sand and this was in it."
            jaf "I see..."
            abd "Should I throw it away?"
            jaf "Of course."
            jaf "It's another rock, under the sun and over time, it will break into sand."
            "..."
            jaf "Wait a minute!"
            abd "What?"
            jaf "Sand!"
            abd "Huh?"
            jaf "It's the same stuff as sands of time."
            "..."
            jaf "If we manage to grind it into the right size, we can create more sands of time."
            abd "So it's valuable?"
            jaf "Not to others! But to us, it is."
            "..."
            jaf "Collect these, I'll see what we can do with them."
            abd "Alright."
            jaf "And find a big one. There's something special I want to make with it."
            abd "How big."
            jaf "At least the size of your fist."
            $ qlog.got(find_a_big_quartz)
            $ marble_quarry_mine.act = Show(
                'do_work',
                time = 50,
                text = "Mining rocks...",
                loot = [
                    [marble, 80],
                    [quartz_bit, 10],
                    [big_quartz, 2],
                ]
                )
            if "quarry" in a_diamond_to_sell.flags:
                abd "Can I find one that big in the quarry?"
                jaf "That's where I would look for one."
            else:
                abd "Any idea where I can find one?"
                jaf "Mines or something. Figure it out, I have things to do."
            abd "Alright."
        "I've found the big gem." if qlog.has_line(find_a_big_quartz, "Jafar needs a fist size quartz.") and hero.has(big_quartz):
            abd "I've found the big gem Jafar."
            jaf "It's not a gem..."
            jaf "Hand it over."
            $ hero.drop(big_quartz, 1)
            abd "Alright."
            jaf "Go do something, I have some work to do. A day should do."
            abd "Alright."
            $ find_a_big_quartz.extend(_("Jafar said come back tomorrow."))
            $ timed_quest_extends.append([find_a_big_quartz, "Jafar should be done with the quartz.", 360])
        "Any news?" if qlog.has_line(find_a_big_quartz, "Jafar should be done with the quartz.") and qlog.has(find_a_big_quartz) == "Active":
            abd "Any news Jafar?"
            jaf "About what?"
            abd "The ge... Quartz."
            jaf "Ah yes, I've concocted a plan to save your hide from dying."
            abd "But I already have that."
            jaf "Not for long."
            jaf "I have a hunch that the powers to be are looking to take that away again."
            abd "Who?"
            jaf "Doesn't matter."
            jaf "Consider it a favor done for now."
            $ find_a_big_quartz.complete()
            abd "Alright."

        # Craft a ring chain
        "I've got the money." if hero.cash > 2000 and qlog.has(cash_in_hand) == "Active":
            abd "I've got the money."
            jaf "Excellent!"
            $ hero.got(ring_recipe, 1)
            jaf "take this to the jeweller in bazaar and tell him to make a copper ring as instructed."
            abd "Why not bronze?"
            jaf "Bronze is too shiny, nobody will steal a copper ring from you."
            abd "Ah, alright."
            $ cash_in_hand.complete()
            $ qlog.got(make_a_copper_ring)
            jaf "Is there anything else?"
            abd "No!"
            jaf "get going then."
            abd "Right!"
            jump inside_lamp
        "The ring is ready..." if qlog.has(make_a_copper_ring) == "Active" and hero.has(copper_ring):
            abd "The ring is ready."
            jaf "Excellent!"
            jaf "I have plans for it, don't lose it."
            abd "Alright."
            $ make_a_copper_ring.complete()

        # Book quest
        "I have some books" if qlog.has(books_for_jafar) and False:
            jaf "Bating, go away."

        # Planted evidence chain
        "About Hakim." if qlog.has(planted_evidence) == "Active" and planted_evidence.info[-1] in ["Talk to jafar and find a solution to Hakim's predicament.", "Rasoul wants you to plant one of Jafar's books in Hakim's shop."]:
            abd "There's a situation with hakim, Jafar."
            jaf "What's wrong?"
            abd "Rasoul is after him."
            jaf "How so?"
            abd "He gave me this book."
            $ hero.drop(the_free_lie_book, 1)
            jaf "It's one of my books."
            jaf "What doe it have to do with Hakim?"
            abd "Rasoul told me to hide it in Hakim's shop."
            jaf "Why? It's nothing out of ordinary to have one of my books."
            jaf "Lots of people have them."
            abd "Not anymore, they made your books illegal and collected them all in the barracks."
            jaf "I see..."
            jaf "They made it a crime and using that excuse to persecute the dissidents."
            "..."
            jaf "Those whom oppose them."
            abd "Aha! I see."
            abd "What should we do?"
            jaf "Let me think."
            "..."
            jaf "I know it, buy a bottle of wine and plant in in Hakim's shop."
            abd "With the book?"
            jaf "No the book stays here with me for the time being."
            abd "But Rasoul will throw me in jail when he doesn't find the book."
            jaf "Tell him that you've planted the book and a bottle of wine just in case Hakim finds the book and destroys it."
            abd "But he will still arrest Hakim for the wine."
            jaf "That's the outcome we're hopping for."
            abd "I don't get it."
            jaf "This way Rasoul gets to sink his teeth into Hakim by arresting him for the wine."
            jaf "But Hakim is a man of medicine, he can explain owning a bottle of wine and get himself out of this situation mostly unharmed."
            jaf "And you'll be off the hook since it seems you did what he told you."
            abd "I see."
            $ planted_evidence.extend(_("Plant a bottle of wine in Hakim's shop."))
            jaf "Now hurry back and save our friend."
            if hero.cash < 100:
                abd "Um..."
                jaf "What now?"
                abd "They took all of my money at the jail."
                jaf "Ask hakim, he will gladly chip in."
                $ planted_evidence.extend(_("Ask hakim for some money for the wine."))
            abd "Sure."
            jump inside_lamp

        # Pick pocket chain
        "I think I've got rubbed." if hero.pick_pocket_alert > 0 and not qlog.has(learn_pick_pocket):
            abd "I think I've got rubbed Jafar."
            jaf "Let me guess, Ahmad?"
            abd "I think so, how do you know?"
            jaf "Caught him for picking pockets long ago."
            abd "But he still has both hands!"
            jaf "Yes, I don't like cutting parts of people."
            jaf "And his skilled hands where more useful to me attached to his arms."
            jaf "I let him keep them, and in exchange he acquired some items for me."
            jaf "And his promise to find an honorable line of work of course."
            jaf "You should go back and talk to him soon."
            abd "Why? I'm sure he'll deny everything."
            jaf "You should learn what he does."
            jaf "It can be a pretty handy skill to have."
            jaf "Tell him you know about his deal with me, and you'll reward him handsomely for few lessons."
            abd "But rewarding needs money."
            jaf "Go get some, you're good at it."
            $ qlog.got(learn_pick_pocket)
            "..."
            jaf "Don't stand around, go!"
            abd "Alright."

        # To do list quest
        "I got the scroll." if qlog.has(my_to_do_list) == "Active" and hero.has(skin_scroll):
            abd "I got the scroll Jafar."
            jaf "Excellent!{w=0.2} Hold it up."
            show jaf magic
            pause 1
            $ hero.drop(skin_scroll, 1)
            $ hero.got(quest_log_item, 1)
            $ quest_log_ui_icon = True

            show jaf normal
            jaf "There."
            jaf "It keeps track of your tasks, now go do them."
            $ my_to_do_list.complete()
            abd "But...{w=.2}{nw}"
            jaf "Go figure it out.{w=.2} I can't explain everything to you."

        # An old friend quest
        "I've met an interesting farm girl." if "about a farm girl" in hero.flags:
            abd "I've met an interesting farm girl."
            jaf "Don't fool around chasing young girls."
            abd "It's not like that."
            abd "I'm just delivering her homework to her."
            jaf "An educated farm girl? That is interesting."
            abd "Her name is Ariana."
            jaf "Did you get her family name?"
            abd "No why?"
            jaf "I know somebody with a daughter named Ariana."
            jaf "But he lives in the city."
            abd "She mentioned moving from Agrabah to the village."
            jaf "Then it should be him."
            jaf "It is possible they've chased my supporter out of the city."
            jaf "You should seek him out, he can be a great help towards our end goal."
            abd "Alright, but what should I tell him?"
            jaf "Tell him: \"Jafar said hi\"."
            abd "And?"
            jaf "That's it."
            abd "Is saying \"hi,\" some code between rich people?"
            abd "She asked me to do something similar."
            jaf "Not a code, sending regards just shows we think and care about the other party."
            jaf "And often starts a conversation as if we have meet in person."
            $ qlog.got(jafar_said_hi)
            abd "I see..."
            jaf "Now get going."
            abd "Alright."
            python:
                try:
                    hero.flags.remove("about a farm girl")
                except:
                    pass
        "Ariana's father asked for your writing." if qlog.has(jafars_writing) == "Active" and not "Buy some paper and ink." in jafars_writing.info:
            abd "Ariana's father asked for your writing."
            jaf "The ever skeptical wants proof. How predictable."
            jaf "Go buy some paper and ink."
            "..."
            jaf "What are you waiting around for?"
            abd "Can't you use the ones you have here?"
            jaf "I rather avoid using what I've conjured."
            jaf "You don't want the not to evaporate into thin air as soon as you leave the lamp, do you?"
            abd "I..."
            abd "When you're right, you're right."
            abd "I'll go buy some then."
            $ jafars_writing.extend(_("Buy some paper and ink."))
        "Got the paper and ink." if qlog.has_line(jafars_writing, "Buy some paper and ink.") and hero.has(paper) and hero.has(black_ink):
            abd "Got the paper and ink."
            jaf "Excellent, hand them to me."
            $ hero.drop(black_ink, 1)
            $ hero.drop(paper, 1)
            abd "Sure."
            pause 6
            $ hero.got(jafars_writing_note)
            jaf "Here, Take this to him."
            abd "The girl won't let me talk to him directly."
            jaf "Hand it to her then."
            $ jafars_writing.extend(_("Give the note to Ariana."))
            abd "Alright."
        
        # rapier chain
        "I need a rapier." if qlog.has_line(seeking_painful, "Ask Jafar."):
            abd "I need a rapier"
            jaf "Where did you learn that."
            abd "The viking at heaven oasis."
            jaf "One of the European swords, They're not crafted around here."
            abd "I know, I need instructions to craft one."
            jaf "You know the drill, get me some ink and paper."
            $ seeking_painful.extend("Bring jafar some ink and paper.")
            abd "Alright."
        "Got the ink and paper." if qlog.has_line(seeking_painful, "Bring jafar some ink and paper.") and hero.has(paper) and hero.has(black_ink):
            $ hero.drop(black_ink, 1)
            $ hero.drop(paper, 1)
            abd "Got the ink and paper."
            jaf "Alright."
            "..."
            $ hero.got(rapier_instructions)
            jaf "Here you go."
            $ seeking_painful.extend("Take the instructions to Rahman.")
            abd "Thank you."

    jump inside_lamp


default quest_log_item = item(
    _("Quest log"),
    _("This allows viewing your quests anywhere."),
    "quest_log_item",
    0,
    ["unsellable"],
    )
default jafars_writing_note = item(
    _("Jafar's writing"),
    _("The note that jafar wrote for Ariana's father."),
    "paper",
    0,
    ["unsellable"],
    )
default rapier_instructions = item(
    _("Rapier instructions"),
    _("Materials, instructions and sketches."),
    "paper",
    0,
    ["unsellable"],
    )
