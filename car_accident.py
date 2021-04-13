import requests

def acci_car_info(count, data):
  Api_Key ='fNvxK%2FUyrQNf0idM7oR3xQuXiYlusJ32hafxCVzjKzrZEY48j4jdg5zoTPnsHrhgqQ5jmaHZVFELvdWUjdV4fA%3D%3D'
  url = f'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath?serviceKey=fNvxK%2FUyrQNf0idM7oR3xQuXiYlusJ32hafxCVzjKzrZEY48j4jdg5zoTPnsHrhgqQ5jmaHZVFELvdWUjdV4fA%3D%3D&searchYear=2019&siDo=1100&guGun=1117&type=json&numOfRows=10&pageNo=1'

  response = requests.get(url)
  print (response)
  return response

def accident_car_info(i,car):
  map = car['items']['item'][i]['occrrnc_lc_sido_cd']
  where = car['items']['item'][i]['occrrnc_lc_sgg_cd']
  year = car['items']['item'][i]['acc_year']
  date = car['items']['item'][i]['occrrnc_dt']
  death = car['items']['item'][i]['dth_dnv_cnt']
  busang = car['items']['item'][i]['injpsn_cnt']
  jungsang = car['items']['item'][i]['se_dnv_cnt']
  gyeongsang = car['items']['item'][i]['sl_dnv_cnt']
  menu = car['items']['item'][i]['acc_ty_cd']

  return map,where,year,date,death,busang,jungsang,gyeongsang,menu

def accident_car_total(car):
  total = car['items']['item']['total_Count']
  return total

def in_accident_car(data,count):
  result = acci_car_info(count,year)
  result = result.content.decode('utf-8')
  print(result)
  return result

import json

if __name__ == '__main__':

  year =2019
  count = 10
  result = in_accident_car(count,year)
  myjson = json.loads(result)

  for i in range(count):
    map,where,year,date,death,busang,jungsang,gyeongsang,menu = accident_car_info(i, myjson)
    patients = abs(int(busang)+int(jungsang)+int(gyeongsang))
    print("위치 코드 : "+map + " / 지역 코드 : " + where + " / 연도 : " + year + " / 정확한 날짜 " + date+" / 사망자 : "+ str(death)+"명"+" / 부상자 : "+str(busang)+"명"+" / 중상자 : "+str(jungsang)+"명"+" / 경상자 : "+ str(gyeongsang)+"명"+" / 총합 환자수 : "+str(patients)+" / 사고 부류 코드 : "+menu)
