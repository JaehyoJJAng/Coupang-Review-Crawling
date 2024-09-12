# Coupang-Review-Crawling

파이썬을 이용한 쿠팡 리뷰 크롤링 프로그램

<br>

## 설치 | Installation

```
$ git clone https://github.com/JaehyoJJAng/Coupang-Review-Crawling.git
$ cd Coupang-Review-Crawling
$ pip install -r ./requirements.txt
```

<br>

## 사용방법 | Usage

**How to use**  
```
$ python3 main.py
```

<br>

Enter the URL of the product you want.

<img width="1417" alt="image" src="https://user-images.githubusercontent.com/91415701/197674856-31baa0b0-90b6-4cf9-9f3b-d5039ddc62ca.png">  

```shell
원하시는 상품의 URL 주소를 입력해주세요

Ex)
https://www.coupang.com/vp/products/7335597976?itemId=18741704367&vendorItemId=85873964906&q=%ED%9E%98%EB%82%B4%EB%B0%94+%EC%B4%88%EC%BD%94+%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&itemsCount=36&searchId=0c5c84d537bc41d1885266961d853179&rank=2&isAddedCart=

:
```

<br>

***

## 출력 결과 | Print

```
[INFO] Start crawling page 1 ...

...
...
...
...

[INFO] Start crawling page 5 ...

{'title': '마니커 생닭(16호) 국내산 당일생산, 1550g, 2개', 'prod_name': '마니커 생닭(16호) 국내산 당일생산, 4개, 1550g', 'review_date': '2024.03.13', 'user_name': 'Bha****** ******', 'rating': 5, 'headline': '등록된 헤드라인이 없습니다', 'review_content': '등록된 리뷰내용이 없습니다', 'answer': '맛 평가 없음'}

{'title': '마니커 생닭(16호) 국내산 당일생산, 1550g, 2개', 'prod_name': '마니커 생닭(16호) 국내산 당일생산, 4개, 1550g', 'review_date': '2024.03.06', 'user_name': 'Bre*** ****', 'rating': 5, 'headline': '등록된 헤드라인이 없습니다', 'review_content': '등록된 리뷰내용 이 없습니다', 'answer': '맛 평가 없음'}

{'title': '마니커 생닭(16호) 국내산 당일생산, 1550g, 2개', 'prod_name': '마니커 생닭(16호) 국내산 당일생산, 4개, 1550g', 'review_date': '2024.02.23', 'user_name': 'Sha* **** ***', 'rating': 5, 'headline': '등록된 헤드라인이 없습니다', 'review_content': '등록된 리뷰내 용이 없습니다', 'answer': '맛 평가 없음'}
```

<br>

## 출력 결과 | Excel

![image](https://github.com/JaehyoJJAng/githubio.comment/assets/91415701/050415c6-2320-4d01-8d34-abb5358a314c)

***

# 🔥 Notice

**해당 프로그램을 상업적인 목적으로 이용하여 생기는 불이익은 프로그램 사용자에게 있습니다**