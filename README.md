# Coupang-Review-Crawling

<p>파이썬을 이용한 쿠팡 리뷰 크롤링 프로그램</p>

<h1>설치 | Installation</h1>

```
$ git clone https://github.com/JaehyoJJAng/Coupang-Review-Crawling.git
$ cd Coupang-Review-Crawling
$ pip install -r ./requirements.txt
```

<h1>사용방법 | Usage</h1>
<p><strong>사용방법 | How to use</strong></p>

```
$ python3 main.py
```

<br>

> ## URL 입력<br>

<img width="1417" alt="image" src="https://user-images.githubusercontent.com/91415701/197674856-31baa0b0-90b6-4cf9-9f3b-d5039ddc62ca.png">

<br>

<h2>페이지 수 입력</h2>
<img width="226" alt="image" src="https://user-images.githubusercontent.com/91415701/197675042-c7101429-ae90-4a02-bc49-81807efa69c7.png">
</hr>

<br>

***

> ## 출력 결과 | Print

```
{'prod_name': '힘내바 초코 스니커즈, 40g, 12개', 'user_name': '이명희', 'rating': 4, 'headline': '등록된 헤드라인이 없습니다', 'review_content': '일반 초코바 크기랑 같아요이가 좋지않은데도 씹기힘들지않고사르륵 부서져요안에 건과가 있어서 고소해요얼집에서 일하는데 중간에 당떨어져서생각나서 삿는데 은근히 양이 좀되네요ㅎㅎ', 'answer': '괜찮아요'}

{'prod_name': '힘내바 초코 스니커즈, 40g, 12개', 'user_name': '0wisdom0', 'rating': 5, 'headline': '힘내바~!', 'review_content': '살까말까 살까말까ㅋㅋ장바구니 담아놨다가 결국 결제하기~!ㅋㅋ여름이라 초코바 사두기가 고민이 됐어요ㅋ눅진눅진 해질것도 그렇고..아이들 초코바 쥐어주면 엉망될까 싶기도 하고~^^;근데 초코가 땡기는 날 결제를 하고 있는 나..ㅋ한번에 다 꺼내먹지 못하게 냉장고 젤 윗칸에 킵~!하나 맛보기로 받자마자 뜯어봅니다..ㅋ울퉁불퉁한표면..여름은 여름인가봅니다..손으로 집어 돌리는 순간 손가락에 묻어나오는 쬬꼬ㅠㅠ얼른 입에 쏙 넣어야 할까봐요~ㅋㅋ맛은..씨리얼 초코에 말아먹는 맛이에요~^^*근데 엄청 달거나 그러지 않고 생각보다 적당히 달달하니..씨리얼의 고소한맛도 나서..하나 다 먹어도 또 생각이 나네요~^^*아이들도 잘 먹어요~ㅋ힘내바~! 문구에 힘도 나는듯요ㅋㅋ회사 직원들 나눠주면 좋을 것 같아 한박스 더 사려고 들어갔더니 이틀째 품절이네요ㅠㅠ재입고알람신청 해두고 입고되면 한박스 더~!ㅋㅋ', 'answer': '예상보다 맛있어요'}

{'prod_name': '힘내바 초코 스니커즈, 40g, 12개', 'user_name': '돈쑤니', 'rating': 5, 'headline': '힘내바~~~', 'review_content': '요즘 많이 하는말같네요.힘내자!!!지인들과 나누려고 사봤어요.초코만있음 넘단데 땅콩이랑 크런키 같은게 있어서바삭하고 씹는맛이 재밌네요.당떨어질때  진짜힘이 필요할때 잘먹을께요~♡박스에 담겨와서 파손없이 잘받았어요', 'answer': '괜찮아요'}

{'prod_name': '힘내바 초코 스니커즈, 40g, 12개', 'user_name': '유*혜', 'rating': 5, 'headline': '달지 않은 건강바', 'review_content': '달지 않고 자극적이지 않아요.그렇다고 견과류가 듬푹 들어가서  건강해지는 만도 아니고 가격만큼..딱 그 정도에요~', 'answer': '괜찮아요'}

{'prod_name': '힘내바 초코 스니커즈, 40g, 12개', 'user_name': '윤*숙', 'rating': 5, 'headline': '맛있어요', 'review_content': '할인 하길래 몇번째 재 구매인지는생각 안나지만 너무 맛있어서 주문 했어요초코바중 덜달고 맛있게 달고 바싹하니 식감이 좋아요', 'answer': '예상보다 맛있어요'}

파일 저장완료!

/Users/jaehyolee/PycharmProjects/pythonProject/02_크롤링 프로젝트(Class)/55_쿠팡 상품리뷰 크롤링/쿠팡-상품리뷰-크롤링/힘내바 초코 스니커즈, 40g, 12개.xlsx
```

<br>

> ## 출력 결과 | Excel

![image](https://github.com/JaehyoJJAng/githubio.comment/assets/91415701/050415c6-2320-4d01-8d34-abb5358a314c)

***

> ## 해당 프로그램을 상업적인 목적으로 이용하여 생기는 불이익은 프로그램 사용자에게 있습니다
