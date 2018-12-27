#include <stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char **argv)
{
 char buff[7];
 if(argc != 2) {
 puts("Need an argument!");
 exit(1);
 }
 printf("Exploiting via returnig into libc function\n");
 strcpy(buff, argv[1]); 
 printf("\nYou typed [%s]\n\n", buff);
 return(0);
}

