class ReverseString {
    public String reverseString(String s) {
        int len = s.length();
        char[] rev = new char[len];
        for(char c: s.toCharArray()){
            rev[--len] = c;
        }
        return new String(rev);
    }
}