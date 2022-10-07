from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

OldZobrozne = Language('Old Zobrozne', 'OZob', SIPA)
NVol_to_OZob = ChangeSet([
    # unstressed a reduction
    sc(f'V[+{Open},+{Central},-{Stressed}] -> 0[-{Open},+{Mid}]'),
    sc(f'V[+{Mid},+{Central}] -> 0[-{Mid},+{Open}] / _#'),

    # nasal diffrentiation
    sc(f'C[+{Nasal}]V[]C[+{Nasal}]V[] -> 0[+{Alveolar},-{Bilabial}]1[]2[+{Bilabial},-{Alveolar}]3[]'),

    # length simplification
    sc(f'V[+{Overlong}] -> 0[-{Overlong},+{Long}]'),
    sc(f'V[+{Close_mid},-{Lengthened},-{Long}] -> 0[-{Close_mid},+{Open_mid}]'),
    sc(f'V[+{Lengthened}] -> 0[-{Lengthened}]'),

    # final lenition
    sc(f'C[+{Plosive},+{Voiced}] -> 0[-{Plosive},+{Fricative}] / _#'),
    sc(f'C[+{Bilabial},+{Fricative}] -> 0[-{Bilabial},+{Labiodental}]'),

    # zobroznian back chain shift
    sc(f'V[+{Back},+{Close}] -> 0[-{Back},+{Central}]'),
    sc(f'V[+{Back},+{Close_mid},+{Long}] -> 0[-{Close_mid},+{Close}]'),
    sc(f'V[+{Back},+{Close_mid},+{Overlong}] -> 0[-{Close_mid},+{Close}]'),
    sc(f'V[+{Back},+{Open_mid},+{Long}] -> 0[-{Open_mid},+{Close_mid}]'),
    sc(f'V[+{Back},+{Open_mid},+{Overlong}] -> 0[-{Open_mid},+{Close_mid}]'),

    # palatalized simplification
    sc(f'C[+{Lateral},+{Palatalized}] -> j'),
    sc(f'mʲ -> m // _V[]'),

    # cluster simplifying
    sc(f'C[+{Plosive},+{Alveolar}] -> / C[+{Affricate}]_'),
])

MiddleZobrozne = Language('Middle Zobrozne', 'MZob', SIPA)
OZob_to_MZob = ChangeSet([
    # front close-mid vowels break
    sc(f'V[+{Close_mid},+{Front},-{Long}] -> j0[-{Close_mid},+{Open_mid}] // _j'),
    sc(f'V[+{Close_mid},+{Back},-{Long}] -> 0[-{Close_mid},+{Open_mid}]'),

    # ja -> je
    sc(f'jV[+{Open},+{Central}] -> 0[]1[-{Open},-{Central},+{Open_mid},+{Front}]'),

    # diphthong simplification
    sc(f'V[+{Close_mid}]j -> 0[-{Close_mid},+{Open_mid}]j'),
    sc(f'V[+{Open},+{Central}]j -> 0[-{Open},-{Central},+{Back},+{Open_mid},+{Rounded}]j'),

    # palatalized simplification, again
    sc(f'jj -> j'),
    sc(f'j -> / C[+{Postalveolar}]_'),
    sc(f'C[+{Alveolar}]j -> 0[+{Palatalized}]'),
    sc(f'C[+{Lateral},+{Palatalized}] -> j'),

    # long vowel loss
    sc(f'V[+{Long}] -> 0[-{Long}]'),

    # palatals
    sc(f'C[+{Alveolar},+{Palatalized},+{Nasal}] -> 0[-{Alveolar},-{Palatalized},+{Palatal}]'),
    sc(f'C[+{Alveolar},+{Palatalized},-{Trill},-{Plosive}] -> 0[-{Alveolar},-{Palatalized},+{Alveopalatal}]'),
    sc(f'C[+{Alveolar},+{Palatalized},+{Plosive}] -> 0[-{Alveolar},-{Palatalized},-{Plosive},+{Affricate},+{Alveopalatal}]'),

    # close central vowels simplify
    sc(f'V[+{Central},+{Close}] -> 0[-{Central},+{Front},-{Rounded}]'),    

    # final a change after palatalized
    sc(f'V[+{Open}] -> 0[+{Open_mid},-{Open},-{Central},+{Front}] / C[+{Palatalized}]_'),
])
OldZobrozne.add_child(MiddleZobrozne, OZob_to_MZob)

