# Model - Template - View 연동
  - urls.py 수정
  ```python
  path('',views.index,name = 'index')
  ```
  - views.py 수정
  ```python
  from .models import GuessNumbers
def index(request):
	lottos = GuessNumbers.objects.all()
	#object들 전부 가져옴
	return render(request,'lotto/default.html',{'lottos':lottos})
```
- template 파일 수정
  - view에서 불러온 model의 object를 template파일에 적용
```python
<div class = "container lotto">
	{% for lotto in lottos %}
	<h2>{{lotto.text}}<h2>
	<p>last update : {{lotto.update_date}} by {{lotto.name}}</p>
	<p>{{lotto.lottos|linebreaksbr}}</p>
	{% endfor %}
</div>
```
  
