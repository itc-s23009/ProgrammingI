a = [ ['0001', 'Male', 'Yamada' , 'Tarou' , 25, 'Tokyo'], ['0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'Kanagawa'], ['0003' , 'Female', 'Tanake' , 'Yuko' , 25 , 'Saitama'], ['0004' , 'Male' , 'Suzuki'  , 'Ichirou' , 35 , 'HOkkaido'] ]


member_information = {}

for record in a:
    key = record[0]
    info = record[1:]
    member_information[key] = info



print('number', 'information', sep='\t')
for key, info in  member_information.items():
    print(key,info)
