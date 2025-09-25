#ifndef VECTOR_H
#define VECTOR_H

class vector
{
public:
    vector(double x, double y)
        : _x(x), _y(y)
    {}

    double get_x() const;
    double get_y() const;

private:
    double _x, _y;
};

#endif
