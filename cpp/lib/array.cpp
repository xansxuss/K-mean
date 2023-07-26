#include <iostream>

using namespace std;

int arr(int s[], int length)
{
    int *p = s;

    int lengths = sizeof(s) / sizeof(s[0]);
    cout << lengths << endl;
    cout << sizeof(s) << endl;
    cout << p << endl;
    // cout << sizeof(s[0]) << endl;

    for (int i = 0; i < length; i++)
    {
        cout << "s[" << i << "]=" << s[i] << '\n';
    }
    return 0;
}