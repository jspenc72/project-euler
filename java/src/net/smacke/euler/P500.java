package net.smacke.euler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Problem 500 -- least number with 2^500500 divisors
 * Idea: greedily multiply current by a prime to a power of 2
 * 'Greedy' because we pick least such value
 * Do this 500500 times
 */

public class P500 {
    private static final int P = 8000000;
    private static final int M = 500500507;
    private static final boolean[] prime = new boolean[P];

    private static List<Integer> ccalcprimes() {
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;
        for (int i=0; i*i<P; i++) {
            if (!prime[i]) continue;
            for (int j=i*i; j<P; j+=i) {
                prime[j] = false;
            }
        }

        List<Integer> primes = new ArrayList<Integer>();
        for (int i=0; i<P; i++) {
            if (prime[i]) {
                primes.add(i);
            }
        }
        return primes;
    }

    public static void main(String[] args) {
        PriorityQueue<Long> q = new PriorityQueue<Long>();
        List<Integer> primes = ccalcprimes();

        q.add((long)primes.get(0));
        int nextprime = 1;
        long ans = 1;

        for (int i=0; i<500500; i++) {
            if (q.peek() > primes.get(nextprime)) {
                q.add((long)primes.get(nextprime++));
            }
            long val = q.poll();
            ans = (ans * val) % M;
            q.add(val*val); // pray for no overflow
        }

        System.out.println(ans);
    }

}
