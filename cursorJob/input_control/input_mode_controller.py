import pyautogui
import time
import re
import pyperclip
from .input_mode_detector import detect_input_mode, is_korean_text
from .hangul_english_key import press_hangul_english_smart

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

def analyze_text_mode(text):
    """텍스트가 한글인지 영문인지 분석"""
    if not text:
        return None
    
    if is_korean_text(text):
        return 'korean'
    else:
        return 'english'

def sync_input_mode_with_content(content_file_path):
    """입력 모드와 파일 내용을 동기화"""
    print("=== 입력 모드 동기화 시작 ===")
    
    # 1. 현재 입력 모드 감지 (A)
    print("1. 현재 입력 모드 감지 중...")
    current_mode = detect_input_mode()
    print(f"현재 입력 모드: {current_mode}")
    
    if current_mode is None:
        print("입력 모드를 감지할 수 없습니다.")
        return False
    
    # 2. 파일 내용 분석 (B)
    print("2. 파일 내용 분석 중...")
    content = read_content_file(content_file_path)
    if content is None:
        print("파일 내용을 읽을 수 없습니다.")
        return False
    
    content_mode = analyze_text_mode(content)
    print(f"파일 내용 모드: {content_mode}")
    
    # 3. 모드 비교 및 동기화
    print("3. 모드 비교 및 동기화...")
    if current_mode != content_mode:
        print(f"모드 불일치 감지! 현재: {current_mode}, 필요: {content_mode}")
        print("한/영 키를 눌러서 모드를 전환합니다...")
        
        # 한/영 키 입력
        if press_hangul_english_smart():
            print("입력 모드 전환 완료")
            time.sleep(0.5)  # 전환 후 안정화 대기
            
            # 전환 후 재확인
            new_mode = detect_input_mode()
            print(f"전환 후 입력 모드: {new_mode}")
            
            if new_mode == content_mode:
                print("✅ 입력 모드 동기화 성공!")
                return True
            else:
                print("❌ 입력 모드 동기화 실패")
                return False
        else:
            print("❌ 한/영 키 입력 실패")
            return False
    else:
        print(f"✅ 모드 일치! 현재: {current_mode}, 필요: {content_mode}")
        return True

def main():
    """메인 실행 함수"""
    print("입력 모드 동기화 프로그램")
    print("3초 후에 시작합니다. 텍스트 입력이 가능한 창에 포커스를 맞춰주세요.")
    time.sleep(3)
    
    # content.txt 파일 경로
    content_file = "content.txt"
    
    # 동기화 실행
    success = sync_input_mode_with_content(content_file)
    
    if success:
        print("\n🎉 모든 작업이 성공적으로 완료되었습니다!")
    else:
        print("\n⚠️ 작업 중 문제가 발생했습니다.")

if __name__ == "__main__":
    main()
