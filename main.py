import os 
import pandas as pd
path = '.'
dirs = os.listdir(path)
cnt = 0
sheet = 'Ответы на форму (1)'
df_total = pd.DataFrame()
excels = []
dirs.sort()
for item in dirs:
	if os.path.isdir(item):
		files = os.listdir(path+'/'+item)
		for file in files:
			if file.endswith('xlsx') and file.find("администр")!=-1:
				file_name = path+'/'+item+'/'+file
				excels.append(pd.ExcelFile(file_name))
				# df = pd.read_excel(io=file_name, sheet_name=sheet)
				# df_total = df_total.append(df)

frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]
frames[1:] = [df[1:] for df in frames[1:]]
combined = pd.concat(frames)
combined.to_excel("Анкета_администрация.xlsx", header=False, index=False)
# df_total.to_excel('combined_files.xlsx', header=False, index=False)