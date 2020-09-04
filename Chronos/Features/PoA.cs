using Chronos.Features;

namespace Chronos.Phonology
{
    public class PoA : Feature
    {
        public PoA(string name) : base(name)
        {}
        
        public static readonly PoA Labial = new PoA("Labial");
        public static readonly PoA Dental = new PoA("Dental");
        public static readonly PoA Alveolar = new PoA("Alveolar");
        public static readonly PoA Postalveolar = new PoA("Postalveolar");
        public static readonly PoA Palatal = new PoA("Palatal");
        public static readonly PoA Velar = new PoA("Velar");
        public static readonly PoA Uvular = new PoA("Uvular");
        public static readonly PoA Glottal = new PoA("Glottal");
        public static readonly PoA[] PoAs = {Labial, Dental, Alveolar, Postalveolar, Palatal, Velar, Uvular, Glottal};
    }
}