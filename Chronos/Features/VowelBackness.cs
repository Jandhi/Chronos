using Chronos.Features;

namespace Chronos.Phonology
{
    public class VowelBackness : Feature
    {
        public VowelBackness(string name) : base(name)
        {
        }
        
        public static readonly VowelBackness Front = new VowelBackness("Front");
        public static readonly VowelBackness Central = new VowelBackness("Central");
        public static readonly VowelBackness Back = new VowelBackness("Back");
        public static readonly VowelBackness[] Backnesses = {Front, Central, Back};
    }
}