import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> pq = new PriorityQueue<>(); // 최소 힙 사용

        for (int i = 0; i < score.length; i++) {
            pq.offer(score[i]); // 점수를 추가
            if (pq.size() > k) {
                pq.poll(); // k개 이상이면 최소값 제거
            }
            answer[i] = pq.peek(); // 현재 k번째로 낮은 점수 저장
        }

        return answer;
    }
}