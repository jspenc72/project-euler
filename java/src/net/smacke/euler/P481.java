package net.smacke.euler;

import java.util.Arrays;
import java.util.Iterator;

/**
 * Strategy: Basically just do a memoized simulation according to
 * the rules given in the problem statement. Occasionally, we have
 * equations that look like x = [stuff] + [things]*x, so to avoid
 * infinitely recursing, we make sure that we only make function calls
 * that knock some chef out, and we explicitly solve for 'x' above
 * programmatically in order to handle the recursive part.
 * 
 * @author smacke
 *
 */
public class P481 {
    private static final int N = 14;
    private static final int[][] killmem = new int[N][1<<N];
    private static final double[][][] wmem = new double[N][N][1<<N];
    private static final double[][] emem = new double[N][1<<N];
    private static final int[] fibmem = new int[N+1];
    private static double[] S = new double[N];
    
    public static double W(int i) {
        return W(i,0,(1<<N)-1);
    }
    
    /**
     * Loops through chef indices, assuming that left is the bitset of
     * remaining chefs. Starts at the first remaining chef whose turn
     * comes after chef i's.
     */
    private static Iterable<Integer> iterate(final int i, final int left) {
        return new Iterable<Integer>() {
            @Override
            public Iterator<Integer> iterator() {
                return new Iterator<Integer>() {

                    int cur = i;
                    {
                        do {
                            cur = (cur + 1)%N;
                        } while (!contains(left,cur));
                    }

                    @Override
                    public boolean hasNext() {
                        return cur != i;
                    }

                    @Override
                    public Integer next() {
                        int ret = cur;
                        do {
                            cur = (cur + 1)%N;
                        } while (!contains(left,cur));
                        return ret;
                    }

                    @Override
                    public void remove() {
                        throw new UnsupportedOperationException();
                    }
                    
                };
            }
            
        };
    }
    
    /**
     * Whose turn is it after chef i's, given that left
     * is the bitset of remaining chefs?
     */
    private static int getNextTurn(int i, int left) {
        return iterate(i,left).iterator().next();
    }
    
    /**
     * Given that it is chef i's turn and that left is
     * the bitset of remaining chefs, if chef i has the
     * opportunity to knock somebody out, it will always
     * be the same chef. This function returns the chef
     * that i wishes to kill in this case.
     */
    private static int kill(int i, int left) {
        if (killmem[i][left] != -1) {
            return killmem[i][left];
        }
        double maxp_i_winning = 0.0;
        int argmax = -1;
        for (int j : iterate(i,left)) {
            double test = W(i,getNextTurn(i, left&~(1<<j)),left&~(1<<j));
            if (test > maxp_i_winning) {
                argmax = j;
                maxp_i_winning = test;
            }
        }
        killmem[i][left] = argmax;
        return argmax;
    }
    
    /**
     * Probability that chef i wins, given that it is
     * chef j's turn, and that left is the bitset of
     * remaining chefs.
     */
    private static double W(int i, int j, int left) {
        if (!contains(left,i)) {
            return 0.0;
        }
        if (bitcount(left) == 1) {
            return 1.0;
        }
        if (wmem[i][j][left] != -1.0) {
            return wmem[i][j][left];
        }
        int killj = kill(j,left);
        int nextturn = getNextTurn(j,left&~(1<<killj));
        double ret = S[j]*W(i,nextturn,left&~(1<<killj));
        double mult = 1.0 - S[j];
        for (int k : iterate(j, left)) {
            int killk = kill(k,left);
            ret += mult*S[k]*W(i,getNextTurn(k, left&~(1<<killk)),left&~(1<<killk));
            mult *= (1-S[k]);
        }
        ret = ret / (1.0-mult);
        wmem[i][j][left] = ret;
        return ret;
    }
    
    public static double E() {
        return E(0, (1<<N)-1);
    }
    
    /**
     * Expected number of turns, given that it's chef i's turn,
     * and that left is a bitset of the remaining chefs.
     */
    private static double E(int i, int left) {
        if (bitcount(left)==1) {
            return 0.0;
        }
        if (emem[i][left] != -1.0) {
            return emem[i][left];
        }
        int killi = kill(i, left);
        double ret = 1.0 + S[i] * E(getNextTurn(i, left&~(1<<killi)), left&~(1<<killi));
        double mult = (1.0 - S[i]);
        for (int j : iterate(i, left)) {
            int killj = kill(j,left);
            ret += mult*(1.0 + S[j]*E(getNextTurn(j, left&~(1<<killj)), left&~(1<<killj)));
            mult *= (1.0 - S[j]);
        }
        ret = ret / (1.0-mult);
        emem[i][left] = ret;
        return ret;
    }
    
    private static int bitcount(int v) {
        int ret=0;
        while (v!=0) {
            ret++;
            v &= (v-1);
        }
        return ret;
    }
    
    private static boolean contains(int set, int i) {
        return (set & (1<<i)) != 0;
    }
    
    private static int fib(int k) {
        if (k <= 1) {
            return 1;
        }
        if (fibmem[k] != -1) {
            return fibmem[k];
        }
        int ret = fib(k-1) + fib(k-2);
        fibmem[k] = ret;
        return ret;
    }
    
    public static void main(String[] args) {
        for (int i=0; i<wmem.length; i++) {
            for (int j=0; j<wmem[i].length; j++) {
                Arrays.fill(wmem[i][j], -1.0);
            }
        }
        for (int i=0; i<killmem.length; i++) {
            Arrays.fill(killmem[i], -1);
            Arrays.fill(emem[i], -1.0);
        }
        Arrays.fill(fibmem, -1);
        for (int i=0; i<N; i++) {
            S[i] = ((double)fib(i))/fib(N);
        }
        System.out.println(E());
    }
}
