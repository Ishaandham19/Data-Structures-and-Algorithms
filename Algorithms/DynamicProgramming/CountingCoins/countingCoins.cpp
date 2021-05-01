#include <iostream>
#include <cstdlib>
#include <vector> 
#include <algorithm>
using namespace std;


//using memoization 
vector<int> minValues(1000,-1);

int min(vector<int> values){
    int least = 0;
    if (!values.empty()){
        least = values[0];
        for (int value : values){
            if (value < least)  least = value;
        }
    }   
    else throw "no solution";  // the denominations cannot give exact change

    return least;
}

//recursive method - O(nm) where n = atm, and m = denoms.length()
int minCoins(const vector<int> &denoms, int amt){ 
    if (amt == 0) return 0;  
    else {
        if (minValues[amt] != -1){ //check if value already exists in the minValues array
            return minValues[amt];
        }
        else {
           vector<int> values;
           for (int deno : denoms){
               if (amt >= deno)
                    values.push_back(minCoins(denoms,amt-deno)); //store subproblem values in array  
           }
           minValues[amt] = min(values) + 1; //add subproblem solution (min value) to the minValues array
           return minValues[amt];
           
        }
    }
}

//iterative approach O(nm) where n = atm, and m = denoms.length()
int minCoinsItr(const vector<int> & denoms, int amt){
    vector<int> dp(1000,-1);
    dp[0] = 0;
   
    for (int i = 1; i <= amt; i++){
        vector<int> values;
        bool flag  = true;
        for (int deno : denoms){
            if (i == deno){
                dp[i] = 1;   //a single denomination is equal to amount
                flag = false;
            }
            else{
                if (i > deno) values.push_back(dp[i-deno]);   // place all subproblems values in array
            }
        }
        if (!values.empty() && flag){
            int min_val = *min_element(values.begin(),values.end());  //function fails for -1 values present in the array
            if (min_val != -1)
                dp[i] = min_val + 1; // dp[i] = the minimum of all subproblems + 1
        }
    }

    return dp[amt];
}

int main(){
    const vector<int> denominations = {2,5}; // denominations
    int amt = 55;
    int ans = -1;  //initialized to -1 for the recursive solution answer

    //try catch block for the recursive meth
    try{
         ans = minCoins(denominations,amt);
    } catch (const char* msg){
        cout << msg << endl;
    }

    cout << "Minimum number of coins: " << ans << endl;
    cout << "Minimum number of coins itr: " << minCoinsItr(denominations, amt) << endl;
    return 0;
}