# problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

def birthday_cake_candels(array):
    tallest_candle = max(array)
    return array.count(tallest_candle)

if __name__ == '__main__':
    candles = [4, 4, 1, 3]
    print(birthday_cake_candels(candles))