using System.Collections.Generic;
using System.Linq;
using System.Text;
using Chronos.Change.Generation;
using Chronos.Coding;
using Chronos.Features;
using Chronos.Phonology;

namespace Chronos.Change
{
    public class SoundChange
    {
        public SoundChange(Pattern pattern, List<Generator> generators, Context context, Context exception = null)
        {
            Pattern = pattern;
            Context = context;
            Generators = generators;
            Exception = exception;
        }

        public bool Forwards { get; } = true;
        public Pattern Pattern { get; }
        public Context Context { get; }
        public Context Exception { get; }
        public List<Generator> Generators { get; }
        
        public Sequence Apply(Sequence old)
        {
            var word = old.ToSequence().WithEnds();
            for (var start = 0; start < word.Count; start++)
            {
                var maxLen = word.Count;
                for (var len = maxLen - start; len > 0; len--)
                {
                    var sequence = word.Subsequence(start, len);
                    var before = word.Subsequence(0, start);
                    var after = word.Subsequence(start + len);

                    if (Matches(sequence, before, after))
                    {
                        var modified = Modify(sequence);
                        start += (modified.Count - sequence.Count);

                        word.Clear();
                        word.AddRange(before);
                        word.AddRange(modified);
                        word.AddRange(after);
                        break;
                    }
                }
            }

            return word;
        }

        public bool Matches(Sequence sequence, Sequence before, Sequence after)
        {
            if (Context.Before.Count > before.Count || Context.After.Count > after.Count)
            {
                return false;
            }

            var sequenceMatches = Pattern.Matches(sequence);
            var beforeSequence = before.Subsequence(before.Count - Context.Before.Count);
            var beforeMatches = Context.Before.Matches(beforeSequence);
            var afterSequence = after.Subsequence(0, Context.After.Count);
            var afterMatches = Context.After.Matches(afterSequence);

            if (Exception != null && Exception.Before.Count <= before.Count && Exception.After.Count <= after.Count)
            {
                var beforeException = Exception.After.Matches(before.Subsequence(before.Count - Exception.Before.Count));
                var afterException = Exception.After.Matches(after.Subsequence(0, Exception.After.Count));
                if (beforeException && afterException) return false;
            }
            
            return sequenceMatches && beforeMatches && afterMatches;
        }

        public Sequence Modify(Sequence sequence)
        {
            Sequence result = new Sequence();
            foreach (var element in Generators)
            {
                element.ModifySequence(sequence, result);
            }

            return result;
        }

        public string ToString(Cypher cypher)
        {
            var sb = new StringBuilder();
            Pattern.ForEach(pt => sb.Append(pt.ToString(cypher)));
            sb.Append("/");
            Generators.ForEach(gen => sb.Append(gen.ToString(cypher)));
            sb.Append("/");
            Context.Before.ForEach(pt => sb.Append(pt.ToString(cypher)));
            sb.Append("_");
            Context.After.ForEach(pt => sb.Append(pt.ToString(cypher)));
            if (Exception != null)
            {
                Exception.Before.ForEach(pt => sb.Append(pt.ToString(cypher)));
                sb.Append("_");
                Exception.After.ForEach(pt => sb.Append(pt.ToString(cypher)));
            }

            return sb.ToString();
        }
    }
}