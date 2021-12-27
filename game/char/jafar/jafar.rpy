# Jafar images
# excited
image jaf_normal_blink:
    "char/jafar/normal_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image jaf_normal_mouth_moving:
    "char/jafar/normal_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image jaf_normal_mouth = ConditionSwitch(
    "_last_say_who == 'jaf'", "jaf_normal_mouth_moving",
    "not _last_say_who == 'jaf'", "char/empty.webp")

image jaf normal = Composite((783, 1063),
    (0,0), "char/jafar/normal.webp",
    (0,0), "jaf_normal_mouth",
    (0,0), "jaf_normal_blink",
)

# thinking
image jaf_thinking_blink:
    "char/jafar/thinking_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image jaf_thinking_mouth_moving:
    "char/jafar/thinking_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image jaf_thinking_mouth = ConditionSwitch(
    "_last_say_who == 'jaf'", "jaf_thinking_mouth_moving",
    "not _last_say_who == 'jaf'", "char/empty.webp")

image jaf thinking = Composite((783, 1097),
    (0,0), "char/jafar/thinking.webp",
    (0,0), "jaf_thinking_mouth",
    (0,0), "jaf_thinking_blink",
)

# angry
image jaf_angry_blink:
    "char/jafar/angry_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image jaf_angry_mouth_moving:
    "char/jafar/angry_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image jaf_angry_mouth = ConditionSwitch(
    "_last_say_who == 'jaf'", "jaf_angry_mouth_moving",
    "not _last_say_who == 'jaf'", "char/empty.webp")

image jaf angry = Composite((783, 1097),
    (0,0), "char/jafar/angry.webp",
    (0,0), "jaf_angry_mouth",
    (0,0), "jaf_angry_blink",
)
image jaf genie = "char/jafar/genie.webp"
image jaf genie bent = "char/jafar/genie_bent.webp"
image jaf disappointed = "char/jafar/disappointed.webp"
image jaf magic = "char/jafar/magic.webp"
# image jaf angry = "char/jafar/angry.webp"
image jaf smile = "char/jafar/smile.webp"
image jaf annoyed = "char/jafar/annoyed.webp"
image jaf probing = "char/jafar/probing.webp"
image jaf looking:
    "char/jafar/looking1.webp"
    pause 2
    "char/jafar/looking2.webp"
    pause 2
    repeat

