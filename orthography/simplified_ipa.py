
from orthography.orthography import Orthography, post_symbol
from phonology.features import Affricate, Alveolar, Alveopalatal, Approximant, Back, Bilabial, Central, Close, Close_mid, Fricative, Front, Glottal, Labiovelar, Lateral, Lengthened, Long, Mid, Nasal, Nasalized, Open, Open_mid, Overlong, Palatal, Palatalized, Plosive, Postalveolar, Retroflex, Rounded, Tap, Trill, Uvular, Velar
from phonology.sound import Consonant, Vowel

processors = [
    post_symbol(Lengthened, '\u0301'),
    post_symbol(Long, '\u0304'),
    post_symbol(Overlong, '\0302'),
    post_symbol(Nasalized, '\u0303'),
    post_symbol(Palatalized, 'ʲ'),
]

symbols = [
    # Vowels
    (Vowel(Close, Front).make(), 'i'),
    (Vowel(Close, Front).rounded().make() , 'y'),
    (Vowel(Close_mid, Front).make() , 'e'),
    (Vowel(Close_mid, Front).rounded().make() , 'ø'),
    (Vowel(Open_mid, Front).make() , 'ɛ'),
    (Vowel(Open_mid, Front).rounded().make() , 'œ'),
    (Vowel(Open, Central).make() , 'a'),
    (Vowel(Mid, Central).make() , 'ə'),
    (Vowel(Close, Back).rounded().make() , 'u'),
    (Vowel(Close_mid, Back).rounded().make() , 'o'),
    (Vowel(Open_mid, Back).rounded().make() , 'ɔ'),
    # Nasals
    (Consonant(Bilabial, Nasal).voiced().make() , 'm'),
    (Consonant(Alveolar, Nasal).voiced().make() , 'n'),
    (Consonant(Palatal, Nasal).voiced().make() , 'ɲ'),
    (Consonant(Velar, Nasal).voiced().make() , 'ŋ'),
    # Plosives
    (Consonant(Bilabial, Plosive).make() , 'p'),
    (Consonant(Bilabial, Plosive).voiced().make() , 'b'),
    (Consonant(Alveolar, Plosive).make() , 't'),
    (Consonant(Alveolar, Plosive).voiced().make() , 'd'),
    (Consonant(Palatal, Plosive).make() , 'c'),
    (Consonant(Palatal, Plosive).voiced().make() , 'ɟ'),
    (Consonant(Velar, Plosive).make() , 'k'),
    (Consonant(Velar, Plosive).voiced().make() , 'g'),
    (Consonant(Uvular, Plosive).make() , 'q'),
    (Consonant(Uvular, Plosive).voiced().make() , 'ɢ'),
    # Fricatives
    (Consonant(Bilabial, Fricative).make(), 'ɸ'),
    (Consonant(Bilabial, Fricative).voiced().make(), 'β'),
    (Consonant(Labiovelar, Fricative).make(), 'f'),
    (Consonant(Labiovelar, Fricative).voiced().make(), 'v'),
    (Consonant(Alveolar, Fricative).make(), 's'),
    (Consonant(Alveolar, Fricative).voiced().make(), 'z'),
    (Consonant(Alveopalatal, Fricative).make(), 'ɕ'),
    (Consonant(Alveopalatal, Fricative).voiced().make(), 'ʑ'),
    (Consonant(Postalveolar, Fricative).make(), 'ʃ'),
    (Consonant(Postalveolar, Fricative).voiced().make(), 'ʒ'),
    (Consonant(Retroflex, Fricative).make(), 'ʂ'),
    (Consonant(Retroflex, Fricative).voiced().make(), 'ʐ'),
    (Consonant(Palatal, Fricative).make(), 'ç'),
    (Consonant(Palatal, Fricative).voiced().make(), 'ʝ'),
    (Consonant(Velar, Fricative).make(), 'x'),
    (Consonant(Velar, Fricative).voiced().make(), 'ɣ'),
    (Consonant(Uvular, Fricative).make(), 'χ'),
    (Consonant(Uvular, Fricative).voiced().make(), 'ʁ'),
    (Consonant(Glottal, Fricative).make(), 'h'),
    (Consonant(Glottal, Fricative).voiced().make(), 'ɦ'),
    # Affricates
    (Consonant(Alveolar, Affricate).make(), 'ts'),
    (Consonant(Alveolar, Affricate).voiced().make(), 'dz'),
    (Consonant(Postalveolar, Affricate).make(), 'tʃ'),
    (Consonant(Postalveolar, Affricate).voiced().make(), 'dʒ'),
    # Approximants and trills
    (Consonant(Labiovelar, Approximant).make(), 'ʍ'),
    (Consonant(Labiovelar, Approximant).voiced().make(), 'w'),
    (Consonant(Alveolar, Approximant).voiced().make(), 'ɹ'),
    (Consonant(Alveolar, Trill).voiced().make(), 'r'),
    (Consonant(Alveolar, Tap).voiced().make(), 'ɾ'),
    (Consonant(Alveolar, Approximant).with_feature(Lateral).voiced().make(), 'l'),
    (Consonant(Palatal, Approximant).voiced().make(), 'j'),
]

SimplifiedIpa = Orthography('simplified ipa', processors, symbols)

