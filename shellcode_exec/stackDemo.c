#include <stdio.h>
// code by fre3vil
// Mac => gcc stackDemo.c -fno-pie -o stackDemo
// linux 32 => gcc stackDemo.c -m32 -no-pie -o stackDemoy32
// linux 64 => gcc stackDemo.c -no-pie -o stackDemoy64



void func1()
{
    int x = 1;
    printf("This is function1.\n");
}

void func2()
{
    int y = 2;
    printf("This is function2.\n");
}


int main(int argc, char** argv)
{
    int x = 10;
    printf("This is main function.\n");
    func1();
    printf("After calling function1.\n");
    func2();
    printf("After calling function2.\n");
    return 0;
}
