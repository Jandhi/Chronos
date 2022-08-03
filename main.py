
from chronology.sound_change import Category, SoundChange, Transform
from orthography.simplified_ipa import SimplifiedIpa as SIPA
from phonology.features import Close, Front, Long, Plosive, Voiced, Vowel

word = SIPA.string_to_word('māmbõrtla')


sc = SoundChange(
    input=[Category().has(Plosive).without(Voiced)],
    output=[Transform(0).add(Voiced)],
    prefix=[Category().has(Vowel)],
)

word = sc.apply(word)
SIPA.print_syllables(word)
SIPA.print_word(word)