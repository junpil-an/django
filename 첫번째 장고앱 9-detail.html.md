# urls.py
  - detail.html추가
  ```python
	path('detail/',views.detail, name = 'detail'),
  ```
# view.py
  ```python
  def detail(request):
	lotto = GuessNumbers.objects.get(pk= lottokey)
	return render(request,'lotto/detail.html',{'lotto':lotto})
  #pk가 lottokey와 일치하는 object를 가져온다
  #pk는 클래스 object 생성 시 자동으로 가져올 수 있다
```


#detail.html 새로 만들어줌
  - `page-header` - 제일 위에 내용
  - `container lotto` - lotto class object로 나타내겠다
  - `{{}}` : python code 가져올 때 사용
  
  ```html
  <!doctype html>
{% load static %}
<html lang ="ko">
<head>
<link rel ="stylesheet" href="{%static 'css/lotto.css'%}">
</head>
<body>
	<div class = "page-header">
	<h1>My Lotto page<h2>
	</div>
	<div class = "container lotto">
		
		<h2>{{lotto.text}}<h2>
		<p>by {{lotto.name}}</p>
		<p>{{lotto.update_date}}</p>
		<p>{{lotto.lottos|linebreaksbr}}</p>	
	</div>
</body>
```

# `default.html` 템플릿 수정
  ```html
  <a herf="{% url 'new_lotto' %}">
      <span class="glyphicon glyphicon-plus btn btn-default"></span>
  </a>
 ```   
# `detail` 링크 추가    
  ```html
 <div class="page-header">
<h1>My Lotto Page
  <a href="{% url 'new_lotto' %}"><span class="glyphicon glyphicon-plus btn btn-default"></span></a></h1>
</div>

<h2><a href="{% url 'lotto_detail' lottokey=lotto.pk  %}">{{lotto.text}}</a></h2>

  
  ```
  
  
