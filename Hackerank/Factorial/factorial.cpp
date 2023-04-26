#include <iostream>
#include<string>
#include<vector>
using namespace std;

string Multiply(string val1, string val_2){
    int len1 = val1.size();
    int len2 = val_2.size();
    int non_zero = 0;
    // int decr_count = 0;
    string val2;
    for(int x=0; x<len2; x++){
         if(val_2[x] != '0'){
            non_zero = 1;
        }
        if(non_zero){
            val2 = val2 + val_2[x];
        }
        
            
    }
    len2 = val2.size();
    
    vector<int> result(len1 + len2, 0);
    int ptr1=0;
    int ptr2=0;
    
    for(int i=(len1-1); i>=0; i--){
        int num1 = val1[i] - '0';
        int carry = 0;
        ptr2 = 0;
        for(int j=(len2-1); j>=0; j--){
            int num2 = val2[j] - '0';
            int sum = num1*num2 + result[ptr1 + ptr2]+carry;
            carry = sum/10;
            result[ptr1 + ptr2] = sum%10;
            ptr2++;
        }
        if(carry>0){
            result[ptr1+ptr2] += carry;
        }
        ptr1++;
    }
    
    int size_result = result.size() - 1;
    string final_result;

    while (size_result>=0 && result[size_result] == 0)
    size_result--;
    
    while(size_result>=0){
        final_result += to_string(result[size_result--]);
    }
    return final_result;
}

int main()
{
    
    string result;
    int n=25;
    for(int i=n; i>=1; i--){
        if(i==n){
        result = to_string(n);
        }
        else{
            string string_n = to_string(i);
            string string_res = result;
            string val = Multiply(string_n, string_res);
            result = val;
            
            
        } 
           
    }
    cout<<result;
    

    //cout<<Multiply("22","000013800");
}
    




