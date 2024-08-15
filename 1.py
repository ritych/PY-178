def get_divisors(n):
    """
    Возвращает список целочисленных делителей числа n.

    :param n: Число, для которого необходимо получить делители.
    :return: Список целочисленных делителей числа n.
    """
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != (n // i):
                divisors.append(n // i)
    return sorted(divisors)


n = 11_111_111
divisors = get_divisors(n)
print(divisors)
