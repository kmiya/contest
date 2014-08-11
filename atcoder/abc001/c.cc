#include <iostream>
using namespace std;

string dig[] = {"N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"};
int W[] = {25,155,335,545,795,1075,1385,1715,2075,2445,2845,3265,999999};
int main() {
  double deg;
  int dis;
  cin >> deg >> dis;
  string dir = dig[((int)(deg*10+1125)/2250)%16];
  int i = 0;
  while (dis*10 >= W[i]*6)
    i++;
  if (!i) dir = "C";
  cout << dir << " " << i << endl;
}
