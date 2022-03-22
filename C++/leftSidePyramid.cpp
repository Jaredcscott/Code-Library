#include <iostream>
#include <string>
using namespace std;

int main() 
{
  int limit = 11;
  int var = 1;
  int row = 1;
  int count = limit/2+1;
  string spaces = "       ";
  while (var < limit) {
   if (row != 4) {
      std::cout << spaces;
    }
    for ( int i = 0;i < row;i++) {
      std::cout << std::to_string(var) + " ";
      var = var + 1;
    }
    for (int j = 0; j < 2;j++){
      spaces.pop_back();
    }
    std::cout << "\n";
    row = row + 1;
  }
}
