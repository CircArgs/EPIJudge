from test_framework import generic_test


def reverse(x: int) -> int:
    neg=x<0
    ret=int(str(abs(x))[::-1])
    return -ret if neg else ret

def reverse(x):
    neg=x<0
    x=abs(x)
    ret=0
    dt=1
    t=x
    count=0
    while t>0:
        # print(t)
        dt*=10
        count+=1
        t//=10

    for _ in range(count):
        dt//=10
        # print(x, dt, x%10)
        ret+=dt*(x%10)
        x//=10
    return -ret if neg else ret
        

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_digits.py", "reverse_digits.tsv", reverse
        )
    )
