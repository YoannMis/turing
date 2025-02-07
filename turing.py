"""
MACHINE DE TURING

version: 1.0
date: 29.nov.2024
author: J@nu$
"""

from time import sleep
from colorama import Fore, Style
from enum import Enum


class TextColor(Enum):
    RIBBON = Fore.LIGHTBLUE_EX
    HEAD = f"{Fore.WHITE}{Style.BRIGHT}"
    BRACES = Fore.RED
    STATE = Fore.MAGENTA
    RESET = Style.RESET_ALL


class Turing:
    def __init__(self, program: str, ribbon: str, init_state: str, final_states: set[str], head: int):
        """Initialise la Classe.

        Args:
            program (str): suite d'instructions à suivre par la machine de Turing
            ribbon (str): état du ruban au départ
            init_state (str): état initial de la machine de Turing
            final_states (set): ensemble des états finaux qui marquent l'arrêt de la machine de Turing
            head (int): position de départ de la tête de lecture sur le ruban
        """
        self.program = program
        self.ribbon = ribbon
        self.init_state = init_state
        self.final_states = final_states
        self.head = head
        self.cur_state = init_state  # état courant de la machine de Turing
        self.instructions = self.convert_program()  # dictionnaire des différentes instructions du programme

    @property
    def split_ribbon(self) -> list[str]:
        """Convertit le contenu du ruban en une liste.

        Returns (list): liste contenant les symbols inscrits sur le ruban
        """
        return [symbol for symbol in self.ribbon]

    @property
    def read(self) -> str:
        """Renvoie l'élément du ruban qui est lu par la tête de lecture.

        Returns (str): élément lu par la tête de lecture
        """
        return self.ribbon[self.head]

    @property
    def instruction(self):
        return self.instructions[self.cur_state + self.read]

    def write(self, symbol: str) -> None:
        """Permet d'écrire un symbol sur le ruban au niveau de la tête de lecture.

        Args:
            symbol (str): symbol à écrire

        Returns: None
        """
        if symbol != " ":
            ribbon = self.split_ribbon
            ribbon[self.head] = symbol
            self.ribbon = "".join(ribbon)

    def move(self, direction: str) -> None:
        """Permet de déplacer la tête de lecture en fonction de
        la direction donnée en argument.

        Args:
            direction (str): direction donnée "<" ou ">"

        Returns: None
        """
        if direction == "<":
            self.head -= 1
        elif direction == ">":
            self.head += 1

    def convert_program(self) -> dict:
        """Convertit le programme donné à la machine de Turing en dictionnaire
        permettant de différencier les différentes instructions du programme.

        Returns (dict): {état de la machine avec le symbol lu par la tête de lecture:
                         l'instruction qui en découle}
        """
        # Liste des instructions du programme en récupérant dans le programme chaque instruction
        # par groupe de 5 caractères.
        instructions = [self.program[i:i + 5] for i in range(0, len(self.program), 5)]
        return {instruction[:2]: instruction for instruction in instructions}

    def mainloop(self) -> None:
        """Lance la machine de Turing jusqu'à ce que la machine soit
        dans un des états d'arrêt donné par le programme.

        Returns: None
        """
        while self.cur_state not in self.final_states:
            print(self)  # Afficher le ruban
            # Récupérer les différentes étapes de l'instruction en cours
            # s: State; r: Read; w: Write; m: Move; n: New state
            s, r, w, m, n = self.instruction
            self.write(w)  # Écrire sur le ruban le symbole correspondant à l'instruction
            self.move(m)  # Déplacer la tête de lecture selon l'instruction
            if n != " ":
                self.cur_state = n  # Changer l'état de la machine de Turing

            sleep(1)  # Délay de 1 sec entre chaque affiche du ruban

    def __str__(self) -> str:
        # Afficher le ruban en mettant en évidence où est la tête de lecture ainsi que l'état de la machine de Turing
        return (f"{TextColor.RESET.value}ribbon: {TextColor.RIBBON.value}{self.ribbon[:self.head]}"
                f"{TextColor.HEAD.value}{self.ribbon[self.head]}{TextColor.RESET.value}"
                f"{TextColor.RIBBON.value}{self.ribbon[self.head+1:]}"
                f"{TextColor.BRACES.value}[{TextColor.STATE.value}{self.cur_state}{TextColor.BRACES.value}]")


if __name__ == '__main__':
    turing1 = Turing("a_ < a0  pa1  i", "10110001__", "a", {"p", "i"}, 9)
    turing1.mainloop()
    turing2 = Turing("a_ < a0  pa1  i", "10110010__", "a", {"p", "i"}, 9)
    turing2.mainloop()
    turing3 = Turing("a_ > a10>ba01>bb10> b01> b_  @", "_10110001_", "a", {"@"}, 0)
    turing3.mainloop()
