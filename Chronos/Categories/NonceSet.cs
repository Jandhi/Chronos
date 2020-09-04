using System.Collections.Generic;
using System.Linq;
using System.Text;
using Chronos.Coding;
using Chronos.Features;

namespace Chronos.Categories
{
    public class NonceSet : IMatcher
    {
        public NonceSet(List<IMatcher> set)
        {
            Set = set;
        }

        public List<IMatcher> Set { get; }

        public bool IsMatch(Lingon lingon)
        {
            return Set.Any(matcher => matcher.IsMatch(lingon));
        }

        public bool Equals(NonceSet other)
        {
            return Set.All(match => other.Set.Any(match.Equals))
                   && Set.Count == other.Set.Count;
        }

        public string ToString(Cypher cypher)
        {
            var sb = new StringBuilder("[");
            Set.ForEach(item => sb.Append(item.ToString(cypher)));
            sb.Append("]");
            return sb.ToString();
        }
    }
}