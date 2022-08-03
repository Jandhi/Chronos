

from chronology.sound_change import Category, SoundChange, Transform
from phonology.features import Consonant, Vowel
from phonology.sound import Sound
from util import DIGITS, min_index
from word import Word


def post_symbol(feature, symbol):

    def filter(sound : set):
        return feature in sound

    def rfilter(string : str):
        return string.endswith(symbol)

    def func(sound : set, orthography : Orthography):
        new_sound = sound.copy()
        new_sound.remove(feature)

        return f'{orthography.sound_to_string(new_sound)}{symbol}'
    
    def rfunc(string : str, orthography : Orthography):
        snd : set = orthography.string_to_sound(string[:-1])

        if snd is None:
            return snd

        snd.add(feature)
        return snd

    return filter, func, rfilter, rfunc

class Orthography:
    def __init__(self, 
        name, processors, symbols
    ) -> None:
        self.name = name
        self.processors = processors
        self.symbols = symbols
    
    def sound_to_string(self, sound):
        for filter, func, rfilter, rfunc in self.processors:
            if filter(sound):
                return func(sound, self)
        
        for snd, string in self.symbols:
            if snd == sound:
                return string
        
        print(f'Could not write the sound {sound}')
    
    def word_to_string(self, word : Word):
        string = ''

        for sound in word.sounds:
            string = f'{string}{self.sound_to_string(sound)}'
        
        return string
    
    def string_to_sound(self, string) -> set:
        for filter, func, rfilter, rfunc in self.processors:
            if rfilter(string):
                snd = rfunc(string, self)

                if snd is not None:
                    return snd
        
        for snd, symbol in self.symbols:
            if string == symbol:
                return snd.copy()
        
        return None
    
    def string_to_word(self, string):
        sounds = []

        while len(string) > 0:
            length = len(string)

            while length > 0:
                substring = string[:length]

                sound = self.string_to_sound(substring)

                if sound is None:
                    length -= 1
                else:
                    string = string[length:]
                    sounds.append(sound)
                    break
            
            if length == 0:
                print(f'Could not translate string {string}')
                return
        
        return Word.from_sounds(sounds)
    
    def print_word(self, word : Word):
        print(self.word_to_string(word))
    
    def print_syllables(self, word : Word):
        s = ''
        for syllable in word.syllables:
            s = f'{s}{self.word_to_string(syllable.to_word())}.'

        print(s[:-1])
    
    def parse_match(self, string : str):
        list = []

        while len(string) > 0:
            if string.startswith('C') or string.startswith('V') or string.startswith('?'):
                end = string.index(']')
                cat = Category()

                if string.startswith('C'):
                    cat.features.add(Consonant)
                elif string.startswith('V'):
                    cat.features.add(Vowel)

                fset = string[2:end].split(',')

                for feature in fset:
                    if feature.startswith('+'):
                        cat.features.add(feature[1:])
                    else:
                        cat.not_features.add(feature[1:])

                list.append(cat)
                string = string[end + 1:]

            elif 'C' in string or 'V' in string or '?' in string:
                end = min_index(string, 'C', 'V', '?')

                word = self.string_to_word(string[:end])

                for fset in word.sounds:
                    list.append(Sound(fset))
                
                string = string[end:]
            else:
                word = self.string_to_word(string)
                
                for fset in word.sounds:
                    list.append(Sound(fset))
                
                string = ''
        
        return list
    
    def parse_result(self, string : str):
        list = []

        while len(string) > 0:
            if any(string.startswith(x) for x in DIGITS):
                end = string.index(']')
                transform = Transform(int(string[0]))

                fset = string[2:end].split(',')

                for feature in fset:
                    if feature.startswith('+'):
                        transform.add(feature[1:])
                    else:
                        transform.remove(feature[1:])

                list.append(transform)
                string = string[end + 1:]

            elif any(x in string for x in DIGITS):
                end = min_index(string, *DIGITS)

                word = self.string_to_word(string[:end])

                for fset in word.sounds:
                    list.append(Sound(fset))
                
                string = string[end:]
            else:
                word = self.string_to_word(string)
                
                for fset in word.sounds:
                    list.append(Sound(fset))
                
                string = ''
        
        return list
    
    def parse_sc(self, string : str):
        direction = 1

        if string.endswith('<<'):
            string = string[:-2]
            direction = -1

        first_split = string.split('->')
        input = self.parse_match(first_split[0].strip())

        second_split = first_split[1].split('/')
        output = self.parse_result(second_split[0].strip())

        prefix = None
        suffix = None
        at_start = False
        at_end = False

        if len(second_split) > 1:
            third_split = second_split[1].split('_')
            prefix_string = third_split[0].strip()
            if prefix_string.startswith('#'):
                at_start = True
                prefix_string = prefix_string[1:]
            prefix = self.parse_match(prefix_string)

            suffix_string = third_split[1].strip()
            if suffix_string.endswith('#'):
                at_end = True
                suffix_string = suffix_string[:-1]
            suffix = self.parse_match(suffix_string)
        
        return SoundChange(input, output, prefix, suffix, direction, at_start, at_end)