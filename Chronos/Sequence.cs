using System.Collections.Generic;
using System.Text;
using Chronos.Features;

namespace Chronos
{
    public class Sequence : List<Lingon>
    {
        public override string ToString()
        {
            var sb = new StringBuilder();
            foreach (var lingon in this)
            {
                sb.Append(lingon);
            }

            return sb.ToString();
        }

        public Sequence WithEnds()
        {
            if (Count == 0 || this[0] != Lingon.StartOfWord)
            {
                Insert(0, Lingon.StartOfWord);
                Add(Lingon.EndOfWord);
            }
            return this;
        }

        public Sequence WithoutEnds()
        {
            Remove(Lingon.StartOfWord);
            Remove(Lingon.EndOfWord);
            return this;
        }

        public Sequence Desyllabify()
        {
            RemoveAll(lingon => lingon == Lingon.SyllableBreak);
            return this;
        }

        public Sequence Syllabify()
        {
            for (var vowelIndex = 0; vowelIndex < Count; vowelIndex++)
            {
                if (this[vowelIndex].Features.Contains(Feature.Vowel))
                {
                    var index = vowelIndex;
                    while (true)
                    {
                        index--;
                        if (this[index] == Lingon.StartOfWord)
                        {
                            break;
                        }

                        if (this[index].Features.Contains(Feature.Vowel))
                        {
                            if (vowelIndex - index > 2)
                            {
                                Insert(index + 2, Lingon.SyllableBreak);
                                vowelIndex += 1;
                                break;
                            }
                            else
                            {
                                Insert(index + 1, Lingon.SyllableBreak);
                                vowelIndex += 1;
                                break;
                            }
                        }
                    }
                }
            }

            return this;
        }

        public Sequence Subsequence(int start, int length = -1)
        {
            return this.Sublist(start, length).ToSequence();
        }
    }

    public static class WordFunctions
    {
        public static Sequence ToSequence(this IEnumerable<Lingon> list)
        {
            var word = new Sequence();
            word.AddRange(list);
            return word;
        }

        public static List<T> Sublist<T>(this List<T> list, int start, int length = -1)
        {
            if (length == -1) length = list.Count - start;
            var result = new List<T>();
            for (var i = start; i < start + length; i++)
            {
                result.Add(list[i]);
            }

            return result;
        }
    }
}