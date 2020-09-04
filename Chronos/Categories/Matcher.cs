using Chronos.Coding;
using Chronos.Features;

namespace Chronos.Categories
{
    public interface IMatcher
    {
        bool IsMatch(Lingon lingon);
        string ToString(Cypher cypher);
    }
}