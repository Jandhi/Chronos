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
    SIPA.parse_sc(f'V[+{Close_mid},-{Long}] -> 0[+{Lengthened}] / #_'),
    SIPA.parse_sc(f'C[]V[+{Close_mid},-{Long}] -> 0[]1[+{Lengthened}] / #_'),
    SIPA.parse_sc(f'V[+{Close_mid},-{Long},-{Lengthened}] -> 0[-{Close_mid},+{Close}] // _j'),
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
    SIPA.parse_sc(f'V[+{Close},-{Long}] -> 0[-{Close},+{Close_mid}] / _r / V[]_'),
])
EarlyVolodnian.add_child(GreaterVolodnian, EVoltoGVol)

NorthEasternVolodnian = Language('Northeastern Volodnian', 'NEVol', SIPA)
GVoltoNEVol = ChangeSet([
    # Diphthong Reduction
    SIPA.parse_sc(f'V[+{Open}]V[+{Close},+{Back},+{Nasalized}] -> ɔ̄̃'),
    SIPA.parse_sc(f'V[+{Open}]V[+{Close},+{Back}] -> ɔ̄'),
    SIPA.parse_sc(f'V[+{Open}]V[+{Close},+{Front},+{Nasalized}] -> ɛ̄̃'),
    SIPA.parse_sc(f'V[+{Open}]V[+{Close},+{Front}] -> ɛ̄'),

    # Great Collapse

    # lengthening
    SIPA.parse_sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]i <<'),
    SIPA.parse_sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]u <<'),
    SIPA.parse_sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]i <<'),
    SIPA.parse_sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]u <<'),
    
    # fricatives voice along the way
    SIPA.parse_sc(f'V[]C[+{Fricative}] -> 0[]1[+{Voiced}] / #_V[+{Close},-{Long},-{Overlong},-{Lengthened},-{Nasalized}]'),
    SIPA.parse_sc(f'C[]V[]C[+{Fricative}] -> 0[]1[]2[+{Voiced}] / #_V[+{Close},-{Long},-{Overlong},-{Lengthened},-{Nasalized}]'),

    # final step : erasure
    SIPA.parse_sc(f'C[]i -> 0[+{Palatalized}]'),
    SIPA.parse_sc(f'C[]u -> 0[]'),

    # some illegal palatalizations
    SIPA.parse_sc(f'C[+{Approximant},+{Palatalized},-{Lateral}] -> 0[-{Palatalized}]'),

    # Cracking down on Illegal clusters
    SIPA.parse_sc(f'C[+{Nasal},+{Palatalized}] -> 0[]e / #_C[]'),
    SIPA.parse_sc(f'C[+{Nasal},-{Palatalized}] -> 0[]a / #_C[]'),
    SIPA.parse_sc(f'C[+{Approximant},+{Palatal}] -> 0[]e / #_C[]'),
    SIPA.parse_sc(f'C[+{Approximant},-{Palatal}] -> 0[]a / #_C[]'),
    
    # Fricatives in the same position can't touch
    SIPA.parse_sc(f'C[+{Fricative},+{Velar},+{Palatalized}] -> 0[]e / #_C[+{Fricative},+{Velar}]'),
    SIPA.parse_sc(f'C[+{Fricative},+{Velar},-{Palatalized}] -> 0[]a / #_C[+{Fricative},+{Velar}]'),

    # Getting rid of weird palatalization
    SIPA.parse_sc(f'C[+{Palatalized},+{Postalveolar}] -> 0[-{Palatalized}]'),
    SIPA.parse_sc(f'C[+{Palatalized},+{Palatal}] -> 0[-{Palatalized}]'),

    # Voicing spreads backwards (except for r or l)
    SIPA.parse_sc(f'C[-{Voiced},-{Approximant},-{Nasal},-{Trill}] -> 0[+{Voiced}] / _C[+{Voiced},-{Trill},-{Approximant}]'),
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
    SIPA.parse_sc(f'V[-{Stressed}]C[]C[] -> 0[+{Stressed}]1[]2[] / #_#'),
    SIPA.parse_sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_#'),
    SIPA.parse_sc(f'C[]V[-{Stressed}]C[] -> 0[]1[+{Stressed}]2[] / #_#'),
    SIPA.parse_sc(f'C[]V[-{Stressed}]C[]C[] -> 0[]1[+{Stressed}]2[]3[] / #_#'),
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_#'),
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}]C[] -> 0[]1[]2[+{Stressed}]3[] / #_#'),
    SIPA.parse_sc(f'C[]C[]V[-{Stressed}]C[]C[] -> 0[]1[]2[+{Stressed}]3[]4[] / #_#'),

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

    # zobroznian back chain shift
    SIPA.parse_sc(f'V[+{Back},+{Close}] -> 0[-{Back},+{Central}]'),
    SIPA.parse_sc(f'V[+{Back},+{Close_mid},+{Long}] -> 0[-{Close_mid},+{Close}]'),
    SIPA.parse_sc(f'V[+{Back},+{Close_mid},+{Overlong}] -> 0[-{Close_mid},+{Close}]'),
    SIPA.parse_sc(f'V[+{Back},+{Open_mid},+{Long}] -> 0[-{Open_mid},+{Close_mid}]'),
    SIPA.parse_sc(f'V[+{Back},+{Open_mid},+{Overlong}] -> 0[-{Open_mid},+{Close_mid}]'),

    # palatalized simplification
    SIPA.parse_sc(f'C[+{Lateral},+{Palatalized}] -> j'),
    SIPA.parse_sc(f'mʲ -> m // _V[]'),
])
NorthernVolodnian.add_child(OldZobrozne, NVoltoOZob)

