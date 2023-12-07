#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){

    int left,right,mid;
    int sz;
    

    cout << "Enter a number :: ";
    cin >> sz;

    vector<int> arr(sz);

    for(int i=0; i<sz; i++){
        arr[i] = rand()%10000;
    }

    sort(arr.begin(), arr.end());

    for(int i=0; i<sz; i++){
        cout << arr[i] << " ";
    }

    int num;
    cout << "\nEnter element to search :: ";
    cin >> num;

    left = 0;
    right = sz-1;
    mid = (left+right) / 2;

    while(left<=right){
        mid = (left+right) /2;

        if(num == arr[mid]){
            cout << "\nElement found at index "<<mid;
            break;
        }else if(num < arr[mid]){
            right = mid-1;
        }else{
            left = mid+1;
        }
    }

    if(left>right){
        cout << "Element not found";
    }

    return 0;
}