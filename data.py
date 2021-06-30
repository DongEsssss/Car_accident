import requests
import csv

def acci_car_info(count, data):
  Api_Key='fNvxK%2FUyrQNf0idM7oR3xQuXiYlusJ32hafxCVzjKzrZEY48j4jdg5zoTPnsHrhgqQ5jmaHZVFELvdWUjdV4fA%3D%3D'
  url=f'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath?serviceKey=fNvxK%2FUyrQNf0idM7oR3xQuXiYlusJ32hafxCVzjKzrZEY48j4jdg5zoTPnsHrhgqQ5jmaHZVFELvdWUjdV4fA%3D%3D&searchYear=2019&siDo=1100&guGun=1117&type=json&numOfRows=10&pageNo=1'
  response = requests.get(url)
  print (response)
  return response
def accident_car_info(i,car):
  year = car['items']['item'][i]['acc_year']
  date = car['items']['item'][i]['occrrnc_dt']
  dayandnight = car['items']['item'][i]['dght_cd']
  msday = car['items']['item'][i]['occrrnc_day_cd']
  death = car['items']['item'][i]['dth_dnv_cnt']
  jungsang = car['items']['item'][i]['se_dnv_cnt']
  gyeongsang = car['items']['item'][i]['sl_dnv_cnt']
  map = car['items']['item'][i]['occrrnc_lc_sido_cd']
  menu = car['items']['item'][i]['acc_ty_cd']
  roadtype = car['items']['item'][i]['road_frm_lclas_cd']  
  accidenttype = car['items']['item'][i]['acc_ty_lclas_cd']
  return year,date,dayandnight,msday,death,jungsang,gyeongsang,map,menu,roadtype,accidenttype
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
    year,date,dayandnight,msday,death,jungsang,gyeongsang,map,menu,roadtype,accidenttype = accident_car_info(i, myjson)
    print("year : "+year + " / date : " + date + " / dayandnight " + dayandnight + " / msday "+msday  + " / death " + str(death)+ "명"+ " / jungsang " + str(jungsang) +"명"+" / gyeongsang : "+ str(gyeongsang)+"명"+" / map : "+map+" / menu : "+menu+" / roadtype : "+roadtype+" / accidenttype : "+accidenttype)

with open("total.csv".format(accident_car_info), "w", newline='') as csv_file:
    fieldnames = ['year','date','dayandnight','msday','death','jungsang','gyeongsang','map','menu','roadtype','accidenttype']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'year': year, 'date':  date, 'dayandnight':  dayandnight,'msday':  msday, 'death':death, 'jungsang':jungsang,  'gyeongsang':gyeongsang,  'map':map,  'menu':menu,  'roadtype':roadtype,'accidenttype':accidenttype })
