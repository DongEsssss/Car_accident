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

accident_df[['msday']]

#데이터를 그룹화하기
msday_data = accident_df.groupby(['msday']).count()
msday= msday_data.iloc[0,0]
msday_data

accident_df['msday'].value_counts()

# 요일이 섞여서 나와 따로 리스트를 만들어 표를 추출한 데이터를 시각화
df = pd.DataFrame()
plt.figure(figsize=(20,10))
df['days'] = ['월','화','수','목','금','토','일']   # 요일
df['num'] = [5033,4984,4837,4879,5123,5028,4261]    # 월부터 일까지의 사망교통사고 정보 데이터
plt.bar(df['days'],df['num'], color='b', alpha=0.7) # x축에는 요일 y축에는 요일별 사망교통사고 정보 데이터를 넣었습니다.
plt.title('요일별 사망교통사고 수',fontsize=20)    
plt.xlabel("요일별",fontsize=15)
plt.ylabel("사망교통사고 건 수",fontsize=15)
plt.show()

#4번째 사망교통사고 주야 비율

#데이터를 그룹화하기
dayandnight_data = accident_df.groupby(['dayandnight']).count()
dayandnight= dayandnight_data.iloc[:,:]
dayandnight_data

accident_df['dayandnight'].value_counts()

# dayandnight에 대한 데이터 그래프를 pie로 시각화
plt.figure(figsize=(10,10))
plt.title('사망교통사고 주야 비율' , fontsize=20)
plt.ylabel('주야 시간대' , fontsize=15)
accident_df['dayandnight'].value_counts().plot.pie(autopct = '%.2f%%' , colors = ['lightblue', 'orange'] ,  textprops = {'fontsize' : 12 , 'weight' : 'bold'})
plt.show()

#데이터를 그룹화하기
death_data = accident_df.groupby(['death']).count()
death= death_data.iloc[:,0]
death_data

accident_df['death'].value_counts()
#7하고 9가 없는데 이는 사망교통사고 한번에 7명,9명이 사망했다는 데이터가 없다는 것
