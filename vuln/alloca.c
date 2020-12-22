#ifdef __GNUC__
#include <alloca.h>
#else
#include <malloc.h>
#endif
#include <stdio.h>


void func()
{
	char *buf = (char*)alloca(600);
#ifdef __GNUC__
	snprintf(buf, 600, "Hi! %d, %d, %d\n", 1, 2, 3);	// GCC
#else
	_snprintf(buf, 600, "Hi! %d, %d, %d\n", 1, 2, 3);// MSVC
#endif
	puts(buf);

}
int main(int argc, char** argv)
{
	func();
	return 0;
}
