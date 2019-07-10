import random

class User:
    def __init__(self):
        self.name=input('캐릭터 이름을 입력하세요: ')
        self.power=random.randint(6,8)
        self.intel=random.randint(6,8)
        if self.power>self.intel:
            self.job='전사'
        elif self.power==self.intel:
            self.job='궁수'
        elif self.power<self.intel:
            self.job='법사'


me=User()

print('캐릭터 이름: %s\n캐릭터 정보: 힘(%d), 지력(%d)\n캐릭터 직업: %s'%(me.name,me.power,me.intel,me.job))
