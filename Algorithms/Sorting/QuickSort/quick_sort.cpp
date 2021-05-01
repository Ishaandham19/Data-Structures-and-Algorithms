#include <iostream>

void swap(int array[],int i, int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}


int partition(int array[], int p, int r){
    int x = array[r];  //create a pivot

    //dividing the array into a 4 part invariant
    int i = p-1;       

    for (int j = p; j < r; j++){
        if (array[j] <= x){
            i++;
            swap(array,i,j);
        }
    }
    //insert pivot in the correct postion 
    swap(array,i+1,r);

    //return the postion of the pivot
    return i+1;
}

void quickSort(int array[], int p, int r){
    if (p < r){
        int q = partition(array,p,r);
        quickSort(array,p,q-1);
        quickSort(array,q+1,r);
    }
}

void displayArr(int array[], int size){
    for (int x = 0; x < size; x++){
        std::cout << array[x] << " ";
    }
    std::cout << std::endl;
}

int main(){
    //testing the quickSort function

    const int SIZE = 7;

    int foo[SIZE] = {6,2,7,8,1,4,5};

    //displaying unsorted array
    displayArr(foo,SIZE);

    //sorting the array using quickSort
    quickSort(foo,0,SIZE-1);

    //displaying sorted array
    displayArr(foo,SIZE);
    

    return 0;
}