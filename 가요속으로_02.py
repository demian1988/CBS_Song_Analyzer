import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# ✅ 시작일과 종료일 입력 받기
start_date_input = input("시작 날짜를 입력하세요 (예: 2025-04-14): ").strip()
end_date_input = input("종료 날짜를 입력하세요 (예: 2025-04-16): ").strip()
start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
end_date = datetime.strptime(end_date_input, "%Y-%m-%d")

data = []
header = {'User-agent' : 'Mozila/2.0'}

# ✅ 날짜 반복
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    print(f"📅 수집 중: {date_str}")
    response = requests.get(f"https://www.cbs.co.kr/program/playlist/cbs_P000011?date={date_str}&sign=+", headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select(".article")

    for item in items:
        category = item.select_one(".title")
        name = item.select_one(".name")
        if category and name:
            print(category.text.strip(), name.text.strip())    
            data.append([date_str, category.text.strip(), name.text.strip()])
    
    current_date += timedelta(days=1)

# ✅ 데이터프레임 생성 및 엑셀 저장
if data:
    df = pd.DataFrame(data, columns=['날짜', '카테고리', '이름'])
    df.to_excel(f"cbs_김현주_선곡표_{start_date_input}_to_{end_date_input}.xlsx", index=False)
    print(f"\n🎉 저장 완료 ▶ 총 {len(df)}건")
else:
    print("❗ 수집된 데이터가 없습니다.")
