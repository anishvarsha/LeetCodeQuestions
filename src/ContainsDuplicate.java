class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> setter = new HashSet<>();
        for(int i: nums){
            if(setter.contains(i)){
                return true;
            }else{
                setter.add(i);
            }
        }
        return false;
    }
}