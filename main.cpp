#include <stdio.h>
#include <stdlib.h>
#include <float.h>

#include "TriMath.h"
#include "test.h"


typedef enum{
	main_interf = 0,
	
} new_interf;

new_interf interf = main_interf;


double show_main_interf(void){
	interf = main_interf;
	system("cls");
	printf("Welcome to TriCal programme, you can calculate the value of any trigonometric function!\n");
	printf("1. Calculate a sine function.\n");
	printf("2. Calculate a cosine function.\n");
	printf("3. Calculate a tangent function.\n");
	printf("4. Calculate a arcsin function.\n");
	printf("5. Calculate a arccos function.\n");
	printf("6. Calculate a arctan function.\n");
	return 0;
}


double show(void){
	switch (interf){
		case 0:
			return show_main_interf();
		default:
			return DBL_MAX;
	}
} 


int main(int argc, char** argv) {
	double accu = 0.0000001;
	int n = 15;
	double pi = cal_pi(accu), x = 1000;
	double rad = 0;
	double angle = 6800;
	printf("sin(%lf) = %lf\n", rad, taylor_sin(angle_2_rad(angle, pi), n, pi));
	printf("cos(%lf) = %lf\n", rad, taylor_cos(rad, 15, pi));
	printf("tan(%lf) = %lf\n", rad, taylor_tan(rad, 15, pi));
	printf("arcsin(%lf) = %lf\n", x, cmp_arcs(x, n, accu, pi));
	printf("arccos(%lf) = %lf\n", x, cmp_arcc(x, n, accu, pi));
	printf("arctan(%lf) = %lf\n", x, cmp_arct(x, n, accu, pi));
	printf("cos(%lf) = %lf\n", rad, sin_2_cos(rad, n + 1, pi));
	printf("%d\n", taylor_cos(rad, n, pi) - 0.5 > sin_2_cos(rad, n, pi) - 0.5);
	printf("%d\n", cal_abs(taylor_cos(rad, n, pi) - 1) < cal_abs(sin_2_cos(rad, n, pi) - 1));
	printf("deviation of sin(%lf)бу is %lf%%\n", angle, sin_deviat(angle, n, pi) * 100);
	printf("deviation of arctan(%lf) is %lf%%\n", 1000, arct_deviat(1000, n, accu, pi) * 100);
}

