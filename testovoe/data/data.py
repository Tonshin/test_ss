import datetime

TIME_WAIT = 10
CSV_NAME = "transactions.csv"


def result_fibbonaci() -> int:
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

    today = datetime.datetime.today()
    day = today.day + 1
    result = fibonacci(day)
    return result