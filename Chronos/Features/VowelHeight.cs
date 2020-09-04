using Chronos.Features;

namespace Chronos.Phonology
{
    public class VowelHeight : Feature
    {
        public VowelHeight(string name) : base(name)
        {
        }
        
        public static readonly VowelHeight Low = new VowelHeight("Low");
        public static readonly VowelHeight LowMid = new VowelHeight("LowMid");
        public static readonly VowelHeight Mid = new VowelHeight("Mid");
        public static readonly VowelHeight HighMid = new VowelHeight("HighMid");
        public static readonly VowelHeight High = new VowelHeight("High");
        public static readonly VowelHeight[] Heights = {Low, LowMid, Mid, HighMid, High};
    }
}