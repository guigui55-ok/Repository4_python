using System;
using System.Linq;
class Program
{
    static void Main()
    {
        // 入力
        int calSum = int.Parse(Console.ReadLine());
        string[] calSingleArrayStr = Console.ReadLine().Split(" ");
        // 変換
        int[] calSingleArray = calSingleArrayStr.Select(int.Parse).ToArray();
        // 計算・判定
        string result = "";
        if (calSingleArray.Sum() <= calSum) {
            result = "OK";
        } else {
            result = "NG";
        }
        // 結果
        Console.WriteLine(result);
    }
}