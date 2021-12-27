init offset = -1

screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            style_prefix "pref"
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        text _("Display")
                        button:
                            text _("Window")
                            action Preference("display", "window")
                        button:
                            text _("Fullscreen")
                            action Preference("display", "fullscreen")
                vbox:
                    text _("Rollback Side")
                    button:
                        text _("Disable")
                        action Preference("rollback side", "disable")
                    button:
                        text _("Left")
                        action Preference("rollback side", "left")
                    button:
                        text _("Right")
                        action Preference("rollback side", "right")

                vbox:
                    text _("Skip")
                    button:
                        text _("Unseen Text")
                        action Preference("skip", "toggle")
                    button:
                        text _("After Choices")
                        action Preference("after choices", "toggle")
                    button:
                        text _("Transitions")
                        action InvertSelected(Preference("transitions", "toggle"))

            hbox:
                box_wrap True
                vbox:
                    text _("Text Speed")
                    bar value Preference("text speed")
                    text _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        text _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        text _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                button:
                                    text _("Test")
                                    action Play("sound", config.sample_sound)


                    if config.has_voice:
                        text _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                button:
                                    text _("Test")
                                    action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        button:
                            text _("Mute All")
                            action Preference("all mute", "toggle")



style pref_button is zero
style pref_text is zero
style pref_vbox is zero
style pref_hbox is zero
style pref_slider is zero:
    xysize (300,30)


