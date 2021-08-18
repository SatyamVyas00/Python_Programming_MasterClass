import random


class Player:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives > 0:
            self._lives = lives
        else:
            print("Lives cannot be Negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += 1000 * delta
            self._level = level
        else:
            print("Level can't be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)


# both the declaration of player and  enemy class is correct method
class Enemy(object):
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{0._name} took {1} points damage and have {0._hit_points} left".format(self, damage))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit Points: {0._hit_points}".format(self)


# Inheritance (Troll inherits Enemy Class)
class Troll(Enemy):
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampire(Enemy):
    def __init__(self, name):
        super(Vampire, self).__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("**** {0._name} doges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super(Vampire, self).take_damage(damage=damage)


class VampireKing(Vampire):
    def __init__(self, name):
        super(VampireKing, self).__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        super(VampireKing, self).take_damage(damage//4)


# Main
# player1 = Player("Player 1")
# print(player1)
#
# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# random_monster.take_damage(8)
# random_monster.take_damage(8)
# print(random_monster)
#
# ugly_troll = Troll("Pug")
# print("Ugly Troll - {}".format(ugly_troll))
#
# another_troll = Troll("ug")
# print("Another Troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp = Vampire("vamp")
# print(vamp)
#
# print("*"*80)
# while ugly_troll._alive:
#     ugly_troll.take_damage(1)
#     print(ugly_troll)
#
# print("*"*80)
# while vamp._alive:
#     vamp.take_damage(1)
#     # print(vamp)

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)
