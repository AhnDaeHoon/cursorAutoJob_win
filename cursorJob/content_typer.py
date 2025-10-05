import pyautogui
import time
import pyperclip

def read_content_file(file_path):
    """파일 내용을 읽어서 반환"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            print(f"파일 내용: '{content}'")
            return content
    except Exception as e:
        print(f"파일 읽기 오류: {e}")
        return None

def type_text(text, interval=0.05):
    """텍스트를 타이핑"""
    if not text:
        print("타이핑할 텍스트가 없습니다.")
        return False
    
    try:
        print(f"타이핑 시작: '{text}'")
        print(f"타이핑 간격: {interval}초")
        
        # 타이핑 전 잠시 대기
        time.sleep(0.5)
        
        # 실제 타이핑 실행
        pyautogui.write(text, interval=interval)
        
        # 타이핑 후 잠시 대기
        time.sleep(0.5)
        
        print("타이핑 완료")
        return True
    except Exception as e:
        print(f"타이핑 중 오류 발생: {e}")
        return False

def type_text_with_clipboard(text, interval=0.05):
    """클립보드를 사용하여 텍스트를 타이핑 (한글 등 복잡한 문자용)"""
    if not text:
        print("타이핑할 텍스트가 없습니다.")
        return False
    
    try:
        print(f"클립보드 방식으로 타이핑 시작: '{text}'")
        
        # 1. "@" 특수문자 먼저 입력
        print("'@' 특수문자 입력 중...")
        pyautogui.write('@', interval=interval)
        
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
        
        print("클립보드 방식 타이핑 완료")
        return True
    except Exception as e:
        print(f"클립보드 방식 타이핑 중 오류 발생: {e}")
        return False

def type_content_file(file_path, interval=0.05):
    """파일 내용을 읽어서 타이핑"""
    print("=== 파일 내용 타이핑 시작 ===")
    
    # 1. 파일 내용 읽기
    print("1. 파일 내용 읽기 중...")
    content = read_content_file(file_path)
    if content is None:
        print("파일 내용을 읽을 수 없습니다.")
        return False
    
    # 2. 타이핑 실행 (클립보드 방식 사용 - 한글 타이핑 안정성)
    print("2. 타이핑 실행 중...")
    success = type_text_with_clipboard(content, interval)
    
    if success:
        print("✅ 파일 내용 타이핑 완료!")
        return True
    else:
        print("❌ 파일 내용 타이핑 실패")
        return False

def main():
    """메인 실행 함수"""
    print("파일 내용 타이핑 프로그램")
    print("바로 시작합니다. 텍스트 입력이 가능한 창에 포커스를 맞춰주세요.")
    
    # content.txt 파일 경로 (상위 폴더에서 찾기)
    content_file = "../content.txt"
    
    # 타이핑 실행 (일반 타이핑 방식 사용)
    success = type_content_file(content_file, interval=0.05)
    
    if success:
        print("\n🎉 타이핑이 성공적으로 완료되었습니다!")
    else:
        print("\n⚠️ 타이핑 중 문제가 발생했습니다.")

if __name__ == "__main__":
    main()
