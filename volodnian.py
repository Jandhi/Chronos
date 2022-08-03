from re import L
from chronology.change_set import ChangeSet
from chronology.sound_change import Category, SoundChange, Transform
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import Alveolar, Alveopalatal, Back, Bilabial, Central, Close, Close_mid, Fricative, Front, Lengthened, Long, Nasal, Nasalized, Open, Open_mid, Overlong, Palatal, Palatalized, Postalveolar, Rounded, Velar, Voiced
from phonology.sound import Sound

ProtoVolodnian = Language('Proto-Volodnian', 'PVol', SIPA)
EarlyVolodnian = Language('Early Volodnian', 'EVol', SIPA)

PVolToEVol = ChangeSet([
    
    # U Umlaut
    SIPA.parse_sc(f'a -> o / _C[]V[+{Close},+{Rounded}]'),
    SIPA.parse_sc(f'e -> o / _C[]V[+{Close},+{Rounded}]'),
    SIPA.parse_sc(f'ā -> ō / _C[]V[+{Close},+{Rounded}]'),
    SIPA.parse_sc(f'ē -> ō / _C[]V[+{Close},+{Rounded}]'),
    SIPA.parse_sc(f'i -> u / _C[]V[+{Close},+{Rounded}]'),
    SIPA.parse_sc(f'ī -> ū / _C[]V[+{Close},+{Rounded}]'),
    

    # Nasal Merger
    SIPA.parse_sc(f'ŋ -> n'),

    # Nasalization
    SIPA.parse_sc(f'V[]C[+{Nasal}] -> 0[+{Nasalized}] / _C[]'),
    SIPA.parse_sc(f'V[]C[+{Nasal}] -> 0[+{Nasalized}] / _#'),

    # Glide Prothesis
    SIPA.parse_sc(f'V[+{Front}] -> j0[] / #_'),
    SIPA.parse_sc(f'V[-{Front}] -> w0[] / #_'),

    # Short Vowel Merger
    SIPA.parse_sc(f'V[+{Close_mid}] -> 0[+{Lengthened}] / #_'),
    SIPA.parse_sc(f'C[]V[+{Close_mid}] -> 0[]1[+{Lengthened}] / #_'),
    SIPA.parse_sc(f'V[+{Close_mid},-{Lengthened}] -> 0[-{Close_mid},+{Close}]'),
    SIPA.parse_sc(f'V[+{Lengthened}] -> 0[-{Lengthened}]'),
])
ProtoVolodnian.add_child(EarlyVolodnian, PVolToEVol)

GreaterVolodnian = Language('Greater Volodnian', 'GVol', SIPA)
EVoltoGVol = ChangeSet([
    # W hardening
    SIPA.parse_sc('w -> v'),

    # First Palatalization
    SIPA.parse_sc(f'x -> ʃ / _V[+{Front}]'),
    SIPA.parse_sc(f'ɣ -> ʒ / _V[+{Front}]'),
    SIPA.parse_sc(f'k -> tʃ / _V[+{Front}]'),
    SIPA.parse_sc(f'g -> dʒ / _V[+{Front}]'),

    # Nasal Vowel Merger
    SIPA.parse_sc(f'V[+{Close_mid},+{Nasalized}] -> 0[-{Close_mid},+{Open},-{Front},-{Back},-{Rounded},+{Central}]'),
])
EarlyVolodnian.add_child(GreaterVolodnian, EVoltoGVol)

NorthEasternVolodnian = Language('Northeastern Volodnian', 'NEVol', SIPA)
GVoltoNEVol = ChangeSet([
    # Diphthong Reduction
    SIPA.parse_sc(f'au -> ɔ̄'),
    SIPA.parse_sc(f'ai -> ɛ̄'),

    # Great Collapse
    SIPA.parse_sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]i <<'),
    SIPA.parse_sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]u <<'),
    SIPA.parse_sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]i <<'),
    SIPA.parse_sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]u <<'),
    SIPA.parse_sc(f'C[+{Fricative}] -> 0[+{Voiced}] / V[]_V[+{Close},-{Long},-{Overlong},-{Lengthened}]'),
    SIPA.parse_sc(f'u -> '),
    SIPA.parse_sc(f'C[]i -> 0[+{Palatalized}]'),
    SIPA.parse_sc(f'C[]u -> 0[]'),

    # Cracking down on Illegal clusters
    SIPA.parse_sc(f'C[+{Nasal},+{Palatalized}] -> 0[]e / #_C[]'),
    SIPA.parse_sc(f'C[+{Nasal},-{Palatalized}] -> 0[]a / #_C[]'),

    # Getting rid of weird palatalization
    SIPA.parse_sc(f'C[+{Palatalized},+{Postalveolar}] -> 0[-{Palatalized}]'),
    SIPA.parse_sc(f'C[+{Palatalized},+{Palatal}] -> 0[-{Palatalized}]'),

    # Voicing spreads backwards
    SIPA.parse_sc(f'C[-{Voiced}] -> 0[+{Voiced}] / _C[+{Voiced}]'),
    SIPA.parse_sc(f'C[+{Voiced}] -> 0[-{Voiced}] / _C[-{Voiced}]'),
])
GreaterVolodnian.add_child(NorthEasternVolodnian, GVoltoNEVol)

NorthernVolodnian = Language('Northern Volodnian', 'NVol', SIPA)
NEVoltoNVol = ChangeSet([
    # Lengthened Merger
    SIPA.parse_sc(f'V[+{Lengthened},+{Close}] -> 0[-{Close},+{Close_mid}]')
])
NorthEasternVolodnian.add_child(NorthernVolodnian, NEVoltoNVol)

OldZobrozne = Language('Old Zobrozne', 'OZob', SIPA)
NVoltoOZob = ChangeSet([
    # nasal diffrentiation
    SIPA.parse_sc(f'C[+{Nasal}]V[]C[+{Nasal}]V[] -> 0[+{Alveolar},-{Bilabial}]1[]2[+{Bilabial},-{Alveolar}]3[]'),

    # length simplification
    SIPA.parse_sc(f'V[+{Overlong}] -> 0[-{Overlong},+{Long}]'),
    SIPA.parse_sc(f'V[+{Close_mid}-{Lengthened}] -> 0[-{Close_mid},+{Open_mid}]'),
    SIPA.parse_sc(f'V[+{Lengthened}] -> 0[-{Lengthened}]'),
])
NorthernVolodnian.add_child(OldZobrozne, NVoltoOZob)

MiddleZobrozne = Language('Middle Zobrozne', 'MZob', SIPA)
OZobtoMZob = ChangeSet([
    # long vowel loss
    SIPA.parse_sc(f'V[+{Long}] -> 0[-{Long}]'),
])
OldZobrozne.add_child(MiddleZobrozne, OZobtoMZob)

words = [
    'epu', 'kibu', 'keti', 'borugu', 'sukateli', 'karitsi', 'xagigi', 'xitoro', 'kesu', 'naŋau', 'mimare', 'axuta'
]

for word in words:
    ProtoVolodnian.display_word(SIPA.string_to_word(word))