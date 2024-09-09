def is_permutation(str1: str, str2: str) -> bool:
    """
    Check if one string is a permutation of the other.

    Args:
    str1 (str): First string.
    str2 (str): Second string.

    Returns:
    bool: True if str1 is a permutation of str2, False otherwise.
    """
    # If lengths are different, they cannot be permutations
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare
    return sorted(str1) == sorted(str2)
