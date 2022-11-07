init python:
    class work_class:
        def __init__(self, text, time, loot):
            self.text = text
            self.time = time
            self.loot = loot
            self.remaining = time
        def work(self):
            if self.remaining > 0:
                self.remaining -= 1
            else:
                Hide("do_work")()
                if self.loot:
                    Show("loot_all", loot = drop_more(self.loot, random.randint(0,3)))()
            


screen do_work(time, text, loot):
    modal True
    style_prefix "work"
    default g = work_class(text, time, loot)
    frame:
        align .5,.5
        vbox:
            text g.text
            bar value g.remaining range g.time xysize 300,20 left_bar "#fff" right_bar "#fff6"
    timer .1 repeat True action Function(g.work)

style work_frame is zero