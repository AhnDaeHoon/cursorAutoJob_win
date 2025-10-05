import pyautogui
import time
import os
import subprocess

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

def main():
    """메인 실행 함수"""
    print("Ctrl + L 반복 입력 프로그램")
    
    # content.txt 파일의 행 개수 읽기 (상위 폴더에서 찾기)
    content_file = "../content.txt"
    if os.path.exists(content_file):
        repeat_count = read_content_file_lines(content_file)
    else:
        print(f"'{content_file}' 파일을 찾을 수 없습니다. 기본값 3으로 설정합니다.")
        repeat_count = 3
    
    print(f"3초 후에 자동으로 {repeat_count}회 반복 실행합니다. 대상 창에 포커스를 맞춰주세요.")
    time.sleep(3)
    
    # 자동으로 파일 행 개수만큼 반복 실행
    repeat_ctrl_l_auto(repeat_count)

if __name__ == "__main__":
    main()
