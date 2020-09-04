using Chronos.Coding;
using Chronos.Features;

namespace Chronos.Change.Generation
{
    public class Adder : Generator
    {
        public Adder(Lingon lingon)
        {
            Lingon = lingon;
        }

        public Lingon Lingon { get; }
        
        public override void ModifySequence(Sequence source, Sequence sequence)
        {
            sequence.Add(Lingon);
        }

        public override string ToString(Cypher cypher)
        {
            return cypher.DecodeWord(new Sequence {Lingon});
        }
    }
}