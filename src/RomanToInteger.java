class RomanToInteger {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romans = new HashMap<Character, Integer>();
        
        romans.put('I', 1);
        romans.put('V', 5);
        romans.put('X', 10);
        romans.put('L', 50);
        romans.put('C', 100);
        romans.put('D', 500);
        romans.put('M', 1000);
        int su = 0;
        int len = s.length();
        
        char[] arr = s.toCharArray();
        int i = 0;
        while(i<len-1){
            if(romans.get(arr[i])>=romans.get(arr[i+1])){
                su+=romans.get(arr[i]);
            }else{
                su-=romans.get(arr[i]);
            }
            i+=1;
        }
        su+=romans.get(arr[len-1]);
        return su;
    }
}