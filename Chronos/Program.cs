using System;
using System.Collections.Generic;
using System.Linq;
using Chronos.Change;
using Chronos.Coding;

namespace Chronos
{
    class Program
    {
        static void Main(string[] args)
        {
            var cypher = new VolodnianCypher();
            
            
            
            var changes = VolodnianCypher.ChangeStrings.Select(cypher.EncodeSoundChange).ToList();
            var words = VolodnianCypher.Dictionary.Select(cypher.EncodeWord).ToList();
            
            foreach (var word in words)
            {
                var result = word.ToSequence();
                result = changes.Aggregate(result, (current, change) => change.Apply(current));
                Console.WriteLine($"{cypher.DecodeWord(word.WithoutEnds())} > {cypher.DecodeWord(result.WithoutEnds())}");
            }
            
        }
    }
}
