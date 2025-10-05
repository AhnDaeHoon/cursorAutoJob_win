import pyautogui
import time
import os
import subprocess
import pyperclip

def press_ctrl_l():
    """Ctrl + L 키 조합을 입력"""
    try:
        pyautogui.hotkey('ctrl', 'l')
        print("Ctrl + L 키가 입력되었습니다.")
        return True
    except Exception as e:
        print(f"Ctrl + L 입력 중 오류 발생: {e}")
        return False

def repeat_ctrl_l_sequence():
    """Ctrl + L 반복 시퀀스 실행"""
    print("=== Ctrl + L 반복 시퀀스 시작 ===")
    
    # 최초 실행: Ctrl + L 한 번 입력
    print("최초 실행: Ctrl + L 입력")
    if not press_ctrl_l():
        return False
    
    # 0.3초 딜레이
    print("0.3초 대기...")
    time.sleep(0.3)
    
    # 반복 시퀀스 시작
    sequence_count = 1
    while True:
        print(f"\n--- 시퀀스 {sequence_count} ---")
        
        # 첫 번째 Ctrl + L
        print("첫 번째 Ctrl + L 입력")
        if not press_ctrl_l():
            break
        
        # 0.5초 딜레이
        print("0.5초 대기...")
        time.sleep(0.5)
        
        # 두 번째 Ctrl + L
        print("두 번째 Ctrl + L 입력")
        if not press_ctrl_l():
            break
        
        # 0.6초 딜레이
        print("0.6초 대기...")
        time.sleep(0.6)
        
        # content_typer.py 실행 (가상환경 활성화)
        print("content_typer.py 실행 중...")
        try:
            # Windows에서 가상환경 활성화 후 실행 (상위 폴더의 venv 사용)
            subprocess.run(['..\\venv\\Scripts\\python.exe', 'content_typer.py'], check=True)
            print("content_typer.py 실행 완료")
        except subprocess.CalledProcessError as e:
            print(f"content_typer.py 실행 중 오류 발생: {e}")
        except Exception as e:
            print(f"content_typer.py 실행 중 예상치 못한 오류: {e}")
        
        # 5초 딜레이
        print("5초 대기...")
        time.sleep(5)
        
        sequence_count += 1
        
        # 사용자 확인 (선택사항)
        print(f"시퀀스 {sequence_count-1} 완료. 계속하려면 Enter를 누르세요 (종료하려면 Ctrl+C)")
        try:
            input()
        except KeyboardInterrupt:
            print("\n사용자에 의해 중단되었습니다.")
            break

def repeat_ctrl_l_auto(count=5):
    """자동으로 지정된 횟수만큼 Ctrl + L 반복"""
    print(f"=== Ctrl + L 자동 반복 시작 (총 {count}번) ===")
    
    # 최초 실행: Ctrl + L 한 번 입력
    print("최초 실행: Ctrl + L 입력")
    if not press_ctrl_l():
        return False
    
    # 0.3초 딜레이
    print("0.3초 대기...")
    time.sleep(0.3)
    
    # 반복 시퀀스 실행
    for i in range(count):
        print(f"\n--- 시퀀스 {i+1}/{count} ---")
        
        # 첫 번째 Ctrl + L
        print("첫 번째 Ctrl + L 입력")
        if not press_ctrl_l():
            break
        
        # 0.5초 딜레이
        print("0.5초 대기...")
        time.sleep(0.5)
        
        # 두 번째 Ctrl + L
        print("두 번째 Ctrl + L 입력")
        if not press_ctrl_l():
            break
        
        # 0.6초 딜레이
        print("0.6초 대기...")
        time.sleep(0.6)
        
        # content.txt의 해당 시퀀스 라인만 타이핑
        print("content.txt 라인별 타이핑 시작...")
        content_lines = read_content_file_lines_list("../content.txt")
        
        # 현재 시퀀스에 해당하는 라인만 타이핑 (i는 0부터 시작하므로 i번째 라인)
        if i < len(content_lines):
            line_content = content_lines[i]
            print(f"\n--- 시퀀스 {i+1} 라인 {i+1}/{len(content_lines)} 타이핑 ---")
            print(f"타이핑할 내용: '{line_content}'")
            
            # 라인 타이핑 실행
            success = type_single_line_with_clipboard(line_content)
            if success:
                print(f"라인 {i+1} 타이핑 완료")
            else:
                print(f"라인 {i+1} 타이핑 실패")
        else:
            print(f"시퀀스 {i+1}에 해당하는 라인이 없습니다.")
        
        # 시퀀스 간 10초 대기 (마지막 시퀀스가 아닌 경우)
        if i < count - 1:
            print("10초 대기...")
            time.sleep(10)
    
    print(f"\n✅ 총 {count}번의 시퀀스가 완료되었습니다!")

