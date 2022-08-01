init python:
    from copy import copy
    class leveling:
        def __init__(self, level, type):
            self.level = 0
            self.exp = 0
            self.points = 0
            self.used_points = 0
            self.type = type
            self.level_up(level)

        def got_exp(self, exp):
            self.exp += exp
            if self.exp > 99:
                self.exp -= 100
                self.level_up(1)

        def level_up(self, levels):
            for i in range(levels):
                self.level += 1
                self.points += 10
            distribute_points(self)

    class stats:
        def __init__(self):
            self.health = 10
            self.mana = 0
            self.stamina = 10

            self.max_health = 10
            self.max_mana = 0
            self.max_stamina = 10

            self.strength = 2
            self.agility = 2
        def sleep(self, amount):
            for i in range(amount):
                self.health += int(self.max_health/20)
                if self.health > self.max_health:
                    self.health = self.max_health
                
                self.mana += int(self.max_mana/20)
                if self.mana > self.max_mana:
                    self.mana = self.max_mana
                
                self.stamina += int(self.max_stamina/10)
                if self.stamina > self.max_stamina:
                    self.stamina = self.max_stamina
        def recover(self, amount):
            for i in range(amount):
                self.mana += int(self.max_mana/40)
                if self.mana > self.max_mana:
                    self.mana = self.max_mana
                
                self.stamina += int(self.max_stamina/40)
                if self.stamina > self.max_stamina:
                    self.stamina = self.max_stamina
        
    class fighter_animation:
        def __init__(self):
            self.animation = "idle"
            self.variation = None

    class fighting:
        def __init__(self):
            pass
        def choose_action(self):
            if not self.animation == "dead":
                if self.stamina < int(self.max_stamina / 10):
                    self.action = "Rest"
                else:
                    ac = random.randint(1,100)
                    chances = arcDic[self.type][1]
                    if ac < chances[0]:
                        self.action = "Attack"
                    elif ac < chances[1]:
                        self.action = "Defend"
                    elif ac < chances[2]:
                        self.action = "Spell"
                    elif ac < chances[3]:
                        self.action = "Item"
                    elif ac < chances[4]:
                        if self.health > self.max_health / 2:
                            self.action = "Attack"
                        else:
                            self.action = "Escape"
                    else:
                        if (self.mana > self.max_mana / 2) or (self.stamina > self.max_stamina):
                            self.action = "Attack"
                        else:
                            self.action = "Rest"

        def rest(self, divider = 5):
            self.mana += int(self.max_mana / divider)
            if self.mana > self.max_mana:
                self.mana = self.max_mana
            self.stamina += int(self.max_stamina / divider)
            if self.stamina > self.max_stamina:
                self.stamina = self.max_stamina

    class fighter(leveling, stats, fighter_animation, fighting):
        def __init__(self, name, level = 1, type = "Peasant"):
            stats.__init__(self)
            leveling.__init__(self, level, type)
            fighter_animation.__init__(self)
            fighting.__init__(self)
            self.name = name
            self.action = None
        def reset(self):
            self.health = self.max_health
            self.mana = self.max_mana
            self.stamina = self.max_stamina
            self.animation = "idle"


    class player(leveling, stats, fighting):
        def __init__(self, name, level = 1, type = "Peasant"):
            stats.__init__(self)
            leveling.__init__(self, level, type)
            fighting.__init__(self)
            self.name = name
            self.alive = True

    class battle_class:
        def __init__(self):
            self.turn = 0
            self.enemy_turn = 0
            self.enemies = []
            self.action = None
            self.loot_table = None
            self.loot = None
            self.exp = 0
        def set(self, enemies, loot):
            self.turn = 2
            self.enemy_turn = 0
            self.enemies = enemies
            for i in enemies:
                if not i.animation == "dead":
                    exp = i.level - main_fighter.level
                    if exp < 1:
                        exp = 1
                    self.exp += exp
            self.action = None
            self.loot_table = loot
            if self.check_for_win():
                self.turn = 4
        def set_action(self, action):
            self.action = action
        def defend(self, unit):
            self.action = "Defend"
            unit.rest(10)
            self.turn = 1
        def rest(self, unit):
            unit.rest()
            self.turn = 1
        def escape(self, unit):
            chance = random.randint(1,4)
            if chance == 1:
                return "escaped"
            else:
                self.turn = 1
        def attack(self, caster, target):
            if self.action == "Kill Attack":
                damage = 1000
                target.animation = "hit"
                Show("battle_attack", g = self, damage = damage, target = target, caster = caster)()
                return
            
            damage = caster.strength
            caster.stamina -= int(caster.strength/2)
            if target.action == "Defend":
                damage = int(damage / 20)
            else:
                target.animation = "hit"
            Show("battle_attack", g = self, damage = damage, target = target, caster = caster)()

        def after_attack(self, damage, target, caster):
            target.health -= damage
            interupt = random.randint(-10, 20)
            if caster.agility + interupt > target.agility:
                target.action = None
            if target.health < 1:
                target.health = 0
                target.action = None
                target.animation = "dead"
                
            else:
                target.animation = "idle"
            self.action = None
            self.turn = 1
            Hide("battle_attack")()
            if self.check_for_win():
                self.turn = 4

        def check_for_win(self):
            for i in self.enemies:
                if not i.animation == "dead":
                    return False
            else:
                return True

        def set_enemy_action(self):
            if self.enemy_turn < len(self.enemies):
                enemy = self.enemies[self.enemy_turn]
                enemy.choose_action()
                self.enemy_turn += 1
            else:
                self.enemy_turn = 0
                self.turn = 0
                Hide("battle_enemy_set_action")()

        def enemy_ai(self):
            if self.enemy_turn < len(self.enemies):
                unit = self.enemies[self.enemy_turn]
                if unit.action == "Attack":
                    unit.animation = "attack"
                    damage = unit.strength
                    Show("battle_enemy_attack", g = self, damage = damage)()
                elif unit.action in ["Rest", "Defend", "Escape", "Item"]:
                    Show("battle_enemy_wait", g = self, unit = unit)()
                elif unit.action == "Spell":
                    Show("battle_enemy_spell", g = self, unit = unit)()
                else:
                    self.enemy_turn += 1
            else:
                self.turn = 2
                self.action = None
                self.enemy_turn = 0

        def enemy_after_spell(self, unit):
            unit.action = None
            self.enemy_turn += 1
            Hide("battle_enemy_spell")()

        def enemy_after_wait(self, unit):
            if unit.action == "rest":
                unit.rest()
            elif unit.action == "Defend":
                unit.rest(10)
            elif unit.action == "Escape":
                pass
            elif unit.action == "Item":
                pass
            unit.action = None
            self.enemy_turn += 1
            Hide("battle_enemy_wait")()

        def enemy_after_attack(self, damage, target):
            unit = self.enemies[self.enemy_turn]
            if self.action == "Defend":
                damage = int(damage/20)
            target.health -= damage
            if target.health < 1:
                target.health = 0
                self.turn = 3
            unit.action = None
            unit.animation = "idle"
            self.enemy_turn += 1 
            Hide("battle_enemy_attack")()
        def calculate_loot(self):
            if self.loot_table:
                self.loot = drop_more(self.loot_table, len(self.enemies))
        def loot_all(self):
            if self.loot:
                for i in self.loot:
                    hero.got(i, 1)
                self.loot = None
            main_fighter.got_exp(self.exp)
            self.exp = 0

