# form 만들기
  -mylotto/forms.py 새로 만들기
  -forms.py 코드 작성
  ```python
  from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
	class Meta:
		model = GuessNumbers
		fields =('name','text','num_lotto',)
		#입력 받을 것 따로 설정
  ```
 - `urls.py` 수정
 ```python
	path('lotto/new',views.post, name ='new_lotto'),
 ```
 - `views.py` 수정
 ```python
 from .forms import PostForm

 post(request):
	form = PostForm()
	return render(request,'lotto/form.html',{'form':form})
 ```
 -`form.html` 템플릿 작성
```python
 <!doctype html>
{% load static %}
<html lang= "ko">
  <head>
    <title>My Little Lotto</title>
	<meta name = "viewport" content= "width=device-width,initial-scale=1">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
	<link href="//fonts.googleapis.com/css?family=Space+Mono" rel="stylesheet">
	<link rel="stylesheet" href="{% static 'css/lotto.css' %}">
 
  </head>
  <body>
	  <div class= "page-header">
		<form method= "POST" class="post-form">
		  {% csrf_token %}
		  {{form.as_p}}
		  <button type = "submit" class ="sava btn btn-default">save</button>
		</form>  
	  </div>
  </body>
</html>
```  
- `{{form.as_table}}` : <tr> tag로 form을 렌더링 해준다
- `{{form.as_p}}` : <p>로 감싸 form을 렌더링 해준다
- `{{form.as_ul}}` : <li>로 감싸 form을 렌더링 해준다

- post 처리
  - get으로 접속했을때 화면과,post로 접속했을 때 화면을 분기
- `views.py`  `post` 수정
```python
from djnago.shortcuts import render,redirect
from .forms import PostForm

	
def post(request):
	if request.method == "POST":
		#PostForm으로 부터 받은 데이터처리를 위한 인스턴스 생성
		form = PostForm(request.POST)
		if form.is_valid():
			lotto =form.save(commit = False)
			#lotto 오브젝트를 form으로 부터 가져오지만 DB반영은 하지 않음
			lotto.generate()
			return redirect('index')
			#url의 name을 경로대신 입력함
	else:
		form = PostForm()
		return render(request,'lotto/form.html',{'form':form})
	
```
  
