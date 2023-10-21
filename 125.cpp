//Valid Palindrome 
//can make it without creating the new_string string , by mutating only the original string s
#include <iostream>
#include <string>
using namespace std;


bool isPalindrome(string s) {
    string new_string="";
    for (int i=0;i<s.length();i++){
        if (isupper(s[i])){
            new_string+=tolower(s[i]);
        }
        else if ((s[i]>=97 && s[i]<=122) || (s[i]>=48 && s[i]<=57)){
            new_string+=s[i];
        }
    }
    cout<<new_string<<endl;
    for (int i=0;i<new_string.length()/2;i++){
        if (new_string[i]!=new_string[new_string.length()-i-1]){
            return false;
        }
    }
    return true;
}



int main(){

//string s = "A man, a plan, a canal: Panama";
string s="0P";
bool result=isPalindrome(s);
cout<<result;


}