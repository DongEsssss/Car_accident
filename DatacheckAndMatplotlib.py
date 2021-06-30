import pandas as pd               # pandas 패키지를 pd라는 이름으로 사용한다
import matplotlib.pyplot as plt   # matplotlib 패키지를 plt라는 이름으로 사용한다
from datetime import date
from matplotlib import font_manager, rc

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
#한글이 깨지기 때문에 나눔폰트를 설치하였습니다.

plt.rc('font', family='NanumBarunGothic') #폰트를 나눔바른고딕체로 바꿔줬습니다.

accident_df = pd.read_csv('total.csv', encoding='euc-kr')
#encoding='euc-kr' csv파일 안에 한글이 있을때 넣어주는 명렁어 입니다.
accident_df

#불러온 csv파일에 행과 열의 크기를 확인
accident_df.shape

# 불러온 csv파일에 정보를 확인
accident_df.info()

#데이터 프레임에 대한 설명
accident_df.describe

#columns 조회
accident_df[0:0]

#row 조회
accident_df.loc[0::]

 # 날짜별로 데이터 추출
accident_df[['year','date','dayandnight','msday']]

# 사고로 인해 생긴 사망자 중상자 부상자 데이터 추출
accident_df[['map']]

# 사고로 인한 사망자 중상자 경상자
accident_df[['death','jungsang','gyeongsang']]

# 사고의 종류와 유형 데이터 추출
accident_df[['menu','accidenttype']]

# 사고의 도로 종류
accident_df[['roadtype']]

#첫 번째 사망교통사고가 일어난 연도에 대해 데이터를 추출하고 시각화 하기

#데이터를 그룹화하기
year_data = accident_df.groupby(['year']).count()
year= year_data.iloc[:,0]
year_data

accident_df['year'].value_counts()

# year 데이터 시각화
plt.figure(figsize=(20,10))
plt.bar(year.index, year, color='b', alpha=0.7)
plt.title('연도별 교통사고의 수',fontsize=20)
plt.xlabel("연도별",fontsize=15)
plt.ylabel("사망교통사고 건 수",fontsize=15)
plt.show()
