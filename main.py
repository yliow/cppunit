from latextool_basic import *
s = r'''
#include <iostream>
#include <typeinfo>

int main()
{
    int x = 42;
    std::cout << (typeid(x) == typeid(int)) << '\n';
    std::cout << (typeid(42) == typeid(int)) << '\n';
    std::cout << typeid(int).name() << '\n';
    std::cout << typeid(unsigned int).name() << '\n';
    std::cout << typeid(char).name() << '\n';
    std::cout << typeid(bool).name() << '\n';
    std::cout << typeid(int *).name() << '\n';
    std::cout << typeid(int []).name() << '\n';
    std::cout << typeid(int &).name() << '\n';
    std::cout << (typeid(int &) == typeid(int)) << '\n';

    return 0;
}
'''.strip()
print console(s)
file('typeinfo/main.cpp', 'w').write(s)
print shell('g++ main.cpp; ./a.out', dir='typeinfo')

