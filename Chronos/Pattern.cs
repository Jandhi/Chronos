using System.Collections.Generic;
using Chronos.Categories;
using Chronos.Features;

namespace Chronos
{
    public class Pattern : List<IMatcher>
    {
        public bool Matches(List<Lingon> lingons)
        {
            if (lingons.Count != Count) return false;
            for (var i = 0; i < Count; i++)
            {
                if (!this[i].IsMatch(lingons[i])) return false;
            }
            return true;
        }
    }

    public static class PatternFunctions
    {
        public static Pattern ToPattern(this IEnumerable<IMatcher> list)
        {
            var pattern = new Pattern();
            pattern.AddRange(list);
            return pattern;
        }
    }
}