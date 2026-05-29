# Con-Log 🎬📚🎮

**여가 컨텐츠 아카이빙 + AI 추천 시스템**

대학생의 일상을 책임지는 AI 비서 - 본 영화, 읽은 책, 팬 팀 경기까지 모두 기록하고,
AI가 당신의 취향을 분석해 상황에 맞는 컨텐츠를 추천합니다.

## 🎯 주요 기능

### 1️⃣ 여가 컨텐츠 아카이빙
- 📽️ **영화**: 본 영화 기록, 평점, 감상평
- 📺 **드라마**: 현재 진행 상황, 평점
- 📖 **책**: 읽은 책, 저자, 감상평
- 🎨 **웹툰**: 플랫폼, 현재 화, 평점
- 🎬 **애니메이션**: 에피소드 진행률, 평점
- 🎮 **게임**: 플레이 시간, 진행률, 평점
- ⚽ **스포츠**: 팔로우 팀의 경기 결과 및 다음 경기 일정

### 2️⃣ AI 추천 시스템
- "지금 뭐 할까?" - 상황별 추천
- "기분에 맞는 컨텐츠" - 감정 기반 추천
- "스트레스 해소 활동" - 휴식 추천
- "오늘의 추천" - 개인화 추천

### 3️⃣ 캘린더 + 통계
- 여가 계획 일정 관리
- 월별/주별 컨텐츠 통계
- "이번 달 본 영화", "읽은 책 수" 등

## 🛠️ 기술 스택

- **언어**: Python 3.8+
- **AI**: Google Gemini API
- **데이터 저장**: JSON
- **개발 환경**: VS Code

## 📁 프로젝트 구조

```
con-log/
├── src/
│   ├── main.py                 # 메인 실행 파일
│   ├── gemini_api.py           # Gemini API 연동
│   ├── leisure_manager.py      # 여가 컨텐츠 관리
│   ├── ai_recommender.py       # AI 추천 기능
│   ├── calendar_manager.py     # 캘린더 관리
│   └── utils.py                # 유틸 함수
├── data/
│   ├── leisure_archive.json    # 여가 기록
│   ├── calendar.json           # 캘린더
│   └── user_profile.json       # 사용자 정보
├── .env                        # API 키 (Git 제외)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/geopotter5/con-log.git
cd con-log
```

### 2. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 3. API 키 설정

1. [Google AI Studio](https://aistudio.google.com/app/apikey)에서 API 키 발급
2. 프로젝트 루트에 `.env` 파일 생성
3. 다음 내용 추가:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. 실행
```bash
python src/main.py
```

## 📖 사용법

### 메인 메뉴
```
╔════════════════════════════════════════════╗
║   🎬 Con-Log - AI 추천 시스템           ║
║        여가 컨텐츠 아카이빙 + AI 추천   ║
╚════════════════════════════════════════════╝

[메인 메뉴]
1. 🎮 여가 컨텐츠 기록
2. 🤖 AI 추천받기
3. 📚 아카이브 조회
0. 🚪 종료

선택> _
```

## ⚠️ 주의사항

- Google Gemini API 무료 플랜: 하루 50회 요청 제한
- `.env` 파일은 Git에 올라가지 않음 (.gitignore에 등록됨)
- JSON 파일은 자동으로 `data/` 폴더에 생성됨

## 📝 과제 정보

- **과목**: SW기초프로그래밍
- **과제명**: 나만의 맞춤형 AI 비서 개발
- **마감**: 2026년 5월 31일
- **개발자**: geopotter5

## 📜 라이선스

MIT License
