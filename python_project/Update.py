import time
import random
from Create import Character_select

class fight(Character_select):
         
    def __init__(self, instance):
        self.attack = ["가위", "바위", "보"]  # 가위바위보 선택지
        self.instance = instance  # Character_select 인스턴스 참조
        # 초성/전체 입력을 정규 표현으로 변환하는 매핑 테이블
        self.input_map = {
            "ㄱㅇ": "가위", "가위": "가위",
            "ㅂㅇ": "바위", "바위": "바위",
            "ㅂ": "보", "보": "보"
        }
        self.a = None

    def start_battle(self):
        myhp = self.instance.my_hp  # 전투 시작 전 HP 저장 (전투 후 복구용)
        n2 = 1  # 전투 페이즈 카운터

        # 가위바위보 승리 조건: key가 enemy를 이긴다
        win_rule = {
            "가위": "보",
            "바위": "가위",
            "보": "바위"    
        }

        # 적 목록에서 랜덤으로 한 명 등장
        now_enemy = random.choice(self.instance.enemy)

        print("\n" + "="*50)
        print(f"⚔️  {now_enemy['enemy_name']} 이(가) 등장했습니다!")
        print("="*50)
        print("🔥 전투를 준비하세요...\n")
        time.sleep(0.5)

        while True:
            # 현재 스탯 출력
            print("-"*50)
            print(f"🩸 현재 HP : {self.instance.my_hp}")
            print(f"💥 현재 공격력 : {self.instance.my_damage}")
            print("-"*50)

            print(f"\n🎯 {n2}번째 전투 페이즈! (enter) ")
            # 가위바위보 구호를 시간차로 출력
            print("\n▶ 안 내면 진 거, 가위✌️", end=" ", flush=True)
            time.sleep(0.3)
            print("바위✊", end=" ", flush=True)
            time.sleep(0.3)
            print("보!🖐️", flush=True)
            n2+=1

            # 초성 또는 전체 입력을 받아 정규 표현으로 변환
            n1 = input("")
            n = self.input_map.get(n1, n1)  # 매핑에 없으면 입력값 그대로 사용
            if n not in win_rule:
                print("❌ 잘못된 입력입니다! 다시 입력해주세요.\n")
                continue  # HP 소모 없이 재입력

            print("\n🤖 적이 공격을 선택하고 있습니다...")
            time.sleep(0.5)

            # 적의 가위바위보 랜덤 선택
            enemy = random.choice(self.attack)

            print("\n⚡ 전투 시작!")
            time.sleep(0.5)

            print(f"👿 적의 공격 : {enemy}")
            print(f"🧑 당신의 선택 : {n}\n")
            time.sleep(0.5)

            # 승패 판정
            if n == enemy:
                print("⚖️  무승부입니다! 다시 승부하세요!\n")

            elif win_rule[n] == enemy:
                # 플레이어 승리: 적 HP 감소
                print(f"✅ 공격 성공! 💥 {self.instance.my_damage} 의 피해를 입혔습니다!\n")
                now_enemy['enemy_hp'] -= self.instance.my_damage

            else:
                # 플레이어 패배: 내 HP 감소
                print(f"❌ 공격 실패... 💔 {now_enemy['enemy_damage']} 의 피해를 입었습니다!\n")
                self.instance.my_hp -= now_enemy['enemy_damage']

            # 패배 처리: HP 0 이하
            if self.instance.my_hp <= 0:
                print("\n" + "="*50)
                print("💀 전투에서 패배하였습니다...")
                print("="*50 + "\n")
                self.instance.my_lose += 1
                self.instance.my_hp = myhp  # HP 원래대로 복구
                break

            # 승리 처리: 적 HP 0 이하
            elif now_enemy['enemy_hp'] <= 0:
                print("\n" + "="*50)
                print("🏆 전투에서 승리하였습니다!!")
                print("="*50)

                # 랜덤 전리품 획득
                n4 = random.randint(0, 6)
                self.mybooty = self.instance.booty[n4]

                print(f"\n🎁 전리품 획득!")
                print(f"등급 : ✨ {self.mybooty['item_grade']}")
                print(f"아이템 : 🗡️ {self.mybooty['item_name']}")

                # 획득한 전리품을 "이름.등급" 형식으로 목록에 추가
                self.instance.booty2.append(
                    f"{self.mybooty['item_name']}.{self.mybooty['item_grade']}"
                )
                print("\n📈 능력치 상승!")
                print(f"❤️ HP +{self.mybooty['item_hp']}")
                print(f"💥 공격력 +{self.mybooty['item_damage']}\n")

                self.instance.my_win += 1
                self.instance.my_hp = myhp + self.mybooty['item_hp']  # 기존 HP + 아이템 HP
                self.instance.my_damage += self.mybooty['item_damage']

                print("🎊 전투가 종료되었습니다!")
                print("="*50 + "\n")
                break


