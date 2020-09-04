using System.Collections.Generic;
using System.Linq;
using System.Text;
using Chronos.Coding;
using Chronos.Features;

namespace Chronos.Change.Generation
{
    public class Modifier : Generator
    {
        public Modifier(int index, List<Feature> addFeatures, List<Feature> subtractFeatures = null)
        {
            Index = index - 1;
            AddFeatures = addFeatures;
            SubtractFeatures = subtractFeatures ?? new List<Feature>();
        }

        public int Index { get; }
        public List<Feature> AddFeatures { get; }
        public List<Feature> SubtractFeatures { get; }
        
        public override void ModifySequence(Sequence source, Sequence sequence)
        {
            sequence.Add(Modify(source[Index]));
        }

        public Lingon Modify(Lingon lingon)
        {
            var result = new Lingon(lingon.Symbol, lingon.Features.Where(ft => !SubtractFeatures.Contains(ft)).ToArray());
            foreach (var feature in AddFeatures.Where(ft => !result.Features.Contains(ft)))
            {
                result.Features.Add(feature);
            }
            return result;
        }

        public override string ToString(Cypher cypher)
        {
            var sb = new StringBuilder($"{Index}");
            foreach (var feature in AddFeatures)
            {
                sb.Append($"[+{feature.Name}]");
            }
            foreach (var feature in SubtractFeatures)
            {
                sb.Append($"[-{feature.Name}]");
            }

            return sb.ToString();
        }
    }
}