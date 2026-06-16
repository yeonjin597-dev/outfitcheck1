# 👔 오늘 뭐 입지? — 날씨 기반 코디 추천 앱

> Streamlit + FastAPI + Docker + AWS EC2 기반 추천 웹 애플리케이션

## 📌 프로젝트 소개

현재 날씨(OpenWeatherMap API)와 사용자의 일정·스타일 정보를 바탕으로  
오늘의 코디 콘셉트 및 아이템을 추천해주는 웹 서비스입니다.

## 🗂️ 폴더 구조

```
outfit-recommender/
├── back/                   # FastAPI 백엔드
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── front/                  # Streamlit 프론트엔드
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env                    # API 키 (gitignore 처리)
├── .gitignore
└── README.md
```

## ⚙️ 기술 스택

| 역할 | 기술 |
|------|------|
| 프론트엔드 | Streamlit |
| 백엔드 | FastAPI |
| 날씨 API | OpenWeatherMap |
| 컨테이너 | Docker, Docker Compose |
| 배포 | AWS EC2 |

## 🌐 배포 주소 (AWS EC2)

| 서비스 | 주소 |
|--------|------|
| Streamlit (프론트) | http://54.242.224.187:8501 |
| FastAPI Docs | http://54.242.224.187:8000/docs |

---

## 🚀 실행 방법

### 1. 환경변수 설정

`.env` 파일을 루트에 생성하고 아래 내용을 입력합니다:

```
OPENWEATHER_API_KEY=여기에_API_키_입력
```

### 2. Docker Compose로 실행

```bash
docker-compose up --build
```

### 3. 접속

| 서비스 | 주소 |
|--------|------|
| Streamlit (프론트) | http://localhost:8501 |
| FastAPI (백엔드) | http://localhost:8000 |
| FastAPI Docs | http://localhost:8000/docs |

## 🔄 서비스 흐름

```
사용자 입력 (도시, 일정, 스타일, 성별)
    ↓
Streamlit → FastAPI POST /recommend
    ↓
FastAPI → OpenWeatherMap API (날씨 조회)
    ↓
날씨 + 입력값 기반 추천 로직 실행
    ↓
JSON 응답 반환
    ↓
Streamlit 화면에 결과 출력
```

## 📥 입력 항목

- **도시명**: 영문 도시명 (예: Seoul, Busan)
- **일정**: 데이트 / 학교 / 운동 / 재택
- **스타일**: 캐주얼 / 미니멀 / 스트릿 / 포멀
- **성별**: 남 / 여 / 무관

## 📤 출력 결과

- 현재 날씨 (기온, 날씨 아이콘)
- 오늘의 코디 콘셉트명 + 설명
- 상의 / 하의 추천 아이템
- 아우터 (기온·날씨 조건부)
- 악세서리 & 슈즈
- 스타일 팁
