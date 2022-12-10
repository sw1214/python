import json,os

def myself(x):
    return x[1]


files_list = []
for _,_,files in os.walk("year"):
    files_list.append(files)
print(files_list[0])


for i in files_list[0]:
    url = "year/" + i
    with open(url,'r',encoding='utf-8') as wp:
        json_data = json.load(wp)
    returncode,returndata = json_data.items()
    returndata = myself(returndata)
    datanodes,_,_,wdnodes = returndata.items()
    datanodes = myself(datanodes)
    wdnodes = myself(wdnodes)
    for i in datanodes:
        code,data,_ = i.items()
        code = myself(code)
        data = myself(data)
        code_finish = (code.split('.')[1]).split('_')[0]
        time_finish = (code.split('.')[2])
        data_finish = data.get('strdata')
        # print(code_finish,data_finish,time_finish)
        nodes = wdnodes[0].get("nodes")
    for j in nodes:
        cname,code,_,_,_,_,_,_,_,_,_ = j.items()
        cname = myself(cname)
        code = myself(code)
        # print(cname,code)
        finish = "中文名:"+cname+"编号:" + code_finish + "时间:" + time_finish + "数据:" + data_finish
        print(finish)













"""
 datanodes -> 具体id所表达的具体时间r下的具体数据数值
 wdnodes -> 具体id所表达的中文名称
x.returndata.datanodes
x.returndata.wdnodes
"""

""" datanodes: 

    for i in x.returndata.datanodes:
        # i.code -> id + time i.data.strdata -> value 
        i.code
            i.code: 'zb.A060101_sj.202210' 
            code_index = (str(i.code).split('.')[1]).split('_')[0]
            code_time = str(i.code).split('.')[2]
        i.data.strdata

"""