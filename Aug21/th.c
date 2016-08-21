#include <unistd.h>

#include <stdio.h>
#include <pthread.h>


/* main() for thread */
void *thFunc(void *arg) {
    char *str;
    
    int i = 0;
    str = (char*) arg;

    while (i < 10) {
        usleep(1);
        printf("thFunc: %s %d\n", str, i);
        i++;
    }
    
    return NULL;
}


int main(void) {
    pthread_t pth;

    int i = 0;

    pthread_create(&pth, NULL, thFunc, "thread msg");
    pthread_join(pth, NULL);

    while (i < 10) {
        usleep(1);
        printf("main() running\n");
        i++;
    }
    
    return 0;
}
