# a = int(input('숫자를 입력해주세요! : '))

# if a > 10:
#     print(f'a는 {a}, 10보다 큽니다.')
#     print(f'{type(a)}')
# elif a == 5:
#     print(f'a는 {a}, 입니다.')
# else:
#     print(f'a는 {a}, 10보다 작습니다.')

# if a > 5:
#     print('a는 5보다 큽니다.')
#
# if a > 0:
#     print('a는 자연수입니다.')

# if a > 0:
#     print('a는 자연수입니다.')
#     if a % 2 == 0:
#         print('a는 짝수입니다.')
#     else:
#         print('a는 홀수입니다.')
# else:
#     print('a는 음수입니다.')

# temp_str = '오늘은 날씨가 좋은 토요일 오후입니다.'
#
# for i in range(len(temp_str)):
#     print(f'"{temp_str[i]}" 의 인덱스는 : {i}\n')
#
#
# def mysum(a, b):
#     c = a + b
#     return c
#
#
# print(mysum(5, 10))
#
# for i in [1, 2, 3, 4]:
#     if i == 2:
#         continue
#     print(i)
#
# print('\n')
#
# a = 1
# while True:
#     print(a)
#     a += 1
#     if a == 100:
#         break

class NSS:
    body = '강화합금'

    def run(self):
        print('나는 달립니다.')


NSS_1 = NSS()
NSS_2 = NSS()

NSS_1.run()
print(NSS_1.body)
NSS_1.sense = 'happy'  # 객체변수
print(NSS_1.sense)
print(NSS_2.sense)