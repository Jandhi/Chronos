
from operator import not_
from util import not_none
from word import Word

class Category:
    def __init__(self, features = None, not_features = None) -> None:
        self.features : set[str] = not_none(features, set())
        self.not_features : set[str] = not_none(not_features, set())

    def has(self, feature):
        self.features.add(feature)
        return self

    def without(self, feature):
        self.not_features.add(feature)
        return self

    def is_match(self, sound) -> bool:
        for feature in self.features:
            if feature not in sound:
                return False
        
        for feature in self.not_features:
            if feature in sound:
                return False
        
        return True

class Transform:
    def __init__(self, position, add_features = None, remove_features = None) -> None:
        self.position = position
        self.add_features : set[str] = not_none(add_features, set())
        self.remove_features : set[str] = not_none(remove_features, set())
    
    def add(self, feature):
        self.add_features.add(feature)
        return self
    
    def remove(self, feature):
        self.remove_features.add(feature)
        return self

    def get_fset(self, input):
        snd = input[self.position].copy()
        for ft in self.add_features:
            snd.add(ft)
        for ft in self.remove_features:
            if ft in snd:
                snd.remove(ft)
        
        return snd

class SoundChange:
    def __init__(self, 
            input : list[Category], 
            output : list[Transform], 
            prefix : list[Category] = None, 
            suffix : list[Category] = None, 
            direction : int = 1, 
            at_start = False, 
            at_end = False,
            exception_prefix : list[Category] = None,
            exception_suffix : list[Category] = None) -> None:
        self.input = input
        self.output = output
        self.prefix : list[Category] = not_none(prefix, [])
        self.suffix : list[Category] = not_none(suffix, [])
        self.direction = direction
        self.at_start = at_start
        self.at_end = at_end
        self.exception_prefix = exception_prefix
        self.exception_suffix = exception_suffix
    
    def apply(self, word : Word, start = 0) -> Word:
        i = start

        if (start == 0 and self.direction == -1) or self.at_end:
            i = len(word.sounds) - len(self.input)

        while i < len(word.sounds) and i >= 0:
            if self.at_start and i != 0:
                return word

            if self.is_match(word, i):
                return self.apply(*self.apply_to_match(word, i))
            
            i += self.direction

        return word

    def apply_to_match(self, word : Word, start) -> Word:
        end = start + len(self.input)
        prefix = word.sounds[:start]
        input = word.sounds[start : end]
        suffix = word.sounds[end:]

        sounds = []

        for result in self.output:
            sounds.append(result.get_fset(input))
        
        return Word.from_sounds(prefix + sounds + suffix), len(prefix) + len(sounds)

    def is_match(self, word : Word, start) -> Word:
        sounds = word.sounds
        end = start + len(self.input)

        if end > len(sounds):
            return False

        if len(self.prefix) > start or len(self.suffix) > len(sounds) - end:
            return False
        
        for i in range(len(self.prefix)):
            cat = self.prefix[i]
            sound = sounds[start - len(self.prefix) + i]

            if not cat.is_match(sound):
                return False
        
        for i in range(len(self.input)):
            cat = self.input[i]
            sound = sounds[start + i]

            if not cat.is_match(sound):
                return False

        for i in range(len(self.suffix)):
            cat = self.suffix[i]
            sound = sounds[end + i]

            if not cat.is_match(sound):
                return False
        
        if self.exception_prefix is not None:
            for i in range(len(self.exception_prefix)):
                cat = self.exception_prefix[i]

                if start - len(self.exception_prefix) + i < 0:
                    break

                sound = sounds[start - len(self.exception_prefix) + i]

                if not cat.is_match(sound):
                    break
                
                if i == len(self.exception_prefix) - 1:
                    return False
        
        if self.exception_suffix is not None:
            for i in range(len(self.exception_suffix)):
                cat = self.exception_suffix[i]

                if end + i >= len(sounds):
                    break

                sound = sounds[end + i]

                if not cat.is_match(sound):
                    break
                
                if i == len(self.exception_suffix) - 1:
                    return False
        
        return True