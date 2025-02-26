for _ in range(3):
    t_list = list(map(int, input().split()))
    in_time = t_list[0]*3600 + t_list[1]*60 + t_list[2]
    out_time = t_list[3]*3600 + t_list[4]*60 + t_list[5]
    
    work_time = out_time - in_time
    h = work_time // 3600
    m = work_time % 3600 // 60
    s = work_time % 3600 % 60
    
    print(f"{h} {m} {s}")