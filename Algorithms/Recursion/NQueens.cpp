#include <iostream>
using namespace std;

/*
 Program solves the N Queens problem
*/

//size of the square grid (can be changed to any int value)
const int SIZE = 8;

//int** createGrid()
// preconditions: global variable SIZE must be defined
// postconditons: returns a initialized (to 0) 2D array of size - SIZE x SIZE
int** createGrid() {
    //dynamically allocating a 2D array
    int** grid = new int* [SIZE];
    for (int i = 0; i < SIZE; i++) {
        grid[i] = new int[SIZE];
    }

    //initializing the 2D array to zeroes
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            grid[i][j] = 0;
        }
    }

    return grid;
}

//bool condition(int**, int r, int c)
// postcondtions: returns a true if a queen can be placed in (r,c) position in the grid, else returns false
bool condition(int** grid, int r, int c) {
    //checking the row
    for (int i = 0; (i >= 0 && i < SIZE); i++) {
        if (grid[r][i] == 1)
            return false;
    }

    //checking the col
    for (int i = 0; (i >= 0 && i < SIZE); i++) {
        if (grid[i][c] == 1)
            return false;
    }
    //checking the primary diagonal (lower)
    for (int i = r, j = c;((i >= 0) && (i < SIZE)) && ((j >= 0) && (j < SIZE)); i++, j++) {
        if (grid[i][j] == 1)
            return false;
    }
    //checking the primary diagonal (upper)
    for (int i = r, j = c;((i >= 0) && (i < SIZE)) && ((j >= 0) && (j < SIZE)); i--, j--) {
        if (grid[i][j] == 1)
            return false;
    }
    //checking the secondary diagonal (lower)
    for (int i = r, j = c;((i >= 0) && (i < SIZE)) && ((j >= 0) && (j < SIZE)); i++, j--) {
        if (grid[i][j] == 1)
            return false;
    }
    //checking the secondary diagonal (upper)
    for (int i = r, j = c;((i >= 0) && (i < SIZE)) && ((j >= 0) && (j < SIZE)); i--, j++) {
        if (grid[i][j] == 1)
            return false;
    }

    return true;
}


//void display()
// postcondtions: displays the grid (used when a solution is found)
void display(int** grid, int count) {
    cout << "Solution -" << count << endl;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            cout << grid[i][j] << ' ';
        }
        cout << endl;
    }
    cout << endl;
}

//bool NQueens(int** grid, int row)
// postcondtions: displays all the possible solutions (i.e Queen placements)
bool NQueens(int** grid, int row) {
    static int count = 0;  //keeps track of the number of solutions 

    //end condition for a solution
    if (row == SIZE) {
        count++;
        return true;
    }

    for (int col = 0; col < SIZE; col++) {
        if (condition(grid, row, col)) {   //checks if position is valid for queen
            grid[row][col] = 1;
            if (NQueens(grid, row + 1)) {   //backtracking step
                display(grid, count);       //displays the solution
                grid[row][col] = 0;         //ensures the function keeps on going until all the solutions
            }
            else {
                grid[row][col] = 0;
            }
        }
    }

    return false;
}


//main to call the function
int main() {  
    //create the grid (2D array)
    int** grid = createGrid();
    //NQueens function call
    NQueens(grid,0);
   
    return 0;

}
