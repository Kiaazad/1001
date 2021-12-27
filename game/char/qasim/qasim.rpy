define qasim = Character("Qasim", color="#4ff", what_text_color="#dff")
# Normal
image qasim_normal_blink:
    "char/qasim/normal_blink.webp"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image qasim_normal_mouth_moving:
    "char/qasim/normal_bla.webp"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image qasim_normal_mouth = ConditionSwitch(
    "_last_say_who == 'qasim'", "qasim_normal_mouth_moving",
    "not _last_say_who == 'qasim'", "char/empty.webp")

image qasim normal = Composite((840, 700),
    (0,0), "char/qasim/normal.webp",
    (0,0), "qasim_normal_mouth",
    (0,0), "qasim_normal_blink",
)
