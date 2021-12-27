init offset = -1

screen history():
    tag menu
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                if h.who:
                    text h.who:
                        substitute False
                        ## Take the color of the who text from the Character, if
                        ## set.
                        # if "color" in h.who_args:
                        #     text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
        if not _history_list:
            text _("The dialogue history is empty.")

## This determines what tags are allowed to be displayed on the history screen.
define gui.history_allow_tags = { "alt", "noalt" }


style history_text is zero