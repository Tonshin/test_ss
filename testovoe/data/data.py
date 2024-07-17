import datetime


def result_fibbonaci():
    def fibonacci(n):

        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

    today = datetime.datetime.today()
    day = today.day + 1
    result = fibonacci(day)
    return result



TIME_WAIT = 10