import logging
import random

from utils.grid import Button, SliderLikeElement, Switch, Actions, GridElement
from utils.special_commands import DummyBlackHoleCommand, DummyAsteroidCommand, SpecialCommand


class Instruction:
    def __init__(self, source, target, target_command):
        self.source = source
        self.target = target
        self.target_command = target_command
        self.value = self.generate_value()  # new value to set the target command to. Only for sliders/switches
        self.text = self.generate_text()    # instruction text, visible to the client

    def generate_value(self):
        if type(self.target_command) is Button:
            # No extra actions required for buttons
            return None
        elif issubclass(type(self.target_command), SpecialCommand):
            # Same for asteroids and black holes
            return None
        elif issubclass(type(self.target_command), SliderLikeElement):
            # For slider-like elements, pick a new random value between min and max, excluding the current one
            return random.choice([x for x in range(self.target_command.min, self.target_command.max + 1) if x != self.target_command.value])
        elif type(self.target_command) is Switch:
            # If it's a switch, flip it
            return not self.target_command.toggled
        elif type(self.target_command) is Actions:
            return random.choice(self.target_command.actions)

    def generate_text(self):
        if type(self.target_command) is Button:
            sentences = [
                "Operate {name}",
                "Insert {name}",
                "Press {name}"
            ]
        elif issubclass(type(self.target_command), SliderLikeElement):
            sentences = [
                "Set {name} to {value}",
                "Change {name} to {value}",
                "Place {name} on {value}"
            ]
            if self.value > self.target_command.value:
                sentences.append("Increase {name} a {value}")
            else:
                sentences += ["Decrease {name} a {value}", "Reduce {name} a {value}"]

            if self.value == self.target_command.max:
                sentences += ["Increase {name} to maximum", "Set {name} to maximum"]
            elif self.value == self.target_command.min:
                sentences += ["Decrease {name} to minimum", "Set {name} to minimum"]
        elif type(self.target_command) is Actions:
            sentences = ["{value} {name}"]
        elif type(self.target_command) is Switch:
            # Switch
            if self.value:
                sentences = [
                    "Activate {name}",
                    "Engage {name}",
                    "Switch on {name}",
                ]
            else:
                sentences = [
                    "Deactivate {name}",
                    "Disengage {name}",
                    "Switch off {name}",
                ]
        elif type(self.target_command) is DummyAsteroidCommand:
            sentences = ["Asteroid! (everyone shake the mouse)"]
        elif type(self.target_command) is DummyBlackHoleCommand:
            sentences = ["Black hole! (press enter multiple times)"]
        else:
            raise ValueError("Invalid command type")

        # Choose a random sentence form the possible ones and format it
        sentence = random.choice(sentences)
        if issubclass(type(self.target_command), GridElement):
            if "symbol" in self.target_command.additional_data:
                name = "${}".format(self.target_command.name)
            else:
                name = self.target_command.name
        else:
            name = ""
        s = sentence.format(name=name, value=self.value.capitalize() if type(self.value) is str else self.value)
        return s
