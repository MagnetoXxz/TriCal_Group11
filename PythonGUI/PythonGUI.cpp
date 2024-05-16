 
#include <stdio.h>
#include <float.h>
// #include "TriMath.h"

#define left 0
#define right 1

/********************************************************
* Function name: cal_exp
* Description        : Get the exponent value of a given number.
* Parameter         ��
* @num            : The base number.
* @index            : The index of the exponent.
* Return          ��The exponent value, namely, it will return <num> ^ <index>.
**********************************************************/  
double cal_exp(double num, int index){
	if (!num && index){
		return 0;
	}
	double res = 1;
	if (index > 0){
		for (int i = 0; i < index; i++){
			res *= num;
		}		
	} else if (index < 0){
		for (int i = 0; i > index; i--){
			res *= (1 / num);
		}	
	} else{ // when index = 0, any ^ 0 = 1
		return 1;
	}
	return res;
}
/*
In the whole file, DBL_MAX means not a valid retval.
*/


/********************************************************
* Function name: cal_abs
* Description        : Judge and return the absolute value of the input number.
* Parameter         ��
* @num            : A number which you want to get the absolute value of.
* Return          ��The absolute value of the input number.
**********************************************************/         
double cal_abs(double num){
	return num > 0? num: -num;
}


/********************************************************
* Function name: cal_sqrt
* Description        : Calculate the square root of an input number, with a precision to limit the deviation.
						Using Newton iteration to work out, namely, x_k+1 = 0.5 * (x_k + (a ��x_k)), where <a> is the input number which
						we want get the square root of,  when <x_k+1> is very close to <x_k>, they will be samely close to the sqruare 
						root of <a>.
* Parameter         ��
* @num            : A number which you want to get squrae root of.
* @prec            : The precision of the calculating process, the smaller <prec> is, the closer output will be to the true value.
* Return          ��The square root of the input number.
**********************************************************/    
double cal_sqrt(double num, double prec){
	if (prec <= 0 || num < 0){ // if precision or num is less than 0, return DBL_MAX to show an input error.
		return DBL_MAX;
	}
	if (num == 0){
		return 0;
	}
	double x_k, x_k_1 = num;
	while (1){
		x_k = x_k_1;
		x_k_1 = 0.5 * (x_k + (num / x_k));
		if (cal_abs(x_k_1 - x_k) <= prec){
			break;
		}
	}
	return x_k_1;
}


/********************************************************
* Function name: cal_pi
* Description        : Get pi through calculating an integral of a half-circle function, with a precision to limit the deviation.
						Namely, (-1~1)��(1 - x^2)^0.5 = pi / 2. 
* Parameter         ��
* @accu            : The precision of the calcuting process, if smaller, more intervals will be divided to compute the integral, 
						which will benifit the final precision.
* Return          ��Pi.
**********************************************************/    
double cal_pi(double accu){
	double x = -1;
	double intval = (1 - (-1)) * accu;
	double res = 0;
	double sqrt;
	double exp;
	int intval_num;
	if ((intval_num = (int) (1 / accu)) <= 0){
		return DBL_MAX;
	}
	for (int i = 0; i < intval_num; i++){
		if ((exp = cal_exp(x, 2)) == DBL_MAX){
			return DBL_MAX;
		}
		if ((sqrt = cal_sqrt(1 - exp, accu)) == DBL_MAX){
			return DBL_MAX;
		}
		res += intval * sqrt;
		x += intval;
	}
	return 2 * res;
}


/********************************************************
* Function name: cal_dfact
* Description        : Get double factorial value of a given number. Namely, n!! = n * (n-2) * (n-4) *...* 3 * 1.
						Specially, we set 0!! = 1, (-1)!! = 1.
* Parameter         ��
* @num            : The number which you want to get the double factorial value of.
* Return          ��The double factorial of the input number.
**********************************************************/    
double cal_dfact(int num){
	if (num < -1){
		return DBL_MAX;  // if num < -1, return DBL_MAX to show an input error.
	} else if (num == 1 || num == 2){
		return num;
	} else if (num == -1 or num == 0){
		return 1;
	}
	return num * cal_dfact(num - 2);
}


/********************************************************
* Function name: cal_fact
* Description        : Get factorial value of a given number. Namely, n! = n * (n-1) * (n-2) *...* 2 * 1.
						Specially, we set 0! = 1.
* Parameter         ��
* @num            : The number which you want to get the factorial value of.
* Return          ��The factorial of the input number.
**********************************************************/  
double cal_fact(int num){
	if (num < 0){
		return DBL_MAX;  // if num < 0, return DBL_MAX to show an input error.
	} else if (!num){
		return 1;
	}
	return num * cal_fact(num - 1);	
}





/********************************************************
* Function name: angle_2_rad
* Description        : Transform an angle scalar to radian.
* Parameter         ��
* @angle            : The angle to transform.
* @pi            : Pi given in the programme. 
* Return          ��The radian value. Namely, <rad> = <pi> * <angle> / 180.
**********************************************************/  
double angle_2_rad(double angle, double pi){
	return angle / 180 * pi;
}


