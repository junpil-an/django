from django.db import models
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
		
	#admin 내 표시방법 변경
	def __str__(self):
		return '%s - %s' %(self.name,self.text)