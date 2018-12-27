#include<stdlib.h>
#include<string.h>
#include<stdio.h>

/*0xbffffdf0*/

int main() {
char *shell = getenv("MYSHELL");
if (shell)
printf("%x\n", (unsigned int)shell);
return 0;
}
