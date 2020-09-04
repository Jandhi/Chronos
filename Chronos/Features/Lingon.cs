using System.Collections.Generic;
using System.Linq;
using System.Text;
using Chronos.Categories;
using Chronos.Coding;
using Chronos.Phonology;

namespace Chronos.Features
{
    public class Lingon : IMatcher
    {
        public virtual List<Feature> Features { get; }
        public virtual string Symbol { get; }
        
        protected Lingon(){}
        
        public Lingon(string symbol, List<Feature> features)
        {
            Symbol = symbol;
            Features = features;
        }

        public Lingon(string symbol, params Feature[] features)
        {
            Symbol = symbol;
            Features = features.ToList();
        }
        
        public override string ToString()
        {
            var sb = new StringBuilder(Symbol);
            foreach (var feature in Features.Where(ft => ft != Feature.Vowel && ft != Feature.Consonant))
            {
                sb.Append($"[+{feature.Name}]");
            }

            return sb.ToString();
        }

        public virtual bool IsMatch(Lingon lingon)
        {
            return Features.TrueForAll(ft => lingon.Features.Contains(ft));
        }

        public bool Equals(Lingon other)
        {
            return Features.TrueForAll(ft => other.Features.Contains(ft)) &&
                other.Features.TrueForAll(ft => Features.Contains(ft));
        }

        public static Lingon MakeVowel(VowelHeight height, VowelBackness backness, params VowelFeature[] vowelFeatures)
        {
            var lingon = new Lingon("V", height, backness, Feature.Vowel);
            lingon.Features.AddRange(vowelFeatures);
            return lingon;
        }

        public static Lingon MakeConsonant(PoA poA, MoA moA, params ConsonantalFeature[] consonantalFeatures)
        {
            var lingon = new Lingon("C", poA, moA, Feature.Consonant);
            lingon.Features.AddRange(consonantalFeatures);
            return lingon;
        }

        public static readonly Lingon EndOfWord = new Lingon("#", Feature.EndOfWord);
        public static readonly Lingon StartOfWord = new Lingon("#", Feature.StartOfWord);
        public static readonly Lingon SyllableBreak = new Lingon(".", Feature.EndOfSyllable);
        public static readonly Lingon Unknown = new Lingon("?", Feature.Unknown);
        public static readonly Lingon[] DefaultSet = {EndOfWord, StartOfWord, SyllableBreak, Unknown};

        public string ToString(Cypher cypher)
        {
            return cypher.DecodeWord(new Sequence {this});
        }
    }
}