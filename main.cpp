#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include<conio.h>

#include "TriMath.h"
#include "test.h"


typedef enum{
	main_interf = 0,
	
} new_interf;

new_interf interf = main_interf;

//定义函数 
double show_main_interf(void);
double show(void);
double arc_scan();
double angel_scan(double pi);

int main(int argc, char** argv) {
    double accu = 0.0000001;
    int n = 15; //泰勒展开精度 
    double pi = cal_pi(accu);
    double x, rad;
    int key;
	
	while(1)
	{
		system("cls");
		show();
		scanf("%d", &key);
		
		if (key == 9)
		{
			return 0;
		}
		//选择计算模式 
		switch (key)
    	{
	    	case 1:
				rad = angel_scan(pi);
	    		printf("sin(%lf) = %lf\n", rad, taylor_sin(rad, n, pi));
	    		break;
	    	case 2:
				rad = angel_scan(pi);
	    		printf("cos(%lf) = %lf\n", rad, taylor_cos(rad, n, pi));
	    		break;
	    	case 3:
	    		double tan; 
				rad = angel_scan(pi);
				tan = taylor_tan(rad, n, pi);
				if (tan == DBL_MAX)
				{
					printf("tan(%lf) 不存在\n", rad);
				}
				else
				{
					printf("tan(%lf) = %lf\n", rad, tan);
				} 
	    		break;   		    	
	        case 4:
	        	x = arc_scan();
	        	if(x ==2){
	        		break;
				}
				printf("arcsin(%lf) = %lf\n", x, cmp_arcs(x, n, accu, pi));
	            break;
	        case 5:
				x = arc_scan();
				if(x ==2){
	        		break;
				}
				printf("arccos(%lf) = %lf\n", x, cmp_arcc(x, n, accu, pi));
	            break;
	        case 6:
				x = arc_scan();
				printf("arctan(%lf) = %lf\n", x, cmp_arct(x, n, accu, pi));
	            break;       
	        default:
	            printf("无效的输入\n");
//	            return 0; 
	            break;
    	}
	    printf("请按任意键继续...\n");
        getch();
	}
	return 0;
}

double show_main_interf(void){
	interf = main_interf;
//	system("cls");
	printf("Welcome to TriCal programme, you can calculate the value of any trigonometric function!\n");
	printf("1. Calculate a sine function.\n");
	printf("2. Calculate a cosine function.\n");
	printf("3. Calculate a tangent function.\n");
	printf("4. Calculate a arcsin function.\n");
	printf("5. Calculate a arccos function.\n");
	printf("6. Calculate a arctan function.\n");
	printf("请输入对应函数的序号, 输入数字9退出程序.\n");
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

double angel_scan(double pi){
	double rad, angle;
    int mode;
	printf("请选择输入 1. 弧度 rad 或 2. 角度 angle：");
	scanf("%d", &mode);
	
	switch (mode)
	{
		case 1:
			printf("请输入弧度 rad 的值：");
			scanf("%lf", &rad);
			break;
		case 2:
			printf("请输入角度 angle 的值：");
			scanf("%lf", &angle);
			rad = angle_2_rad(angle, pi);
			break;
		default:
    		printf("错误输入\n");
    		printf("请输入弧度 rad 的值：");
			scanf("%lf", &rad);
    		break; 
	}
	return rad;
}
 
double arc_scan(){
	double x;
	double error = 2;
	printf("请输入 x 的值：");
	scanf("%lf", &x);
	
	if (x < -1 || x > 1) {
		printf("错误：x 的值必须在 -1 和 1 之间。\n");
		return error;
	}
	else{
		return x;
	} 
}
