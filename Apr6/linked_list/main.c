#include <stdlib.h>

/* 
 *  -----------           -----------
 *  Data | Next   ---->   Data | Next
 *  -----------           -----------
 */

struct node {
    int n;
    struct node *next;
};

int main() {
    struct node *root;
    root = (struct node *)malloc(sizeof(struct node));
    root->next = 0;
    root->n = 5;
}
