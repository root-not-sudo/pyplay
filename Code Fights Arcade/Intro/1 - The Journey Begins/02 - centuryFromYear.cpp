//#include <math.h>
int centuryFromYear(int year) {
    year = year - 1;
    float cent = 0;
    cent = floor(year/100) + 1;
    return cent;
}
