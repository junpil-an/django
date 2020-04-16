#urls.py 수정
  - `__init.py__` : 해당 파일이 폴더가 module이라는 뜻
  - `setting.py` :장고 setting
  - `urls.py` : url
  - urls.py에서 추가
  ```python
  from mylotto import views
  path('',views.index, name ='hello'), #창 접속시 views에 index method를 실행하라
]
```

## url 정규표현식
  - `^post/(\d+)/$` 의 뜻 
  - ^post/` :  장고에게 url  post/가 있다는 것을 말해 준다
  
  - `(\d+)` : 숫자가 있다는 뜻입니다. 
  - `/` : 장고에게 /뒤에 문자가 있음을 말해줌
  - `$`: URL의 끝이 방금 전에 있던 /로 끝난다는 걸 알려줌

#views.py 수정
  - views에 index 추가
  ```python
  from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>로또앱 index!</h1>')
```

# 정리
  - urls.py 에 경로 지정해 views.py 에 method를 실행시킨다
