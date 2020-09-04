using Chronos.Features;

namespace Chronos.Phonology
{
    public class VowelFeature : Feature
    {
        public VowelFeature(string name) : base(name)
        {
        }
        
        public static readonly VowelFeature Rounded = new VowelFeature("Rounded");
        public static readonly VowelFeature Lengthened = new VowelFeature("Lengthened");
        public static readonly VowelFeature Long = new VowelFeature("Long");
        public static readonly VowelFeature Overlong = new VowelFeature("Overlong");
        public static readonly VowelFeature Nasalized = new VowelFeature("Nasalized");
        public static readonly VowelFeature[] VowelFeatures = {Rounded, Lengthened, Long, Overlong, Nasalized};
    }
}