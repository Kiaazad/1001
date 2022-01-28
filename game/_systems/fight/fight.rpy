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


    class fighter_animation:
        def __init__(self):
            self.animation = "idle"
            self.variation = None

    class fighting:
        def __init__(self):
            pass
        def choose_action(self):
            if not self.animation == "dead":
                if self.stamina < self.max_stamina / 10:
                    self.action = "Rest"
                else:
                    ac = renpy.random.randint(1,100)
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
            self.mana += self.max_mana / divider
            if self.mana > self.max_mana:
                self.mana = self.max_mana
            self.stamina += self.max_stamina / divider
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

        def set(self, enemies):
            self.turn = 2
            self.enemy_turn = 0
            self.enemies = enemies
            self.action = None

        def set_action(self, action):
            self.action = action
        def defend(self, unit):
            self.action = "Defend"
            unit.rest(10)
            self.turn = 1
        def rest(self, unit):
            unit.rest()
            self.turn = 1



        def attack(self, caster, target):
            damage = caster.strength
            caster.stamina -= caster.strength/2
            if target.action == "Defend":
                damage = damage / 20
            else:
                target.animation = "hit"
            Show("battle_attack", g = self, damage = damage, target = target, caster = caster)()

        def after_attack(self, damage, target, caster):
            target.health -= damage
            interupt = renpy.random.randint(-10, 20)
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
                damage = damage/20
            target.health -= damage
            if target.health < 1:
                target.health = 0
                self.turn = 3
            unit.action = None
            unit.animation = "idle"
            self.enemy_turn += 1 
            Hide("battle_enemy_attack")()




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
screen battle(enemies):
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
    on "show" action Function(g.set, enemies)

    style_prefix "battle"

    button align .0,.0:
        text "arc"
        action Show("btl_arc")

    # add "#fff9"
    for n,i in enumerate(g.enemies):
        vbox:
            anchor .5,1.0 align .5,.78
            offset positions[n]
            if i.action and not i.action == "Rest":
                add "battle_{}".format(i.action.lower()) align .5,.5
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
                    if g.action == "Attack":
                        action Function(g.attack, main_fighter, i)
                add "{} {}".format(i.name.lower(), i.animation)

    vbox spacing 8 align .5,1.0 yoffset -20:
        if g.turn == 0:
            hbox align .5,.5 spacing 8:
                if not g.action:
                    button:
                        text _("Attack")
                        if main_fighter.stamina >= main_fighter.strength/2:
                            action Function(g.set_action, "Attack")
                    button:
                        text _("Defend")
                        action Function(g.defend, main_fighter)
                    button:
                        text _("Spell")
                        action Show("battle_spell")
                    button:
                        text _("Item")
                        action Show("battle_item")
                    button:
                        text _("Rest")
                        action Function(g.rest, main_fighter)
                    button:
                        text _("Escape")
                        action Return()
                else:
                    button:
                        text _("Cancel")
                        action Function(g.set_action, None)
        elif g.turn == 1:
            timer .01 repeat True action Function(g.enemy_ai)
            text "Enemy's turn"
        elif g.turn == 2:
            timer .1 action Show("battle_enemy_set_action", g = g)

        fixed:
            bar value main_fighter.health range main_fighter.max_health xysize(800,25) left_bar "#900" right_bar "#9005"
            text "{} / {}".format(main_fighter.health, main_fighter.max_health) size 20
        fixed:
            bar value main_fighter.mana range main_fighter.max_mana xysize(800,25) left_bar "#006e99" right_bar "#006e9955"
            text "{} / {}".format(main_fighter.mana, main_fighter.max_mana) size 20
        fixed:
            bar value main_fighter.stamina range main_fighter.max_stamina xysize(800,25) left_bar "#996900" right_bar "#99960055"
            text "{} / {}".format(main_fighter.stamina, main_fighter.max_stamina) size 20
        text "Strength: {}  Agility: {}".format(main_fighter.strength, main_fighter.agility)

    if g.turn == 3:
        button:
            background None
            action NullAction()
        frame:
            vbox:
                text _("You're dead.")
                button:
                    text _("Exit")
                    action Return("Lost")
    elif g.turn == 4:
        button:
            background None
            action NullAction()
        frame:
            vbox:
                text _("You won.")
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
screen battle_spell():
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










default sketch = fighter("Sketch", 4)
default sketch1 = fighter("Sketch", 1, "Wizard")
default sketch2 = fighter("Sketch", 1, "Warrior")
default sketch3 = fighter("Sketch", 1, "Rogue")
default sketch4 = fighter("Sketch", 1, "Demon")

label battle_example:
    call screen battle([sketch])
    call screen battle([sketch, sketch1, sketch2, sketch3, sketch4])


