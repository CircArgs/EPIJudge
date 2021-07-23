from test_framework import generic_test

def levenshtein_distance(a: str, b: str) -> int:
    t=[[i if j<1 else (j if i<1 else None) for i in range(len(a)+1)] for j in range(len(b)+1)]
    for j in range(1, len(a)+1):
        for i in range(1, len(b)+1):
            t[i][j]=min((t[i-1][j]+1, t[i][j-1]+1, t[i-1][j-1]+(a[j-1]!=b[i-1])))
    return t[-1][-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "levenshtein_distance.py", "levenshtein_distance.tsv", levenshtein_distance
        )
    )
