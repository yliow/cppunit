#include <iostream>
#include <string>
#include <sstream>

int main()
{
    std::ostringstream cout;
    cout << 135;
    std::string s = cout.str();
    std::cout << s[0] << '\n';
    return 0;
}
