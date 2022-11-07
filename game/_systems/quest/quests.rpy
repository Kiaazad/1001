init python:
    class quest:
        def __init__(self, name, info, items = [], objc = [], rewards = [], img = []):
            self.name = name
            self.info = info
            self.objc = objc
            self.rewards = rewards
            self.img = img
            self.stat = "Active"
            self.flags = []
        def complete(self):
            if self.stat == "Active":
                self.stat = "Completed"
                Show("quest_notif", s = "qst_completed")()
        def cancel(self):
            if self.stat == "Active":
                self.stat = "Canceled"
                Show("quest_notif", s = "qst_canceled")()
        def fail(self):
            Show("quest_notif", s = "qst_failed")()
        def extend(self, text):
            if not text in self.info:
                self.info.append(_(text))
                msg.msg("Changed quest: {}\n{}".format(self.name, text))
        
    class quest_log:
        def __init__(self):
            self.log = []
            self.slc = None
            self.filt = 0

        def chose(self, n):
            self.slc = n
        def filter(self):
            if self.filt < 4:
                self.filt += 1
            else:
                self.filt = 0


        def got(self, q):
            if q not in self.log:
                self.log.append(q)
                msg.msg("New quest: {}".format(q.name))
                Show("quest_notif", s = "qst_accepted")()
        def has(self, quest):
            if quest in self.log:
                return quest.stat
            else:
                return False
        def has_line(self, quest, line):
            stat = self.has(quest)
            if stat:
                if quest.info[-1] == line:
                    return True
                else:
                    return False
            else:
                return False
image quest_notification = Live2D("_systems/quest/quest_menu_l2d/quest_menu.model3.json", loop=False, zoom=0.5
    )

screen quest_notif(s):
    add "quest_notification [s]":
        align .5,.9
    timer 5 action Hide("quest_notif")

default qlog = quest_log()


style quest_frame is zero
style quest_button is zero
screen quests(q = qlog):
    style_prefix "quest"
    default filters = ["All", "Active", "Completed", "Canceled", "Failed"]
    default colors = {
        "All": "#fff",
        "Active": "#ffc",
        "Completed": "#6f0",
        "Canceled": "#005",
        "Failed": "#444",
    }
    modal True
    drag align .5,.5:
        frame:
            ysize 650
            hbox:
                vbox:
                    align 0.0,0.0
                    button:
                        xsize 300
                        at btn
                        text "Filter: {}".format(filters[q.filt]) color colors[filters[q.filt]]
                        action Function(q.filter)
                    viewport:
                        xsize 300 draggable True mousewheel True edgescroll 200,200
                        frame:
                            xsize 300
                            vbox:
                                for i in q.log:
                                    if i.stat == filters[q.filt] or filters[q.filt] == "All":
                                        button:
                                            at btn
                                            background None selected_foreground Frame("quest_arrow", 10,0,32,0) xalign 0.0 padding 10,10,40,10 
                                            text i.name:
                                                color colors[i.stat]
                                            action Function(q.chose, i), SelectedIf(i == q.slc)
                
                frame:
                    yfill True xsize 400
                    if q.slc:
                        viewport:
                            draggable True
                            vbox:
                                yalign 0.0
                                for i in q.slc.info:
                                    text i 
                        hbox align .5,1.0:
                            text "Status:"
                            text q.slc.stat:
                                color colors[q.slc.stat]

    button:
        align 1.0,1.0 margin 100,100
        text "Return"
        action Hide("quests"), Return()




