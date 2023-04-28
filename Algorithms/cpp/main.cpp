#include <iostream>
#include "algorithm.h"
#include <map>
#include <vector>
#include <string>

using namespace std;
class Testcases
{
    public:
        
        Testcases(int data[],int arr_size=3, int query=3, int output=2){
        inputs = data;
        query = query;
        size =arr_size;
        out =  output;}

        int inputs[];
        int query;
        int size;
        int out;


};
int main(){
    SearchAlgorithm algorithm;
    int output = -1;
    int data_1[] = {10, 20, 30, 40}; 
    int arr_size = sizeof(data_1)/sizeof(int);
    Testcases test(data_1, arr_size, 40, 3);
    Testcases *ptr_box;
    ptr_box = &test;
    //int query=test['query'][0];
    //int data[] = test['data']

    output = algorithm.linear_search(ptr_box->inputs(), ptr_box->size(), ptr_box->query());
    cout<<output<<endl;


}
