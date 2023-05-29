#include <iostream>
using namespace std;

const int row = 8;
const int col = 8;
int dp[row][col];
int main() {
  // dp[i][j] = dp[i-1][j] + dp[i][j-1]
  // dp[i][j]表示从(0,0)到(i,j)的路径数
  for (int i = 0; i < row; i++)
    for (int j = 0; j < col; j++) {
      if (i == 0 || j == 0)
        dp[i][j] = 1;
      else
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  for (int i = 0; i < row; i++) {
    for (int j = 0; j < col; j++) {
      cout << dp[i][j] << "\t";
    }
    cout << endl;
  }
  cout << "number of route:(use dp)" << dp[row - 1][col - 1] << endl;

  // 从(0,0)到(i,j)走了(i+j)-(0+0)=i+j步，其中i步向下，j步向右
  // 从(0,0)到(i,j)的路径数为C(i+j,i)从i+j步中选i步向下的方案数*1
  // C(i+j,i) = (i+j)!/(i!*(i+j-i)!) = (i+j)!/(i!*j!)
  // C(14,7)=14*13*12*11*10*9*8/(7*6*5*4*3*2*1)=3432
  cout << "number of route:C(14,7)=3432";
  return 0;
}