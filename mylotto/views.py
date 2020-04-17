from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):
	lottos = GuessNumbers.objects.all()
	#object들 전부 가져옴
	return render(request,'lotto/default.html',{'lottos':lottos})
	
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
	
