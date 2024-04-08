#include <stdio.h>
#include <math.h>
#include "TriMath.h"

#define PI acos(-1)


double pi_deviat(double pi){
	return cal_abs(pi - PI) / PI;
}


double sin_deviat(double angle, int n, double pi){
	double rad_pi = angle_2_rad(angle, pi);
	double rad_PI = angle_2_rad(angle, PI);
	double tl_sin = taylor_sin(rad_pi, n, pi);
	double nom_sin = sin(rad_PI);
	printf("normal sine is %lf, approximated sine is %lf\n", nom_sin, tl_sin);
	return cal_abs((tl_sin - nom_sin) / nom_sin);
}


double cos_deviat(double angle, int n, double pi){
	double rad_pi = angle_2_rad(angle, pi);
	double rad_PI = angle_2_rad(angle, PI);
	double tl_cos = taylor_cos(rad_pi, n, pi);
	double nom_cos = cos(rad_PI);
	printf("normal cosine is %lf, approximated cosine is %lf\n", nom_cos, tl_cos);
	return cal_abs((tl_cos - nom_cos) / nom_cos);
}


double tan_deviat(double angle, int n, double pi){
	double rad_pi = angle_2_rad(angle, pi);
	double rad_PI = angle_2_rad(angle, PI);
	double tl_tan = taylor_tan(rad_pi, n, pi);
	double nom_tan = tan(rad_PI);
	printf("normal tangent is %lf, approximated tangent is %lf\n", nom_tan, tl_tan);
	return cal_abs((tl_tan - nom_tan) / nom_tan);
}


double arcs_deviat(double x, int n, double accu, double pi){
	double cmp_rad = cmp_arcs(x, n, accu, pi);
	double nom_rad = asin(x);;
	double cmp_angle = rad_2_angle(cmp_rad, pi);
	double nom_angle = rad_2_angle(nom_rad, PI);
	printf("normal arcsine is %lf, approximated arcsine is %lf\n", nom_angle, cmp_angle);
	return cal_abs((cmp_angle - nom_angle) / nom_angle);
}


double arcc_deviat(double x, int n, double accu, double pi){
	double cmp_rad = cmp_arcc(x, n, accu, pi);
	double nom_rad = acos(x);
	double cmp_angle = rad_2_angle(cmp_rad, pi);
	double nom_angle = rad_2_angle(nom_rad, PI);
	printf("normal arccosine is %lf, approximated arccosine is %lf\n", nom_angle, cmp_angle);
	return cal_abs((cmp_angle - nom_angle) / nom_angle);
}


double arct_deviat(double x, int n, double accu, double pi){
	double cmp_rad = cmp_arct(x, n, accu, pi);
	double nom_rad = atan(x);
	double cmp_angle = rad_2_angle(cmp_rad, pi);
	double nom_angle = rad_2_angle(nom_rad, PI);	
	printf("normal arctangent is %lf, approximated arctangent is %lf\n", nom_angle, cmp_angle);
	return cal_abs((cmp_angle - nom_angle) / nom_angle);
}

