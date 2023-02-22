# 코드 실행 시 테케는 맞는데, 제출하면 하나도 안 맞음.

def solution(enroll, referral, seller, amount):
    answer = []
    for i in range(len(enroll)):
        master_slave[enroll[i]] = referral[i]
        seller_benefit[enroll[i]] = 0
    for i in range(len(seller)):
        dadangye(seller[i], amount[i]*100)
    for i in range(len(enroll)):
        answer.append(seller_benefit[enroll[i]])
    return answer
def dadangye(slave, money):
    if money >= 10:
        seller_benefit[slave] += money - int(money*0.1)
        if master_slave[slave] != '-':
            dadangye(master_slave[slave], int(money*0.1))
        else:

            return
    else:
        seller_benefit[slave] += money
        return
master_slave = {}
seller_benefit = {}

# 두 번째,

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll,referral,seller,amount))
