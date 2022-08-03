from phonology.features import Consonant, Long
from phonology.sound import is_light_vowel, is_vocalic


class Syllable:
    def __init__(self) -> None:
        self.pre = []
        self.core = []
        self.post = []
    
    def sounds(self):
        return self.pre + self.core + self.post
    
    def to_word(self):
        return Word.from_sounds(self.sounds())

class Word:
    def __init__(self) -> None:
        self.sounds : list[set[str]] = []
        self.syllables : list[Syllable] = []

    @classmethod
    def from_sounds(cls, sounds : list[set[str]]):
        word = Word()
        word.sounds = sounds
        word.syllables = get_syllables(sounds)
        return word
    
    @classmethod
    def from_syllables(cls, syllables : list[Syllable]):
        word = Word()
        word.syllables = syllables
        
        for syllable in syllables:
            for sound in syllable.sounds():
                word.sounds.append(sound)
        
        return word
    
    def __eq__(self, __o: object) -> bool:
        return self.sounds == __o.sounds

def get_syllables(sounds):
    syllables = []

    curr_syllable = Syllable()

    for i in range(len(sounds)):
        prev = sounds[i - 1] if i > 0 else None
        sound = sounds[i]
        next = sounds[i + 1] if i < len(sounds) - 1 else None

        if Consonant in sound:
            if len(curr_syllable.core) == 0:
                curr_syllable.pre.append(sound)
            elif (next is not None and is_vocalic(next)) or (prev is not None and not is_vocalic(prev)):
                syllables.append(curr_syllable)
                curr_syllable = Syllable()
                curr_syllable.pre.append(sound)
            else:
                curr_syllable.post.append(sound)
        else:
            # vowel
            if len(curr_syllable.core) == 0 or (len(curr_syllable.core) == 1 and is_light_vowel(curr_syllable.core[0]) and is_light_vowel(sound)):
                curr_syllable.core.append(sound)
            else:
                syllables.append(curr_syllable)
                curr_syllable = Syllable()
                curr_syllable.core.append(sound)
    
    if len(curr_syllable.core) > 0:
        syllables.append(curr_syllable)

    return syllables