# 로또만들기 , 프로젝트 & 앱 생성
- MTV
  - Model
  - Template
  - View
 ![MTV](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F991AD1365B448DA70224A9)
 
 - Routing(-urls.py) : URL parsing 후에 View에 전달
 - View :
    - URL Routing 규칙을 처리하는 오브젝트 - URL 디스패치
    - URL 경로를 정해 View로
    - Model로 부터 데이터 수집
    - 수집한 데이터를 Template으로 처리
 - Template :
    - html, presentation layer 담당
 - Model : DB조작을 쉽게 해줌(ORM: Object Relational Model)
 - DB - Data 저장소 ,데이터 읽고 쓰는데 Model을 사용
 
## 프로젝트 & 앱 생성

- 가상환경 설치 & 실행
```shell
//1.가상환경 설정
python -m venv django

//2.가상환경 실행
python django/bin/activate

//3.설치된 패키지 확인
pip freeze

//4.프로젝트 생성
django-admin startproject lotto
```
- 5.lotto 폴더에 setting.py에서 수정
  - LANGUAGE_CODE = 'ko-kr'
  - TIME_ZONE = 'Asia/Seoul'
  - STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  - **STATIC_ROOT 사용 이유**
    - STATICFILES_DIRS - 정적 파일이 위치한 경로들을 지정하는 설정 항목(list나 tuple로 담으면 됨)
    - 보통 static 이라는 디렉토리에 정적 파일을 담는다 , `,`를 꼭 추가해야함!!
```shell
//6.app 생성
python manage.py startapp mylotto
```
- 7.stting.py 에 등록해줌
  - INSTALLED_APPS=[
      'mylotto',/*admin
      ....
      ]
- 8.서버 실행
```shell
python manage.py runserver
Starting development server at http://127.0.0.1:8000/
```
   




```
