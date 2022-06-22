from utils.singleton import singleton


@singleton
class WordsStorage:
    def __init__(self):
        self.PREFIXES = [
            ""
        ]

        self.ROLE_0 = {
            "rare_nouns": [],
            "rare_adjectives": [],
            "nouns": [],
            "adjectives": []
        }

        self.ROLE_1 = {
            "rare_nouns": [],
            "rare_adjectives": [],
            "nouns": [],
            "adjectives": []
        }

        self.ROLE_2 = {
            "rare_nouns": [],
            "rare_adjectives": [],
            "nouns": [],
            "adjectives": []
        }

        self.ROLE_3 = {
            "rare_nouns": [],
            "rare_adjectives": [],
            "nouns": [],
            "adjectives": []
        }

        self.VERBS = []

    def load_nouns(self):
        lines = []
        with open("words/nouns.txt", "r") as f:
            lines += [(x.lower().strip(), False) for x in f.readlines()]
        with open("words/rare_nouns.txt", "r") as f:
            lines += [(x.lower().strip(), True) for x in f.readlines()]

        for (line, rare) in lines:
            parts = line.split(",")
            if len(parts) == 2:
                noun, role = parts
                if role == "0":
                    dest_list = self.ROLE_0["{}nouns".format("rare_" if rare else "")]
                elif role == "1":
                    dest_list = self.ROLE_1["{}nouns".format("rare_" if rare else "")]
                elif role == "2":
                    dest_list = self.ROLE_2["{}nouns".format("rare_" if rare else "")]
                elif role == "3":
                    dest_list = self.ROLE_3["{}nouns".format("rare_" if rare else "")]
                dest_list.append(noun)

            else:
                print(f"Warning: The word '{line}' in the {'RARE' if rare else ''} NOUNS wordlist wasn't configured correctly! Ensure each entry has a comma followed by its role.")

    def load_adjectives(self):
        lines = []
        with open("words/adjectives.txt", "r") as f:
            lines += [(x.lower().strip(), False) for x in f.readlines()]
        with open("words/rare_adjectives.txt", "r") as f:
            lines += [(x.lower().strip(), True) for x in f.readlines()]

        for (line, rare) in lines:
            parts = line.split(",")
            if len(parts) == 2:
                noun, role = parts
                if role == "0":
                    dest_list = self.ROLE_0["{}adjectives".format("rare_" if rare else "")]
                elif role == "1":
                    dest_list = self.ROLE_1["{}adjectives".format("rare_" if rare else "")]
                elif role == "2":
                    dest_list = self.ROLE_2["{}adjectives".format("rare_" if rare else "")]
                elif role == "3":
                    dest_list = self.ROLE_3["{}adjectives".format("rare_" if rare else "")]
                dest_list.append(noun)

            else:
                print(f"Warning: The word '{line}' in the {'RARE' if rare else ''} ADJECTIVES wordlist wasn't configured correctly! Ensure each entry has a comma followed by its role.")

    def load_verbs(self):
        with open("words/verbs.txt", "r") as f:
            self.VERBS = [x.lower().strip() for x in f.readlines()]

    def load(self):
        self.load_nouns()
        self.load_adjectives()
        self.load_verbs()