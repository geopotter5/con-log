import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env 파일에서 API 키 로드
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY가 .env 파일에 없습니다!")

# Gemini 설정
genai.configure(api_key=GEMINI_API_KEY)

def get_ai_response(prompt, temperature=0.7, max_tokens=1000):
    """
    Gemini AI에 프롬프트를 보내고 응답받기
    
    Args:
        prompt (str): AI에게 보낼 질문/요청
        temperature (float): 창의성 정도 (0.0~1.0)
        max_tokens (int): 최대 응답 길이
    
    Returns:
        str: AI의 응답
    """
    try:
        model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ AI 응답 오류: {str(e)}"

def get_content_recommendation(user_mood, available_time, watched_before):
    """
    사용자의 기분과 시간에 맞춰 컨텐츠 추천
    
    Args:
        user_mood (str): 현재 기분 (예: "스트레스", "외로움", "즐거움")
        available_time (int): 사용 가능한 시간 (분)
        watched_before (list): 지금까지 본 컨텐츠 목록
    
    Returns:
        str: AI의 추천 컨텐츠
    """
    watched_summary = ", ".join(watched_before[-5:]) if watched_before else "없음"
    
    prompt = f"""
    당신은 엔터테인먼트 전문 AI 추천가입니다.
    
    사용자 상황:
    - 현재 기분: {user_mood}
    - 사용 가능한 시간: {available_time}분
    - 최근 본 컨텐츠: {watched_summary}
    
    이 상황에 최적의 컨텐츠 3가지를 추천해주세요.
    (영화, 드라마, 웹툰, 애니, 책, 게임, 유튜브 등 다양한 미디어 포함)
    
    각 추천마다:
    1. 컨텐츠명
    2. 이유 (왜 이게 좋을까?)
    3. 소요 시간
    
    형식으로 답변해주세요.
    """
    
    return get_ai_response(prompt, temperature=0.8)

def analyze_content_taste(content_list):
    """
    사용자의 컨텐츠 기록을 분석해 취향 파악
    
    Args:
        content_list (list): 컨텐츠 기록 리스트
    
    Returns:
        str: 취향 분석 결과
    """
    content_summary = "\\n".join([f"- {c}" for c in content_list[-20:]])
    
    prompt = f"""
    다음은 사용자가 본 컨텐츠 기록입니다:
    
    {content_summary}
    
    이 데이터를 바탕으로:
    1. 주요 취향 장르
    2. 시청 패턴
    3. 추천할 새로운 컨텐츠 유형
    
    을 분석해주세요. 간결하게 답변해주세요.
    """
    
    return get_ai_response(prompt, temperature=0.5)

if __name__ == "__main__":
    # API 연동 테스트
    print("🧠 Gemini API 테스트 중...")
    test_response = get_ai_response("안녕하세요! 당신은 누구인가요?")
    print(f"✅ API 연동 성공!\\n응답: {test_response}")
