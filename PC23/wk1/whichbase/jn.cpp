#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int set;
    int number;
   
    cin >> set;

    int array[set];
   
    for(int i = 0; i < set; i++) {
       
        // cout << i << " ";            // take this out
        int pos;
        cin >> pos;      // you are parsing this wrong, you were grabbing 1, 1234, then 2

        cin >> number;
       
        array[i] = number;
    }
   
    for( int i = 0; i < set; i++) {
        int number = array[i];
        int hexiTemp = array[i];
        int octalTemp = array[i];
        int decimalNumber = 0;
        int hexiDecimalNumber = 0;
        int j = 0;
        int k = 0;
       
        cout << i+1 << " ";
        while(octalTemp != 0) {
            int digit = octalTemp % 10;
            if((digit == 9) || (digit == 8)) {
                decimalNumber = 0;
                break;
            }
            else {
                decimalNumber = decimalNumber + digit * pow(8, j);
                j++;
                octalTemp /= 10;
            }
        }
        cout << decimalNumber << " " << number << " ";
        while(hexiTemp != 0) {
            int digit = hexiTemp % 10;
            hexiDecimalNumber = hexiDecimalNumber + digit * pow(16, k);
            k++;
            hexiTemp /= 10;
        }
        cout << hexiDecimalNumber << " " << endl;
    }
}