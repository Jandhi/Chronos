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
            var cypher = new LatinCypher();
            
            var changeStrings = new List<string>
            {
                "[sm]//_#",
                "i/j/_V",
                "L/1[-long]/_",
                "e//Vr_#",
                "v//V_V",
                "u/o/_#",
                "gn/nh/_",
                "S/1[+voiced]/V_V",
                "c/i/F_t",
                "c/u/B_t",
                "p//V_t",
                "ii/i/_",
                "e//C_rV",
                "lj/lh/_"
            };

            var dictionary = new List<string>
            {
                "lector",
                "doctor",
                "focus",
                "jocus",
                "districtus",
                "cīvitatem",
                "adoptare",
                "opera",
                "secundus",
                "fīliam",
                "pōntem",
            };
            
            var changes = changeStrings.Select(cypher.EncodeSoundChange).ToList();
            var words = dictionary.Select(cypher.EncodeWord).ToList();
            
            foreach (var word in words)
            {
                var result = word.ToSequence();
                result = changes.Aggregate(result, (current, change) => change.Apply(current));
                Console.WriteLine($"{cypher.DecodeWord(word.WithoutEnds())} > {cypher.DecodeWord(result.WithoutEnds())}");
            }
            
        }
    }
}