CentralZobrozne = Language('Central Zobrozne', 'CZob', SIPA)
MZob_to_CZob = ChangeSet([
    # Palatal simplifying
    sc(f'C[+{Alveopalatal}] -> 0[-{Alveopalatal},+{Postalveolar}]'),
    sc(f'C[+{Palatalized},+{Trill},+{Alveolar}] -> 0[-{Alveolar},+{Postalveolar},-{Trill},+{Fricative},-{Palatalized}]'),
    sc(f'C[+{Palatalized},+{Velar}] -> 0[-{Palatalized},-{Velar},+{Palatal}]'),

    # Schwa loss
    sc(f'V[+{Mid},+{Central}] -> / V[]C[]_C[]V[]'),
    sc(f'V[+{Mid},+{Central}] -> / C[+{Fricative}]_'),

    # Final schwa
    sc(f'V[+{Open},+{Central}] -> 0[+{Mid},-{Open}] / V[]C[]_#'),
    sc(f'V[+{Open},+{Central}] -> 0[+{Mid},-{Open}] / V[]C[]C[]_#'),

    # Final voiced velar fricative loss
    sc(f'C[+{Velar},+{Voiced},+{Fricative}] -> u // _V[]'),
    sc(f'uu -> ū'),

    # Nasalization loss
    sc(f'V[+{Nasalized}] -> 0[-{Nasalized}]'),

    # Diphthong Simplified
    sc(f'əj -> i'),

    # Clusters simplify
    sc(f'C[+{Fricative},+{Postalveolar}]C[+{Fricative},+{Palatal},+{Voiced}] -> 0[+{Voiced}]0[+{Voiced}]'),
    sc(f'C[+{Fricative},+{Postalveolar}]C[+{Fricative},+{Palatal},-{Voiced}] -> 0[-{Voiced}]0[-{Voiced}]'),
])
MiddleZobrozne.add_child(CentralZobrozne, MZob_to_CZob)

SouthZobrozne = Language('South Zobrozne', 'SZob', SIPA)
MZob_to_SZob = ChangeSet([
    # Palatal simplifying
    sc(f'C[+{Alveopalatal}] -> 0[-{Alveopalatal},+{Postalveolar}]'),
    sc(f'C[+{Palatalized}] -> 0[-{Palatalized}]'),
    sc(f'C[+{Nasal},+{Palatal}] -> 0[-{Palatal},+{Alveolar}]'),

    # Vowel Simplifying
    sc(f'V[+{Mid}] -> 0[-{Mid},+{Open}]'),
    sc(f'V[+{Central}] -> 0[-{Central},+{Back}]'),

    # Vowel Harmony
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _j'),
    # once
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),
    # twice
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),
    # three times 
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),
    # four times for good measure 
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]V[+{Back}]'),
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]C[]V[+{Front}]'),
    sc(f'V[+{Front}] -> 0[-{Front},+{Back}] / _C[]C[]V[+{Back}]'),

    # moving jsa
    sc(f'C[+{Palatal},+{Approximant}] -> 0[-{Palatal},+{Velar}] / _V[+{Back}]'),
    sc(f'C[+{Palatal},+{Approximant}] -> 0[-{Palatal},+{Velar}] / V[+{Back}]_'),

    # realign fronted as
    sc(f'V[+{Front},+{Open}] -> 0[-{Open},+{Open_mid}]'),
    

    # realign stress on first syllable
    sc(f'V[+{Stressed}] -> 0[-{Stressed}]'),
    sc(f'V[] -> 0[+{Stressed}] / #_'),
    sc(f'C[]V[] -> 0[]1[+{Stressed}] / #_'),
    sc(f'C[]C[]V[] -> 0[]1[]2[+{Stressed}] / #_'),

    # raise stressed vowels
    sc(f'V[+{Close_mid},+{Stressed}] -> 0[-{Close_mid},+{Close}]'),
    sc(f'V[+{Open_mid},+{Stressed}] -> 0[-{Open_mid},+{Close_mid}]'),

    # unstressed mid vowels merge
    sc(f'V[+{Close_mid},-{Stressed}] -> 0[-{Close_mid},+{Open_mid}]'),

    # realign back vowels
    sc(f'V[+{Back},+{Close_mid},-{Rounded}] -> 0[-{Close_mid},+{Close}]'),
    sc(f'V[+{Back},+{Open_mid},-{Rounded}] -> 0[-{Open_mid},+{Open}]'),

    # velar harmony
    sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / _V[+{Back}]'),
    sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / V[+{Back}]_'),
    sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / _C[]V[+{Back}]'),
    sc(f'C[+{Velar},-{Approximant}] -> 0[-{Velar},+{Uvular}] / V[+{Back}]C[]_'),

    # no nasalization
    sc(f'V[+{Nasalized}] -> 0[-{Nasalized}]'),

    # no velar approximant at start
    sc(f'C[+{Velar},+{Approximant}] -> / #_')
])
MiddleZobrozne.add_child(SouthZobrozne, MZob_to_SZob)