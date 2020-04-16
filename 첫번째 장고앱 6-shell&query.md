# shell을 이용한 장고 관리
  - class.objects.all()
  - class의 object를 리스트로 가져옴 -> `python manage.py shell`
  ```shell
   from mylotto.models import GuessNumbers
   import datetime
   GuessNumbers.objects.all()
   ```
# 쿼리셋 정리
  -  queryset : 전달받은 목록
  - `class.objects.all()` : 전달받은 객체의 전체목록 + `ordered_by('Id')` id순으로 정렬
  - `class.objects.get()` : 특정 오브젝트를 가져옴 
  - `class.objects.create()` : 특정 모델의 새 row 저장 INSERT INTO SQL을 생성해 주는 인터페이스
  - `queryset.filter`(조건필드1= 조건값1,조건필드2=조건값2) 모델전체에서 조건필드 1,2추가
## 쿼리셋작성팁
  - DB로 전달/실행 되는 SQL개수 줄이고 각 SQL 성능/처리속도 최적화 필요
  - 로직 복잡도 중요함
  - 프로그래밍언어 종류는 대개 미미하다
  - django-debug-toolbar(디버깅 라이브러리) - request/response에 다양한 디버깅 정보보여줌
  - `debug` : 컴퓨터 프로그램이나 하드웨어 장치에서 잘못된 부분(버그)를 찾아 수정하거나 에러를 피해나가는 처리과정
