import requests,json
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Cookie':'_trs_uv=lb24v679_6_37zx; wzws_sessionid=gWE4MThhYqBjkV/IgDEyMy4xMTkuMjMyLjU3gmZjNWVlMQ==; JSESSIONID=Tl3v3hYXivr5HqUZqbGUi7dyfS1nx-0b5ZYmGiDkf3XhRbC56Vqj!430577256; u=1'
    }
file_save_url = ["month","year"]
web_data_url = ["月度","年度"]

for flag in range(0,2):

    df = pd.read_excel("url.xlsx",sheet_name=web_data_url[flag])
    df_url = df['url']
    df_kind = df['类别']
    for i in range(1,len(df)):
        if df_url[i] == "None":
            continue
        url = df_url[i]
        response = requests.get(url=url,headers=headers,verify=False)
        response.encoding = response.apparent_encoding
        x = response.json()
        file_url = file_save_url[flag] +"/"+ df_kind[i]
        with open(file_url, 'w', encoding='utf-8') as f:
            f.write(json.dumps(x, ensure_ascii=False))

