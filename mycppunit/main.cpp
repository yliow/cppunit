
#include <iostream>
#include "vector.h"

int main()
{
    double x;
    std::cin >> x;
    vector v(x, 3);
    std::cout << v.get_x() << std::endl;
    return 0;
}