class delete(fight):

    def __init__(self, player_obj):
        self.player = player_obj  # fight 인스턴스 참조

        print("\n" + "="*40)
        print(" 명예 퇴직 ")
        print("="*40)
        time.sleep(0.5)
        # 강한 스탯일 경우 아쉬움 멘트 출력
        if self.player.instance.my_damage >= 100:
            print(f" 현재 공격력이 {self.player.instance.my_damage}입니다! 이 정도로 강한데 유감입니다...")
        time.sleep(0.5)
        if self.player.instance.my_hp >= 100:
            print(f" 현재 체력이 {self.player.instance.my_hp}입니다! 이 정도로 튼튼한데 유감입니다...")
        time.sleep(0.5)
        print(f"현재 {self.player.instance.name} 선수의 은퇴를 진행중입니다...")

        self.execute_delete()
            

    def execute_delete(self):
        # 캐릭터 모든 스탯 및 데이터 초기화 (완전 삭제)
        print(f"\n[시스템] {self.player.instance.name} 선수는 링을 떠납니다...")

        self.player.instance.name = ""
        self.player.instance.my_hp = 0
        self.player.instance.my_maxhp = 0
        self.player.instance.my_damage = 0
        self.player.instance.my_win = 0
        self.player.instance.my_lose = 0        
        self.player.user = None 
        self.player.instance.booty2 = []

        print("----------- 은퇴 및 시스템 초기화 완료 -----------")
        print("\n[시스템] 캐릭터가 완전히 삭제되었습니다.")
        print("="*40)
        return


class Info(fight):
    def __init__(self, instance):
        self.instance = instance

        # 기본 캐릭터 정보 출력
        print(f"{'사용자 정보':=^40}")
        print(f"캐릭터: {self.instance.name}")
        print(f"체력: {self.instance.my_hp}")
        print(f"공격력: {self.instance.my_damage}")
        print(f"전적: {self.instance.my_win}승 {self.instance.my_lose}패")
        print(f"전리품: {self.instance.booty2}")
        print("="*40+'\n')
    
        # 승률 계산 후 전적 출력 (전투 없으면 0%)
        print(f"{'전적':=^40}")
        win = self.instance.my_win
        lose = self.instance.my_lose
        total = win + lose
        win_rate = (win / total * 100) if total > 0 else 0

        print(f"전적: {win}승 {lose}패. 승률 {win_rate:.1f}%!")
        print('='*40+'\n')


class Save:
    def __init__(self, instance):
        self.instance = instance
        
        saveFile = input(
            "게임을 저장하시겠습니까?\n"
            "저장은 '1' 입력, 저장하지 않으신다면 '2' 입력 : "
        )

        if saveFile != "1":
            print("저장하지 않고 종료합니다.")
            return

        # 전리품 등급 문자열 및 최고 등급 계산
        end = ""
        grade_priority = {"S":4, "A":3, "B":2, "C":1}
        highest_grade = ""
        highest_score = 0

        for item in self.instance.booty2:
            if "." not in item:
                continue

            name, grade = item.split(".", 1)
            grade = grade.strip()
            end += grade + " "

            # 등급 우선순위 비교로 최고 등급 갱신
            if grade_priority[grade] > highest_score:
                highest_score = grade_priority[grade]
                highest_grade = grade

        # 캐릭터 정보를 save.txt 파일에 저장
        with open('save.txt', 'w', encoding='utf-8') as f:
            f.write(
                f"캐릭터 정보\n"
                f"이름 : {self.instance.name}\n"
                f"체력 : {self.instance.my_hp}\n"
                f"공격력 : {self.instance.my_damage}\n"
                f"승패기록 : {self.instance.my_win}승 {self.instance.my_lose}패\n"
                f"전리품 등급 : {end}\n"
                f"최고 등급 아이템 : {highest_grade}\n"
            )

        print("저장이 완료되었습니다!")


def a():
    q = Character_select()   # 캐릭터 생성
    w = fight(q)             # 전투 객체 생성

    while True:
        n = input("1. 전투 시작 2. 게임 종료 3. 내 정보 보기 : ")
        if n == "1":
            print("전투 준비 ..\n")
            w.start_battle()
        elif n == "2":
            n1 = input("전투를 안하신다니... 은퇴 하실건가요?(Y/N)")
            if n1 == 'Y':
                e = delete(w)   # 캐릭터 삭제 후 종료
                break
            elif n1 == 'N':
                print("게임 종료 및 내 전적을 업로드합니다..\n")
                r = Save(w.instance)  # 파일 저장 후 종료
                break
            else:
                print("Y 또는 N 만 입력해주세요..\n")
                continue
        elif n == "3":
            e = Info(w.instance)  # 정보 출력

a()