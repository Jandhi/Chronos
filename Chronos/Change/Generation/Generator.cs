using Chronos.Coding;

namespace Chronos.Change.Generation
{
    public abstract class Generator
    {
        public abstract void ModifySequence(Sequence source, Sequence sequence);
        public abstract string ToString(Cypher cypher);
    }
}