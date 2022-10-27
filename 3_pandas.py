# 판다스로 통계데이터 다루기

import pandas as pd 

df = pd.read_csv('survey.csv')

# print(df)  # 데이터 프레임 출력
# print(df.head())  # 처음 5개 행만 출력

# print(df.income.mean())  # 평균 구하기, 각 인덱스의 데이터들의 평균을 구한다.

# 데이터의 기초통계량 보기, describe()
result = df.describe()
print(result)

# 빈도분석, value_counts(), df.변수.value_counts() 형태로 변수가 몇번 나오는지 센다.
count = df.sex.value_counts()  # sex 인덱스열에서 m,f의 숫자를 센다.
print(count)

# 집단 평균 구하기 , groupby()
group = df.groupby(df.sex).mean()  # sex 구분으로 m,f 그룹의 평균값을 구한다.
print(group)

