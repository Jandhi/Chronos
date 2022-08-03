

from phonology.features import Long, Overlong, Rounded, Vocalic, Voiced, Vowel as vw, Consonant as cons
from util import not_none

class Sound:
    def __init__(self, features = None) -> None:
        self.features = not_none(features, set())

    def with_feature(self, feature):
        self.features.add(feature)
        return self

    def make(self) -> set:
        return self.features
    
    def is_match(self, other) -> bool:
        return self.features == other
    
    def get_fset(self, input):
        return self.features.copy()

class Vowel(Sound):
    def __init__(self, openness, backness) -> None:
        super().__init__()
        self.features.add(vw)
        self.features.add(openness)
        self.features.add(backness)
    
    def rounded(self):
        self.features.add(Rounded)
        return self

class Consonant(Sound):
    def __init__(self, place_of_articulation, manner_of_articulation) -> None:
        super().__init__()
        self.features.add(cons)
        self.features.add(place_of_articulation)
        self.features.add(manner_of_articulation)
    
    def voiced(self):
        self.features.add(Voiced)
        return self

def is_vocalic(snd):
    return vw in snd or Vocalic in snd

def is_light_vowel(snd):
    return vw in snd and Long not in snd and Overlong not in snd