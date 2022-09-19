from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

NorthEasternVolodnian = Language('Northeastern Volodnian', 'NEVol', SIPA)
GVol_to_NEVol = ChangeSet([
    # Diphthong Reduction
    sc(f'V[+{Open}]V[+{Close},+{Back},+{Nasalized}] -> ɔ̄̃'),
    sc(f'V[+{Open}]V[+{Close},+{Back}] -> ɔ̄'),
    sc(f'V[+{Open}]V[+{Close},+{Front},+{Nasalized}] -> ɛ̄̃'),
    sc(f'V[+{Open}]V[+{Close},+{Front}] -> ɛ̄'),

    # Great Collapse

    # lengthening
    sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]i <<'),
    sc(f'V[-{Long},-{Lengthened}] -> 0[+{Lengthened}] / _C[]u <<'),
    sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]i <<'),
    sc(f'V[+{Long}] -> 0[+{Overlong},-{Long}] / _C[]u <<'),
    
    # fricatives voice along the way
    sc(f'V[]C[+{Fricative}] -> 0[]1[+{Voiced}] / #_V[+{Close},-{Long},-{Overlong},-{Lengthened},-{Nasalized}]'),
    sc(f'C[]V[]C[+{Fricative}] -> 0[]1[]2[+{Voiced}] / #_V[+{Close},-{Long},-{Overlong},-{Lengthened},-{Nasalized}]'),

    # final step : erasure
    sc(f'C[]i -> 0[+{Palatalized}]'),
    sc(f'C[]u -> 0[]'),

    # some illegal palatalizations
    sc(f'C[+{Approximant},+{Palatalized},-{Lateral}] -> 0[-{Palatalized}]'),

    # Cracking down on Illegal clusters
    sc(f'C[+{Nasal},+{Palatalized}] -> 0[]e / #_C[]'),
    sc(f'C[+{Nasal},-{Palatalized}] -> 0[]a / #_C[]'),
    sc(f'C[+{Approximant},+{Palatal}] -> 0[]e / #_C[]'),
    sc(f'C[+{Approximant},-{Palatal}] -> 0[]a / #_C[]'),
    
    # Fricatives in the same position can't touch
    sc(f'C[+{Fricative},+{Velar},+{Palatalized}] -> 0[]e / #_C[+{Fricative},+{Velar}]'),
    sc(f'C[+{Fricative},+{Velar},-{Palatalized}] -> 0[]a / #_C[+{Fricative},+{Velar}]'),

    # Getting rid of weird palatalization
    sc(f'C[+{Palatalized},+{Postalveolar}] -> 0[-{Palatalized}]'),
    sc(f'C[+{Palatalized},+{Palatal}] -> 0[-{Palatalized}]'),

    # Voicing spreads backwards (except for r or l)
    sc(f'C[-{Voiced},-{Approximant},-{Nasal},-{Trill}] -> 0[+{Voiced}] / _C[+{Voiced},-{Trill},-{Approximant},-{Nasal}]'),
    sc(f'C[+{Voiced},-{Approximant},-{Nasal},-{Trill}] -> 0[-{Voiced}] / _C[-{Voiced}]'),

    # Syncope for weak syllables with l or r
    sc(f'V[-{Long}] -> / V[]C[+{Plosive}]_C[+{Trill}]V[]'),
    sc(f'V[-{Long}] -> / V[]C[+{Plosive}]_C[+{Lateral}]V[]'),

    # palatals spread
    sc(f'C[-{Palatalized},-{Palatal},-{Postalveolar}] -> 0[+{Palatalized}] / _C[+{Palatalized}]'),
    sc(f'C[-{Palatalized},-{Palatal},-{Postalveolar}] -> 0[+{Palatalized}] / C[+{Palatalized}]_'),
])

NorthernVolodnian = Language('Northern Volodnian', 'NVol', SIPA)
NEVoltoNVol = ChangeSet([

    # Stress Schema
    sc(f'V[+{Stressed}] -> 0[-{Stressed}]'),

    # Single Syllable Stress
    sc(f'V[-{Stressed}] -> 0[+{Stressed}] / #_#'),
    sc(f'V[-{Stressed}]C[] -> 0[+{Stressed}]1[] / #_#'),
    sc(f'V[-{Stressed}]C[]C[] -> 0[+{Stressed}]1[]2[] / #_#'),
    sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_#'),
    sc(f'C[]V[-{Stressed}]C[] -> 0[]1[+{Stressed}]2[] / #_#'),
    sc(f'C[]V[-{Stressed}]C[]C[] -> 0[]1[+{Stressed}]2[]3[] / #_#'),
    sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_#'),
    sc(f'C[]C[]V[-{Stressed}]C[] -> 0[]1[]2[+{Stressed}]3[] / #_#'),
    sc(f'C[]C[]V[-{Stressed}]C[]C[] -> 0[]1[]2[+{Stressed}]3[]4[] / #_#'),

    # LH start
    sc(f'C[]C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Long},-{Stressed}] -> 0[]1[]2[]3[]4[+{Stressed}] / #_'),
    sc(f'C[]C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Overlong},-{Stressed}] -> 0[]1[]2[]3[]4[+{Stressed}] / #_'),
    sc(f'C[]C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Lengthened},-{Stressed}] -> 0[]1[]2[]3[]4[+{Stressed}] / #_'),
    sc(f'C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Long},-{Stressed}] -> 0[]1[]2[]3[+{Stressed}] / #_'),
    sc(f'C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Overlong},-{Stressed}] -> 0[]1[]2[]3[+{Stressed}] / #_'),
    sc(f'C[]V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Lengthened},-{Stressed}] -> 0[]1[]2[]3[+{Stressed}] / #_'),
    sc(f'V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Long},-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_'),
    sc(f'V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Overlong},-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_'),
    sc(f'V[-{Long},-{Overlong},-{Stressed}]C[]V[+{Lengthened},-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_'),

    # LL start
    sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_C[]V[-{Stressed}]'),
    sc(f'C[]C[]V[-{Stressed}] -> 0[]1[]2[+{Stressed}] / #_C[]C[]V[-{Stressed}]'),
    sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_C[]V[-{Stressed}]'),
    sc(f'C[]V[-{Stressed}] -> 0[]1[+{Stressed}] / #_C[]C[]V[-{Stressed}]'),
    sc(f'V[-{Stressed}] -> 0[+{Stressed}] / #_C[]V[-{Stressed}]'),
    sc(f'V[-{Stressed}] -> 0[+{Stressed}] / #_C[]C[]V[-{Stressed}]'),

    # Lengthened Merger
    sc(f'V[+{Lengthened},+{Close}] -> 0[-{Close},+{Close_mid}]'),

    # Deaffrication
    sc(f'C[+{Affricate},+{Voiced}] -> 0[-{Affricate},+{Fricative}] / _'),

    # Cluster merging
    sc(f'C[+{Fricative},+{Velar}] -> / C[+{Postalveolar}]_'),
    sc(f'C[+{Fricative},+{Velar}] -> 0[-{Velar},+{Postalveolar}] / _C[+{Postalveolar},+{Affricate}]'),
    sc(f'C[+{Fricative},+{Velar}] -> / _C[+{Postalveolar}]'),
])
NorthEasternVolodnian.add_child(NorthernVolodnian, NEVoltoNVol)

from vol.zobroznan import *
NorthernVolodnian.add_child(OldZobrozne, NVol_to_OZob)

from vol.valarkan import *
NorthernVolodnian.add_child(OldValarkan, NVol_to_OVal)