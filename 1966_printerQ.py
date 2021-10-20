for _ in range(int(input())):
    n,m = map(int,input().split())
    prior = list(input().split())
    queue = [(i,v) for i,v in enumerate(prior)]
    answer = 0

    while True:
        cur = queue.pop(0)
        if any(cur[1] < p[1] for p in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == m:
                break
    print(answer)
