cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups =    [0, 2, 0, 1, 0, 2, 0]
cnt_deliver = 0
cnt_pickup = 0
cnt_deliver_route = []
cnt_pickup_route = []
street = 0
while(sum(deliveries)!=0 or sum(pickups)!=0):
    for i in range(n):
        if cnt_deliver+deliveries[i] > cap:
            continue
        elif cnt_deliver+deliveries[i] == cap:
            print(i)
            cnt_deliver_route.append(i)
            for j in range(len(cnt_deliver_route)):
                deliveries[cnt_deliver_route[j]] = 0
            street += (i+1)*2
            cnt_deliver = 0
            cnt_deliver_route = []
            for k in reversed(range(i+1)):
                if cnt_pickup+pickups[k]>cap:
                    continue
                elif cnt_pickup+pickups[k] == cap:
                    cnt_pickup_route.append(k)
                    for p in range(len(cnt_pickup_route)):
                        pickups[cnt_pickup_route[p]] = 0
                else:
                    cnt_pickup += pickups[k]
                    cnt_pickup_route.append(k)
            for p in range(len(cnt_pickup_route)):
                pickups[cnt_pickup_route[p]] = 0
            cnt_pickup = 0
            cnt_pickup_route = []
        else:
            cnt_deliver += deliveries[i]
            cnt_deliver_route.append(i)
    print(cnt_deliver_route)
    if sum(cnt_deliver_route)!=0:
        street += (max(cnt_deliver_route)+1) *2
        for j in range(len(cnt_deliver_route)):
            deliveries[cnt_deliver_route[j]] = 0
        cnt_deliver = 0
        cnt_deliver_route = []
        for k in reversed(range(i)):
            if cnt_pickup+pickups[k]>cap:
                continue
            elif cnt_pickup+pickups[k] == cap:
                cnt_pickup_route.append(k)
                for p in range(len(cnt_pickup_route)):
                    pickups[cnt_pickup_route[p]] = 0
            else:
                cnt_pickup += pickups[k]
                cnt_pickup_route.append(k)
        for p in range(len(cnt_pickup_route)):
                pickups[cnt_pickup_route[p]] = 0
print(street)













# cnt_deliver = 0
# cnt_pickup = 0
# answer = 0
# guri = []
# for i in reversed(range(n)):
#     if deliveries[i]==0 and pickups[i]==0:
#         continue
#     else:
#         guri.append(i+1)
#         cnt_deliver += deliveries[i]
#         cnt_pickup += pickups[i]
#         if cnt_deliver >= cap or cnt_pickup>=cap:
#             print(i,cnt_deliver,cnt_pickup,guri)
#             cnt_deliver = 0
#             cnt_pickup = 0
#             answer += guri[0] *2
#             guri = []
# print(answer)