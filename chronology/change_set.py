from chronology.sound_change import SoundChange
from word import Word


class ChangeSet:
    def __init__(self, sound_changes : list[SoundChange]) -> None:
        self.sound_changes = sound_changes
    
    def apply(self, word) -> Word:
        for sc in self.sound_changes:
            word = sc.apply(word)
        
        return word

class ParallelSet:
    def __init__(self, sound_changes : list[SoundChange]) -> None:
        self.sound_changes = sound_changes
    
    def apply(self, word) -> Word:
        for sc in self.sound_changes:
            new_word = sc.apply(word)

            if new_word != word:
                return new_word
        
        return word