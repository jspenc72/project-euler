#include <stdio.h>
#define N 1500000

char a[N+1];

int gcd(int x, int y) {
    while (y != 0) {
        int temp = x;
        x = y;
        y = temp%y;
    }
    return x;
}

int main(int ac, char** av)
{
   int u = 0;
   while (++u)
   {
      int v = u;
      while (++v)
      {
         if (gcd(u,v)==1 && (u+v)&1)
         {
            int peri = 2*v*(u+v);
            if (peri > N)
               break;
            int ix = peri;
            do
               a[ix]++;
            while ((ix+=peri) < N);
         }
      }
      if (u+1 == v)
         break;
   }
   int sum = 0;
   int ix = -1;
   while (++ix < N)
      sum += a[ix]==1;
   printf("%d\n", sum);
   return 0;
}
