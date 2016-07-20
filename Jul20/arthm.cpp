#include <iostream>

using namespace std;
const int MAX = 3;

void sample_one() {
    int arr[MAX] = {1, 2, 3};
    int *ptr;

    ptr = arr;

    for (int i = 0; i < MAX; i++) {
        cout << "Address of arr[" << i << "] = ";
        cout << ptr << endl;
        ptr++;
    }
}

int main() {
    sample_one();
    return 0;
}