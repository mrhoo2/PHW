from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
        pass


class Death(scene):

    def enter(self):
        print(f"You have died due to dysentery. Congrats!")
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            Quick on the draw, you yank out your blaster and fire
            it at the Gothon. His clown costume is flowing and
            moving around his body, which throws off your aim.
            Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother
            bought him, which makes him fly into an insane rage
            and blast you repeatedly in the face until you are
            dead. Then he eats you.
            """))
            return('death')

        elif action == "dodge!":
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and
            slide right as the Gothon's blaster cranks a laser
            past your head. In the middle of your artful dodge
            your foot slips and you band your head on the metal
            wall and pass out. You wake up shortly after only to
            die as the Gothon stomps on your head and eats you.
            """))
            return('death')

        elif action == "tell a joke":
            print(dedent("""
            Lucky for you they made you learn Gothon insults in
            the academy. You tell the one Gothon joke you know:
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
            fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
            not to laugh, then busts out laughing and can't move.
            While he's laughing you run up and shoot him square in
            the head putting him down, then jump through the
            Weapon Armory door.
            """))
            return('laser_weapon_armory')

        else:
            print("DOES NOT COMPUTE!")
            return('central_corridor')


class LaserWeaponArmory(Scene):

    def enter(self):
        try:
            keycode = input("You enter a vast, cathedral-style room. It is ",
                            "full of weapons. This is clearly the laser ",
                            "armory. You spot a door in the center with a ",
                            "number pad on it. What four numbers do you ",
                            "press?")
            if keycode == password:
                a_map = Map('TheBridge')
                # a_game = Engine(a_map)
                # a_game.play()
        except TypeError:
            print("The keypad shocks you, paralyzing your muscles. You hear",
                  " an alarm, and you see several Gothons coming your way.",
                  "/nThe room fades to white.")

            a_map = Map('Death')
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

while True:
    