default battle_handler = battle_class()


default player_1 = player("Me", 4)
default main_fighter = player_1
style battle_text is zero:
    align (.5,.5)
style battle_fixed:
    fit_first True
    align (.5,.5)
style battle_button is zero
style battle_frame is zero
style battle_slider:
    xysize (800,20)
screen battle(enemies, loot = None):
    modal True
    if len(enemies) in [1, 3, 5]:
        default positions = [
            [0,0],
            [300,-40],
            [-300,-40],
            [500,-100],
            [-500,-100],
        ]
    else:
        default positions = [
            [150, 0],
            [-150, 0],
            [350,-40],
            [-350,-40],
            [0,0],
        ]
    default g = battle_handler
    on "show" action Function(g.set, enemies, loot)

    style_prefix "battle"

    button align .0,.0:
        text "arc"
        action Show("btl_arc")

    add "#0009"
    for n,i in enumerate(g.enemies):
        vbox spacing 8 anchor .5,1.0 align .5,.7:
            offset positions[n]
            if i.action and not i.action == "Rest":
                frame:
                    add "battle_{}".format(i.action.lower()) align .5,.5
            frame:
                vbox:
                    text i.name
                    text "level: {} {}".format(i.level, i.type) size 20
                    fixed:
                        bar value i.health range i.max_health xysize(120,25) left_bar "#900" right_bar "#9005"
                        text "{} / {}".format(i.health, i.max_health) size 20
            button:
                background None
                if not i.animation == "dead":
                    if n == g.enemy_turn and (g.turn == 2 or (g.turn == 1 and i.action)):
                        background "#f003"
                    hover_background "#0f03"
                    if g.action in ["Attack", "Kill Attack"]:
                        action Function(g.attack, main_fighter, i)
                add "{} {}".format(i.name.lower(), i.animation)

    vbox spacing 8 align .5,1.0 yoffset -20:
        if g.turn == 0:
            hbox align .5,.5 spacing 8:
                if not g.action:
                    button:
                        text _("Attack")
                        if main_fighter.stamina >= main_fighter.strength/2:
                            action Function(g.set_action, "Attack") keysym "1"
                    button:
                        text _("Defend")
                        action Function(g.defend, main_fighter) keysym "2"
                    button:
                        text _("Rest")
                        action Function(g.rest, main_fighter) keysym "3"
                    button:
                        text _("Spell")
                        action Show("battle_spell", g=g) keysym "4"
                    button:
                        text _("Item")
                        action Show("battle_item") keysym "5"
                    button:
                        text _("Escape")
                        action SetScreenVariable("escaping", True) keysym "6"
                else:
                    button:
                        text _("Cancel")
                        action Function(g.set_action, None)
        elif g.turn == 1:
            timer .01 repeat True action Function(g.enemy_ai)
            text "Enemy's turn"
        elif g.turn == 2:
            timer .1 action Show("battle_enemy_set_action", g = g)
        # elif g.turn == 4:
        #     button:
        #         text _("Leave")
        #         action Return()

        fixed:
            bar value main_fighter.health range main_fighter.max_health left_bar "#900" right_bar "#9005" style "battle_slider"
            text "{} / {}".format(main_fighter.health, main_fighter.max_health) size 20
        fixed:
            bar value main_fighter.mana range main_fighter.max_mana left_bar "#006e99" right_bar "#006e9955" style "battle_slider"
            text "{} / {}".format(main_fighter.mana, main_fighter.max_mana) size 20
        fixed:
            bar value main_fighter.stamina range main_fighter.max_stamina left_bar "#996900" right_bar "#99960055" style "battle_slider"
            text "{} / {}".format(main_fighter.stamina, main_fighter.max_stamina) size 20
        fixed:
            bar value main_fighter.exp range 100 left_bar "#535353" right_bar "#60606055" style "battle_slider"
            text f"{main_fighter.exp} / 100" size 20
        frame:
            text "You are level: {}  Strength: {}  Agility: {}".format(main_fighter.level, main_fighter.strength, main_fighter.agility)

    if g.turn == 3:
        button:
            background None
            action NullAction()
        frame:
            vbox spacing 10:
                text _("You're dead.")
                button:
                    text _("Let the darkness take over")
                    action MainMenu()
                button:
                    text _("Reach for the sands of time")
                    action ShowMenu("load")


    default escaping = False
    if escaping and g.turn == 0: # Run away
        timer .4 repeat True action Function(g.escape, main_fighter)
        button:
            background None
            action NullAction()
        frame:
            vbox:
                text "Looking for a chance!"


    elif g.turn == 4:
        timer .4 action Function(g.calculate_loot)
        button:
            background None
            action NullAction()
        frame:
            vbox spacing 10:
                text _("You won.")
                if g.exp:
                    text _(f"{g.exp} exp.")
                if g.loot:
                    text _("Here's your loot.")
                    hbox align .5,.5 spacing 10:
                        for i in g.loot:
                            add i.icon
                if g.loot or g.exp:
                    button:
                        text _("Take all")
                        action Function(g.loot_all)
                button:
                    text _("Exit")
                    action Return("won")


