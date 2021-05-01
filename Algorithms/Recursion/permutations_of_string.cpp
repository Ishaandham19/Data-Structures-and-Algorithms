//Displays all the permutations of a string


//erase element from a string  -  string& erase (pos,1); (modifies the string)

#include <iostream>
#include <string>
#include <vector>


std::string remove(std::string s, int pos){
    std::string ans  = "";
    if (s == "") return "";

    for (int i = 0; i < s.length(); i++){
        if (i != pos) ans += s[i];
    }

    return ans;
}

std::vector<std::string> permutations(std::string s){
    std::vector<std::string> perms;
    if (s.length() == 0) return ""; // base case
    else{
        for (int i = 0 ; i < s.length(); i++){
            for (std::string x : permutations(remove(s,i)){

            }
        }
    }

}
  

//driver function
int main(){
    std::string s = "abc";
    permutations(s);
    std::cout << "Number of permutations: " << count() << std::endl;

}