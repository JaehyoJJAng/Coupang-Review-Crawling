from bs4 import BeautifulSoup as bs
from pathlib import Path
from typing import Optional,Union,Dict,List
from openpyxl import Workbook
import time
import os
import re
import requests as rq
import json

def get_headers(
    key: str,
    default_value: Optional[str] = None
    )-> Dict[str,Dict[str,str]]:
    """ Get Headers """
    JSON_FILE : str = 'json/headers.json'

    with open(JSON_FILE,'r',encoding='UTF-8') as file:
        headers : Dict[str,Dict[str,str]] = json.loads(file.read())

    try :
        return headers[key]
    except:
        if default_value:
            return default_value
        raise EnvironmentError(f'Set the {key}')

class Coupang:
    @staticmethod
    def get_product_code(url: str)-> str:
        """ 입력받은 URL 주소의 PRODUCT CODE 추출하는 메소드 """
        prod_code : str = url.split('products/')[-1].split('?')[0]
        return prod_code

    def __init__(self)-> None:
        self.__headers : Dict[str,str] = get_headers(key='headers')

    def main(self)-> List[List[Dict[str,Union[str,int]]]]:
        # URL 주소
        URL : str = self.input_review_url()

        # URL의 Product Code 추출
        prod_code : str = self.get_product_code(url=URL)

        # URL 주소 재가공
        URLS : List[str] = [f'https://www.coupang.com/vp/product/reviews?productId={prod_code}&page={page}&size=5&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=3&ratingSummary=true' for page in range(1,self.input_page_count() + 1)]

        # __headers에 referer 키 추가
        self.__headers['referer'] = URL

        with rq.Session() as session:
            return [self.fetch(url=url,session=session) for url in URLS]

    def fetch(self,url:str,session)-> List[Dict[str,Union[str,int]]]:
        save_data : List[Dict[str,Union[str,int]]] = list()

        with session.get(url=url,headers=self.__headers) as response :
            html = response.text
            soup = bs(html,'html.parser')

            # Article Boxes
            article_lenth = len(soup.select('article.sdp-review__article__list'))

            for idx in range(article_lenth):
                dict_data : Dict[str,Union[str,int]] = dict()
                articles = soup.select('article.sdp-review__article__list')

                # 구매자 이름
                user_name = articles[idx].select_one('span.sdp-review__article__list__info__user__name')
                if user_name == None or user_name.text == '':
                    user_name = '-'
                else:
                    user_name = user_name.text.strip()

                # 평점
                rating = articles[idx].select_one('div.sdp-review__article__list__info__product-info__star-orange')
                if rating == None:
                    rating = 0
                else :
                    rating = int(rating.attrs['data-rating'])

                # 구매자 상품명
                prod_name = articles[idx].select_one('div.sdp-review__article__list__info__product-info__name')
                if prod_name == None or prod_name.text == '':
                    prod_name = '-'
                else:
                    prod_name = prod_name.text.strip()

                # 헤드라인(타이틀)
                headline = articles[idx].select_one('div.sdp-review__article__list__headline')
                if headline == None or headline.text == '':
                    headline = '등록된 헤드라인이 없습니다'
                else:
                    headline = headline.text.strip()

                # 리뷰 내용
                review_content = articles[idx].select_one('div.sdp-review__article__list__review > div')
                if review_content == None :
                    review_content = '등록된 리뷰내용이 없습니다'
                else:
                    review_content = re.sub('[\n\t]','',review_content.text.strip())

                # 맛 만족도
                answer = articles[idx].select_one('span.sdp-review__article__list__survey__row__answer')
                if answer == None or answer.text == '':
                    answer = '맛 평가 없음'
                else:
                    answer = answer.text.strip()

                dict_data['prod_name'] = prod_name
                dict_data['user_name'] = user_name
                dict_data['rating'] = rating
                dict_data['headline'] = headline
                dict_data['review_content'] = review_content
                dict_data['answer'] = answer

                save_data.append(dict_data)

                print(dict_data , '\n')

            time.sleep(1)

            return save_data
    
    @staticmethod
    def clear_console() -> None:
        command: str = 'clear'
        if os.name in ('nt','dos'):
            command = 'cls'
        os.system(command=command)

    def input_review_url(self)-> str:
        while True:
            self.clear_console()
            
            # Review URL
            review_url : str = input('원하시는 상품의 URL 주소를 입력해주세요\n\nEx)\nhttps://www.coupang.com/vp/products/7335597976?itemId=18741704367&vendorItemId=85873964906&q=%ED%9E%98%EB%82%B4%EB%B0%94+%EC%B4%88%EC%BD%94+%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&itemsCount=36&searchId=0c5c84d537bc41d1885266961d853179&rank=2&isAddedCart=\n\n:')
            if not review_url :
                # Window
                os.system('cls')
                # Mac
                #os.system('clear')
                print('URL 주소가 입력되지 않았습니다')
                continue
            return review_url

    def input_page_count(self)-> int:
        self.clear_console()

        while True:
            page_count : str = input('페이지 수를 입력하세요\n\n:')
            if not page_count:
                print('페이지 수가 입력되지 않았습니다\n')
                continue

            return int(page_count)

class OpenPyXL:
    @staticmethod
    def save_file()-> None:
        # 크롤링 결과
        results : List[List[Dict[str,Union[str,int]]]] = Coupang().main()

        wb = Workbook()
        ws = wb.active
        ws.append(['상품명','구매자 이름','구매자 평점','리뷰 제목','리뷰 내용','맛 만족도'])

        row = 2

        for x in results:
            for result in x :
                ws[f'A{row}'] = result['prod_name']
                ws[f'B{row}'] = result['user_name']
                ws[f'C{row}'] = result['rating']
                ws[f'D{row}'] = result['headline']
                ws[f'E{row}'] = result['review_content']
                ws[f'F{row}'] = result['answer']

                row += 1

        savePath : str = os.path.abspath('쿠팡-상품리뷰-크롤링')
        fileName : str = results[0][0]['prod_name'] + '.xlsx'

        if not os.path.exists(savePath):
            os.mkdir(savePath)

        wb.save(os.path.join(savePath,fileName))
        wb.close()

        print(f'파일 저장완료!\n\n{os.path.join(savePath,fileName)}')
