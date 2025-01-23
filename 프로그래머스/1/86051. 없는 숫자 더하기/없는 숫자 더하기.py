def solution(numbers):
    all_numbers = set(range(10))
    missing_numbers = all_numbers - set(numbers)
    return sum(missing_numbers)