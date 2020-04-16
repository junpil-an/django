# views와 template 연동
  -`urls.py` 수정
  ```python
  path('lotto/',views.index, name ='index')
  ```
  
  -`models.py` 수정
  ```python
  def index(request):
	return render(request,'lotto/default.html') #요청받은 템플릿을 렌더링 해줌
  
  ```
  
  - mylotto/templates/lotto 폴더 속에 `default.html`을 넣어줌
  - mylotto/static/css 폴더 속에 `lotto.css`를 넣어줌
  - default.html에 넣어줌
  
  ```html
  <!doctype html>
{% load staticfiles %}

<link rel ="stylesheet" href="{%static 'css/lotto.css'%}">
```
- *장고에게 static 파일(css)이 생겼다고 알려줌*
```shell
python manage.py collectstatic
```
