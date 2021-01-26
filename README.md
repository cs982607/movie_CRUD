# Movie_CRUD

이 프로젝트는 Python 3.8.5버전에서 작성되었습니다.

테스트를 위해 SecretKey와 같이 업로드 되었습니다.

### 질문 1 
### 1-1. RESTful API인 /movies 의 Movie Data Model

```
    name        #영화 제목
    country     #영화 제작 국가
    main_image  # 메인 이미지
    description # 영화 소개
    show_time   # 상영 시간
    genre       # 영화 장르
    director    # 영화 제작 감독
    actor       # 영화 출연 배우 
```
### 1-2. 기대하는 HTTP Status code와 JSON data 형식.
``` 
------------------------------------------------------------------------------------------

GET /movies
Status = 200 
{
    "movies": [
        {
            "name": "크루아상",
            "main_image": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=197496#"
        },
        {
            "name": "소울",
            "main_image": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=184517#"
        },
        {
            "name": "아이엠히어",
            "main_image": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=189457#"
        },
        {
            "name": "라라랜드",
            "main_image": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=134963#"
        },
        {
            "name": "블라인드",
            "main_image": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=68520#"
        },
        {
            "name": "블라인드",
            "main_image": "??"
        }
    ]
}

GET /movies
Not found
Status = 404
{
    "message": "NOT_EXIST_MOVIE"
}

------------------------------------------------------------------------------------------

GET /movies/{movie_id}
Success
Status = 200

{
    "movie_detail": {
        "name": "크루아상",
        "country": "한국",
        "main_image": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=197496#",
        "description": "빵알못 공시생, 크루아상의 세계에 입문하다!",
        "show_time": 122,
        "genre": "코미디",
        "director": "조성규",
        "actor": "남보라, 혁"
    }
}

GET /movies/{movie_id}
Not found
Status = 404

{
    "message": "NOT_EXIST_MOVIE"
}

------------------------------------------------------------------------------------------

POST /movies
Created
Status = 200
{
    "name"        : "블라인드",
    "country"     : "미국",
    "main_image"  : "이미지",
    "description" : "“내 사랑 나를 기억해줘.”",
    "show_time"   : 95,
    "genre"       : "멜로/로맨스",
    "director"    : "타마르",
    "actor"       : "요런 셀데슬라흐츠"
}

POST /movies
Conflict
Status = 404
{
    "message": "KEY_ERROR"
}

------------------------------------------------------------------------------------------

PUT /movies/{movie_id}
Accepted
Status = 200
{
    "message": "SUCCESS"
}

PUT /movies/{movie_id}
Not acceptable
Status = 404
{
    "message": "NOT_EXIST_MOVIE"
}

------------------------------------------------------------------------------------------

DELETE /movies/{movie_id}
No contents 
Status = 200
{
    "message": "SUCCESS"
}

DELETE /movies/{movie_id}
Method not allowed 
Status = 404
{
    "message": "NOT_EXIST_MOVIE"
}

------------------------------------------------------------------------------------------
```

# 프로젝트 초기화 
### 1. GitHub Clone 
$ git clone https://github.com/cs982607/movie_CRUD

### 2. 가상환경 설정하기 
이 프로젝트는 Conda로 가상환경을 설정하였습니다.

#### 미니콘다 설치
>Mac 버전

$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

>Ubuntu 버전

$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

$chmod -R 755 Miniconda3-latest-Linux-x86_64.sh

$./Miniconda3-latest-Linux-x86_64.sh

#### - conda 가상환경 만들기
$ conda create -n "가상환경이름" python=3.8

#### - conda 가상환경으로 활성화하기
$ conda activate "가상환경이름"

### 3. 라이브러리 설치

해당 폴더(requirements.txt파일이 있는 디렉토리)에 들어가 명령어를 작성한다.

$ pip install -r requirements.txt

### 4. Python 서버 실행

해당 폴더(manage.py파일이 있는 디렉토리)에 들어가 명령어를 작성한다.

$ python manage.py runserver

### 4. 응답 API

GET  /movies (movies 전체 리스트)

POST /movies (movies 생성)

GET /movies/{movie_id} (movie 상세리스트)

PUT /movies/{movie_id} (movie 업데이트)

DELETE /movies/{movie_id} (movie 삭제)

ex) http://127.0.0.1:8000/movies

### 5. 유닛 테스트

해당 폴더(manage.py파일이 있는 디렉토리)에 들어가 명령어를 작성한다.

$ python manage.py test movie


