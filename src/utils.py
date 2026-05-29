import json
import os
from datetime import datetime
from pathlib import Path

# 데이터 폴더 설정
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

LEISURE_FILE = DATA_DIR / "leisure_archive.json"
CALENDAR_FILE = DATA_DIR / "calendar.json"
USER_PROFILE_FILE = DATA_DIR / "user_profile.json"

def load_json(file_path):
    """
    JSON 파일 로드
    파일이 없으면 빈 딕셔너리 반환
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ 파일 로드 오류: {e}")
            return {}
    return {}

def save_json(file_path, data):
    """
    JSON 파일 저장
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ 파일 저장 오류: {e}")
        return False

def get_next_id(items):
    """
    새로운 항목의 ID 생성
    """
    if not items:
        return 1
    return max([item.get('id', 0) for item in items]) + 1

def format_date(date_str):
    """
    날짜 포맷팅
    YYYY-MM-DD 형식
    """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except:
        return datetime.now().strftime('%Y-%m-%d')

def print_menu(title, options):
    """
    메뉴 출력
    """
    print(f"\\n{'='*50}")
    print(f"📋 {title}")
    print(f"{'='*50}")
    for key, value in options.items():
        print(f"{key}. {value}")
    print(f"{'='*50}\\n")

def print_header(text):
    """
    헤더 출력
    """
    print(f"\\n{'╔' + '═'*48 + '╗'}")
    print(f"║ {text:^46} ║")
    print(f"{'╚' + '═'*48 + '╝'}")

def print_success(text):
    """성공 메시지"""
    print(f"\\n✅ {text}")

def print_error(text):
    """에러 메시지"""
    print(f"\\n❌ {text}")

def print_info(text):
    """정보 메시지"""
    print(f"\\nℹ️  {text}")

def get_rating_stars(rating):
    """
    평점을 별로 표현
    예: 8 -> ★★★★★★★★☆☆
    """
    filled = int(rating)
    empty = 10 - filled
    return "★" * filled + "☆" * empty
