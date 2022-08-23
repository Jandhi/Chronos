from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

SouthWesternVolodnian = Language('Southwestern Volodnian', 'SWVol', SIPA)
GVol_to_SWVol = ChangeSet([
    
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

])
SouthWesternVolodnian.add_child(WesternVolodnian, SWVol_to_WVol)

from volta import *
WesternVolodnian.add_child(SouthernVoldna, WVol_to_SVld)