from test_framework import generic_test
from collections import Counter

def can_form_palindrome(s: str) -> bool:
    counts = Counter(s)
    counts = Counter([i%2 for i in counts.values()])
    return counts[1]<2


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
