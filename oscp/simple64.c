#include <stdio.h>
#include <string.h>


// 32 bit
// gcc -no-pie -m32 simple64.c -o simple

int main(int argc, char** argv)
{
    char buffer[64];
    if (argc < 2) {
        printf("Error - You must supply at least one arguement\n");
        return 1;
    }
    strcpy(buffer, argv[1]);
    puts(buffer);
    return 0;
}



