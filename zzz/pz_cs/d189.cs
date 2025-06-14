using System;
class Program
{
    static void Main()
    {
        var line = Console.ReadLine();
        int yearA = int.Parse(line);
        line = Console.ReadLine();
        int yearB = int.Parse(line);
        int diff = yearB - yearA;
        string result = diff.ToString();
        Console.WriteLine(result);
    }
}