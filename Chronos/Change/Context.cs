namespace Chronos.Change
{
    public class Context
    {
        public Context(Pattern before = null, Pattern after = null)
        {
            Before = before ?? new Pattern();
            After = after ?? new Pattern();
        }

        public Pattern Before { get; }
        public Pattern After { get; }
    }
}