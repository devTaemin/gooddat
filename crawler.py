from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def driver(urlLink):
    print("URL transmission complete.")
    textList = [["너무 빨라요!"], ["색깔이 너무 예뻐요"]]
    return textList


def flyday(url):
    '''
    우선 주소 specific하게 정의된 함수를 사용하였다.
    또한 해당 홈페이지 내에 iframe tag에 있는 html에 접근하였다는 가정하에 코드를 짰다.
    더 붙여야하는 코드:
        -url 받으면 댓글 몇 개 있는지 확인하고 몇 번 돌릴지 확인하는 함수.
        -이에 따라 page=의 인덱스 찾아 url내용 바꿔주는 코드
    '''
    textfile=open('comment.txt','w')
    for i in range(1,249):
        url=urlopen("http://widgets2.cre.ma/flyday.co.kr/products/reviews?app=0&iframe=1&iframe_id=crema-product-reviews-1&page="+str(i)+"&parent_url=http%3A%2F%2Fwww.flyday.co.kr%2Fshop%2Fshopdetail.html%3Fbranduid%3D1115007%26xcode%3D018%26mcode%3D001%26scode%3D%26sort%3Dorder%26cur_code%3D018001%26ref%3Dwmobi&product_code=1115007&widget_env=100")
        obj=soup(url,"html.parser")
        
        comm=obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"widget_reviews__body products_reviews_list__body"}).find('div',{"class":"page"}).find('ul',{"class":"reviews reviews-product"}).find_all('li',{"class":"review products_reviews_list_review product_review__container "})
        
        for j in comm:
            comment=j.find('div',{"class":"products_reviews_list_review__inner"}).find('div',{"class":"products_reviews_list_review__lcontents"}).find('div',{"class":"products_reviews_list_review__content review_content "}).find('div',{"class":"products_reviews_list_review__message"}).find("div",{"class":"review_message review_message--collapsed review_message--collapsed3"}).text.strip()
            comment=comment.replace(" ","")
            textfile.write(comment+"\n")
            #print("page ",i," finished!")
    textfile.close()