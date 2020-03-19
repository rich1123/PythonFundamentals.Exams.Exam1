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
    # if start == stop:
    #     print(start)
    # else:
    #     res = []
    #     while start < (stop + 1):
    #         res.append(start)
    #         start += step
    #         yield res
    r = [strategy(item) for item in range(start, stop,  step)]
    return r

    # def generate_list_with_strategy(start, stop, step, strategy):
    #     d = [strategy(x) for x in range(start, stop, step)]
    #     return d





generate_list_with_strategy(1, 5, 1, lambda x: x**2)

# generate_list_with_strategy(3, 20, 1, strategy)

# generate_list_with_strategy(6, 10, 2, strategy)