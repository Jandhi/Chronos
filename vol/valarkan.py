from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

OldValarkan = Language('Old Valarkan', 'OVal', SIPA)
NVol_to_OVal = ChangeSet([
    # a merger
    sc(f'V[+{Open},-{Long},-{Overlong}] -> 0[-{Open},+{Close_mid},-{Central},+{Back},+{Rounded}]'),
    sc(f'V[+{Close_mid},+{Long},+{Back}] -> 0[-{Close_mid},+{Open},-{Back},+{Central},-{Rounded}]'),
    sc(f'V[+{Close_mid},+{Overlong},+{Back}] -> 0[-{Close_mid},+{Open},-{Back},+{Central},-{Rounded}]'),
    sc(f'V[+{Close_mid},+{Long},+{Front}] -> 0[-{Close_mid},+{Open},-{Front},+{Central}]'),
    sc(f'V[+{Close_mid},+{Overlong},+{Front}] -> 0[-{Close_mid},+{Open},-{Front},+{Central}]'),
    
    # short front vowels delete after j
    sc(f'V[+{Front},-{Long},-{Overlong}] -> / V[]j_'),

    # palatal fricatives
    sc(f'C[+{Plosive},+{Alveolar},+{Palatalized}] -> 0[-{Plosive},+{Affricate}]'),

    # diphthong shift
    sc(f'V[+{Close_mid},+{Back},+{Rounded}] -> 0[-{Close_mid},+{Open},-{Back},+{Central},-{Rounded}] / _j'),

    # l to r after fricative or plosive
    sc(f'C[+{Lateral}] -> 0[-{Lateral},-{Approximant},+{Trill}] / C[+{Plosive}]_'),
    sc(f'C[+{Lateral}] -> 0[-{Lateral},-{Approximant},+{Trill}] / C[+{Affricate}]_'),
])

MiddleValarkan = Language('Middle Valarkan', 'MVal', SIPA)
OVal_to_MVal = ChangeSet([
    # final devoicing
    sc(f'C[+{Voiced},-{Lateral},-{Trill},-{Nasal},-{Approximant}] -> 0[-{Voiced}] / _#'),

    # diphthong rise
    sc(f'V[+{Long},+{Open_mid}] -> 0[-{Open_mid},+{Close_mid}]'),
    sc(f'V[+{Overlong},+{Open_mid}] -> 0[-{Open_mid},+{Close_mid}]'),

    # retroflexes
    sc(f'C[+{Postalveolar}] -> 0[-{Postalveolar},+{Retroflex}]'),

    # alveolar palatals move
    sc(f'C[+{Alveolar},+{Palatalized},-{Lateral},-{Trill},-{Nasal}] -> 0[-{Alveolar},-{Palatalized},+{Alveopalatal}]'),

    # voicing difference turns to aspiration difference
    sc(f'C[+{Plosive},-{Voiced}] -> 0[+{Aspirated}] / #_'),
    sc(f'C[+{Plosive},+{Voiced}] -> 0[-{Voiced}] / #_'),
])
OldValarkan.add_child(MiddleValarkan, OVal_to_MVal)

HighValarkan = Language('High Valarkan', 'HVal', SIPA)
MVal_to_HVal = ChangeSet([

])
MiddleValarkan.add_child(HighValarkan, MVal_to_HVal)

LowValarkan = Language('Low Valarkan', 'LVal', SIPA)
MVal_to_LVal = ChangeSet([
    # alveolar fricatives move back
    sc(f'C[+{Fricative},+{Alveolar}] -> 0[-{Alveolar},+{Retroflex}] // _V[]'),
    sc(f'C[+{Affricate},+{Alveolar}] -> 0[-{Alveolar},+{Retroflex}] // _V[]'),

    # lenition  
    sc(f'C[+{Voiced},+{Plosive}] -> 0[-{Plosive},+{Fricative}] / V[]_ / _V[+{Stressed}]'),
    sc(f'C[-{Voiced},+{Plosive}] -> 0[+{Voiced}] / V[]_ / _V[+{Stressed}]'),
    sc(f'C[-{Voiced},+{Fricative}] -> 0[+{Voiced}] / V[]_ / _V[+{Stressed}]'),

    sc(f'C[+{Voiced},+{Fricative},+{Velar}] -> / V[]_V[]'),

    # superfinal vowel loss
    sc(f'V[-{Long},-{Overlong},-{Stressed}] -> / V[-{Stressed}]C[]_#'),
    sc(f'V[-{Long},-{Overlong},-{Stressed}] -> / V[-{Stressed}]C[]C[]_#'),
])
MiddleValarkan.add_child(LowValarkan, MVal_to_LVal)

OldSkorosh = Language('Old Skorosh', 'OSkr', SIPA)
OVal_to_OSkr = ChangeSet([
    sc(f'C[+{Voiced},+{Fricative}] -> // _V[]'),
])
OldValarkan.add_child(OldSkorosh, OVal_to_OSkr)

WoodlandSkorosh = Language('Woodland Skorosh', 'WSkr', SIPA)
OSkr_to_WSkr = ChangeSet([

])
OldSkorosh.add_child(WoodlandSkorosh, OSkr_to_WSkr)

CoastalSkorosh = Language('Coastal Skorosh', 'CSkr', SIPA)
OSkr_to_CSkr = ChangeSet([

])
OldSkorosh.add_child(CoastalSkorosh, OSkr_to_CSkr)



