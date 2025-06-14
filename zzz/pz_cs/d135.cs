using System;
class Program
{
    static void Main()
    {
        // Input
        var line = Console.ReadLine();
        int D = int.Parse(line);
        // 計算
        double N = (D / 180) + 2;
        // 結果
        string result = ((int)N).ToString();
        Console.WriteLine(result);
    }
}