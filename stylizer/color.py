from typing import Any

class Style:

    def __init__(self):

        # Styles de texte
        self.RESET = "0m"
        self.BOLD = "1m"
        self.DIM = "2m"
        self.ITALIC = "3m"
        self.UNDERLINE = "4m"
        self.DOUBLE_UNDERLINE = "21m"
        self.BLINK = "5m"
        self.RAPID_BLINK = "6m"
        self.REVERSE = "7m"
        self.HIDDEN = "8m"
        self.STRIKETHROUGH = "9m"
        self.FRAME = "51m"
        self.ENCIRCLE = "52m"
        self.OVERLINE = "53m"

        self.PROPORTIONAL_FONT = "10m"  # Police proportionnelle
        self.VARIABLE_WIDTH = "11m"  # Largeur variable
        self.FONT = "12m"  # Choix de police
        self.FONT2 = "13m"  # Autre police
        self.FONT3 = "14m"  # Autre police
        self.FONT4 = "15m"  # Autre police

        # Couleurs texte
        self.BLACK = "30m"
        self.RED = "31m"
        self.GREEN = "32m"
        self.YELLOW = "33m"
        self.BLUE = "34m"
        self.MAGENTA = "35m"
        self.CYAN = "36m"
        self.WHITE = "37m"
        self.DEFAULT = "39m"

        # Couleurs texte haute intensité
        self.BRIGHT_BLACK = "90m"
        self.BRIGHT_RED = "91m"
        self.BRIGHT_GREEN = "92m"
        self.BRIGHT_YELLOW = "93m"
        self.BRIGHT_BLUE = "94m"
        self.BRIGHT_MAGENTA = "95m"
        self.BRIGHT_CYAN = "96m"
        self.BRIGHT_WHITE = "97m"

        # Couleurs de fond
        self.BG_BLACK = "40m"
        self.BG_RED = "41m"
        self.BG_GREEN = "42m"
        self.BG_YELLOW = "43m"
        self.BG_BLUE = "44m"
        self.BG_MAGENTA = "45m"
        self.BG_CYAN = "46m"
        self.BG_WHITE = "47m"
        self.BG_DEFAULT = "49m"

        # Couleurs de fond haute intensité
        self.BG_BRIGHT_BLACK = "100m"
        self.BG_BRIGHT_RED = "101m"
        self.BG_BRIGHT_GREEN = "102m"
        self.BG_BRIGHT_YELLOW = "103m"
        self.BG_BRIGHT_BLUE = "104m"
        self.BG_BRIGHT_MAGENTA = "105m"
        self.BG_BRIGHT_CYAN = "10m"
        self.BG_BRIGHT_WHITE = "107m"

        # Effacement du terminal et des lignes
        self.CLEAR_LINE = "2K"  # Efface la ligne actuelle
        self.CLEAR_SCREEN = "2J"  # Efface tout le terminal
        self.CLEAR_TO_END = "0J"  # Efface du curseur à la fin
        self.CLEAR_TO_START = "1J"  # Efface du curseur au début
        self.CLEAR_FROM_CURSOR = "K"  # Efface de la position du curseur à la fin de la ligne
        self.CLEAR_START_TO_CURSOR = "1K"  # Efface de la position du curseur au début de la ligne

        # Manipulation du curseur
        self.MOVE_UP = "A"  # Déplacer le curseur vers le haut
        self.MOVE_DOWN = "B"  # Déplacer le curseur vers le bas
        self.MOVE_RIGHT = "C"  # Déplacer le curseur vers la droite
        self.MOVE_LEFT = "D"  # Déplacer le curseur vers la gauche
        self.MOVE_TO_TOP_LEFT = "H"  # Déplacer le curseur en haut à gauche
        self.MOVE_TO_BOTTOM_LEFT = "F"  # Déplacer le curseur en bas à gauche

        # Autres effets
        self.UNDERLINE_OFF = "24m"  # Désactive le soulignement
        self.BLINK_OFF = "25m"  # Désactive le clignotement
        self.REVERSE_OFF = "27m"  # Désactive l'inversion des couleurs
        self.HIDDEN_OFF = "28m"  # Rend le texte visible
        self.STRIKETHROUGH_OFF = "29m"  # Désactive le texte barré
        self.DOUBLE_UNDERLINE_OFF = "24m"  # Désactive le double soulignement

        for key, value in self.__dict__.items():
            self.__dict__[key] = f"\033[{value}"





    def color_arg(self, arg: Any, *colors: str) -> str:
        """
        Color any args from the param "color".
        EX : color_arg("My arg", BLUE, BOLD, ITALIC)

        :param colors: Property from "Style" class.
        :param arg: Any
        :return: A string like "\033[5mMY ARG\033[0m"
        """
        # Accède à RESET via la classe, pas l'instance, pour éviter __getattribute__
        return f"{''.join(colors)}{arg}{self.RESET}"

    def get_progress_bar(self):  # Supprime le type hint incorrect
        """
        Get a progress_bar
        """
        return ProgressBar()  # Retourne une instance de ProgressBar

    def __str__(self) -> str:
        """
        Make all to default value
        :return:
        """
        return self.DEFAULT  # Accède via la classe


class ProgressBar:

    def __init__(self, length: int = 50, fill_caracter = '#', empty_caracter = '~'):
        """
        Init a progress bar
        :param length: the progress bar length in caract
        """
        self.__length = length
        self.__fill_caracter = fill_caracter
        self.__empty_caracter = empty_caracter

        self.__stat = 0

        self.__style = Style()

    def print(self) -> None:
        """
        Print the progress bar in a terminal
        :return:
        """
        print(f"{self.__style.CLEAR_LINE}[{''.join([self.__style.color_arg(self.__fill_caracter, self.__style.GREEN) for _ in range(self.__stat)])}{''.join([self.__empty_caracter for _ in range(self.__length - self.__stat)])}]{self.__stat}%", end='\r')

    def update(self, iteration: int, current_iteration: int) -> None:
        """

        :param iteration: Total iteration to end a task
        :param current_iteration: the current iteration
        :return:
        """
        self.__stat = (current_iteration*100)//iteration
        self.print()

s = Style()
bar = s.get_progress_bar()
import time
for i in range(150):
    bar.update(iteration=150, current_iteration=i+1)
    time.sleep(1)
