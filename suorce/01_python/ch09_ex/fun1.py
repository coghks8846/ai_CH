# funcyions.py => fn1~()부터 fn9()
from customer import Customer
def fn1_insert_customer_info():
    '''
    사용자로부터 name, phone, email, age, grade, etc를 입력받아 Customer형 객체 반환
    '''
#     import re
    name = input('이름 : ')
#     name_pattern = r'[가-힣]{2,}'
#     while not re.search(name_pattern, name):
#         print('이름을 제대로 입력하세요(한글 2글자 이상)')
    phone = input("전화번호 : ")
    email = input("이메일 : ")
    while True:
        try:
            age = int(input("나이 : "))
            if (age<0) | (age>130):
                raise Exception('나이를 정확히 입력하세요')
            break
        except:
            print('올바른 나이를 입력하세요')
    try:
        grade = int(input("고객등급(1~5) : "))
        if grade < 1 :
            grade = 1
        if grade > 5 :
            grade = 5
    except ValueError as e:
        print('유효하지 않은 등급을 입력시 등급은 1로 초기화')
        grade = 1
    etc = input("기타 정보 : ")
    customer = Customer(name, phone, email, age, grade, etc)
    return customer

def fn2_print_customers(customer_list):
    'customer_list를 출력(pdf 40page 스타일)'
    print('='*70)
    print('{:^70}'.format('고객 정보'))
    print('-'*70)
    print("{:>5}\t{:3}\t{:13}\t{:15}\t{:3}\t{}".format('GRADE', '이름', '전화',
                                                       '메일', '나이', '기타'))
    print('-'*70)
    for customer in customer_list:
        print(customer)

# 3. 삭제(동명이인이 있을 경우 해당 동명이인을 지울지 한사람 한사람 묻고 지우기 Y/N)
def fn3_delete_customer(customer_list):
    '''삭제하고자 하는 고객이름을 input으로 받아
    매개변수로 들어온 customer_list에서 삭제하고 "삭제했음/삭제못했음"을 메세지로 출력'''
    delete_name = input('삭제할 고객 이름은?')
    delete_idx = [] # 삭제할 인덱스 저장하는 용도
    for idx,customer in enumerate(customer_list):
        if customer.name == delete_name:
            delete_idx.append(idx)
    if delete_idx:
        for idx in delete_idx[::-1]: # [1,0]
            print(customer_list[idx], '지우겠습니까?', end='')
            answer = input('(Y/N)')
            if answer.upper == 'Y':
                print('요청하신 {}({})님 삭제 완료'.format(delete_name,
                                                 customer_list[idx].phone))
                del customer_list[idx]
    else:
        print('{}님 데이터가 존재하지 않습니다'.format(delete_name))

# 4. 이름찾기
def fn4_search_customer(customer_list):
    search_name = input('이름')
    search_list = []
    for idx, customer in enumerate(customer_list):
        if customer.name == search_name:
            search_list.append(idx)
    if search_list:
        fn2_print_customers(search_list)
    else:
        print('{}는 없음'.format(search_name))

# 5. 내보내기(CSV)
def fn5_save_customer_csv(customer_list):
    '매개변수로 받은 customer_list를 딕셔너리리스트로 변환해서 csv 출력'
    import csv
    if customer_list:        
        customer_dic_list = []
        for customer in customer_list:
            customer_dic_list.append(customer.as_dic())
        fieldnames = list(customer_dic_list[0].keys())
        filename = input('저장할 csv 파일명은?')
        with open('data/{}.csv'.format(filename), 'w', encoding='UTF-8', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader() # 해더 
            dict_writer.writerows(customer_dic_list)
            print(f"data/{filename}.csv 내보내기 완료")
    else:
        print('입력된 회원 데이터가 없어 csv 내보내기 취소합니다')

# 9. 종료 (종료하기 전 customer_list를 txt파일에 저장하고 종료)
def fn9_save_customer_txt(customer_list):
    """customer_list를 
    to_list_style()를 이용해서 ['홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해\n',~]
    ch09_customers.txt로 백업
    """
    customer_txt_list = []
    for customer in customer_list:
        customer_txt_list.append(customer.to_list_style() + '\n')
    with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
        f.writelines(customer_txt_list)