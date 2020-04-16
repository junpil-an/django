# MODEL 클래스 만들기
  - 모델과 DB를 연결해서 DB에 영구적으로 저장하게되는데 ORM(Object -Relational Mapping)이라함
  - DB에 데이터를 저장,불러오기 위해 모델을 사용
  - models.py 작성 후, 장고에게 모델을 만들었다는걸 알려줌
  ```shell
  python manage.py makemigrations //변경점들을 확인
  python manage.py migrate //변경점들을 저장
  ```
# model.py에 class 추가
```python

from django.utils import timezone
import random
# Create your models here.

class GuessNumbers(models.Model):
	#상위 클래스에서 Model을 받음
	name = models.CharField(max_length = 24)
	lottos = models.CharField(max_length =255, default=
	'[1,2,3,4,5,6,]')
	text = models.CharField(max_length =255)
	num_lotto = models.IntegerField(default =5)
	update_date =models.DateTimeField()
	
	#method 정의
	def generate(self):
		self.lottos =""
		origin = list(range(1,46))
		# self.num_lotto 만큼 반복해서 수행
		for _ in range(0,self.num_lotto):
			#origin list 순서 섞는다
			random.shuffle(origin)
			guess = origin[:6]
			guess.sort()
			self.lottos += str(guess)+'\n'
		self.update_date = timezone.now()
		#object를 DB에 저장
		self.save() 
 ```
 # admin site에 model등록
  - [관리자서버](http://127.0.0.1:8000/admin/) 접속
  ```shell
  python.manage.py createsuperuser //계정 생성
  ```
  - `admin.py`에 모델 등록
  ```python
  from mylotto.models import GuessNumbers
  admin.site.register(GuessNumbers)
  ```
  
  - model에 `__str__` method 추가
  ```python
    def __str__(self):
		return '%s - %s' %(self.name,self.text)
  ```
  
  
  
 