/********************************************************
* Function name: rad_2_angle
* Description        : Transform an radian scalar to angle.
* Parameter         ��
* @rad            : The radian to transform.
* @pi            : Pi given in the programme. 
* Return          ��The angle value. Namely, <angle> = 180 * <radian> / <pi>.
**********************************************************/ 
double rad_2_angle(double rad, double pi){
	return rad / pi * 180;
}


/********************************************************
* Function name: taylor_sin
* Description        : Taylor formula approximation of sin function.
* Parameter         ��
* @x            : The input number to get the sin value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* @pi            : Pi given in the programme. 
* Return          ��The approximated sin value, namely, sin(x) ��x - x^3 / 3! + x ^ 5 / 5! - ... 
**********************************************************/ 
double taylor_sin(double x, int n, double pi){
	double res = 0;
	double exp, fact, sig;
	while (1){
		if (x >= -pi && x < pi){
			break;
		} else if (x >= pi){
			x -= 2 * pi;
		} else{
			x += 2 * pi;
		}
	}
	for (int i = 0; i < n; i++){
		exp = cal_exp(x, 2 * i + 1);
		fact = cal_fact(2 * i + 1);
		sig = cal_exp(-1, i);
		if (exp == DBL_MAX || fact == DBL_MAX || sig == DBL_MAX){
			return DBL_MAX;
		}
		res += sig * exp / fact;
	}
	if (res > 1){
		res = 1;
	} else if (res < -1){
		res = -1;
	}
	return res;
}


double sin_2_cos(double x, int n, double pi){
	double sin = taylor_sin(x, n, pi);
//	printf("sin = %lf\n", sin);
	double exp = cal_exp(sin, 2);
//	printf("exp = %lf\n", exp);	
//	printf("== 0 ? %d\n", 1 - exp == 0);	
	double sqrt = cal_sqrt(1 - exp, 0.000001);
//	printf("sqrt = %lf\n", sqrt);	
	return sqrt;
} 


/********************************************************
* Function name: taylor_cos
* Description        : Taylor formula approximation of cosine function.
* Parameter         ��
* @x            : The input number to get the cosine value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* @pi            : Pi given in the programme. 
* Return          ��The approximated cosine value, namely, cos(x) ��1 - x^2 / 2! + x^4 / 4! - ... 
**********************************************************/ 
double taylor_cos(double x, int n, double pi){
	double res = 0;
	double exp, fact, sig;
	while (1){
		if (x >= -pi && x < pi){
			break;
		} else if (x >= pi){
			x -= 2 * pi;
		} else{
			x += 2 * pi;
		}
	}
	for (int i = 0; i < n; i++){
		exp = cal_exp(x, 2 * i);
		fact = cal_fact(2 * i);
		sig = cal_exp(-1, i);
		if (exp == DBL_MAX || fact == DBL_MAX || sig == DBL_MAX){
			return DBL_MAX;
		}
		res += sig * exp / fact;
	}
	if (res > 1){
		res = 1;
	} else if (res < -1){
		res = -1;
	}
	return res;	
}


/********************************************************
* Function name: taylor_tan
* Description        : Taylor formula approximation of tangent function.
* Parameter         ��
* @x            : The input number to get the cosine value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* @pi            : Pi given in the programme. 
* Return          ��The approximated tangent value, namely, tan(x) ��taylor_sin(x) / taylor_cos(x).
					Specially, we note that when directly using taylor formula to approximate tangent function is far away from the
					actual value, because the taylor formula of tangent has only "+", not including a "-", it causes the high deviation
					when computing, only is <n> very very high could approximation be very close, so we pass the idea. 
**********************************************************/ 
double taylor_tan(double x, int n, double pi){
	while (1){
		if (x >= -pi / 2 && x < pi / 2){
			break;
		} else if (x >= pi / 2){
			x -= pi;
		} else{
			x += pi;
		}
	}
	if (x == -pi / 2){
		return DBL_MAX;
	}
	double sin, cos;
	sin = taylor_sin(x, n, pi);
	cos = taylor_cos(x, n, pi);
	if (sin == DBL_MAX || cos == DBL_MAX || cos == 0){
		return DBL_MAX;
	} else{
		return sin / cos;
	}
}


/********************************************************
* Function name: cmp_arcs
* Description        : Using taylor_sin to find a value that is close to input <x>.
* Parameter         ��
* @x            : The input number to get the arcsin value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* @accu            : The precision of the computing process, the larger, the more precise.
* @pi            : Pi given in the programme. 
* Return          : Originally, we set <res> to 0, and repeatedly use taylor_sin to get the sin value of <res>, and compare the value with
					<x>, when they are very close(within <prec>), it will return <res>, it is the approximation of arcsin(x).
**********************************************************/ 
double cmp_arcs(double x, int n, double accu, double pi){
	if (accu <= 0 || x < -1 || x > 1){
		return DBL_MAX;
	}
	double res = 0, sin, abs, criti = accu * cal_exp(x, 2);
	double decay = 0.1, ratio = 0.1;
	int last = 0; // 0 means left, 1 means right
	while (1){
		sin = taylor_sin(res, n, pi);
		abs = cal_abs(sin - x);
		if (sin == DBL_MAX || abs == DBL_MAX){
			return DBL_MAX;
		}
		if (abs <= criti){
			break;
		}
		if (x - sin > 0){
			res += ratio * (pi / 2 - res);
			if (last == left){
				ratio *= decay;	
			}
		} else{
			res += ratio * (-pi / 2 - res);
			if (last == right){
				ratio *= decay;
			}
		}
		last = (x > sin);
	}
	return res;
}


