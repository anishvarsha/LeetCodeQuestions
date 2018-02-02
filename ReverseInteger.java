class ReverseInteger {
    public int reverse(int x) {
        boolean sign = false;
        if(x<0){
            sign = true;
        }
        
        int num = Math.abs(x);
        int rev = 0;
        while(num != 0){
            int temp = rev*10 + num%10;
            if((temp - num%10)/10 != rev){
                return 0;
            }else{
                rev = temp;
            }
            num = num/10;
        }
        if(sign){
            return rev*-1;
        }
        return rev;
    }
}