class Solution {
    public String solution(int[] food) {
        String answer = "0";
        for(int i=food.length-1; 0<i; i--){
            String iStr = Integer.toString(i);
            int count = food[i] / 2;
            if(count > 0){
               for(int j=1; j<count+1; j++){
                   answer = iStr + answer + iStr;
               }
            }
        }
        
        return answer;
    }
}