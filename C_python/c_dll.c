#include<stdio.h>

void my_add(int num){

long int result = 0;

for (long int i=1; i<=num; i++){
    result += i;
}
printf("��1��%d�ۼӵļ�����Ϊ%ld\n",num,result);
}
