import json,os,xlwt


files_list = []
for _,_,files in os.walk("year"):
    files_list.append(files)
for file_name in files_list[0]:
    url = "year/" + file_name
    with open(url,'r',encoding='utf-8') as wp:
        json_data = json.load(wp)
    datanodes = json_data.get('returndata').get("datanodes")
    wdnodes = json_data.get('returndata').get("wdnodes")
    datanodes_collect_list = []
    wdnodes_collect_list = []
    final_value_list = []
    for i in datanodes:
        code = i.get("code")
        data = i.get("data")
        code_finish = (code.split('.')[1]).split('_')[0]
        time_finish = (code.split('.')[2])
        data_finish = data.get('strdata')
        value = [code_finish,data_finish,time_finish]
        datanodes_collect_list.append(value)
    for i in wdnodes[0].get("nodes"):
        value = [i.get("cname"),i.get("code")]
        wdnodes_collect_list.append(value)
    # print(datanodes_collect_list,wdnodes_collect_list)

    for i in wdnodes_collect_list:
        for j in datanodes_collect_list:
            if j[0] in i[1]:
                value = [j[0],j[1],j[2],i[0]]
                final_value_list.append(value)
    print(final_value_list)
    print("======================================")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('sheetname', cell_overwrite_ok=True)
    col = ('id', 'value', 'time', 'label')
    for i in range(0, 4):
        sheet.write(0, i, col[i])
    for i in range(0, len(final_value_list)):
        data = final_value_list[i]
        for j in range(0, 4):
            sheet.write(i + 1, j, data[j])
    url = "year_excel/" + file_name + ".xls"
    book.save(url)

