# pandas 롤 데이터 프레임을 이용해보자

import pandas as pd

df = pd.read_csv('apt.csv', encoding='cp949')

# print(df)
# print(len(df))
# print(df.head())  # 처음 5행의 데이터만 출력
# print()
# print(df.tail())  # 마지막 5행의 데이터만 출력

# print(df.지역)  # 헤더가 '지역'인 열의 데이터만 출력
# print(df['가격'])  # 헤더가 '가격'인 열의 데이터만 출력
# #print(df.면적>130)  # 면적이 130을 넘는지 여부를 True, False로 보여준다.
# print(df[df.면적>130])  # 면적이 130을 넘는 아파트의 정보를 모두 보여준다.
# print(df.가격[(df.면적>130)&(df.가격<15000)])  # 면적이 130 초과 하면서 가격은 1억5천 미만인 곳의 가격

# 특정 조건을 만족하는 데이터를 추출하기
# loc()를 사용한다.
# # loc[행의조건,열의조건]
# df_1 = df.loc[:,['아파트','가격']]
# print(df_1)  # 데이터의 전행에서 '아파트', '가격'에 해당하는 열만 추출

print(df.loc[:,['아파트','가격']][df.가격 < 15000])  # 가격이 15000 미만인 아파트의 이름과 가격을 출력