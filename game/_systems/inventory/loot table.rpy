init python:
    def drop_loot(table):
        sum1 = 0
        for i in table:
            sum1 += i[1]
        r = random.randint(1,sum1)
        sum2 = 0
        for i in table:
            sum2 += i[1]
            if r < sum2:
                return i[0]

    def drop_more(table, n):
        loot = []
        for i in range(n):
            item = drop_loot(table)
            if not item == None:
                loot.append(item)
        return loot

    def take_loot(loot):
        for i in loot:
            hero.got(i, 1)
        Hide("loot_all")()
        for i in loot:
            if i.quest:
                Call(i.quest)()
                break

screen loot_all(loot):
    modal True
    style_prefix "loot"
    frame:
        align .5,.5
        vbox spacing 10:
            if loot:
                text _("Here's your loot.")
                hbox align .5,.5 spacing 10:
                    for i in loot:
                        button:
                            padding 0,0 background None
                            add i.icon
                            tooltip i
                            action NullAction()
                button:
                    text _("Take all")
                    action Function(take_loot, loot)
            else:
                text _("You've got nothing.")

            button:
                text _("Exit")
                action Hide("loot_all")

style loot_frame is zero
style loot_button is zero