/********************************************************
* Function name: cmp_arcc
* Description        : Using taylor_cos to find a value that is close to input <x>.
* Parameter         ��
* @x            : The input number to get the arccos value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* @accu            : The precision of the computing process, the larger, the more precise.
* @pi            : Pi given in the programme. 
* Return          : Originally, we set <res> to 0, and repeatedly use taylor_cos to get the sin value of <res>, and compare the value with
					<x>, when they are very close(within <prec>), it will return <res>, it is the approximation of arccos(x).
**********************************************************/ 
double cmp_arcc(double x, int n, double accu, double pi){
	if (accu <= 0 || x < -1 || x > 1){
		return DBL_MAX;
	}
	double res = pi / 2, cos, abs, criti = accu * cal_exp(x, 2);
	double decay = 0.1, ratio = 0.1;
	int last = 0; // 0 means left, 1 means right
	while (1){
		cos = taylor_cos(res, n, pi);
		abs = cal_abs(cos - x);
		if (cos == DBL_MAX || abs == DBL_MAX){
			return DBL_MAX;
		}
		if (abs <= criti){
			break;
		}
		if (x - cos > 0){
			res += ratio * (0 - res);
			if (last == left){
				ratio *= decay;	
			}
		} else{
			res += ratio * (pi - res);
			if (last == right){
				ratio *= decay;
			}
		}
		last = (x > cos);
	}
	return res;
}


/********************************************************
* Function name: taylor_arcs
* Description        : Taylor formula approximation of arcsin function.
* Parameter         ��
* @x            : The input number to get the arcsin value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* Return          ��The approximated arcsin value, namely, arcsin(x) ��x + 1!!/2!! * x^3/3 + 3!!/4!! * x^5/5 + ...
					Specially, there exists great deviation when using this idea due to the same reason as tangent. 
**********************************************************/ 
double taylor_arcs(double x, int n){
	if (x < -1 || x > 1){
		return DBL_MAX;
	} 
	double exp, res = 0, dfact;
	for (int i = 0; i < n; i++){
		exp = cal_exp(x, 2 * i + 1);
		dfact = cal_dfact(2 * i - 1) / cal_dfact(2 * i);
		res += exp * dfact / (2 * i + 1);
//		printf("res: %lf, exp: %lf, dfact: %lf  %lf\n", res, exp, dfact, exp * dfact / (double)(2 * i + 1));
	}
	return res;
}


/********************************************************
* Function name: cmp_arct
* Description        : Using taylor_tan to find a value that is close to input <x>.
* Parameter         ��
* @x            : The input number to get the arctan value of.
* @n            : The numebr of items of taylor formula, the larger, the more precise.
* @accu            : The precision of the computing process, the larger, the more precise.
* @pi            : Pi given in the programme. 
* Return          : Originally, we set <res> to 0, and repeatedly use taylor_tan to get the tan value of <res>, and compare the value with
					<x>, when they are very close(within <prec>), it will return <res>, it is the approximation of arctan(x).
**********************************************************/ 
double cmp_arct(double x, int n, double accu, double pi){
	if (accu <= 0){
		return DBL_MAX;
	}
	double res = 0, tan, abs, criti = cal_exp(x, 2) * accu;
	double decay = 0.1, ratio = 0.1;
	int last = 0; // 0 means left, 1 means right
	while (1){
		tan = taylor_tan(res, n, pi);
		abs = cal_abs(tan - x);
		if (tan == DBL_MAX || abs == DBL_MAX){
			return DBL_MAX;
		}
		if (abs <= criti){
			break;
		}
		if (x - tan > 0){
			res += ratio * (pi / 2 - res);
			if (last == left){
				ratio *= decay;	
			}
		} else{
			res += ratio * (-pi / 2 - res);	
			if (last == right){
				ratio *= decay;
			}
		}
		last = (x > tan);
	}
	return res;
}


 
 extern "C"
 {

    void C_taylor_tan(double x, int n, double pi)
 	{
 		taylor_tan(x, n, pi);
	}

    void C_taylor_cos(double x, int n, double pi)
 	{
 		taylor_cos(x, n, pi);
	}

    void C_taylor_sin(double x, int n, double pi)
 	{
 		taylor_sin(x, n, pi);
	}

      void C_taylor_arcs(double x, int n)
 	{
 		taylor_arcs(x, n);
	}

    void C_cmp_arcc(double x, int n, double accu, double pi)
 	{
        cmp_arcc( x,  n,  accu,  pi);
	}
 	void C_cmp_arct(double x, int n, double accu, double pi)
 	{
         cmp_arct( x,  n,  accu,  pi);
	}

} 