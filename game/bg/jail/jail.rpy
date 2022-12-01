default jail_barracks = pnco(
    "Barracks",
    "bg/no_image.png",
    (924, 929),
    Jump('barracks'),
    )

default jail_books = pnco(
    "Books",
    "bg/no_image.png",
    (236, 839),
    Jump('jail_books'),
    )

default jail_qasim = pnco(
    "Qasim",
    "bg/no_image.png",
    (1431, 697),
    Jump('jail_qasim'),
    )

default jail_cells = pnco(
    "Cells",
    "bg/no_image.png",
    (689, 669),
    Jump('jail_cells'),
    )

default jail_map = pncs(
    "Jail",
    [
        jail_barracks,
        jail_books,
        jail_qasim,
        jail_cells,

    ]
    )

"""
Background design notes:
There are two doors, one goes to the jail cells and another to Qasim's room.
Qasim's room can't be entered and doesn't need a background 

Cells:
(I Imagined it as a round basement with a series of indentations in the wall that are separated from the middle with bars)
the middle hosts some torture devices and a set of stairs to the entrance.
"""
image bg jail = "bg/jail/bg.webp"
label jail:
    scene
    show bg jail onlayer bg
    show screen pnc(hero, jail_map)
    pause
    jump jail

label jail_books:
    scene
    show qasim normal with dissolve
    qasim "Don't touch those."
    jump jail

label jail_qasim:
    scene
    show qasim normal with dissolve
    qasim "Don't touch me."
    jump jail

label jail_cells:
    scene
    show qasim normal with dissolve
    qasim "Don't go there."
    jump jail


