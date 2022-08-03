from re import L
from chronology.change_set import ChangeSet
from chronology.sound_change import Category, SoundChange, Transform
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import Affricate, Alveolar, Alveopalatal, Approximant, Back, Bilabial, Central, Close, Close_mid, Fricative, Front, Labiodental, Lateral, Lengthened, Long, Mid, Nasal, Nasalized, Open, Open_mid, Overlong, Palatal, Palatalized, Plosive, Postalveolar, Rounded, Stressed, Trill, Uvular, Velar, Voiced
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
    SIPA.parse_sc(f'V[+{Close_mid},-{Lengthened}] -> 0[-{Close_mid},+{Close}] // _j'),
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
    SIPA.parse_sc(f'k -> t͡ʃ / _V[+{Front}]'),
    SIPA.parse_sc(f'g -> d͡ʒ / _V[+{Front}]'),

    # Nasal Vowel Merger
    SIPA.parse_sc(f'V[+{Close_mid},+{Nasalized}] -> 0[-{Close_mid},+{Open},-{Front},-{Back},-{Rounded},+{Central}]'),

    # R Lowering
    SIPA.parse_sc(f'V[+{Close}] -> 0[-{Close},+{Close_mid}] / _r')
])
EarlyVolodnian.add_child(GreaterVolodnian, EVoltoGVol)

NorthEasternVolodnian = Language('Northeastern Volodnian', 'NEVol', SIPA)
GVoltoNEVol = ChangeSet([
    # Diphthong Reduction
    SIPA.parse_sc(f'au -> ɔ̄'),
    SIPA.parse_sc(f'ai -> ɛ̄'),

    # Great Collapse

    # lengthening
    SIPA.parse_sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]i <<'),
    SIPA.parse_sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]u <<'),
    SIPA.parse_sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]i <<'),
    SIPA.parse_sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]u <<'),
    
    # fricatives voice along the way
    SIPA.parse_sc(f'V[]C[+{Fricative}] -> 0[]1[+{Voiced}] / #_V[+{Close},-{Long},-{Overlong},-{Lengthened}]'),
    SIPA.parse_sc(f'C[]V[]C[+{Fricative}] -> 0[]1[]2[+{Voiced}] / #_V[+{Close},-{Long},-{Overlong},-{Lengthened}]'),

    # final step : erasure
    SIPA.parse_sc(f'C[]i -> 0[+{Palatalized}]'),
    SIPA.parse_sc(f'C[]u -> 0[]'),

    # Cracking down on Illegal clusters
    SIPA.parse_sc(f'C[+{Nasal},+{Palatalized}] -> 0[]e / #_C[]'),
    SIPA.parse_sc(f'C[+{Nasal},-{Palatalized}] -> 0[]a / #_C[]'),

    # Getting rid of weird palatalization
    SIPA.parse_sc(f'C[+{Palatalized},+{Postalveolar}] -> 0[-{Palatalized}]'),
    SIPA.parse_sc(f'C[+{Palatalized},+{Palatal}] -> 0[-{Palatalized}]'),

    # Voicing spreads backwards (except for r or l)
    SIPA.parse_sc(f'C[-{Voiced},-{Approximant},-{Nasal},-{Trill}] -> 0[+{Voiced}] / _C[+{Voiced},-{Trill}]'),
    SIPA.parse_sc(f'C[+{Voiced},-{Approximant},-{Nasal},-{Trill}] -> 0[-{Voiced}] / _C[-{Voiced}]'),
])
GreaterVolodnian.add_child(NorthEasternVolodnian, GVoltoNEVol)

NorthernVolodnian = Language('Northern Volodnian', 'NVol', SIPA)
NEVoltoNVol = ChangeSet([

    # Stress Schema
    SIPA.parse_sc(f'V[+{Stressed}] -> 0[-{Stressed}]'),

    # Single Syllable Stress
    SIPA.parse_sc(f'V[-{Stressed}] -> 0[+{Stressed}] / #_#'),
    SIPA.parse_sc(f'V[-{Stressed}]C[] -> 0[+{Stressed}]1[] / #_#'),
    SIPA.parse_sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_#'),
    SIPA.parse_sc(f'C[]V[-{Stressed}]C[] -> 0[]1[+{Stressed}]2[] / #_#'),
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_#'),
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}]C[] -> 0[]1[]2[+{Stressed}]3[] / #_#'),

    # LH start
    SIPA.parse_sc(f'C[]C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Long},-{Stressed}] -> 0[]1[]2[]3[]4[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Overlong},-{Stressed}] -> 0[]1[]2[]3[]4[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Lengthened},-{Stressed}] -> 0[]1[]2[]3[]4[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Long},-{Stressed}] -> 0[]1[]2[]3[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Overlong},-{Stressed}] -> 0[]1[]2[]3[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Lengthened},-{Stressed}] -> 0[]1[]2[]3[+{Stressed}] / #_'),
    SIPA.parse_sc(f'V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Long},-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_'),
    SIPA.parse_sc(f'V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Overlong},-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_'),
    SIPA.parse_sc(f'V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Lengthened},-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_'),

    # LL start
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_C[]V[-{Stressed}]'),
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_C[]C[]V[-{Stressed}]'),
    SIPA.parse_sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_C[]V[-{Stressed}]'),
    SIPA.parse_sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_C[]C[]V[-{Stressed}]'),
    SIPA.parse_sc(f'V[-{Stressed}] -> 0[+{Stressed}] / #_C[]V[-{Stressed}]'),
    SIPA.parse_sc(f'V[-{Stressed}] -> 0[+{Stressed}] / #_C[]C[]V[-{Stressed}]'),

    # Lengthened Merger
    SIPA.parse_sc(f'V[+{Lengthened},+{Close}] -> 0[-{Close},+{Close_mid}]'),

    # Deaffrication
    SIPA.parse_sc(f'C[+{Affricate},+{Voiced}] -> 0[-{Affricate},+{Fricative}] / V[]_')
])
NorthEasternVolodnian.add_child(NorthernVolodnian, NEVoltoNVol)