MiddleZobrozne = Language('Middle Zobrozne', 'MZob', SIPA)
OZobtoMZob = ChangeSet([
    # long vowel loss
    SIPA.parse_sc(f'V[+{Long}] -> 0[-{Long}]'),

    # palatals
    SIPA.parse_sc(f'C[+{Alveolar},+{Palatalized},+{Nasal}] -> 0[-{Alveolar},-{Palatalized},+{Palatal}]'),
    SIPA.parse_sc(f'C[+{Alveolar},+{Palatalized},-{Trill},-{Plosive}] -> 0[-{Alveolar},-{Palatalized},+{Alveopalatal}]'),
    SIPA.parse_sc(f'C[+{Alveolar},+{Palatalized},+{Plosive}] -> 0[-{Alveolar},-{Palatalized},-{Plosive},+{Affricate},+{Alveopalatal}]'),

    # front close-mid vowels break
    SIPA.parse_sc(f'V[+{Close_mid},+{Front}] -> j0[-{Close_mid},+{Open_mid}]'),
    SIPA.parse_sc(f'V[+{Close_mid},+{Back}] -> 0[-{Close_mid},+{Open_mid}]'),

    # palatalized simplification, again
    SIPA.parse_sc(f'C[+{Lateral},+{Palatalized}] -> j'),
    SIPA.parse_sc(f'jj -> j'),

    # close central vowels simplify
    SIPA.parse_sc(f'V[+{Central},+{Close}] -> 0[-{Central},+{Front},-{Rounded}]'),
])
OldZobrozne.add_child(MiddleZobrozne, OZobtoMZob)

CentralZobrozne = Language('Central Zobrozne', 'CZob', SIPA)
MZobtoCZob = ChangeSet([
    # Palatal simplifying
    SIPA.parse_sc(f'C[+{Alveopalatal}] -> 0[-{Alveopalatal},+{Postalveolar}]'),
    SIPA.parse_sc(f'C[+{Palatalized},+{Trill},+{Alveolar}] -> 0[-{Alveolar},+{Postalveolar},-{Trill},+{Fricative},-{Palatalized}]'),

    # Schwa loss
    SIPA.parse_sc(f'V[+{Mid},+{Central}] -> / V[]C[]_C[]V[]'),
    SIPA.parse_sc(f'V[+{Mid},+{Central}] -> / C[+{Fricative}]_'),

    # Final schwa
    SIPA.parse_sc(f'V[+{Open},+{Central}] -> 0[+{Mid},-{Open}] / V[]C[]_#'),
    SIPA.parse_sc(f'V[+{Open},+{Central}] -> 0[+{Mid},-{Open}] / V[]C[]C[]_#'),

    # Final voiced velar fricative loss
    SIPA.parse_sc(f'C[+{Velar},+{Voiced},+{Fricative}] -> u // _V[]'),
    SIPA.parse_sc(f'uu -> ū'),

    # Nasalization loss
    SIPA.parse_sc(f'V[+{Nasalized}] -> 0[-{Nasalized}]'),
])
MiddleZobrozne.add_child(CentralZobrozne, MZobtoCZob)

SouthZobrozne = Language('South Zobrozne', 'SZob', SIPA)
MZobtoSZob = ChangeSet([
    # Palatal simplifying
    SIPA.parse_sc(f'C[+{Alveopalatal}] -> 0[-{Alveopalatal},+{Postalveolar}]'),
    SIPA.parse_sc(f'C[+{Palatalized}] -> 0[-{Palatalized}]'),
    SIPA.parse_sc(f'C[+{Nasal},+{Palatal}] -> 0[-{Palatal},+{Alveolar}]'),

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

    # moving jsa
    SIPA.parse_sc(f'C[+{Palatal},+{Approximant}] -> 0[-{Palatal},+{Velar}] / _V[+{Back}]'),
    SIPA.parse_sc(f'C[+{Palatal},+{Approximant}] -> 0[-{Palatal},+{Velar}] / V[+{Back}]_'),

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
    SIPA.parse_sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / _V[+{Back}]'),
    SIPA.parse_sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / V[+{Back}]_'),
    SIPA.parse_sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / _C[]V[+{Back}]'),
    SIPA.parse_sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / V[+{Back}]C[]_'),

    # no nasalization
    SIPA.parse_sc(f'V[+{Nasalized}] -> 0[-{Nasalized}]'),

    # no velar approximant at start
    SIPA.parse_sc(f'C[+{Velar},+{Approximant}] -> / #_')
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

text = ''

def find_language(string, language : Language):
    if language.short_form == string or language.name == string:
        return language
    else:
        for child, changeset in language.children:
            value = find_language(string, child)
            if value != None:
                return value 

while text is not None:
    text = input('Enter a language and word: ')
    parts = text.split(' ')

    if len(parts) == 1:
        ProtoVolodnian.display_word(SIPA.string_to_word(parts[0]))
        continue

    language = find_language(parts[0], ProtoVolodnian)

    if language is None:
        print('not a language!')
        continue

    language.display_word(SIPA.string_to_word(parts[1]))


