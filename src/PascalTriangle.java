class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal= new ArrayList<List<Integer>>();
        for(int line =1; line<=numRows; line++){
            int c = 1;
            List<Integer> temp = new ArrayList<Integer>();
            for(int i = 1; i<=line; i++){
                temp.add(c);
                c = c * (line - i)/i;
            }
            pascal.add(temp);
        }
        return pascal;
    }
}