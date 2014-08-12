#include <iomanip>
#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int a,b,c,d,e,f;
  cin >> a >> b >> c >> d >> e >> f;
  double res = abs((c-a)*(f-b)-(d-b)*(e-a))/2. + 1.e-10;
  cout.setf(ios::fixed);
  cout.precision(1);
  cout << res << endl;
}
