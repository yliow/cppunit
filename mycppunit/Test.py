class Test:
    def __init__(self):
        pass

    def setup(self):
        pass

    def run(self):
        self.setup()
        
class Test:

    def __init__(self,
                 paths=[],
                 maincpp='',
                 stdin=''):
        self.paths = paths
        self.maincpp = maincpp
        self.stdin = stdin
        self.stdout = ''
        self.stderr = ''

    def setup(self):
        import os
        os.system('rm -rf tmp')
        os.system('mkdir tmp')
        for path in paths:
            os.system("cp '%s' tmp" % path)
        file('tmp/main.cpp', 'w').write(self.maincpp)
        os.system('cd tmp; g++ *.cpp')

    def teardown(self):
        import os
        os.system('rm -rf tmp')
        
    def run(self):
        import os
        os.system('cd tmp; ./a.out < stdin.txt > stdout.txt')
        self.setup()
        pass


class Test1(Test):

    def __init__(self,
                 paths=['vector.h', 'vector.cpp'],
                 maincpp=r'''
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
''')

    def run(self):
        self.setup()
        import os
        os.system('./a.out < stdin.txt > stdout.txt 2> stderr.txt')
        self.stdout = file('stdout.txt', 'r').read()
        self.stderr = file('stderr.txt', 'r').read()

class Test11(Test1):
    def __init__(self):
        Test1.__init__(self)
    def setup(self):
        self.stdin = '0'
        Test1.setup(self)
        file('stdin.txt', 'w').write('0')
        
t = Test11()
t.run()
