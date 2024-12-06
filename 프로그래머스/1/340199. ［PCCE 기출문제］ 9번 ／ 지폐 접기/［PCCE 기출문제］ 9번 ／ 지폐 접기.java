class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int bill_0 = bill[0];
        int bill_1 = bill[1];
        int wallet_0 = wallet[0];
        int wallet_1 = wallet[1];
        
        // 지폐가 지갑에 들어갈 수 없는 동안 반복
        while (!((bill_0 <= wallet_0 && bill_1 <= wallet_1)
                 || (bill_1 <= wallet_0 && bill_0 <= wallet_1))) {
            
            // 더 긴 쪽을 반으로 접는다
            if (bill_0 > bill_1) {
                bill_0 /= 2; // 소수점 이하 버리기
            } else {
                bill_1 /= 2;
            }
            
            answer++; // 접기 횟수 증가
        }
        
        return answer;
    }
}