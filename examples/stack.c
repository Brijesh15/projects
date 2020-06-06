#ifdef _WIN32
#   define API __declspec(dllexport)
#else
#   define API
#endif

#include <stdio.h>

//API double* testfun1(double x, double* y, char* str)
API double testfun1(double x, char y[5], char* str)
{
	printf("%lf %p %s\n",x,y,str);
	y[0] = x;
	y[1] = x * 2;
	y[2] = x * 3;
	return x * 4;
}
