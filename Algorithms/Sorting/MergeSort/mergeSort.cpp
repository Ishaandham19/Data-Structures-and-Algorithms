/*
 * Merge Sort - Sorts a list using a divide and conquer approach.
 * Time complexity - O(N * lgN)
 * Space complexity - O(N)
 */  


void merge(int arr[], int l, int m, int r){   
    int *L = new int[m-l+1];       // for left arr
    int *R = new int[r-m];         // for right arr
    for (int i = 0; i < (m-l+1); i++){  //copy elements from arr to left arr
        L[i] = arr[l+i];
    }
    for (int i = 0; i < (r-m); i++){  //copy elements from arr to right arr
        R[i] = arr[m+1+i];
    }

    int a = 0, b = 0;   // counters
    
    for (int i = l; i <= r; i++){
        if (a > (m-l)) {            // condition for L be empty (a > size of L-1)
            arr[i] = R[b];
            b++;
        }
        else if (b > (r-m-1)){       // condition for R to get empty ( b > size of R-1)
            arr[i] = L[a];
            a++;
        }
        else {
            if (L[a] <= R[b]){     // traverse through the arrays simultaneously
                arr[i] = L[a];     // and put the smaller element into arr
                a++;
                //std::cout << "a: " << a << std::endl;
            }
            else{
                arr[i] = R[b];
                b++;
                //std::cout << "b: " << b << std::endl;
            }
        }
    }

}

/* void mergeSort(int arr[], int l, int r)
 *  Inputs: Array to be sorted (arr[]), int left, int right
 *  Output : Mutates the given array and sorts the elements in ascending order
 */

void mergeSort(int arr[], int l, int r){
    int m = l + (r - l)/2;    // calculate mid
    if (l >= r)     // base case (when only two elements remain)
        return;
    else {      
        mergeSort(arr, l, m);     // divide arr into left part
        mergeSort(arr, m + 1, r); // divide arr into right part
        merge(arr,l,m,r);             // merge the two parts together
    }
    
}
 