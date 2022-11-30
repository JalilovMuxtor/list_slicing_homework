def main(numbers):
    """
    A list called numbers is given. Return the items in the odd position.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return numbers[::2]
print(main([1, 5, 6, 9, 2, 7, 3]))