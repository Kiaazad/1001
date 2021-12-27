define ras = Character("Rasoul", color="#f44", what_text_color="#fdd", namebox_align=(1.0, 0.0))
# Rasoul the head of guards
# Normal
image ras_normal_blink:
    "char/rasoul/normal_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image ras_normal_mouth_moving:
    "char/rasoul/normal_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image ras_normal_mouth = ConditionSwitch(
    "_last_say_who == 'ras'", "ras_normal_mouth_moving",
    "not _last_say_who == 'ras'", "char/empty.webp")

image ras normal = Composite((800, 962),
    (0,0), "char/rasoul/normal.webp",
    (0,0), "ras_normal_mouth",
    (0,0), "ras_normal_blink",
)
# Angry
image ras_angry_blink:
    "char/rasoul/angry_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image ras_angry_mouth_moving:
    "char/rasoul/angry_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image ras_angry_mouth = ConditionSwitch(
    "_last_say_who == 'ras'", "ras_angry_mouth_moving",
    "not _last_say_who == 'ras'", "char/empty.webp")

image ras angry = Composite((800, 962),
    (0,0), "char/rasoul/angry.webp",
    (0,0), "ras_angry_mouth",
    (0,0), "ras_angry_blink",
)

# Smile
image ras_smile_blink:
    "char/rasoul/smile_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image ras_smile_mouth_moving:
    "char/rasoul/smile_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image ras_smile_mouth = ConditionSwitch(
    "_last_say_who == 'ras'", "ras_smile_mouth_moving",
    "not _last_say_who == 'ras'", "char/empty.webp")

image ras smile = Composite((800, 962),
    (0,0), "char/rasoul/smile.webp",
    (0,0), "ras_smile_mouth",
    (0,0), "ras_smile_blink",
)


