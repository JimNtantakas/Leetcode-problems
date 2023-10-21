#include <iostream>
#include <string>
using namespace std;

bool isSubsequence(string s, string t) {
    int k=0;
    for (int i=0;i<t.length() && k<s.length();i++){
        if (s[k]==t[i]){
            k++;
        }
    }
    if (k==s.length()){
        return true;
    }
    return false;
}

int main(){
string s,t;
cout<<"Give 2 strings: ";
cin>>s>>t;

bool result=isSubsequence(s,t);
cout<<result;

}
