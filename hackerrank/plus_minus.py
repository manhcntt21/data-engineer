# problem: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

def plus_minus(array, n):
    result = []
    counter_pos_value = 0
    counter_neg_value = 0
    counter_zer_value = 0
    for i in range(n):
        if array[i] > 0: counter_pos_value += 1
        elif array[i] < 0: counter_neg_value += 1
        else: counter_zer_value += 1
    proportion_pos = counter_pos_value/n if counter_pos_value != 0 else 0
    proportion_nes = counter_neg_value/n if counter_neg_value != 0 else 0
    proportion_zor = counter_zer_value/n if counter_zer_value != 0 else 0
    result.append(proportion_pos)
    result.append(proportion_nes)
    result.append(proportion_zor)
    for i in range(len(result)):
        print(result[i])
    return result


if __name__ == '__main__':
    with open('input/plus_minus.txt', encoding='utf-8') as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    n = int(data[0])
    array = data[1].split(' ')
    array = [int(x) for x in array]

    result = plus_minus(array, n)

    with open('input/plus_minus_out.txt', 'w') as f:
        f.write(str(result))
