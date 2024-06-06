

class MyContextManager:
    def __enter__(self):
        print("Entering the block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        else:
            print("Exited without exception")
        # Trueを返すと例外が処理されたことになり、Falseを返すと例外が再発する
        return True  # 例外を処理済みとする

# 使用例
try:
    with MyContextManager() as manager:
        print("Inside the block")
        raise ValueError("Something went wrong!")
except Exception as e:
    print("Caught an exception outside: ", e)
else:
    print("No exception caught outside.")

"""
Pythonでカスタムコンテキストマネージャを作成し、with文を使用した際にブロック内で発生した例外を受け取る方法を示すサンプルコードを以下に示します。この例では、__enter__メソッドと__exit__メソッドを持つクラスを定義し、__exit__メソッド内で例外を検出して処理します。
-
このコードでは、MyContextManagerクラスがコンテキストマネージャとして機能します。with文内で例外（この場合はValueError）が発生すると、__exit__メソッドが自動的に呼び出され、発生した例外の型、値、トレースバックが引数として渡されます。ここで例外を適切に処理し、Trueを返すことで例外が処理済みとされ、外部のtry-exceptブロックでは捕捉されません。
"""
# https://blog.mtb-production.info/entry/2018/04/10/183000
# https://blog.mtb-production.info/entry/2018/04/10/183000

