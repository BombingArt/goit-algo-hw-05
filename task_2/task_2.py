from typing import Callable
import re


def generator_numbers(text: str):
    string_numbers = re.findall('\b\d+\.\d+\b', text)
    for number in string_numbers:
        yield float(number)


def sum_profit(text: str, func: Callable):
    profit = sum(func(text))
    return profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
