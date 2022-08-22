from chronology.change_set import ChangeSet
from orthography.orthography import Orthography
from util import count_combining


class Language:
    def __init__(self, name, short_form, orthography : Orthography, do_display = True) -> None:
        self.name = name
        self.short_form = short_form
        self.children : list[tuple[Language, ChangeSet]] = []
        self.orthography = orthography
        self.do_display = do_display
    
    def add_child(self, child, changeset) -> None:
        self.children.append((child, changeset))
    
    def display_word(self, word):
        print(self.get_display_string(word))
    
    def get_display_string(self, word):
        if not self.do_display:
            return ''

        s = f'{self.short_form}: {self.orthography.word_to_string(word)}'
        # spacing
        s = s.ljust(12 + len(self.short_form) + count_combining(s))

        for child, changeset in self.children:
            s = f'{s}| {child.get_display_string(changeset.apply(word))}'
        
        return s

