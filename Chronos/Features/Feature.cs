using System.Collections.Generic;
using Chronos.Phonology;

namespace Chronos.Features
{
    public class Feature
    {
        public Feature(string name)
        {
            Name = name;
        }

        public string Name { get; }

        public static readonly Feature Vocalic = new Feature("Vocalic");
        public static readonly Feature Vowel = new Feature("Vowel");
        public static readonly Feature Consonant = new Feature("Consonant");
        public static readonly Feature Unknown = new Feature("Unknown");
        public static readonly Feature EndOfWord = new Feature("EndOfWord");
        public static readonly Feature StartOfWord= new Feature("StartOfWord");
        public static readonly Feature EndOfSyllable = new Feature("EndOfSyllable");
        public static readonly Feature[] Features =
            {Vocalic, Vowel, Consonant, Unknown, EndOfWord, StartOfWord, EndOfSyllable};

        public static Feature[] AllFeatures
        {
            get
            {
                var list = new List<Feature>();
                list.AddRange(Feature.Features);
                list.AddRange(ConsonantalFeature.ConsonantalFeatures);
                list.AddRange(MoA.MoAs);
                list.AddRange(PoA.PoAs);
                list.AddRange(VowelBackness.Backnesses);
                list.AddRange(VowelFeature.VowelFeatures);
                list.AddRange(VowelHeight.Heights);
                return list.ToArray();
            }
        }
    }
}