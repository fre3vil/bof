#include <stdio.h>

int main(void)
{
    char * const argv[] = {"cat", "/etc/issue", NULL};
    execve("/bin/cat", argv, NULL);
    return 0;
}
