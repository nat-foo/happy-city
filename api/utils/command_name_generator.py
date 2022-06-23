import random

from singletons.words_storage import WordsStorage


class CommandNameGenerator:
    def __init__(self, words_storage=None):
        if words_storage is None:
            words_storage = WordsStorage()
        self.words_storage = words_storage
        self.used_nouns = []
        self.used_adjectives = []
        self.used_verbs = []

    def random_noun(self, role=0):
        print(f"NOUN: ROLE IS {role}")
        if role == 0:
            nouns = random.choice([self.words_storage.ROLE_0["nouns"] * 4, self.words_storage.ROLE_0["rare_nouns"]])
        elif role == 1:
            nouns = random.choice([self.words_storage.ROLE_1["nouns"] * 4, self.words_storage.ROLE_1["rare_nouns"]])
        elif role == 2:
            nouns = random.choice([self.words_storage.ROLE_2["nouns"] * 4, self.words_storage.ROLE_2["rare_nouns"]])
        elif role == 3:
            nouns = random.choice([self.words_storage.ROLE_3["nouns"] * 4, self.words_storage.ROLE_3["rare_nouns"]])
        noun = random.choice(nouns).lower()
        print (f"NOUN: Picked '{noun}' for role {role}.")
        return noun

    def random_adjective(self, role=0):
        print(f"ADJ: ROLE IS {role}")
        if role == 0:
            adjectives = random.choice([self.words_storage.ROLE_0["adjectives"] * 4, self.words_storage.ROLE_0["rare_adjectives"]])
        elif role == 1:
            adjectives = random.choice([self.words_storage.ROLE_1["adjectives"] * 4, self.words_storage.ROLE_1["rare_adjectives"]])
        elif role == 2:
            adjectives = random.choice([self.words_storage.ROLE_2["adjectives"] * 4, self.words_storage.ROLE_2["rare_adjectives"]])
        elif role == 3:
            adjectives = random.choice([self.words_storage.ROLE_3["adjectives"] * 4, self.words_storage.ROLE_3["rare_adjectives"]])
        adjective = random.choice(adjectives).lower()
        print (f"ADJECTIVE: Picked '{adjective}' for role {role}.")
        return adjective

    def generate_noun(self, role):
        i = 0
        while True:
            noun = self.random_noun(role)
            if (noun not in self.used_nouns):
                break
            if (i >= len(self.used_nouns)):
                noun = None
                break
            i += 1
        if noun is not None: self.used_nouns.append(noun)
        return noun

    def generate_compound_noun(self, role):
        prefix = random.choice(self.words_storage.PREFIXES).lower()

        i = 0
        while True:
            noun = self.random_noun(role)
            if (noun not in self.used_nouns):
                break
            if (i >= len(self.used_nouns)):
                noun = None
                break
            i += 1

        if noun is not None: self.used_nouns.append(noun)

        if prefix.endswith(noun[0]):
            prefix += "-"
        elif " " in noun:
            prefix += " "
        prefixNoun = f"{prefix}{noun}"
        return prefixNoun

    def generate_adjective_noun(self, role):
        i = 0
        while True:
            noun = self.random_noun(role)
            if (noun not in self.used_nouns):
                break
            if (i >= len(self.used_nouns)):
                noun = None
                break
            i += 1

        if noun is not None: self.used_nouns.append(noun)

        i = 0
        while True:
            adjective = self.random_adjective(role)
            if (adjective not in self.used_adjectives):
                break
            if (i >= len(self.used_adjectives)):
                adjective = None
                break
            i += 1
        
        if adjective is not None: self.used_adjectives.append(adjective)

        return "{} {}".format(adjective, noun)

    def generate_command_name(self, role=0):
        generation_options = []
        cname

        if self.words_storage.USE_PREFIXES == True:
            cname = self.generate_compound_noun(role)
            if cname is not None:
                generation_options.append(cname)
        else:
            cname = self.generate_noun(role)
            if cname is not None:
                generation_options.append(cname)

        cname = self.generate_adjective_noun(role)
        if cname is not None:
            generation_options.append(cname)

        if len(generation_options) == 0:
            return None

        return random.choice(generation_options)

    def generate_action(self):
        i = 0
        while True:
            verb = random.choice(self.words_storage.VERBS)
            if verb not in self.used_verbs:
                break
            if (i >= len(self.used_verbs)):
                verb = None
                break
            i += 1
        if verb is not None: self.used_verbs.append(verb)
        return verb
