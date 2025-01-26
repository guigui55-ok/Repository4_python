"""
シンプルな線形合同法 (Linear Congruential Generator, LCG) を使用
"""

class CustomRandom:
    def __init__(self, seed: int = 12345):
        """
        独自のランダム数生成器を初期化する。
        :param seed: シード値 (初期値)
        """
        self.state = seed
        self.a = 1664525  # 乗数
        self.c = 1013904223  # 加算定数
        self.m = 2**32  # モジュラス

    def next(self) -> float:
        """
        次のランダムな値を生成する (0.0から1.0の範囲)。
        :return: ランダムな浮動小数点数
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m

    def randint(self, min_value: int, max_value: int) -> int:
        """
        指定された範囲内のランダムな整数を生成する。
        :param min_value: 範囲の最小値
        :param max_value: 範囲の最大値
        :return: ランダムな整数
        """
        return min_value + int(self.next() * (max_value - min_value + 1))


if __name__ == "__main__":
    # 使用例
    rng = CustomRandom(seed=42)
    print(rng.randint(1, 10))  # 1から10の間のランダムな整数を生成


