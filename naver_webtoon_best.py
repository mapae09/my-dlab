import requests
from bs4 import BeautifulSoup


def get_best_challenge50(_url):
    top50=[]

    for page in range(1,4):
        url = _url + "&page=" + str(page)
        res=requests.get(url)
        soup=BeautifulSoup(res.text,'lxml')

        webtoons=soup.select(".challengeList td>.challengeInfo>.challengeTitle")
        titles=[w.text for w in webtoons]
        titles=[t.replace('/n','') for t in titles]
        titles=[t.strip() for t in titles]

        scores=soup.select(".challengeList td>.challengeInfo>.rating_type>strong")
        scores=[float(s.text) for s in scores]

        images = soup.select(".challengeList td>.fl img")
        images = [img['src'] for img in images]

        info=list(zip(images, titles, scores))
        top50+=info

    return top50[:50]

if __name__ == "__main__":
    view_count_url = "https://comic.naver.com/genre/bestChallenge?m=main&order=ViewCount"
    star_score_url = "https://comic.naver.com/genre/bestChallenge?m=main&order=StarScore"

    view_count50=get_best_challenge50(view_count_url)
    star_score50=get_best_challenge50(star_score_url)



    view_count50_order_score=sorted(view_count50,key=lambda x:x[1],reverse=True)
    #print(view_count50_order_score)
    #print(star_score50)

    view_score_50 = set(view_count50) & set(star_score50)
    #print(len(view_score_50))
    #print(view_score_50)

    view_score_50=[(w,view_count50.index(w)+1,star_score50.index(w)+1)for w in view_score_50]
    view_score_50=sorted(view_score_50,key=lambda x:x[1] ,reverse=False)
    #print(view_score_50)

    view_score_title=['웹툰','조회순위','별점순위']
    view_score_50=[{k:v for k,v in zip(view_score_title,w)} for w in view_score_50]
    print(view_score_50)