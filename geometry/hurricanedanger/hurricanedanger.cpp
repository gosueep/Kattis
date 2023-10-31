#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

template <class T> int sgn(T x) { return (x > 0) - (x < 0); }
template<class T>
struct Point {
	typedef Point P;
	T x, y;
	explicit Point(T x=0, T y=0) : x(x), y(y) {}
	bool operator<(P p) const { return tie(x,y) < tie(p.x,p.y); }
	bool operator==(P p) const { return tie(x,y)==tie(p.x,p.y); }
	P operator+(P p) const { return P(x+p.x, y+p.y); }
	P operator-(P p) const { return P(x-p.x, y-p.y); }
	P operator*(T d) const { return P(x*d, y*d); }
	P operator/(T d) const { return P(x/d, y/d); }
	T dot(P p) const { return x*p.x + y*p.y; }
	T cross(P p) const { return x*p.y - y*p.x; }
	T cross(P a, P b) const { return (a-*this).cross(b-*this); }
	T dist2() const { return x*x + y*y; }
	double dist() const { return sqrt((double)dist2()); }
	// angle to x-axis in interval [-pi, pi]
	double angle() const { return atan2(y, x); }
	P unit() const { return *this/dist(); } // makes dist()=1
	P perp() const { return P(-y, x); } // rotates +90 degrees
	P normal() const { return perp().unit(); }
	// returns point rotated 'a' radians ccw around the origin
	P rotate(double a) const {
		return P(x*cos(a)-y*sin(a),x*sin(a)+y*cos(a)); }
	// friend ostream& operator<<(ostream& os, P p) {
	// 	return os << "(" << p.x << "," << p.y << ")"; }
};

typedef Point<double> P;
template<class P>
double lineDist(const P& a, const P& b, const P& p) {
	return (double)(b-a).cross(p-a)/(b-a).dist();
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);


    int testcases;
    cin >> testcases;
    for (size_t tcase = 0; tcase < testcases; tcase++)
    {
        int x1,y1,x2,y2,n;
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> n;

        double dist = 1000*1000*10;
        // vector<string> closest;
        string closest = "";
        for (size_t i = 0; i < n; i++)
        {
            string city;
            cin >> city;
            int x, y;
            cin >> x >> y;

            double d = abs(lineDist(P(x1,y1), P(x2,y2), P(x,y)));
            if (abs(d-dist) < 0.0001 ) {
                closest = closest + " " + city;
            }
            else if(dist - d > 0.0) {
                dist = d;
                closest = city;
            }
        }
        cout << closest << endl;
    }
}