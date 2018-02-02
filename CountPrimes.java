class CountPrimes {
    public int countPrimes(int n) {
        if(n<=2){
            return 0;
        }
        boolean[] primes = new boolean[n];
        Arrays.fill(primes, Boolean.TRUE);
        int p = 2;
        
        while(p*p<n){
            if(primes[p] == true){
                for(int i = p*2; i<n; i+=p){
                    primes[i] = false;
                }
            }
            p+=1;
        }
        
        int count = 0;
        for(boolean b: primes){
            if(b){
                count+=1;
            }
        }
        return count-2;
    }
}