using System;
class Program
{
    static void Main()
    {
        // 定数
        int FIRST_DISTANCE = 3; //初乗り料金の距離
        int FIRST_FARE = 500; // 初乗り料金の金額
        // 入力
        var lines = Console.ReadLine().Split(" ");
        int distance = int.Parse(lines[0]);
        int fare = int.Parse(lines[1]); //fare:運賃
        // 計算
        int calcDistance = distance - FIRST_DISTANCE;
        if (calcDistance < 0){ calcDistance = 0; }
        int result = (calcDistance * fare) + FIRST_FARE;
        // 結果
        Console.WriteLine(result.ToString());
    }
}