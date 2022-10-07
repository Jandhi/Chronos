from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

ProtoVolodnian = Language('Proto-Volodnian', 'PVol', SIPA)
EarlyVolodnian = Language('Early Volodnian', 'ErVol', SIPA)

PVol_to_EVol = ChangeSet([
    
    # U Umlaut
    sc(f'a -> o / _C[]V[+{Close},+{Rounded}]'),
    sc(f'e -> o / _C[]V[+{Close},+{Rounded}]'),
    sc(f'ā -> ō / _C[]V[+{Close},+{Rounded}]'),
    sc(f'ē -> ō / _C[]V[+{Close},+{Rounded}]'),
    sc(f'i -> u / _C[]V[+{Close},+{Rounded}] / a_'), # doesn't apply to ai
    sc(f'ī -> ū / _C[]V[+{Close},+{Rounded}]'),
    
    # Nasal Merger
    sc(f'ŋ -> n'),

    # Nasalization
    sc(f'V[]C[+{Nasal}] -> 0[+{Nasalized}] / _C[]'),
    sc(f'V[]C[+{Nasal}] -> 0[+{Nasalized}] / _#'),

    # Glide Prothesis
    sc(f'V[+{Front}] -> j0[] / #_'),
    sc(f'V[-{Front}] -> w0[] / #_'),

    # Short Vowel Merger
    sc(f'V[+{Close_mid},-{Long}] -> 0[+{Lengthened}] / #_'),
    sc(f'C[]V[+{Close_mid},-{Long}] -> 0[]1[+{Lengthened}] / #_'),
    sc(f'C[]C[]V[+{Close_mid},-{Long}] -> 0[]1[]2[+{Lengthened}] / #_'),
    sc(f'V[+{Close_mid},-{Long},-{Lengthened}] -> 0[-{Close_mid},+{Close}] // _j'),
    sc(f'V[+{Lengthened}] -> 0[-{Lengthened}]'),
])
ProtoVolodnian.add_child(EarlyVolodnian, PVol_to_EVol)

GreaterVolodnian = Language('Greater Volodnian', 'GVol', SIPA)
EVol_to_GVol = ChangeSet([
    # W hardening
    sc('w -> v'),

    # First Palatalization
    sc(f'x -> ʃ / _V[+{Front}]'),
    sc(f'ɣ -> ʒ / _V[+{Front}]'),
    sc(f'k -> t͡ʃ / _V[+{Front}]'),
    sc(f'g -> d͡ʒ / _V[+{Front}]'),

    # Nasal Vowel Merger
    sc(f'V[+{Close_mid},+{Nasalized}] -> 0[-{Close_mid},+{Open},-{Front},-{Back},-{Rounded},+{Central}]'),
])
EarlyVolodnian.add_child(GreaterVolodnian, EVol_to_GVol)

from vol.north_volodnian import *
GreaterVolodnian.add_child(NorthEasternVolodnian, GVol_to_NEVol)

from vol.south_volodnian import *
GreaterVolodnian.add_child(SouthWesternVolodnian, GVol_to_SWVol)

words = [
    #'xawrebi', 'xasimtā', 'nanauje'
    #'baluka', 'nēla', 'nēle', 'tikura', 'satura', 'bologuru', 'satebai', 'lotai', 'ausoru'
    #'epu', 'kibu', 'keti', 'borugu', 'sukateli', 'karit͡si', 'xagigi', 'xitoro', 'kesu', 'naŋau', 'mimare', 'axuta', 'boki', 'nanauwoj'
    'kesu', 'kesuwoj', 'kesuje', 'kesuxi', 'kesukā', 'kesukāwoj', 'kesukāje', 'kesukāxi',
    'epu', 'epunā', 'epuxa', 'epuwo', 'eput͡si',
]

gvol_words = [
    'vopu', 'vopunā', 'vopuxa', 'vopuvo', 'voput͡si'
]

text = ''

def find_language(string : str, language : Language):
    if language.short_form.lower() == string.lower() or language.name.lower() == string.lower():
        return language
    else:
        for child, changeset in language.children:
            value = find_language(string, child)
            if value != None:
                return value 

while text is not None:
    text = input('Enter words:')
    parts = text.split(' ')

    if parts[0].startswith('-'):
        lang_name = parts[0][1:]
        parts = parts[1:]
        lang = find_language(lang_name, ProtoVolodnian)

        if lang is not None:
            lang.display_tree([SIPA.string_to_word(word) for word in parts])
        else:
            print(f'ERROR: language {lang_name} not found')
    else:
        ProtoVolodnian.display_tree([SIPA.string_to_word(word) for word in parts])
        


