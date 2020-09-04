using System.Collections.Generic;
using System.Linq;
using System.Text;
using Chronos.Coding;
using Chronos.Features;

namespace Chronos.Categories
{
    public class Category : IMatcher
    {
        public Category(List<Feature> hasFeatures = null, List<Feature> notFeatures = null)
        {
            HasFeatures = hasFeatures ?? new List<Feature>();
            NotFeatures = notFeatures ?? new List<Feature>();
        }

        public Category With(params Feature[] features)
        {
            HasFeatures.AddRange(features);
            return this;
        }

        public Category Without(params Feature[] notFeatures)
        {
            NotFeatures.AddRange(notFeatures);
            return this;
        }

        public static Category MakeWith(params Feature[] features)
        {
            return new Category(features.ToList());
        }

        public static Category MakeWithout(params Feature[] notFeatures)
        {
            return new Category(null, notFeatures.ToList());
        }

        public List<Feature> HasFeatures { get; }
        public List<Feature> NotFeatures { get; }
        
        public bool IsMatch(Lingon lingon)
        {
            var has = HasFeatures.TrueForAll(ft => lingon.Features.Contains(ft));
            var not = NotFeatures.TrueForAll(ft => !lingon.Features.Contains(ft));
            return has && not;
        }

        public bool Equals(Category other)
        {
            return HasFeatures.TrueForAll(ft => other.HasFeatures.Contains(ft))
                   && other.HasFeatures.TrueForAll(ft => HasFeatures.Contains(ft))
                   && NotFeatures.TrueForAll(ft => other.NotFeatures.Contains(ft))
                   && other.NotFeatures.TrueForAll(ft => NotFeatures.Contains(ft));
        }

        public string ToString(Cypher cypher)
        {
            if (cypher.Categories.ContainsValue(this))
            {
                return cypher.DecodePattern(new Pattern {this});
            }
            else
            {
                var sb = new StringBuilder("?");
                HasFeatures.ForEach(feature => sb.Append($"[+{feature.Name}]"));
                NotFeatures.ForEach(feature => sb.Append($"[+{feature.Name}]"));
                return sb.ToString();
            }
        }
    }
}