init offset = -1

define zero_frame = "frame"
define zero_frame_margin = [10, 10]
define zero_dim_bg = "#000a"
define zero_mm_bg = "#000a"
define zero_gm_bg = "#000a"

style default:
    font "0gui/fonts/Acme-Regular.ttf"
style zero:
    # All
    align(.5,.5)

    # Text
    color "#fff"
    hover_color "#ff2"
    selected_color "#fff"
    selected_hover_color "#ff2"
    font "0gui/fonts/Acme-Regular.ttf"
    size 24

    # Frame and button
    padding(16,16)
    background Frame(zero_frame, 6, 6)
    hover_background Frame(zero_frame, 6, 6)
    selected_background Frame(zero_frame, 6, 6)
    selected_hover_background Frame(zero_frame, 6, 6)
    insensitive_background Frame(zero_frame, 6, 6)

    # Box
    spacing 8
    box_wrap True
    box_wrap_spacing 8

    # Bar
    left_bar Frame(zero_frame, 6, 6)
    right_bar Frame(zero_frame, 6, 6)
    hover_left_bar Frame(zero_frame, 6, 6)
    hover_right_bar Frame(zero_frame, 6, 6)

    # Sounds
    # hover_sound "0gui/sfx/hover.mp3"
    # activate_sound "0gui/sfx/select.mp3"

transform btn:
    parallel:
        xoffset renpy.random.randint(-1000, 1000) alpha 0 yzoom .01
        pause renpy.random.random()/4
        
        ease .2 xoffset 0 yzoom 1 alpha 1
    parallel:
        on idle:
            easein .2 additive 0 alpha 1
        on hover:
            easein .2 additive .3 alpha 1
        on selected_idle:
            easein .2 additive .2 alpha 1
        on selected_hover:
            easein .2 additive .3 alpha 1
        on insensitive:
            easein .2 additive 0 alpha .5

################################################################################
## Styles
################################################################################

# style default:
#     properties gui.text_properties()
#     language gui.language

# style input:
#     properties gui.text_properties("input", accent=True)
#     adjust_spacing False

# style hyperlink_text:
#     properties gui.text_properties("hyperlink", accent=True)
#     hover_underline True

# style gui_text:
#     properties gui.text_properties("interface")


# style button:
#     properties gui.button_properties("button")

# style button_text is gui_text:
#     properties gui.text_properties("button")
#     yalign 0.5


# style label_text is gui_text:
#     properties gui.text_properties("label", accent=True)

# style prompt_text is gui_text:
#     properties gui.text_properties("prompt")


# style bar:
#     ysize gui.bar_size
#     left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     xsize gui.bar_size
#     top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# style vscrollbar:
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

# style slider:
#     ysize gui.slider_size
#     base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#     thumb "gui/slider/horizontal_[prefix_]thumb.png"

# style vslider:
#     xsize gui.slider_size
#     base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/slider/vertical_[prefix_]thumb.png"


# style frame:
#     padding gui.frame_borders.padding
#     background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
