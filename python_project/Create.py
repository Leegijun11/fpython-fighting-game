import time
import random

class Character_select:

    def __init__(self):
        # 기본 스탯 초기화
        self.name= "" 
        self.my_hp=0
        self.my_maxhp=0
        self.my_damage=0
        self.my_win=0
        self.my_lose=0
        self.user = None  # 캐릭터 중복 생성 방지용 플래그
        self.booty2 = []  # 획득한 전리품 목록

        # 적 목록 (이름, HP, 공격력)
        self.enemy = [
            {'enemy_name':'📝 오타몬','enemy_hp':10,'enemy_damage':3},
            {'enemy_name':'😴 기면증몬','enemy_hp':20,'enemy_damage':10},
            {'enemy_name':'📱 릴스몬','enemy_hp':40,'enemy_damage':15},
            {'enemy_name':'🍺 숙취몬','enemy_hp':60,'enemy_damage':25},
            {'enemy_name':'🐍 대마왕 파이썬','enemy_hp':100,'enemy_damage':30}
        ]

        # 전리품 목록 (이름, 공격력 증가, HP 증가, 등급)
        self.booty = [
            {'item_name':'🎤 선생님의 황금 마이크','item_damage':20,'item_hp':20,'item_grade':'S'},
            {'item_name':'⌨️ 샷건 가능 티타늄 키보드','item_damage':15,'item_hp':5,'item_grade':'A'},
            {'item_name':'☕ 아이스 고추가루 아메리카노','item_damage':5,'item_hp':15,'item_grade':'A'},
            {'item_name':'🔧 강의실 구석에 있던 빠루','item_damage':15,'item_hp':0,'item_grade':'B'},
            {'item_name':'🥤 누군가 먹다 남긴 레드불','item_damage':5,'item_hp':10,'item_grade':'B'},
            {'item_name':'💾 화장실에서 주운 USB','item_damage':3,'item_hp':2,'item_grade':'C'},
            {'item_name':'🤖 챗GPT 3시간 구독권','item_damage':4,'item_hp':1,'item_grade':'C'},
        ]

        while True:
            # 이미 캐릭터가 있을 때: 초기화 여부 확인
            if self.user is not None:
                print(f'이미 {self.name} 캐릭터가 있습니다.')
                retry=input('\n기존 캐릭터를 삭제하고 다시 시작할까요?(y/n)')
                if retry == 'y':
                    # 랜덤 퇴장 메시지 출력 후 스탯 초기화
                    retry_msgs=[
                        f'\n🚚 {self.name}은/는 트럭에 치여 이세계로 떠났습니다..\n',
                        f'\n😱 {self.name}, 기준님의 피드백을 견디지 못하고 탈주합니다..\n', 
                        f'\n🍗 {self.name}은/는 코딩을 접고 치킨집을 차리러 갔습니다..\n'
                    ]
                    retry_msg = random.choice(retry_msgs)
                    print(retry_msg)                    
                    self.name=''
                    self.my_hp=0
                    self.my_maxhp=0
                    self.my_damage=0
                    self.my_win=0
                    self.my_lose=0
                    self.user = None
                    print("-----------시스템 초기화-----------")
                    continue  # 처음부터 다시 캐릭터 선택
                if retry == 'n':
                    return  # 기존 캐릭터 유지하고 종료
                
            # 시작 메뉴 출력
            print("\n" + "="*35)
            print("      🥊 Fpython 격투 세계 🥊")
            print("="*35)
            print("1.캐릭터 선택 2.종료 3.설명")
            start_menu=input('메뉴를 선택하세요 : ')

            if start_menu == '1':
                # 유효한 캐릭터가 선택될 때까지 반복
                while self.user is None:
                    print("\n-----------------🎮 캐릭터 선택 🎮------------------")
                    print("1. 😃 맑은눈의 초보 개발자 (💥 공격력 20, ❤️  체력 90)")
                    print("2. 😵 퀭한눈의 거북목 개발자 (💥 공격력 30, ❤️  체력 70)")
                    print("3. 😏 음흉한 미소의 음지 해커 (💥 공격력 50, ❤️  체력 50)")
                    print("4. 😎 마이크를 찬 신지원 선생님 (💥 공격력 70, ❤️  체력 70)")

                    choice = input("\n번호를 선택하세요 : ")

                    # 선택한 번호에 따라 캐릭터 스탯 지정 (이름, 공격력, HP)
                    if choice == '1':
                        self.user = ("맑은눈의 초보 개발자", 20, 90)
                    elif choice == '2':
                        self.user = ("퀭한눈의 거북목 개발자", 30, 70)
                    elif choice == '3':
                        self.user =("음흉한 미소의 음지 해커", 50, 50)
                    elif choice == '4':
                        self.user = ("마이크를 찬 신지원 선생님", 70, 70)
                    else:
                        print("\n잘못된 번호 입니다. 다시 선택하세요.")
                        continue

                    # 선택한 캐릭터 정보를 인스턴스 변수에 저장
                    self.name = self.user[0]
                    self.my_damage = self.user[1]
                    self.my_hp = self.user[2]
                    self.my_maxhp = self.user[2]

                    print(f'\n시스템 로그 기록 시작.. ✨ {self.name}님이 화려하게 등장했습니다! ✨\n')
                    return

            elif start_menu == '2':
                print("게임을 종료합니다.")
                return None

            elif start_menu == '3':
                self.display_summary()  # 게임 설명 출력 후 메뉴로 복귀
                continue
            else:
                print("1,2,3번 중에 하나를 입력하세요!")

    def display_summary(self):
        # 게임 설명 및 업데이트 노트 출력
        print("\n" + "📜" + "="*50 + "📜")
        print(f"{' [ Fpython 격투 게임 개요 ] ':-^46}")
        print("-" * 52)
        print("1. 🎮 게임 방법")
        print("   - 원하는 캐릭터를 선택하여 개발 세계의 빌런들과 결투합니다.")
        print("   - 전투는 '가위바위보' 방식으로 진행됩니다.")
        print("   - 승리 시 전리품을 획득하며 체력과 공격력이 영구 상승합니다.")
        print("-" * 52)
        print("2. ✨ 업데이트 노트 (불편함 개선)")
        print("   - [입력 편의성]: 이제 '가위, 바위, 보' 전체를 입력할 필요가 없습니다.")
        print("   - 초성 입력 지원: 'ㄱㅇ'(가위), 'ㅂㅇ'(바위), 'ㅂ'(보)만 쳐도 OK!")
        print("   - 유효성 검사 추가: 잘못된 입력 시 기회를 날리지 않고 재입력 가능.")
        print("-" * 52)
        print("="*52 + "\n")
        input("메뉴로 돌아가려면 [Enter]를 누르세요...")