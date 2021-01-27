from django.shortcuts import render
from app.models import Survey
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')  

def Main(request):
    return render(request, 'main.html')

def SurveyView(request):
    return render(request, 'survey.html')

def SurveyProcess(request):
    InsertData(request)    # DB에 신규 데이터 저장
    
    rdata = list(Survey.objects.all().values()) # DB 데이터 읽기
    df, crossTbl, results = Analysis(rdata)     # 데이터 분석 

    # 시각화 결과 저장
    fig=plt.gcf()
    gender_group = df['co_survey'].groupby(df['coNum']).count()
    gender_group.index = ['스타벅스','커피빈','이디아','탐앤탐스']
    print('gender_group : ', gender_group)
    gender_group.plot.bar(subplots=True, color=["cyan","green"], width=0.5)
    plt.xlabel("커피사")
    plt.ylabel("선호 건수")
    plt.title("커피사별 선호 건수")
    fig.savefig('django_web/app/static/images/vbar.png')

    return render(request, 'list.html', {'crossTbl':crossTbl.to_html(), \
                                         'results':results, 'df':df.to_html(index=False)})

def InsertData(request):
    if request.method == 'POST':
        Survey(
            #rnum = len(list(Survey.objects.all().values())) + 1, #자동증가 칼럼이 아닌 경우
            gender = request.POST.get('gender'),
            age = request.POST.get('age'),
            co_survey = request.POST.get('co_survey'),
        ).save()    

import pandas as pd
import scipy.stats as stats

def Analysis(rdata):   # 분석을 위한 데이터 전처리
    print(type(rdata))
    df = pd.DataFrame(rdata)   
    df.dropna() 
    df['genNum'] = df['gender'].apply(lambda g: 1 if g == "남" else 2)
    df['coNum'] = df['co_survey'].apply(lambda c: 1 if c=='스타벅스' else 2 if c=='커피빈' else 3 if c=='이디야' else 4)
    #Cross Table(교차분할표) 생성
    crossTbl = pd.crosstab(index=df['gender'], columns=df['co_survey'])
    #print(crossTbl)
    
    #카이제곱검정분석
    st, pv, _, _ = stats.chi2_contingency(crossTbl)  #위와 결과 동일
    if(pv >= 0.05): 
        results = "p값이 {0}이므로 0.05 <b>이상</b>이므로 <br>성별에 따라 선호 커피브랜드에는 <b>차이가 없다(귀무가설 채택)</b>".format(pv)
    else: 
        results = "p값이 {0}이므로 0.05 <b>이하</b>이므로 <br>성별에 따라 선호 커피브랜드에는 <b>차이가 있다(대립가설 채택)</b>".format(pv)
    
    return df, crossTbl, results