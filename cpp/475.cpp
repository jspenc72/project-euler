#include <map>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <tuple>
#include <utility>
#include <boost/functional/hash.hpp>
//#include <boost/coroutine2/all.hpp>

// TODO: clean this up
//
//typedef boost::coroutines2::coroutine<std::vector<int>&> coro_t;
//
//void splits(int i, std::vector<int>& state,
//        std::vector<int>& split, coro_t::push_type& yield) {
//    if (i==split.size()-1) {
//        if (state.back() >= split.back()) yield(split);
//    } else {
//        for (int j=std::max(0,split[i]-state[i+1]); j<=split[i]; j++) {
//            split[i] -= j;
//            split[i+1] += j;
//            splits(i+1, state, split, yield);
//            split[i] += j;
//            split[i+1] -= j;
//        }
//    }
//}
//
//coro_t::pull_type splits(std::vector<int>& state) {
//    return coro_t::pull_type(boost::coroutines2::fixedsize_stack(),
//            [&](coro_t::push_type& yield) {
//                std::vector<int> split(4);
//                split[0] = 3;
//                splits(0, state, split, yield);
//            });
//}

void add(std::vector<int>& vec1, std::vector<int>& vec2, int off, int mul=1) {
    for (int i=0; i<vec2.size(); i++) {
        vec1[i+off] += mul*vec2[i];
    }
}

int mod = 1000000007;

long long modpow(int n, long long m) {
    if (n==1) return 1;
    long long ret = 1;
    long long npow = n;
    while (m>0) {
        if (m&1) ret = ret*npow%mod;
        m >>= 1;
        npow = npow * npow % mod;
    }
    return ret;
}

std::map<int, long long> invmem;
long long inverse(int n) {
    long long& maybe = invmem[n];
    if (maybe!=0) return maybe;
    return (maybe = modpow(n, mod-2));
}

std::vector<long long> _fact;
long long fact(int n) {
    return _fact[n];
}
long long c(int n, int k) {
    return fact(n) * inverse(fact(k)) % mod * inverse(fact(n-k)) % mod;
}

template<typename T>
void printvec(T&& vec) {
    std::cout << "[ ";
    for (auto i : vec) std::cout << i << " ";
    std::cout << "]" << std::endl;
}


typedef std::tuple<int, int, int, int, int, int> map_key_t;

struct key_hash : public std::unary_function<map_key_t, std::size_t> {
 std::size_t operator()(const map_key_t& k) const {
    size_t seed = 0;
    boost::hash_combine(seed, std::get<0>(k));
    boost::hash_combine(seed, std::get<1>(k));
    boost::hash_combine(seed, std::get<2>(k));
    boost::hash_combine(seed, std::get<3>(k));
    boost::hash_combine(seed, std::get<4>(k));
    boost::hash_combine(seed, std::get<5>(k));
    return seed;
 }
};

struct key_equal : public std::binary_function<map_key_t, map_key_t, bool>
{
   bool operator()(const map_key_t& v0, const map_key_t& v1) const
   {
      return (
               std::get<0>(v0) == std::get<0>(v1) &&
               std::get<1>(v0) == std::get<1>(v1) &&
               std::get<2>(v0) == std::get<2>(v1) &&
               std::get<3>(v0) == std::get<3>(v1) &&
               std::get<4>(v0) == std::get<4>(v1) &&
               std::get<5>(v0) == std::get<5>(v1)
             );
   }
};

//std::map<size_t,int> mem;
//std::map<int,std::map<int,std::map<int,std::map<int,std::map<int,std::map<int,int>>>>>> mem;
std::unordered_map<const map_key_t, int, key_hash, key_equal> mem;

int& getval(std::vector<int>& state, int i, int j) {
//    size_t seed = boost::hash_range(state.begin()+off, state.end());
//    boost::hash_combine(seed, i);
//    boost::hash_combine(seed, j);
//    return mem[seed];
//    return mem[state[1]][state[2]][state[3]][state[4]][i][j];
    return mem[std::make_tuple(state[1], state[2], state[3], state[4], i, j)];
}

long long f(std::vector<int>&);

long long g(std::vector<int>& state, int i, int moved) {
    if (i==state.size()) {
        if (moved != 3) return 0;
        int& maybe = getval(state,i,moved);
        if (maybe==0) maybe = f(state) % mod;
        return maybe;
    }
    int& maybe = getval(state,i,moved);
    if (maybe != 0) return maybe;
    long long ans = 0;
    for (int j=0; j<=std::min(state[i], 3-moved); j++) {
        long long accum = c(state[i], j) % mod * modpow(i, j) % mod;
        state[i] -= j;
        state[i-1] += j;
        ans = (ans + accum * g(state, i+1, moved+j) % mod) % mod;
        state[i] += j;
        state[i-1] -= j;
    }
    maybe = ans;
    return ans;
}

long long f(std::vector<int>& state) {
    if (*std::max_element(state.begin()+1, state.end()) == 0) {
        return 1;
    } else {
//        int& maybe = mem[state[0]][state[1]][state[2]][state[3]][state[4]];
//        if (maybe != 0) return maybe;
//        long long ans = g(state, 1, 0, 1);
        int start = 1;
        while (state[start]==0) start++;
        long long ans = g(state, start, 0);
//        long long ans = 0;
//        for (auto& split : splits(state)) {
//            long long splitways = 1;
//            for (int i=1; i<state.size(); i++) {
//                splitways = splitways * c(state[i], split[i-1]) % mod * modpow(i, split[i-1]) % mod;
//            }
//            add(state,split,1,-1);
//            add(state,split,0);
//            ans = (ans + splitways * f(state) % mod) % mod;
//            add(state,split,0,-1);
//            add(state,split,1);
//        }
//        maybe = ans;
        return ans;
    }
}


int main(int argc, char *argv[]) {
    int N = 50;
//    int N = atoi(argv[1]);
    _fact.push_back(1);
    for (int i=0; i<1000; i++) {
        _fact.push_back(_fact.back() * _fact.size() % mod);
    }
    std::vector<int> state(5);
    state[4] = 3*N;
    std::cout << f(state) * modpow(fact(4*N), mod-2) % mod << std::endl;
}
