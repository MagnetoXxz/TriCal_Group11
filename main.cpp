#include <stdio.h>
#include "TriMath.h"


int main(int argc, char** argv) {
	printf("------------------------------------------------\n");
//	printf("%lf\n", cal_fact(11));
//	printf("%lf\n", cal_exp(2, 0));
//	printf("%lf\n", cal_abs(-2.14));
//	printf("%lf\n", cal_abs(2.14));
//	printf("%lf\n", cal_sqrt(2, 0.0001));
//	printf("%lf\n", cal_pi(0.0001));
	double pi = cal_pi(0.00001);
//	printf("%lf\n", angle_2_rad(60, pi));
//	printf("%lf\n", rad_2_angle(4 * pi, pi));
	double rad = pi;
	printf("pi %lf\n", pi);	
	printf("sin %lf\n", taylor_sin(rad, 7, pi));
	printf("cos %lf\n", taylor_cos(rad, 15, pi));
	printf("tan %lf\n", taylor_tan(rad, 15, pi));
	printf("double fact %lf\n", cal_dfact(6));
//	printf("%lf\n", taylor_arcs(1, 45));
	printf("arcsin %lf\n", cmp_arcs(-1, 15, 0.00000001, pi));
	printf("arctan %lf\n", cmp_arct(0.00000001, 15, 0.00001, pi));
	printf("arccos %lf\n", cmp_arcc(-1, 15, 0.00000001, pi));
	printf("------------------------------------------------\n");
	return 0;
}

