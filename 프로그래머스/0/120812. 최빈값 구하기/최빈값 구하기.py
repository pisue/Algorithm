#문제분석
#1. array의 원소가 0보다크고 1000보다 작다
#2. 원소의 값을 카운트 할 count 배열을 선언한다
#3. array를 for문을 통해 나오는 값을 count의 인덱스로 선택하고 그값에 1을 더해준다
#4. count의 최빈값이 두개 이상이면 -1을 반환한다
#5. 최빈값의 인덱스를 구하고 그 값을 리턴한다


def solution(array):
    count = [0] * 1000
    
    for int in array:
        count[int] += 1
        
    max_value = max(count)
    
    if count.count(max_value) > 1:
        return -1
    
    return count.index(max_value)