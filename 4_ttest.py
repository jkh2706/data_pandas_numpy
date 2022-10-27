# 싸이파이 (Scipy)패키지로 t검정 하기
# t검정 : 두 집단의 분산을 알 수 없을때 두 집단이 t분포를 따른다고 가정하고 평균등을 검정하는 통계방법

import pandas as pd
from scipy import stats 


df = pd.read_csv('survey.csv')
male = df.income[df.sex == 'm']  # 인덱스가 sex 인 데이터가 'm'일경우 income 데이터 객체를 생성
female = df.income[df.sex == 'f'] # 인덱스가 sex 인 데이터가 'f'일경우 income 데이터 객체를 생성

# stats 모듈의 ttest_ind() 함수를 사용하면 t 검정을 쉽게 할 수 있음
result = stats.ttest_ind(male, female)
print(result)

'''
결과 해석
Ttest_indResult(statistic=-0.10650308143428425, pvalue=0.9161940781163369)
value 는 유의확률을 나타내며 그 값이 낮을 수록 유의한 차가 있다가 본다. 보통 0.05 나 0.01 미만의 값이 나오면 유의차가 있다고 본다.
여기서는 pvalue 가 0.91 로 높게 나오기때문에 두 집단사이의 수입에는 유의한 차이가 있다고 보기 어렵다.
'''