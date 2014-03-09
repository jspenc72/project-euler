#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MAX3(a,b,c) MAX(MAX(a,b),c)
#define MAX4(a,b,c,d) MAX(MAX3(a,b,c),d)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MIN3(a,b,c) MIN(MIN(a,b),c)
#define MIN4(a,b,c,d) MIN(MIN3(a,b,c),d)
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;
typedef long long ll;

const ll mod = pow(10,9)+7;

template< class T >
class Matrix
{
    public:
		int m,n;
		T *data;

        Matrix( int m, int n );
		Matrix( const Matrix< T > &matrix );

		const Matrix< T > &operator=( const Matrix< T > &A );
        const Matrix< T > operator*( const Matrix< T > &A );
        const Matrix< T > operator^( int P );
        T& operator[]( const int i );

		~Matrix();
};

template< class T >
Matrix< T >::Matrix( int m, int n )
{
    this->m = m;
    this->n = n;
    data = new T[m*n];
}

template< class T >
Matrix< T >::Matrix( const Matrix< T > &A )
{
    this->m = A.m;
    this->n = A.n;
    data = new T[m*n];
    for( int i = 0; i < m * n; i++ )
		data[i] = A.data[i];
}

template< class T >
Matrix< T >::~Matrix()
{
    delete [] data;
}

template< class T >
const Matrix< T > &Matrix< T >::operator=( const Matrix< T > &A )
{
    if( &A != this )
    {
        delete [] data;
        m = A.m;
        n = A.n;
        data = new T[m*n];
        for( int i = 0; i < m * n; i++ )
			data[i] = A.data[i];
    }
    return *this;
}

template< class T >
const Matrix< T > Matrix< T >::operator*( const Matrix< T > &A )
{
	Matrix C( m, A.n );
	for( int i = 0; i < m; ++i )
		for( int j = 0; j < A.n; ++j )
        {
			C.data[i*C.n+j]=0;
			for( int k = 0; k < n; ++k )
				C.data[i*C.n+j] = (C.data[i*C.n+j] + data[i*n+k]*A.data[k*A.n+j]%mod)%mod;
		}
	return C;
}

template< class T >
const Matrix< T > Matrix< T >::operator^( int P )
{
	if( P == 1 ) return (*this);
	if( P & 1 ) return (*this) * ((*this) ^ (P-1));
	Matrix B = (*this) ^ (P/2);
	return B*B;
}

template< class T >
T& Matrix< T >::operator[]( const int i ) {
    return this->data[i];
}

const int N=2000;

int main() {
    Matrix<int> mat(N,N);
    REP(i,N) {
        REP(j,N) {
            mat[N*i+j]=0;
            if (i==j+1) mat[N*i+j]=1;
        }
    }
    mat[N-2]=mat[N-1]=1;
    Matrix<int> sq = mat^2;
    REP(i,N) {
        REP(j,N) cout << sq[N*i+j] << " ";
        cout << endl;
    }
    return 0;
}
