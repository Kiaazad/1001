init offset = -1

## Say screen ##################################################################

screen say(who, what):
    style_prefix "say"
    button:
        background None
        action Return()
    window:
        id "window"
        align .5,0.0
        xsize 920
        yminimum 101
        padding 30,10
        background Frame("say_box", 0, 20, 0, 30)
        text what id "what" size 30 yoffset -10 align .5,.5

    if who is not None:
        window:
            xsize 510 padding 0,0 id "namebox" background None align (1.0, 0.0)
            frame:
                id "namebox1"
                background Frame("name_box_1", 0, 25, 0, 70)
                padding 30,5,50,5 xalign 0.0
                ysize 87
                text who id "who" align .5,.5 size 25
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')
    config.character_id_prefixes.append('namebox1')


default quest_log_ui_icon = False
screen top_bar():
    zorder 1001
    add "top_frame" align .5,.0
    if quest_log_ui_icon:
        button:
            background None align 0.0,0.0 xoffset 40 padding 0,0
            add "ui_quest"
            action ToggleScreen('quests')
    button:
        background None align 0.0,0.0  padding 0,0
        add "ui_inventory"
        action ToggleScreen('show_bag')
    # button:
    #     background None align 1.0,0.0 xoffset -40  padding 0,0
    #     add "ui_map"
    #     action ToggleScreen('map')
    button:
        background None align 1.0,0.0  padding 0,0
        add "ui_save"
        action ShowMenu("save")
init python:
    config.overlay_screens.append("top_bar")
## Input screen ################################################################

screen input(prompt):
    style_prefix "input"

    frame:
        xsize 400
        vbox:
            text prompt
            input id "input"

style input_frame is zero
style input_button is zero
style input_text is zero
style input_vbox is zero


## Choice screen ###############################################################

screen choice(items):
    style_prefix "choice"
    button:
        background None
        action NullAction()
    vbox:
        for i in items:
            button:
                xsize 900
                text i.caption
                action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_button is zero
style choice_text is zero
style choice_vbox is zero

