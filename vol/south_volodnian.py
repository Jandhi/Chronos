from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

SouthWesternVolodnian = Language('Southwestern Volodnian', 'SWVol', SIPA)
GVol_to_SWVol = ChangeSet([
    # syncope
    sc(f'V[-{Long}] -> / V[]C[]_C[]V[]'),

    # labial shift
    sc(f'C[+{Labiodental}] -> 0[-{Labiodental},+{Bilabial}]'),
    
    # hardening
    sc(f'C[+{Fricative},+{Voiced}] -> 0[-{Fricative},+{Plosive}] / V[]_ '),

    # long vowel shift
    sc(f'V[+{Open},+{Central},+{Long}] -> 0[-{Open},+{Open_mid},-{Central},+{Front}] / C[+{Alveolar},-{Lateral}]_'),
    sc(f'V[+{Open},+{Central},+{Long}] -> 0[-{Open},+{Open_mid},-{Central},+{Back},+{Rounded}]'),
    sc(f'V[+{Open}]V[+{Close}] -> 0[+{Long}]'),
])


SouthernVolodnian = Language('Southern Volodnian', 'SVol', SIPA)
SWVol_to_SVol = ChangeSet([

])
SouthWesternVolodnian.add_child(SouthernVolodnian, SWVol_to_SVol)

WesternVolodnian = Language('Western Volodnian', 'WVol', SIPA)
SWVol_to_WVol = ChangeSet([
    # umlaut
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]V[+{Front},+{Close}]'),
    sc(f'V[+{Central}] -> 0[-{Central},+{Front}] / _C[]V[+{Front},+{Close}]'),
    sc(f'V[+{Back}] -> 0[-{Back},+{Front}] / _C[]j'),
    sc(f'V[+{Central}] -> 0[-{Central},+{Front}] / _C[]j'),

    # dental shift
    sc(f'C[+{Alveolar},+{Fricative}] -> 0[-{Alveolar},+{Dental}]'),

    # deaffrication
    sc(f'C[+{Affricate}] -> 0[-{Affricate},+{Fricative}]'),

    # ja change
    sc(f'je -> ja'),
])
SouthWesternVolodnian.add_child(WesternVolodnian, SWVol_to_WVol)

from vol.volta import *
WesternVolodnian.add_child(SouthernVoldna, WVol_to_SVld)
WesternVolodnian.add_child(NorthernVoldna, WVol_to_NVld)