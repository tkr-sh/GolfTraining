###########
# IMPORTS #
###########
from os import system, name
from questions import questions
import random
import time
import string
import sys


# Changing maximum recursion
sys.setrecursionlimit(999999)


# Default value list
string_lower = string.ascii_lowercase
string_upper = string.ascii_uppercase
string_uplow = string.ascii_letters
digits = string.digits
ints = range(-99, 100)
uints = range(100)
floats = [*map(lambda n:n*.1,range(-1000, 1000))]



# Main
class Training:

    playing: bool = False
    games: int = 1
    selected_lang: str
    response: str
    correct: int = 0
    incorrect: int = 0

    def __init__(self) -> None:
        pass

    # Clear
    def clear(self) -> None:
        """ Function to clear the terminal """
        _ = system('cls') if name == 'nt' else system('clear')


    # Help function
    def help(self) -> None:

        """ List of commands"""

        lst = ['h: For help', 'menu: for the main menu', 'exit: To exit the program', "s: For Solution", "ENTER: To start or to submit input"]
        for e in lst:
            print(f"- {e}")
    

    # Start
    def start(self) -> None:

        """ The introduction Screen """

        self.clear()
        print("""
        ________        __   ________________              __        __
       /  _____/  ____ |  |_/ ____\__    ___/___________  |__| ____ |__| ____    ____
      /   \  ___ /  _ \|  |\   __\  |    |  \_  __ \__  \ |  |/    \|  |/    \  / __ \ 
      \    \_\  \  <_> )  |_|  |    |    |   |  | \// __ \|  |   |  \  |   |  \/ /_/  >
       \______  /\____/|____/__|    |____|   |__|  (____  /__|___|  /__|___|  /\___  /
              \/                                        \/        \/        \//_____/
          =========================================================================
                    PRESS - ENTER to START        PRESS - H for HELP
                                           v0.0.0
        """)
        self.main_menu()


    # Main menu
    def main_menu(self) -> None:

        """ The main menu """

        waiting_for_input = True
        # Basic input
        while waiting_for_input:
            response = input(">>> ").lower()
            waiting_for_input = response not in ["","h"]
            if waiting_for_input:
                print("Not a valid input. You should input '' or 'h'")
        
        match response:
            case 'h':
                self.help()
                self.main_menu()
            case _:
                self.select_lang()
                self.main_loop()


    # Select a lang
    def select_lang(self) -> None:
        self.clear()
        print("""__________ __        __                   __
\______   \__| ____ |  | __   _____      |  | _____    ____    ____
 |     ___/  |/ ___\|  |/ /   \__  \     |  | \__  \  /    \  / __ \ 
 |    |   |  \  \___|    <     / __ \_   |  |__/ __ \|   |  \/ /_/  >
 |____|   |__|\___  >__|_ \   (____  /   |____(____  /___|  /\___  /
                  \/     \/        \/              \/     \//_____/
    - [\033[38;5;220mP\033[39m]ython
    - [\033[38;5;160mR\033[39m]uby
""")
        corr = {"p": "python", "r": "ruby"}
        while (lang:=input(">>> ").lower()) not in corr:
            pass
        self.selected_lang = corr[lang]
        print(self.selected_lang)


    # Main loop
    def main_loop(self) -> None:

        """ Main loop of the training """

        self.clear()
        self.playing = True

        while self.playing:
            # Basic input
            new_questions = dict(filter(lambda x: x[1]["lang"] == self.selected_lang, questions.items()))
            n = random.choice(list(new_questions.keys()))

            ########
            # DATA #
            ########
            # Get the question
            question = questions[n]['question']
            # Get the answerss
            answers = questions[n]['response']
            answers_islist = type(answers) is list
            if answers_islist:
                answers = [*map(lambda answer: answer.replace("'",'"'), answers)]
            else:
                answers = answers.replace("'",'"')
            arguments_str = questions[n]['args']
            rules = questions[n]['rule'] if 'rule' in questions[n] else []
        

            # Converting arguments in letter to a real value
            def get_args() -> list:
                arguments = []
                i = 0

                # Get the arguments
                while i < len(arguments_str):
                    argument = arguments_str[i]
                    match argument:
                        case "s":
                            v = random.choice(string_lower)
                        case "S":
                            v = random.choice(string_uplow)
                        case "$":
                            v = random.choice(string_uplow)
                        case "d":
                            v = random.choice(digits)
                        case "i":
                            v = random.choice(ints)
                        case "u":
                            v = random.choice(uints)
                        case "f":
                            v = random.choice(floats)
                        case _:
                            v = None

                    if v in arguments:
                        continue
                    i += 1
                    arguments.append(v)
                
                b = True
                # Checking for rules
                for rule in rules:
                    new_rule = rule
                    for i in range(10):
                        new_rule=new_rule.replace(f"&&&{i}", f"arguments[{i-1}]")
                    b = eval(new_rule)
                    if not b:
                        break
        
                if not b:
                    arguments = get_args()

                return arguments


            # Put this value in a variable
            arguments = get_args()

            # Translating all the arguments in their value
            for i,elem in enumerate(arguments):
                if type(answers) == str:
                    answers = answers.replace(f"&&&{i+1}", str(elem))
                else:
                    answers = list(map(lambda s: s.replace(f"&&&{i+1}", str(elem)), answers))
                question = question.replace(f"&&&{i+1}", str(elem))

            # Statistics
            if self.games != 1:
                accuracy_str = "".join(f"\033[{31+(100*self.correct/~-self.games>10*i+5)}m#\033[39m" for i in range(10))
                print(f"Accuracy: [{accuracy_str}] - ({round(100 * self.correct / ~-self.games,2)}%)")
            print(f"Question N°{self.games}:\n{question}")
            
            # Getting the input
            response = input(">>> ").replace("'",'"')
            if response == 'h':
                self.help()
                response = input(">>> ").replace("'",'"')
            self.playing = response.lower() != "exit"


            # Action depending ont the input
            if not self.playing: # Stop Playing
                self.clear()
                print("Exiting the game...\n\033[3m\033[38;5;219mSee you next time!\033[39m\033[0m")
                time.sleep(1)
                sys.exit()
            elif response == "menu": # If it's the menu
                self.playing = False
                break
            elif response == "s": # If the user want the answer
                print(f"The solution was:\n{answers}")
                input("Press enter to continue\n")
            elif (answers_islist and response in answers) or (not answers_islist and response == answers): # Good
                print("\033[32mCorrect!\033[39m")
                self.correct += 1
                time.sleep(1)
            else: # Bad
                print(f"\033[31mWrong.\033[39m\nThe answer was `{answers}` not `{response}`")
                self.incorrect += 1
                input("Press enter to continue\n")

            self.clear()
            self.games += 1

        self.start()


# Main
if __name__ == '__main__':
    train = Training()
    train.start()