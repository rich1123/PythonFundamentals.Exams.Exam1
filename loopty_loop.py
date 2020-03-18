from typing import Callable, List


def generate_list(start: int, stop: int, step: int = 1) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :return: A list of integers.
    """
    # if start == stop:
    #     print(start)
    # else:
    #     res = []
    #     while start < (stop + 1):
    #         res.append(start)
    #         start += step
    #     print(res)

    return [item for item in range(start, (stop+step))]



def generate_list_with_strategy(start: int, stop: int, step: int, strategy: Callable) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :param strategy: A function to manipulate each digit .
    :return: A list of integers.
    """


    # strategy = (generate_list_with_strategy())
    if start == stop:
        print(start)
    else:
        res = []
        while start < (stop + 1):
            res.append(start)
            start += step
            yield res
    # r = [item for item in range(start, (stop + step))]
    for strategy in res:
        print(strategy)





generate_list_with_strategy(1, 10, 3, lambda x: x-3)

# generate_list_with_strategy(3, 20, 1, strategy)

# generate_list_with_strategy(6, 10, 2, strategy)