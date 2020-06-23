# Word Chain Game
def WordChainGame():
    """
    This is Word Chain Game Ver 0.1
    Enjoy!
    """
    previousword: str = input("단어를 입력하세요 : ")
    while True:

        if len(previousword) == 3:
            nextword: str = input("다음 단어를 입력하세요 : ")
            if (len(nextword) == 3) and (previousword[2] == nextword[0]):
                previousword = nextword
                print("계속")
                continue
            elif len(nextword) != 3:
                print("3글자를 입력하세요.")
                continue
            else:
                print("틀렸습니다.\n게임 종료.")
                break
        else:
            print("3글자를 입력하세요.")


if __name__ == '__main__':
    WordChainGame()
