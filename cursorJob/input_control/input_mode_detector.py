import pyautogui
import time
import re
import pyperclip

def is_korean_text(text):
    """텍스트가 한글인지 확인"""
    korean_pattern = re.compile(r'[ㄱ-ㅎㅏ-ㅣ가-힣]')
    return bool(korean_pattern.search(text))

def detect_input_mode():
    """텍스트 입력으로 현재 모드 확인"""
    time.sleep(1)  # 최소 대기 시간
    
    try:
        # 테스트 문자 입력
        pyautogui.write('a', interval=0.01)
        time.sleep(0.1)
        
        # 입력된 텍스트 복사
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        
        # 입력된 텍스트 확인
        input_text = pyperclip.paste()
        
        if input_text:
            # 한글인지 영문인지 확인
            if is_korean_text(input_text):
                return 'korean'
            else:
                return 'english'
        else:
            return None
            
    except Exception as e:
        return None
    finally:
        # 입력된 텍스트 삭제
        try:
            pyautogui.press('delete')
        except:
            pass

if __name__ == "__main__":
    print("입력 모드 테스트를 시작합니다...")
    print("3초 후에 테스트를 시작합니다. 테스트할 창에 포커스를 맞춰주세요.")
    time.sleep(3)
    
    result = detect_input_mode()
    print(f"테스트 결과: {result}")
    
    if result is None:
        print("입력 모드를 감지할 수 없습니다. 텍스트 입력이 가능한 창에 포커스를 맞춰주세요.")
    elif result == 'korean':
        print("현재 한글 입력 모드입니다.")
    elif result == 'english':
        print("현재 영문 입력 모드입니다.")
