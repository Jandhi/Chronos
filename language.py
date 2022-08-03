from chronology.change_set import ChangeSet
from orthography.orthography import Orthography


class Language:
    def __init__(self, name, short_form, orthography : Orthography) -> None:
        self.name = name
        self.short_form = short_form
        self.children : list[tuple[Language, ChangeSet]] = []
        self.orthography = orthography
    
    def add_child(self, child, changeset) -> None:
        self.children.append((child, changeset))
    
    def display_word(self, word):
        print(self.get_display_string(word))
    
    def get_display_string(self, word):
        s = f'{self.short_form}: {self.orthography.word_to_string(word)}'

        for child, changeset in self.children:
            s = f'{s} \t| {child.get_display_string(changeset.apply(word))}'
        
        return s

