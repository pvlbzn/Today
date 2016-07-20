#include <iostream>

using namespace std;

const int LEN = 3;

void sample_one(int *ptr) {
    for (int i = 0; i < LEN; i++) {
        cout << "Address of arr[" << i << "] = " << ptr << endl;
        cout << "Value of arr[" << i << "] = " << *ptr << "\n" << endl;
        ptr++;
    }
}

void sample_next(int *ptr) {
    cout << "Last member has " << ptr + 2 << " address" << endl;
    cout << "Value: " << *(ptr+2) << "\n" << endl;
}

int main() {
    int arr[LEN] = {1, 2, 3};
    int *ptr;

    ptr = arr;
    sample_one(ptr);
    sample_next(ptr);

    return 0;
}