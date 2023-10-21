#include <iostream>
#include <vector>
using namespace std;


int removeDuplicates(vector<int>& nums) {
    int counter=0,i=1,removed=0,size=nums.size();
    while (i<nums.size()){
        if (nums[i]==nums[i-1]){
            counter++;
        }
        else{
            counter=0;
        }
        if (counter>1){
            nums.erase(nums.begin()+i);
            removed++;
            continue;
        }
        i++;
    }
    for (int num : nums) {
        cout << num << " ";
    }
    cout<<endl;
    return size-removed;
}



int main(){
vector<int> vect={1,1,1,2,2,3};


int result=removeDuplicates(vect);
cout<<result<<endl;

}