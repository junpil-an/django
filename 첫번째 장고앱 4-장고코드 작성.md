# 장고 테스트 코드 작성
  -test.py 에 테스트를 하기 위해 코드를 작성
  
  ```python
  from django.test import TestCase
  from .models import GuessNumbers
  
  class GuessNumbersTestCase(TestCase):
    def test_generate(self):
      g = GuessNumbers(name='monkey',text ='1등만세!')
      g.generate()
      print(g.update_date)
      print(g.lottos)
      self.assertTrue(len(g.lottos)>20)
      #성공실패 테스트 루틴은 assert method 사용
  ```
  - `python manage.py test` test.py 실행방법
  ```shell
  python manage.py test
  ```
  - test 결과
  ```
  Creating test database for alias 'default'...
System check identified no issues (0 silenced).
2020-04-16 13:39:20.680601+00:00
[2, 12, 22, 36, 37, 38]
[8, 22, 24, 26, 34, 35]
[8, 12, 14, 38, 40, 42]
[1, 3, 6, 31, 36, 43]
[6, 8, 14, 25, 26, 35]
```
