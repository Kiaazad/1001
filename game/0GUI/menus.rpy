init offset = -1

##################################### Navigation

screen navigation():
    vbox:
        align .01,.5
        style_prefix "navigation"
        if main_menu:
            button:
                text _("Start")
                action Start()
        else:
            button:
                text _("History")
                action ShowMenu("history")
            button:
                text _("Save")
                action ShowMenu("save")

        button:
            text _("Load")
            action ShowMenu("load")
        button:
            text _("Preferences")
            action ShowMenu("preferences")

        if _in_replay:
            button:
                text _("End Replay")
                action EndReplay(confirm=True)
        elif not main_menu:
            button:
                text _("Main Menu")
                action MainMenu()

        button:
            text _("About")
            action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            button:
                text _("Help")
                action ShowMenu("help")

        if renpy.variant("pc"):
            button:
                text _("Quit")
                action Quit(confirm=not main_menu)


style navigation_button is zero:
    size_group "navigation"

style navigation_text is zero
style navigation_vbox is zero


##################################### Main Menu

screen main_menu():
    tag menu
    style_prefix "main_menu"
    add "main_menu_bg"
    hbox:
        align(0.72, 0.21)
        button:
            text "Start"
            action Start()
            at btn
        button:
            text "Load"
            action ShowMenu("load")
            at btn
        button:
            text "Settings"
            action ShowMenu("preferences")
            at btn
        button:
            text "Quit"
            action Quit(confirm=not main_menu)
            at btn
    vbox:
        align 1.0,1.0
        # text "[config.name!t]"
        text "[config.version]"

style main_menu_text is zero
style main_menu_button is zero
style main_menu_vbox is zero
style main_menu_hbox is zero

##################################### Game Menu

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add zero_mm_bg
    else:
        add zero_gm_bg

    hbox:
        # frame:
        #     xsize 300
        frame:
            background None
            transclude

    use navigation

    button:
        align 0.0,1.0
        text _("Return")
        action Return()
    frame:
        align 1.0,0.0
        text title 

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_frame is zero    
style game_menu_button is zero
style game_menu_text is zero
style game_menu_hbox is zero


##################################### Quick Menu

screen quick_menu():
    zorder 100

    # if quick_menu:
    #     hbox:
    #         style_prefix "quick"
    #         align 0.5, 1.0
    #         button:
    #             text _("Back")
    #             action Rollback()
    #         button:
    #             text _("History")
    #             action ShowMenu('history')
    #         button:
    #             text _("Skip")
    #             action Skip() alternate Skip(fast=True, confirm=True)
    #         button:
    #             text _("Auto")
    #             action Preference("auto-forward", "toggle")
    #         button:
    #             text _("Save")
    #             action ShowMenu('save')
    #         button:
    #             text _("Q.Save")
    #             action QuickSave()
    #         button:
    #             text _("Q.Load")
    #             action QuickLoad()
    #         button:
    #             text _("Prefs")
    #             action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is zero
style quick_text is zero
style quick_hbox is zero


################################################################################
## Mobile Variants
################################################################################


# style window:
#     variant "small"
#     background "gui/phone/textbox.png"

# style radio_button:
#     variant "small"
#     foreground "gui/phone/button/radio_[prefix_]foreground.png"

# style check_button:
#     variant "small"
#     foreground "gui/phone/button/check_[prefix_]foreground.png"

# style nvl_window:
#     variant "small"
#     background "gui/phone/nvl.png"

# style main_menu_frame:
#     variant "small"
#     background "gui/phone/overlay/main_menu.png"

# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu.png"

# style game_menu_navigation_frame:
#     variant "small"
#     xsize 510

# style game_menu_content_frame:
#     variant "small"
#     top_margin 0

# style pref_vbox:
#     variant "small"
#     xsize 600

# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# style vscrollbar:
#     variant "small"
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

# style slider:
#     variant "small"
#     ysize gui.slider_size
#     base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

# style slider_vbox:
#     variant "small"
#     xsize None

# style slider_slider:
#     variant "small"
#     xsize 900
