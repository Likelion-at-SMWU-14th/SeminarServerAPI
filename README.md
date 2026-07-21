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
source myvenv/Scripts/activate
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

### Python / Django 버전 호환 오류가 발생한다면

관리자 페이지나 Django 내부 파일에서 아래와 같은 예외가 발생한다면, Python과 Django 버전이 호환되지 않는 경우일 수 있습니다.

```text
AttributeError: 'super' object has no attribute 'dicts'
```

본 프로젝트는 다음 버전을 기준으로 실행됩니다.

```text
Python 3.12.x
Django 5.0.6
```

**1. 현재 Python 버전 확인**

```bash
python --version
```

Python 3.13 이상이라면, 기존 가상환경을 삭제하고 Python 3.12 기반으로 다시 만듭니다.
(가상환경 폴더를 삭제해도 프로젝트 코드와 DB 파일은 삭제되지 않습니다.)

**2. 기존 가상환경 비활성화 및 삭제**

```bash
# Mac / Windows Git Bash
deactivate
rm -rf myvenv
```

```powershell
# Windows PowerShell
deactivate
Remove-Item -Recurse -Force myvenv
```

**3. Python 3.12 설치 후 버전 확인**

[Python 공식 홈페이지](https://www.python.org/downloads/)에서 Python 3.12를 설치합니다.

```bash
# Mac
python3.12 --version

# Windows
py -3.12 --version
```

**4. Python 3.12 기반 가상환경 생성**

```bash
# Mac
python3.12 -m venv myvenv

# Windows
py -3.12 -m venv myvenv
```

**5. 가상환경 활성화**

```bash
# Mac
source myvenv/bin/activate

# Windows Git Bash
source myvenv/Scripts/activate

# Windows CMD
myvenv\Scripts\activate
```

```powershell
# Windows PowerShell
.\myvenv\Scripts\Activate.ps1
```

**6. 가상환경 Python 버전 확인** (`Python 3.12.x`가 출력되어야 함)

```bash
python --version
```

**7. 패키지 재설치**

```bash
python -m pip install -r requirements.txt
```

**8. 마이그레이션 및 서버 실행**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

> 가상환경을 새로 만들었는데도 오류가 계속된다면, 아래 명령어로 실행 중인 Python과 Django 버전을 다시 확인하세요.
>
> ```bash
> python --version
> python -m django --version
> ```

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
