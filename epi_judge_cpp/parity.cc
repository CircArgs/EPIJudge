#include "test_framework/generic_test.h"
#include <iostream>
// Original naive implementation
// short Parity(unsigned long long x) {
//   auto count = 0;
//   for(int i = 0; i<sizeof(decltype(x))*8;){
//     count+=(x>>i)&1;
//     i+=1;
//   }
//   return count%2;
// }

// my optimized version
// short Parity(unsigned long long x)
// {
//     auto num_bits = sizeof(decltype(x)) * 8;
//     auto curr_bits = num_bits / 2;
//     auto lower_bits = decltype(x)(~0) >> curr_bits;
//     while (curr_bits > 0 && x > 0)
//     {
//         x = (x >> curr_bits) ^ (x & lower_bits);
//         curr_bits /= 2;
//         lower_bits = lower_bits >> curr_bits;
//     }
//     return x;
// }

short Parity(unsigned long x)
{
    x ^=x >> 32;
    x ^=x >> 16;
    x^=x >> 8;
    x^=x>> 4;
    x^=x >> 2;
    x ^= x >> 1;
    return x & 0b1;
}

int main(int argc, char *argv[])
{
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"x"};
    return GenericTestMain(args, "parity.cc", "parity.tsv", &Parity,
                           DefaultComparator{}, param_names);
}
