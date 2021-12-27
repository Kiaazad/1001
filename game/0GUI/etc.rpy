init offset = -1


screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add zero_dim_bg

    frame:
        vbox:
            spacing 45
            text _(message)
            hbox:
                spacing 150
                button:
                    text _("Yes")
                    action yes_action
                button:
                    text _("No")
                    action no_action

    key "game_menu" action no_action

style confirm_frame is zero
style confirm_button is zero
style confirm_text is zero
style confirm_hbox is zero
style confirm_vbox is zero

screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        align .0,.0
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is zero
style skip_text is zero
style skip_hbox is zero
style skip_vbox is zero

style skip_triangle:
    font "DejaVuSans.ttf"


screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is zero
style notify_text is zero


screen about():
    tag menu
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):
        vbox:
            xsize 900
            style_prefix "about"
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_frame is zero
style about_text is zero
style about_hbox is zero
style about_vbox is zero

