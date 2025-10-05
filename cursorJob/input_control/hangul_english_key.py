import pyautogui
import time

def press_hangul_english():
    """한/영 키를 입력"""
    try:
        # 한/영 키는 보통 'hangul' 키로 매핑됨
        pyautogui.press('hangul')
        print("한/영 키가 입력되었습니다.")
        return True
    except Exception as e:
        print(f"한/영 키 입력 중 오류 발생: {e}")
        return False

def press_hangul_english_alternative():
    """한/영 키 대안 방법 (Alt + Right Shift)"""
    try:
        pyautogui.hotkey('alt', 'right shift')
        print("Alt + Right Shift로 한/영 키를 입력했습니다.")
        return True
    except Exception as e:
        print(f"대안 한/영 키 입력 중 오류 발생: {e}")
        return False

def press_hangul_english_smart():
    """한/영 키를 스마트하게 입력 (주 방법 실패 시 대안 시도)"""
    print("한/영 키를 입력합니다...")
    
    # 주 방법 시도
    if press_hangul_english():
        return True
    
    print("주 방법 실패, 대안 방법을 시도합니다...")
    time.sleep(0.1)
    
    # 대안 방법 시도
    return press_hangul_english_alternative()

def press_hangul_english_with_delay(delay=1.0):
    """지연 시간 후 한/영 키를 입력"""
    print(f"{delay}초 후에 한/영 키를 입력합니다...")
    time.sleep(delay)
    return press_hangul_english_smart()

if __name__ == "__main__":
    print("한/영 키 입력 테스트")
    print("3초 후에 한/영 키를 입력합니다. 입력할 창에 포커스를 맞춰주세요.")
    
    # 3초 대기 후 한/영 키 입력
    press_hangul_english_with_delay(3.0)
