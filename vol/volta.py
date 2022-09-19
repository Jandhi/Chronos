from chronology.change_set import ChangeSet
from language import Language
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import *

sc = SIPA.parse_sc

SouthernVoldna = Language('Southern Voldna', 'SVld', SIPA)
WVol_to_SVld = ChangeSet([
    # Volta Consonant Shift
    sc(f'C[+{Alveolar},+{Plosive},-{Voiced}] -> 0[-{Plosive},+{Affricate}]'), # t -> ts
    sc(f'C[+{Alveolar},+{Plosive},+{Voiced}] -> 0[-{Voiced}]'), # d -> t
    sc(f'C[+{Dental},+{Fricative}] -> 0[-{Dental},-{Fricative},+{Alveolar},+{Plosive}]'), # th dh -> t d

    # Final Consonants Reduced
    sc(f'V[-{Long}] -> / V[]C[]_#'),
    sc(f'V[-{Long}] -> / V[]C[]C[]_#'),
    sc(f'V[+{Long}] -> 0[-{Long}] / V[]C[]_#'),
    sc(f'V[+{Long}] -> 0[-{Long}] / V[]C[]C[]_#'),
])

NorthernVoldna = Language('Northern Voldna', 'NVld', SIPA)
WVol_to_NVld = ChangeSet([

])