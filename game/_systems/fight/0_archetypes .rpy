init python:
    arcDic = { # "Name": [[health, mana, stamina, power, agility]
        "Peasant": [
            [18, 23, 51, 66, 75],
            [18, 37, 40, 49, 77]
        ],
        "Wizard": [
            [21, 54, 62, 86, 100],
            [13, 27, 62, 90, 95]
        ],
        "Dancer": [
            [21, 34, 55, 64, 87],
            [15, 35, 47, 67, 85]
        ],
        "Princess": [
            [15, 33, 44, 52, 62],
            [23, 30, 34, 48, 70]
        ],
        "Beast": [
            [32, 33, 53, 76, 81],
            [53, 71, 72, 73, 80]
        ],
        "Warrior": [
            [41, 42, 58, 87, 100],
            [41, 74, 75, 93, 95]
        ],
        "Rogue": [
            [19, 23, 62, 89, 100],
            [45, 54, 66, 81, 92]
        ],
        "Demon": [
            [37, 46, 56, 95, 100],
            [55, 78, 91, 96, 98]
        ],
        "Dummy": [
            [60, 60, 60, 60, 67],
            [0, 0, 0, 0, 0]
        ],
    }
    def distribute_points(unit):
        while unit.points:
            c = random.randint(1,100)
            jitter = random.randint(-2, 2)
            if c < arcDic[unit.type][0][0]:
                unit.max_health += (10 + jitter)
                unit.health += (10 + jitter)
            elif c < arcDic[unit.type][0][1]:
                unit.max_mana += (10 + jitter)
                unit.mana += (10 + jitter)
            elif c < arcDic[unit.type][0][2]:
                unit.max_stamina += (10 + jitter)
                unit.stamina += (10 + jitter)
            elif c < arcDic[unit.type][0][3]:
                unit.strength += (6 + (int(jitter/2)))
            elif c < arcDic[unit.type][0][4]:
                unit.agility += (6 + (int(jitter/2)))
            unit.points -= 1
            unit.used_points += 1


    class btl_arc_class:
        def __init__(self):
            self.rem = 100
            self.ind = 0

            self.hp = 20
            self.mp = 20
            self.stm = 20
            self.pwr = 20
            self.agl = 20

            self.chances = 100
            self.attack_chance = 20
            self.defend_chance = 20
            self.spell_chance = 20
            self.item_chance = 20
            self.escape_chance = 20
        def get(self):
            health = self.hp
            mana = self.hp + self.mp
            stamina = self.hp + self.mp + self.stm
            strength = self.hp + self.mp + self.stm + self.pwr
            agility = self.hp + self.mp + self.stm + self.pwr + self.agl

            attack = self.attack_chance
            defend = self.attack_chance + self.defend_chance
            spell = self.attack_chance + self.defend_chance + self.spell_chance
            item = self.attack_chance + self.defend_chance + self.spell_chance + self.item_chance
            escape = self.attack_chance + self.defend_chance + self.spell_chance + self.item_chance + self.escape_chance

            return [[health, mana, stamina, strength, agility], [attack, defend, spell, item, escape]]

        def adj(self):
            self.rem = self.hp + self.mp + self.stm + self.pwr + self.agl
            while self.hp + self.mp + self.stm + self.pwr + self.agl > 100:
                if self.ind == 0:
                    if self.hp > 1:
                        self.hp -= 1
                    self.ind += 1
                elif self.ind == 1:
                    if self.mp > 1:
                        self.mp -= 1
                    self.ind += 1
                elif self.ind == 2:
                    if self.stm > 1:
                        self.stm -= 1
                    self.ind += 1
                elif self.ind == 3:
                    if self.pwr > 1:
                        self.pwr -= 1
                    self.ind += 1
                else:
                    if self.agl > 1:
                        self.agl -= 1
                    self.ind = 0
            
            self.chances = self.attack_chance + self.defend_chance + self.spell_chance + self.item_chance + self.escape_chance
            while self.attack_chance + self.defend_chance + self.spell_chance + self.item_chance + self.escape_chance > 100:
                if self.ind == 0:
                    if self.attack_chance > 1:
                        self.attack_chance -= 1
                    self.ind += 1
                elif self.ind == 1:
                    if self.defend_chance > 1:
                        self.defend_chance -= 1
                    self.ind += 1
                elif self.ind == 2:
                    if self.spell_chance > 1:
                        self.spell_chance -= 1
                    self.ind += 1
                elif self.ind == 3:
                    if self.item_chance > 1:
                        self.item_chance -= 1
                    self.ind += 1
                else:
                    if self.escape_chance > 1:
                        self.escape_chance -= 1
                    self.ind = 0



default btl_arc_1 = btl_arc_class()
style arc_label:
    align (.0,.5) xoffset 10
style arc_label_text:
    size 24 color "#fff" outlines [(2, "#000", 0, 0)]

screen btl_arc(x = btl_arc_1):
    style_prefix "arc"
    modal True
    default inp = ""
    timer .1 repeat True action Function(x.adj)
    add "#000d"
    hbox align .5,.5 spacing 10:
        vbox spacing 10:
            text "%{}".format(x.rem)
            fixed fit_first True:
                bar value FieldValue(x, "hp", 60) xysize 500,80 left_bar "#f00" right_bar "#fff9"
                label "Health" 
                label "%{}".format(x.hp) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "mp", 60) xysize 500,80 left_bar "#0ff" right_bar "#fff9"
                label "Mana"
                label "%{}".format(x.mp) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "stm", 60) xysize 500,80 left_bar "#ff0" right_bar "#fff9"
                label "Stamina"
                label "%{}".format(x.stm) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "pwr", 60) xysize 500,80 left_bar "#444" right_bar "#fff9"
                label "Power"
                label "%{}".format(x.pwr) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "agl", 60) xysize 500,80 left_bar "#444" right_bar "#fff9"
                label "Agility"
                label "%{}".format(x.agl) xalign 1.0 xoffset -10
        vbox spacing 10:
            text "%{}".format(x.chances)
            fixed fit_first True:
                bar value FieldValue(x, "attack_chance", 60) xysize 500,80 left_bar "#f00" right_bar "#fff9"
                label "Attack chance"
                label "%{}".format(x.attack_chance) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "defend_chance", 60) xysize 500,80 left_bar "#0ff" right_bar "#fff9"
                label "Defend chance"
                label "%{}".format(x.defend_chance) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "spell_chance", 60) xysize 500,80 left_bar "#ff0" right_bar "#fff9"
                label "Spell chance"
                label "%{}".format(x.spell_chance) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "item_chance", 60) xysize 500,80 left_bar "#444" right_bar "#fff9"
                label "Item chance"
                label "%{}".format(x.item_chance) xalign 1.0 xoffset -10
            fixed fit_first True:
                bar value FieldValue(x, "escape_chance", 60) xysize 500,80 left_bar "#444" right_bar "#fff9"
                label "Escape chance"
                label "%{}".format(x.escape_chance) xalign 1.0 xoffset -10

    hbox align .5,.9:
        frame:
            xsize 300
            input:
                value ScreenVariableInputValue("inp")
        button:
            text "Copy"
            action Function(clip_put, "\"{}\": {}".format(inp, str(x.get())))