def read_content_file_lines(file_path):
    """파일의 행 개수를 읽어서 반환"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len([line for line in lines if line.strip()])  # 빈 줄 제외
            print(f"파일 '{file_path}'에서 {line_count}개의 행을 발견했습니다.")
            return line_count
    except Exception as e:
        print(f"파일 읽기 오류: {e}")
        return 3  # 기본값으로 3 반환

def read_content_file_lines_list(file_path):
    """파일의 각 라인을 리스트로 반환"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # 빈 줄 제외하고 strip() 적용
            content_lines = [line.strip() for line in lines if line.strip()]
            print(f"파일 '{file_path}'에서 {len(content_lines)}개의 라인을 읽었습니다.")
            for i, line in enumerate(content_lines, 1):
                print(f"  라인 {i}: '{line}'")
            return content_lines
    except Exception as e:
        print(f"파일 읽기 오류: {e}")
        return ["direction_1.md", "direction_2.md"]  # 기본값

def type_single_line_with_clipboard(text):
    """단일 라인을 클립보드 방식으로 타이핑"""
    if not text:
        print("타이핑할 텍스트가 없습니다.")
        return False
    
    try:
        print(f"라인 타이핑 시작: '{text}'")
        
        # 1. "@" 특수문자 먼저 입력
        print("'@' 특수문자 입력 중...")
        pyautogui.write('@', interval=0.05)
        
        # 2. 0.5초 딜레이
        print("0.5초 대기 중...")
        time.sleep(0.5)
        
        # 3. 클립보드에 텍스트 복사
        print("클립보드에 텍스트 복사 중...")
        pyperclip.copy(text)
        time.sleep(0.1)
        
        # 4. Ctrl+V로 붙여넣기
        print("붙여넣기 실행 중...")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        
        # 5. 첫 번째 엔터 입력
        print("첫 번째 엔터 입력 중...")
        pyautogui.press('enter')
        time.sleep(0.5)
        
        # 6. 두 번째 엔터 입력
        print("두 번째 엔터 입력 중...")
        pyautogui.press('enter')
        time.sleep(0.1)
        
        print("라인 타이핑 완료")
        return True
    except Exception as e:
        print(f"라인 타이핑 중 오류 발생: {e}")
        return False

def main():
    """메인 실행 함수"""
    print("Ctrl + L 반복 입력 프로그램 (라인별 타이핑)")
    
    # content.txt 파일의 행 개수 읽기 (상위 폴더에서 찾기)
    content_file = "../content.txt"
    if os.path.exists(content_file):
        content_lines = read_content_file_lines_list(content_file)
        repeat_count = len(content_lines)
    else:
        print(f"'{content_file}' 파일을 찾을 수 없습니다. 기본값 2로 설정합니다.")
        repeat_count = 2
    
    print(f"3초 후에 자동으로 {repeat_count}회 반복 실행합니다. 대상 창에 포커스를 맞춰주세요.")
    print("각 시퀀스마다 content.txt의 모든 라인을 개별적으로 타이핑합니다.")
    time.sleep(3)
    
    # 자동으로 파일 행 개수만큼 반복 실행
    repeat_ctrl_l_auto(repeat_count)

if __name__ == "__main__":
    main()
