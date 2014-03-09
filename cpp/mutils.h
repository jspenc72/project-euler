#ifndef MUTILS_H_
#define MUTILS_H_

#define ABS(X) ((X) < 0 ? -(X) : (X))
#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

const unsigned int b[] = {0x2, 0xC, 0xF0, 0xFF00, 0xFFFF0000};
const unsigned int S[] = {1, 2, 4, 8, 16};

unsigned int lg(unsigned int v);
int randnorm();

#endif
