namespace Chronos.Features
{
    public class ConsonantalFeature : Feature
    {
        public ConsonantalFeature(string name) : base(name)
        {
        }

        public static readonly ConsonantalFeature Palatalized = new ConsonantalFeature("Palatalized");
        public static readonly ConsonantalFeature Labialized = new ConsonantalFeature("Labialized");
        public static readonly ConsonantalFeature Voiced = new ConsonantalFeature("Voiced");
        public static readonly ConsonantalFeature[] ConsonantalFeatures = {Palatalized, Labialized, Voiced};
    }
}