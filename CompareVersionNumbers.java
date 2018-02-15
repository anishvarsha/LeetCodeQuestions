class CompareVersionNumbers {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        int lenV1 = v1.length;
        String[] v2 = version2.split("\\.");
        int lenV2 = v2.length;
        int i = 0;
        int max = lenV1>=lenV2? lenV1: lenV2;
        while(i<max){  
            Integer one = i<lenV1?Integer.parseInt(v1[i]):0;
            Integer two = i<lenV2?Integer.parseInt(v2[i]):0;
            int compare = one.compareTo(two);  
            if(compare != 0){
                return compare;
            }
            i+=1;
        }
        return 0;
    }
}