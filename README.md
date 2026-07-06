# SeminarServerAPI

프론트엔드 8주차 **연동 세미나**용 TMI 방명록 CRUD API 서버입니다 ~ 🦁

<br>

## 🛠 기술 스택

- Python 3
- Django 5.0.6
- Django REST Framework
- SQLite (기본 DB)

<br>

## 🚀 실행 방법

> 가상환경(`myvenv`)은 레포에 포함되어 있지 않습니다.
> 아래 순서대로 따라오면 맥/윈도우 관계없이 동일하게 동작합니다.

### 1. 가상환경 활성화

> 가상환경이 없다면 먼저 생성하세요.
>
> ```bash
> python -m venv myvenv     # Windows
> python3 -m venv myvenv    # Mac
> ```

```bash
# Mac / Linux
source myvenv/bin/activate

# Windows
myvenv\Scripts\activate
```

### 2. 패키지 설치 방법

`requirements.txt`가 있는 경우:

```bash
pip install -r requirements.txt
```

없다면 직접 설치:

```bash
pip install django
pip install djangorestframework
```

### 3. DB 생성 (마이그레이션)

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 관리자(슈퍼유저) 계정 생성

admin 페이지 로그인 및 데이터 확인용 계정입니다.

```bash
python manage.py createsuperuser
```

- Username / Password 입력 (Email은 건너뛰어도 됨)
- 비밀번호는 입력해도 화면에 보이지 않습니다 (정상)

### 5. 서버 실행

```bash
python manage.py runserver
```

<br>

## 🔗 접속 주소

| 주소                           | 설명                                  |
| ------------------------------ | ------------------------------------- |
| http://127.0.0.1:8000/entries/ | DRF Browsable API (엔드포인트 테스트) |
| http://127.0.0.1:8000/admin/   | 관리자 페이지 (DB 데이터 직접 확인)   |

<br>

## 📋 API 명세

Base URL: `http://127.0.0.1:8000`

| 기능      | Method | URI                    |
| --------- | ------ | ---------------------- |
| 전체 조회 | GET    | `/entries/`            |
| 작성      | POST   | `/entries/`            |
| 특정 조회 | GET    | `/entries/{entry_id}/` |
| 수정      | PUT    | `/entries/{entry_id}/` |
| 삭제      | DELETE | `/entries/{entry_id}/` |

### 데이터 구조

```json
{
  "id": 1,
  "author": "이연서",
  "comment": "아자아자 파이팅 ~ 💥",
  "timestamp": "2026-07-06T11:03:00Z"
}
```

- `author`, `comment` → 사용자가 입력
- `id`, `timestamp` → 서버가 자동 생성 (요청 시 보낼 필요 없음)

<br>

## ⚠️ 트러블슈팅

### `ModuleNotFoundError: No module named 'corsheaders'`

`corsheaders`가 설치되지 않은 상태입니다. 아래 명령어로 설치하세요.

```bash
pip install django-cors-headers
```

### CORS 에러가 발생한다면

프론트엔드(예: `http://localhost:5173`)에서 요청 시 CORS 에러가 뜨는 경우,
`django-cors-headers` 설치 후 `settings.py`에 설정을 추가합니다.

```bash
pip install django-cors-headers    # Windows
pip3 install django-cors-headers   # Mac
```

`commentbook/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # 가능한 위쪽에
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

<br>

## 📁 프로젝트 구조

```
SeminarServerAPI/
├── commentbook/          # 프로젝트 설정
│   ├── settings.py
│   └── urls.py           # 프로젝트 URL (entries.urls 연결)
├── entries/              # 방명록 앱
│   ├── models.py         # Entry 모델
│   ├── serializers.py    # EntrySerializer
│   ├── views.py          # EntryViewSet (CRUD)
│   ├── urls.py           # DefaultRouter로 /entries/ 등록
│   └── admin.py          # Entry 모델 admin 등록
├── manage.py
└── requirements.txt
```
