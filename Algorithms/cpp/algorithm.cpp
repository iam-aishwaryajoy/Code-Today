#include"algorithm.h"
#include<iostream>
#include<array>
using namespace std;

int SearchAlgorithm::linear_search(int data[], int arr_size, int query){
            int pos = 0;
            while(pos < arr_size){
                if(data[pos] == query){
                    return pos;}
                else{
                    pos = pos + 1;}
            }
            return 0;
}
