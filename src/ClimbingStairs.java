class ClimbingStairs {
    public int climbStairs(int n) {
        if(n==1){
            return 1;
        }
        int a = 1;
        int b = 1;
        int ways = 0;
        ways = a+b;
        int temp = 0;
        for(int i = 2; i<n; i++){
            temp = b;
            b = ways;
            ways = ways+temp;
        }
        return ways;
    }
}