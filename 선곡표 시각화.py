import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# ✅ tkinter 창 숨기기 (배경창 안 보이게)
root = tk.Tk()
root.withdraw()

# ✅ 탐색기에서 엑셀 파일 선택
file_path = filedialog.askopenfilename(
    title="CBS 선곡표 엑셀 파일 선택",
    filetypes=[("Excel Files", "*.xlsx *.xls")]
)

if not file_path:
    print("❗ 파일을 선택하지 않았습니다. 프로그램을 종료합니다.")
    exit()

# ✅ 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ✅ 엑셀 불러오기
df = pd.read_excel(file_path)

# ✅ 가수별 등장 횟수 집계
artist_count = df['이름'].value_counts().head(10)

# ✅ 그래프 그리기
plt.figure(figsize=(10, 6))
artist_count.plot(kind='bar', color='skyblue')
plt.title("🎙️ CBS 선곡표 – 가장 많이 등장한 가수 TOP 10")
plt.xlabel("가수")
plt.ylabel("등장 횟수")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# ✅ 파일명에서 날짜 부분 추출해서 저장 파일명 만들기
filename = file_path.split('/')[-1].replace('.xlsx', '')
output_img = f"{filename}_TOP10.png"

plt.savefig(output_img)
plt.show()

print(f"✅ 그래프 저장 완료: {output_img}")
