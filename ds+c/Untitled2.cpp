// CPP Program to interpolate using 
// newton forward interpolation
#include <bits/stdc++.h>
using namespace std;
 
// calculating u mentioned in the formula
float u_cal(float u, int n)
{
    float temp = u;
    for (int i = 1; i < n; i++)
        temp = temp * (u - i);
    return temp;
}
 
// calculating factorial of given number n
int fact(int n)
{
    int f = 1;
    for (int i = 2; i <= n; i++)
        f *= i;
    return f;
}
 
int main()
{
    // Number of values given
    int n = 5;
    float x[] = {0.5,1.0,1.5,2.0,2.5};
     
    // y[][] is used for difference table
    // with y[][0] used for input
    float y[n][n];
    y[0][0] = 0.22245;
    y[1][0] = 0.25031;
    y[2][0] = 0.27799;
    y[3][0] = 0.30546;
    y[4][0] =0.33269;
    
    // Calculating the forward difference
    // table
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++)
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
    }
 
    // Displaying the forward difference table
//    for (int i = 0; i < n; i++) {
//        cout << setw(4) << x[i] 
//             << "\t";
//        for (int j = 0; j < n - i; j++)
//            cout << setw(4) << y[i][j] 
//                 << "\t";
//        cout << endl;
//    }
 
    // Value to interpolate at
    float value = 1.1;
 
    // initializing u and sum
    float sum = y[0][0];
    float u = (value - x[0]) / (x[1] - x[0]);
    for (int i = 1; i < n; i++) {
        sum = sum + (u_cal(u, i) * y[0][i]) /
                                 fact(i);
    }
 
    cout << "\n Value at " << value << " is "
         << sum << endl;
    return 0;
}
