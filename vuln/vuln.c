#include <stdio.h>

size_t slen(const char* str)
{
    size_t i;
    for (i = 0; str[i]; i++);
    return i;
}

int main(int argc, char** argv)
{
    char list[128];
    char* ptr = list;
    strcpy(list, ptr);
    printf("This is simple buffer overflow program!\n");
    printf("Enter your secret string:");
    gets(ptr);
    printf("**************\n");
    size_t len = slen(ptr);
    printf("Your Input length is: %d\n", len);
    puts(list);
    printf("oops!");
    return 0;
}