screen battle_enemy_set_action(g):
    modal True
    timer .1 repeat True action Function(g.set_enemy_action)
screen battle_enemy_attack(g, damage):
    modal True
    text str(damage) yalign .1
    timer 1 action Function(g.enemy_after_attack, damage, main_fighter)
screen battle_enemy_wait(g, unit):
    modal True
    timer 1 action Function(g.enemy_after_wait, unit)
screen battle_enemy_spell(g, unit):
    modal True
    timer 1 action Function(g.enemy_after_spell, unit)

screen battle_attack(g, damage, target, caster):
    modal True
    timer 1 action Function(g.after_attack, damage, target, caster)
screen battle_spell(g):
    modal True
    button:
        background None
        action NullAction()
    frame align .5,.5 padding 40,40:
        vbox:
            text _("You know no spells.")
            button align .5,.5 padding 40,40:
                text _("OK")
                action Hide("battle_spell")
            button align .5,.5 padding 40,40:
                text _("Kill (test)")
                action Function(g.set_action, "Kill Attack"), Hide("battle_spell")
screen battle_item():
    modal True
    button:
        background None
        action NullAction()
    frame align .5,.5 padding 40,40:
        vbox:
            text _("You have no items.")
            button align .5,.5 padding 40,40:
                text _("OK")
                action Hide("battle_item")


init python:
    def calculate_loot(g):
        loot = []
        for i in g.enemies:
            loot.append(i.loot)
screen battle_loot(g):
    $ loot = calculate_loot(g)

screen battle_points():
    modal True
    vbox:
        fixed:
            bar value main_fighter.exp range 100 left_bar "#535353" right_bar "#60606055" style "battle_slider"
            text f"{main_fighter.exp} / 100" size 20
        
        text f"Points: {main_fighter.points}" size 20





default sketch = fighter("Sketch", 4)
default sketch1 = fighter("Sketch", 1, "Wizard")
default sketch2 = fighter("Sketch", 1, "Warrior")
default sketch3 = fighter("Sketch", 1, "Rogue")
default sketch4 = fighter("Sketch", 1, "Demon")

label battle_example:
    call screen battle([sketch])
    call screen battle([sketch, sketch1, sketch2, sketch3, sketch4])


