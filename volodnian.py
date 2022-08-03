from chronology.change_set import ChangeSet
from chronology.sound_change import Category, SoundChange, Transform
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import Alveolar, Back, Central, Close, Close_mid, Front, Nasalized, Open, Rounded, Velar
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
    SIPA.parse_sc(f'V[]C[+nasal] -> 0[+nasalized] / _C[]'),
    SIPA.parse_sc(f'V[]C[+nasal] -> 0[+nasalized] / _#'),

    # Glide Prothesis
    SIPA.parse_sc(f'V[+front] -> j0[] / #_'),
    SIPA.parse_sc(f'V[-front] -> w0[] / #_'),
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

words = [
    'epu', 'kibu', 'keti'
]

for word in words:
    ProtoVolodnian.display_word(SIPA.string_to_word(word))