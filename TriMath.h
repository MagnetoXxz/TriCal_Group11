#ifndef __TRIMATH_H
#define __TRIMATH_H

double cal_fact(int num);
double cal_exp(double num, int index);
double cal_abs(double num);
double cal_sqrt(double num, double prec);
double cal_pi(double cal_pi_accu);
double angle_2_rad(double angle, double pi);
double rad_2_angle(double rad, double pi);
double taylor_sin(double x, int n, double pi);
double taylor_cos(double x, int n, double pi);
double taylor_tan(double x, int n, double pi);
double cal_dfact(int num);
double cmp_arcs(double x, int n, double accu, double pi);
double taylor_arcs(double x, int n);
double cmp_arct(double x, int n, double accu, double pi);
double cmp_arcc(double x, int n, double accu, double pi);

#endif