OldZobrozne = Language('Old Zobrozne', 'OZob', SIPA)
NVoltoOZob = ChangeSet([
    # unstressed a reduction
    SIPA.parse_sc(f'V[+{Open},+{Central},-{Stressed}] -> 0[-{Open},+{Mid}]'),
    SIPA.parse_sc(f'V[+{Mid},+{Central}] -> 0[-{Mid},+{Open}] / _#'),

    # nasal diffrentiation
    SIPA.parse_sc(f'C[+{Nasal}]V[]C[+{Nasal}]V[] -> 0[+{Alveolar},-{Bilabial}]1[]2[+{Bilabial},-{Alveolar}]3[]'),

    # length simplification
    SIPA.parse_sc(f'V[+{Overlong}] -> 0[-{Overlong},+{Long}]'),
    SIPA.parse_sc(f'V[+{Close_mid},-{Lengthened},-{Long}] -> 0[-{Close_mid},+{Open_mid}]'),
    SIPA.parse_sc(f'V[+{Lengthened}] -> 0[-{Lengthened}]'),

    # final lenition
    SIPA.parse_sc(f'C[+{Plosive},+{Voiced}] -> 0[-{Plosive},+{Fricative}] / _#'),
    SIPA.parse_sc(f'C[+{Bilabial},+{Fricative}] -> 0[-{Bilabial},+{Labiodental}]'),

    # Palatalized simplification
    SIPA.parse_sc(f'C[+{Lateral},+{Palatalized}] -> j')
])
NorthernVolodnian.add_child(OldZobrozne, NVoltoOZob)

MiddleZobrozne = Language('Middle Zobrozne', 'MZob', SIPA)
OZobtoMZob = ChangeSet([
    # long vowel loss
    SIPA.parse_sc(f'V[+{Long}] -> 0[-{Long}]'),

    # palatals
    SIPA.parse_sc(f'C[+{Alveolar},+{Palatalized},+{Nasal}] -> 0[-{Alveolar},-{Palatalized},+{Palatal}]'),
    SIPA.parse_sc(f'C[+{Alveolar},+{Palatalized},-{Trill}] -> 0[-{Alveolar},-{Palatalized},+{Alveopalatal}]')
])
OldZobrozne.add_child(MiddleZobrozne, OZobtoMZob)

CentralZobrozne = Language('Central Zobrozne', 'CZob', SIPA)
MZobtoCZob = ChangeSet([
    # Palatal simplifying
    SIPA.parse_sc(f'C[+{Alveopalatal}] -> 0[-{Alveopalatal},+{Postalveolar}]'),
])
MiddleZobrozne.add_child(CentralZobrozne, MZobtoCZob)

SouthZobrozne = Language('South Zobrozne', 'SZob', SIPA)
MZobtoSZob = ChangeSet([
    # Palatal simplifying
    SIPA.parse_sc(f'C[+{Alveopalatal}] -> 0[-{Alveopalatal},+{Postalveolar}]'),
    SIPA.parse_sc(f'C[+{Palatalized}] -> 0[-{Palatalized}]'),

    # Vowel Simplifying
    SIPA.parse_sc(f'V[+{Mid}] -> 0[-{Mid},+{Open}]'),
    SIPA.parse_sc(f'V[+{Central}] -> 0[-{Central},+{Back}]'),

    # Vowel Harmony
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _j'),
    # once
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),
    # twice
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),
    # three times 
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),
    # four times for good measure 
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    SIPA.parse_sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    SIPA.parse_sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),

    # realign fronted as
    SIPA.parse_sc(f'V[+{Front},+{Open}] -> 0[-{Open},+{Open_mid}]'),
    

    # realign stress on first syllable
    SIPA.parse_sc(f'V[+{Stressed}] -> 0[-{Stressed}]'),
    SIPA.parse_sc(f'V[] -> 0[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]V[] -> 0[]1[+{Stressed}] / #_'),
    SIPA.parse_sc(f'C[]C[]V[] -> 0[]1[]2[+{Stressed}] / #_'),

    # raise stressed vowels
    SIPA.parse_sc(f'V[+{Close_mid},+{Stressed}] -> 0[-{Close_mid},+{Close}]'),
    SIPA.parse_sc(f'V[+{Open_mid},+{Stressed}] -> 0[-{Open_mid},+{Close_mid}]'),

    # unstressed mid vowels merge
    SIPA.parse_sc(f'V[+{Close_mid},-{Stressed}] -> 0[-{Close_mid},+{Open_mid}]'),

    # realign back vowels
    SIPA.parse_sc(f'V[+{Back},+{Close_mid},-{Rounded}] -> 0[-{Close_mid},+{Close}]'),
    SIPA.parse_sc(f'V[+{Back},+{Open_mid},-{Rounded}] -> 0[-{Open_mid},+{Open}]'),

    # velar harmony
    SIPA.parse_sc(f'C[+{Velar}] -> 0[-{Velar},+{Uvular}] / _V[+{Back}]'),
    SIPA.parse_sc(f'C[+{Velar}] -> 0[-{Velar},+{Uvular}] / V[+{Back}]_'),
])
MiddleZobrozne.add_child(SouthZobrozne, MZobtoSZob)

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

for word in gvol_words:
    GreaterVolodnian.display_word(SIPA.string_to_word(word))