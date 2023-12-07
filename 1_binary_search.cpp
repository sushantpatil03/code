#include<iostream>
using namespace std;
int main()
{
    // Code by Sushant Patil
    int i, num, first, last, middle;
    int x, y, size, temp;
    int sz;

    cout<<"Enter the size of array::";
    cin>>sz;
    int arr[sz];
    for(int i=0;i<sz;i++)
        arr[i]= 1 + rand()%10000; //Generate number between 0 to 10000
  
   
    cout<<"The generated array : ";
    for(int i=0;i<sz;i++)
        cout<<arr[i]<<" ";
    
    //Ascending order
    // Its actually Bubble Sort Logic
    for (x = 0; x < sz; x++){
        for (y = x; y < sz; y++){
            if (arr[x] > arr[y+1]){
                temp = arr[x];
                arr[x] = arr[y+1];
                arr[y+1] = temp;
            }
        }
    }
    
    //Output
    cout <<"\nElements sorted in the ascending order are : ";
    for (x = 1; x <= sz; x++){
        cout << arr[x]<<" ";   
    }
    
    cout<<"\nEnter Element to be Searched: ";
    cin>>num;
    first = 0;
    last = sz-1;
    middle = (first+last)/2;
    while(first <= last)
    {
        if(arr[middle]<num)
            first = middle+1;
        else if(arr[middle]==num)
        {
            cout<<"\nThe number, "<<num<<" found at Position "<<middle;
            break;
        }
        else
            last = middle-1;
        middle = (first+last)/2;
    }
    if(first>last)
        cout<<"\nThe number, "<<num<<" is not found in given Array";

    cout<<endl;
    return 0;
}
