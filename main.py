import random


score = 0
com_score = 0


def convert_num_to_str(choice):
    
    if choice == 1:
        choice = '가위'
    elif choice == 2:
        choice = '바위'
    elif choice == 3:
        choice = '보'
    return choice


def convert_num_to_str2(choice):
    print("@@@", choice)
    if choice == 1:
        print('!!')
        choice = a1
    elif choice == 2:
        choice = a2
    return choice

def whowin():
    global com_score
    global score
    if c=='바위' and comran=='가위':  
        print('이겼습니다')
        score = score + 1
    elif c=='보' and comran=='바위':
        print('이겼습니다')
        score = score + 1
    elif c=='가위' and comran=='보':
        print('이겼습니다')
        score = score + 1
        
    elif c == comran:  
        print('비겼습니다')
        
    else:
        print("졌습니다")
        com_score = com_score + 1
        

    

print('========================')
print('가위 바위 보 하나빼기')
print('========================')
print("1. 가위")
print("2. 바위")
print("3. 보")
while score <= 2 or com_score <= 2:
    #사용자 2개
    a1 = int(input())
    a2 = int(input())
    
    a1 = convert_num_to_str(a1)
    a2 = convert_num_to_str(a2)

    print('사용자:', a1, a2)
    
    #컴퓨터 2개
    com1 = random.randint(1, 3)   
    com2 = random.randint(1, 3)
    
    while com1 == com2 :
        com2 = random.randint(1, 3)
        
    com1 = convert_num_to_str(com1)
    com2 = convert_num_to_str(com2)
    
    print('컴퓨터:', com1, com2)
    
    
    #사용자 하나 빼기
    c = input()
    if c == 1:
        user1 = a1
    elif c == 2:
        user1 = a2
    
    user1 = convert_num_to_str2(c)
    
    
    #컴퓨터 하나 빼기
    comran = random.randint(1, 2)
    
    if comran == 1:
        comran = com1
    elif comran == 2:
        comran = com2
        
    print('사용자@@@:', user1)
    print('컴퓨터:',comran)
    
    #승부
    whowin()
    print(score, ':', com_score)
    
        
        
        
        
    # 끝
    if score == 3 or com_score == 3:
        print("경기 종료")
        print(score, ':', com_score)
        break