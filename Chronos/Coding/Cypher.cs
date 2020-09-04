using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Chronos.Categories;
using Chronos.Change;
using Chronos.Change.Generation;
using Chronos.Features;

namespace Chronos.Coding
{
    public class Cypher
    {
        public Cypher(Dictionary<string, Lingon> lingons, Dictionary<string, Category> categories)
        {
            Lingons = lingons;
            Categories = categories;
        }

        public Dictionary<string, Lingon> Lingons { get; }
        public Dictionary<string, Category> Categories { get; }

        public Sequence EncodeWord(string input)
        {
            var word = new Sequence();
            word.Add(Lingon.StartOfWord);
            for (var index = 0; index < input.Length; index++)
            {
                var maxLength = input.Length - index;
                //Maximal munch
                for (var len = maxLength; len > 0; len--)
                {
                    var bunch = input.Substring(index, len);

                    if (Lingons.ContainsKey(bunch))
                    {
                        word.Add(Lingons[bunch]);
                        index += len - 1; //Move to end of bunch
                    }
                    else if (len == 1)
                    {
                        word.Add(Lingon.Unknown);
                    }
                }
            }
            word.Add(Lingon.EndOfWord);

            return word;
        }
        
        public Pattern EncodePattern(string input)
        {
            var pattern = new Pattern();
            for (var index = 0; index < input.Length; index++)
            {
                var maxLength = input.Length - index;
                //Maximal munch
                for (var len = maxLength; len > 0; len--)
                {
                    var bunch = input.Substring(index, len);

                    if (Lingon.DefaultSet.FirstOrDefault(ling => ling.Symbol == bunch) != null)
                    {
                        pattern.Add(Lingon.DefaultSet.FirstOrDefault(ling => ling.Symbol == bunch));
                        index += len - 1;
                        break;
                    } 
                    else if (bunch.StartsWith("[") && bunch.EndsWith("]") && len > 2)
                    {
                        pattern.Add(new NonceSet(EncodePattern(bunch.Substring(1, bunch.Length - 2))));
                        index += len - 1;
                        break;
                    }
                    else if (Lingons.ContainsKey(bunch))
                    {
                        pattern.Add(Lingons[bunch]);
                        index += len - 1; //Move to end of bunch
                        break;
                    }
                    else if (Categories.ContainsKey(bunch))
                    {
                        pattern.Add(Categories[bunch]);
                        index += len - 1; //Move to end of bunch
                        break;
                    }
                    else if (len == 1)
                    {
                        pattern.Add(Lingon.Unknown);
                        break;
                    }
                }
            }

            return pattern;
        }

        public List<Generator> EncodeGenerators(string input)
        {
            var list = new List<Generator>();
            
            for (var index = 0; index < input.Length; index++)
            {
                var maxLength = input.Length - index;
                //Maximal munch
                for (var len = maxLength; len > 0; len--)
                {
                    var bunch = input.Substring(index, len);

                    if (Lingons.ContainsKey(bunch))
                    {
                        list.Add(new Adder(Lingons[bunch]));
                        index += len - 1; //Move to end of bunch
                    }
                    else if (bunch.Length > 2 && bunch.Substring(1).StartsWith("[") && bunch.EndsWith("]"))
                    {
                        var indexString = bunch.Substring(0, 1);
                        try
                        {
                            var indexNum = int.Parse(indexString);
                            var features = bunch.Substring(1).Split("]").ToList().Select(ft => ft.Replace("[", ""));
                            var addFeatures = new List<Feature>();
                            var subFeatures = new List<Feature>();
                            foreach (var feature in features.Where(ft => ft != ""))
                            {
                                var add = !feature.StartsWith("-");
                                var name = feature.Substring(1);
                                (add ? addFeatures : subFeatures).Add(Feature.AllFeatures.First(ft => String.Equals(ft.Name, name, StringComparison.CurrentCultureIgnoreCase)));
                            }
                            
                            list.Add(new Modifier(indexNum, addFeatures, subFeatures));
                            index += len - 1; //Move to end of bunch
                            break;
                        }
                        catch (FormatException e)
                        {
                            break;
                        }
                    }
                }
            }

            return list;
        }

        public string DecodeWord(Sequence sequence)
        {
            var sb = new StringBuilder();
            foreach (var lingon in sequence)
            {
                if (Lingon.DefaultSet.Contains(lingon))
                {
                    sb.Append(lingon.Symbol);
                }
                else
                {
                    sb.Append(Lingons.First(pair => pair.Value.Equals(lingon)).Key);
                }
            }

            return sb.ToString();
        }

        public string DecodePattern(Pattern pattern)
        {
            var sb = new StringBuilder();
            foreach (var matcher in pattern)
            {
                switch (matcher)
                {
                    case Lingon lingon:
                        if (Lingon.DefaultSet.Contains(lingon))
                        {
                            sb.Append(lingon.Symbol);
                        }
                        else
                        {
                            sb.Append(Lingons.First(pair => pair.Value.Equals(lingon)).Key);
                        }
                        break;
                    case Category cat:
                        sb.Append(Categories.First(pair => pair.Value.Equals(cat)).Key);
                        break;
                    case NonceSet nonceSet:
                        sb.Append($"[{DecodePattern(nonceSet.Set.ToPattern())}]");
                        break;
                }
            }

            return sb.ToString();
        }

        public SoundChange EncodeSoundChange(string input)
        {
            input = input.Replace(">", "/");
            var split = input.Split("/");
            var pattern = EncodePattern(split[0]);
            var result = EncodeGenerators(split[1]);
            Context context;
            if (split[2] != "")
            {
                var contextSplit = split[2].Split("_");
                context = new Context(EncodePattern(contextSplit[0]), EncodePattern(contextSplit[1]));
            }
            else
            {
                context = new Context();
            }
            
            var exception = split.Length > 3 ? new Context(EncodePattern(split[3].Split("_")[0]), EncodePattern(split[3].Split("_")[1])) : null;
            return new SoundChange(pattern, result, context, exception);
        }
    }
}