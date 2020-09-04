using Chronos.Features;

namespace Chronos.Phonology
{
    public class MoA : Feature
    {
        public MoA(string name) : base(name)
        {
        }
        
        public static readonly MoA Nasal = new MoA("Nasal"); 
        public static readonly MoA Plosive = new MoA("Plosive");
        public static readonly MoA Fricative = new MoA("Fricative");
        public static readonly MoA Affricate = new MoA("Affricate");
        public static readonly MoA Approximant = new MoA("Approximant");
        public static readonly MoA LateralApproximant = new MoA("LateralApproximant");
        public static readonly MoA Trill = new MoA("Trill");

        public static readonly MoA[] MoAs =
            {Nasal, Plosive, Fricative, Affricate, Approximant, LateralApproximant, Trill};
    }
}