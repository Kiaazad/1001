
default school_teacher_loc = pnco(
    "The teacher",
    "bg/school/teacher.webp",
    (1405, 664),
    Jump('school_teacher'),
    )

default school_agrabah_loc = pnco(
    "Agrabah",
    "bg/school/city.webp",
    (325, 1019),
    Jump('agrabah'),
    )
default school_map = pncs(
    "Agrabah",
    [
        school_teacher_loc,
        school_agrabah_loc,
    ], night = "bg/school/night.webp"
    )



image bg school = "bg/school/bg.webp"
label school:
    scene
    show bg school onlayer bg
    show screen pnc(hero, school_map)
    with dissolve
    pause
    jump school


default skin_scroll = item(
    _("Skin scroll"),
    _("A scroll made of goat skin."),
    "skin_scroll",
    1400,
    ["stationery"],
    )
default paper = item(
    _("Paper"),
    _("A blank sheet of paper."),
    "paper",
    100,
    ["stationery"],
    )
default black_ink = item(
    _("ink"),
    _("Black ink made of some black stuff."),
    "black_ink",
    800,
    ["stationery"],
    )


define tea = Character("Teacher", color="#4ff", what_text_color="#dff")

default teacher_u = unit(
    "Teacher",
    "char/teacher",

    2441,
    [
        (skin_scroll, 6),
        (paper, 22),
        (black_ink, 4),
    ],
    1.1,

    12,
    "Peasant",
    interests = ["book"],
    reject = ["drug", "Weapon", "armor"]
    )

default books_for_school = quest(
    _("Books for school"),
    [_("The school teacher needs books, Jafar's books are preferred.")],
    )
default arianas_homework = quest( 
    _("Ariana's homework'"),
    [_("The teacher wants you to deliver Ariana's homework to her every now and then.")],
    )
default arianas_notes = item(
    _("Ariana's homework"),
    _("A series of notes for Ariana."),
    "paper",
    0,
    ["unsellable"],
    )

label school_teacher:
    scene
    show teacher normal
    if not "first" in teacher_u.flags:
        tea "State your business!"
    else:
        tea "How can I help you?"
    menu:
        "I'm just looking around." if not "first" in teacher_u.flags:
            abd "Ermmm...{w=.5} I'm just looking around."
            tea "This is a place of learning. Please leave."
            $ teacher_u.affection -= 4
        "I need some books." if not "first" in teacher_u.flags:
            abd "I need some books."
            tea "Our library have suffered a great loss, I can't sell you any books right now."
            abd "What happened."
            tea "The guards confiscated all the books Jafar donated as the royal Vizier."
            abd "I see..."
            tea "Only a man of culture seeks books, do you have any books to donate?"
            tea "Or I can buy them from you if the price is fair."
            abd "Not really."
            tea "Alright, let me know if you've came across any."
            $ qlog.got(books_for_school)
            $ teacher_u.affection += 20
            $ teacher_u.add_flag("first")
        "Ariana said \"Hi\"." if qlog.has(ariana_said_hi) == "Active":
            abd "Ariana said \"Hi\"."
            $ ariana_said_hi.complete()
            tea "Oh, she did? How was she?"
            abd "She looked fine."
            "..."
            abd "I mean she was..."
            tea "I got it."
            tea "Would you say \"Hi,\" to her for me when you see her again?"
            abd "Is this going to become a back and forth thing?"
            tea "Sorry, I should be considerate of your time."
            tea "Here..."
            $ hero.gotcash(200)
            tea "Take this for your troubles."
            tea "Excuse me for a moment."
            hide teacher with dissolve
            pause 2
            show teacher normal with dissolve
            $ hero.got(arianas_notes)
            tea "Deliver this to her please."
            abd "That's lots of notes."
            tea "Yes, she's a brilliant student."
            tea "It's a shame she can't attend classes anymore."
            tea "These should enable her to further her education."
            tea "I would appreciate it if you help me with this task on a regular basis."
            $ qlog.got(arianas_homework)
            $ hero.add_flag("about a farm girl")
            abd "Sure."
            tea "Thank you, this means a lot to me."

        "I want to buy something.":
            "I want to buy something."
            tea "Alright."
            show teacher normal at right with move
            call screen shop(s = teacher_u)



    jump school