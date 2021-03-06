﻿using System.Collections.Generic;
using Chronos.Categories;
using Chronos.Features;
using Chronos.Phonology;

namespace Chronos.Coding
{
    public class LatinCypher : Cypher
    {
        public static readonly Dictionary<string, Lingon> LatinLingons = new Dictionary<string, Lingon>
        {
            {"a", Lingon.MakeVowel(VowelHeight.Low, VowelBackness.Back)},
            {"e", Lingon.MakeVowel(VowelHeight.Mid, VowelBackness.Front)},
            {"i", Lingon.MakeVowel(VowelHeight.High, VowelBackness.Front)},
            {"o", Lingon.MakeVowel(VowelHeight.Mid, VowelBackness.Back, VowelFeature.Rounded)},
            {"u", Lingon.MakeVowel(VowelHeight.High, VowelBackness.Back, VowelFeature.Rounded)},
            
            {"ā", Lingon.MakeVowel(VowelHeight.Low, VowelBackness.Back, VowelFeature.Long)},
            {"ē", Lingon.MakeVowel(VowelHeight.Mid, VowelBackness.Front, VowelFeature.Long)},
            {"ī", Lingon.MakeVowel(VowelHeight.High, VowelBackness.Front, VowelFeature.Long)},
            {"ō", Lingon.MakeVowel(VowelHeight.Mid, VowelBackness.Back, VowelFeature.Long, VowelFeature.Rounded)},
            {"ū", Lingon.MakeVowel(VowelHeight.High, VowelBackness.Back, VowelFeature.Long, VowelFeature.Rounded)},
            
            {"p", Lingon.MakeConsonant(PoA.Labial, MoA.Plosive)},
            {"t", Lingon.MakeConsonant(PoA.Alveolar, MoA.Plosive)},
            {"c", Lingon.MakeConsonant(PoA.Velar, MoA.Plosive)},
            {"q", Lingon.MakeConsonant(PoA.Velar, MoA.Plosive, ConsonantalFeature.Labialized)},
            {"b", Lingon.MakeConsonant(PoA.Labial, MoA.Plosive, ConsonantalFeature.Voiced)},
            {"d", Lingon.MakeConsonant(PoA.Alveolar, MoA.Plosive, ConsonantalFeature.Voiced)},
            {"g", Lingon.MakeConsonant(PoA.Velar, MoA.Plosive, ConsonantalFeature.Voiced)},
            
            {"m", Lingon.MakeConsonant(PoA.Labial, MoA.Nasal)},
            {"n", Lingon.MakeConsonant(PoA.Alveolar, MoA.Nasal)},
            {"l", Lingon.MakeConsonant(PoA.Alveolar, MoA.LateralApproximant)},
            {"r", Lingon.MakeConsonant(PoA.Alveolar, MoA.Trill)},
            {"h", Lingon.MakeConsonant(PoA.Glottal, MoA.Fricative)},
            {"s", Lingon.MakeConsonant(PoA.Alveolar, MoA.Fricative)},
            
            {"f", Lingon.MakeConsonant(PoA.Labial, MoA.Fricative)},
            {"v", Lingon.MakeConsonant(PoA.Labial, MoA.Approximant, ConsonantalFeature.Labialized)},
            {"j", Lingon.MakeConsonant(PoA.Palatal, MoA.Approximant)},
            {"nh", Lingon.MakeConsonant(PoA.Palatal, MoA.Nasal)},
            {"lh", Lingon.MakeConsonant(PoA.Palatal, MoA.LateralApproximant)}
        };
        
        public static readonly Dictionary<string, Category> LatinCategories = new Dictionary<string, Category>
        {
            {"V", Category.MakeWith(Feature.Vowel).Without(VowelFeature.Long)},
            {"L", Category.MakeWith(Feature.Vowel, VowelFeature.Long)},
            {"C", Category.MakeWith(Feature.Consonant)},
            {"F", Category.MakeWith(VowelBackness.Front)},
            {"B", Category.MakeWith(VowelBackness.Back)},
            {"S", Category.MakeWith(MoA.Plosive).Without(ConsonantalFeature.Voiced)},
            {"Z", Category.MakeWith(MoA.Plosive, ConsonantalFeature.Voiced)}
        };
        
        public LatinCypher() : base(LatinLingons, LatinCategories)
        {
            
        }
        
        public static readonly List<string> ChangeStrings = new List<string>
        {
            "[sm]//_#",
            "i/j/_V",
            "L/1[-long]/_",
            "e//Vr_#",
            "v//V_V",
            "u/o/_#",
            "gn/nh/_",
            "S/1[+voiced]/V_V",
            "c/i/F_t",
            "c/u/B_t",
            "p//V_t",
            "ii/i/_",
            "e//C_rV",
            "lj/lh/_",
        };

        public static readonly List<string> Dictionary = new List<string>
        {
            "lector",
            "doctor",
            "focus",
            "jocus",
            "districtus",
            "cīvitatem",
            "adoptare",
            "opera",
            "secundus",
            "fīliam",
            "pōntem",
        };
    }
}