def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive "
                         "integers.")
    aliquot = [x for x in range(1, number) if number % x == 0]
    sum_aliquot = sum(aliquot)
    if sum_aliquot == number:
        return "perfect"
    if sum_aliquot > number:
        return "abundant"
    return "deficient"
