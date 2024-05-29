class Solution {
    public int countSeniors(String[] details) {
        int count=0;
        int length=details.length;
        for(int i=0;i<length;i++){
            String arr=details[i];
            char char1=arr.charAt(11);
            int num1=Integer.parseInt(String.valueOf(char1));
            char j=arr.charAt(12);
            int num2=Integer.parseInt(String.valueOf(j));

            int num=num1*10+num2;
            if(num>60){
                count=count+1;
            }
            }
            return count;

        }
        
        
        
}
