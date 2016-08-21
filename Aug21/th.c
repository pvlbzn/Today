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
        printf("thFunc: %s\n", str);
        i++;
    }
    
    return NULL;
}


int main(void) {
    pthread_t pth;

    int i = 0;

    pthread_create(&pth, NULL, thFunc, "creating a thread");
    pthread_join(pth, NULL);

    while (i < 10) {
        usleep(1);
        printf("main() running");
        i++;
    }
    
    return 0;
}
