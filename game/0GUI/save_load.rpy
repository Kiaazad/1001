init offset = -1


## Load and Save screens #######################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    use game_menu(title):
        fixed:
            style_prefix "save"
            order_reverse True
            button:
                key_events True
                align 0.5,.0
                action page_name_value.Toggle()
                input:
                    value page_name_value
            grid 3 2:
                align 0.5,0.5
                spacing 10
                for i in range(3*2):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        vbox:
                            add FileScreenshot(slot) xalign 0.5
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot"))
                            text FileSaveName(slot)
                            key "save_delete" action FileDelete(slot)

            hbox:
                align 0.5,1.0
                spacing 10
                button:
                    text _("<")
                    action FilePagePrevious()
                if config.has_autosave:
                    button:
                        text _("{#auto_page}A")
                        action FilePage("auto")
                if config.has_quicksave:
                    button:
                        text _("{#quick_page}Q")
                        action FilePage("quick")
                for page in range(1, 10):
                    button:
                        text "[page]"
                        action FilePage(page)
                button:
                    text _(">")
                    action FilePageNext()

style save_button is zero
style save_text is zero



