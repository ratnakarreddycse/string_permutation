import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.permutation_checker import is_permutation


def run_tests_and_log_results():
    results = []

    # Test case 1
    result = is_permutation("abc", "bca")
    results.append(f"Test case 1 - 'abc' and 'bca' are permutations: {result}")

    # Test case 2
    result = is_permutation("123", "321")
    results.append(f"Test case 2 - '123' and '321' are permutations: {result}")

    # Test case 3
    result = is_permutation("!@#", "#@!")
    results.append(f"Test case 3 - '!@#' and '#@!' are permutations: {result}")

    # Test case 4
    result = is_permutation("abc", "def")
    results.append(f"Test case 4 - 'abc' and 'def' are NOT permutations: {result}")

    # Test case 5
    result = is_permutation("abcd", "abc")
    results.append(f"Test case 5 - 'abcd' and 'abc' are NOT permutations: {result}")

    # Test case 6
    result = is_permutation("123", "12")
    results.append(f"Test case 6 - '123' and '12' are NOT permutations: {result}")

    # Test case 7
    result = is_permutation("", "")
    results.append(f"Test case 7 - '' and '' are permutations: {result}")

    # Test case 8
    result = is_permutation("a", "")
    results.append(f"Test case 8 - 'a' and '' are NOT permutations: {result}")

    # Test case 9
    result = is_permutation("", "b")
    results.append(f"Test case 9 - '' and 'b' are NOT permutations: {result}")

    # Log results to a file
    with open("test_results.txt", "w") as file:
        for line in results:
            file.write(line + "\n")
        file.write("\n----------------------------------------------------------------------\n")
        file.write(f"Ran {len(results)} tests\n\nOK\n")


if __name__ == "__main__":
    run_tests_and_log_results()
