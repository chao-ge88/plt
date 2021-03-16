import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/88.0.4324.190 Safari/537.36'
    }
url = 'https://p4psearch.1688.com/p4p114/p4psearch/offer2.htm?keywords=%B0%A2%C0%EF%B0%CD%B0%CD%CD%F8&cosite=baidujj&location=landing_t4&trackid=885688131303142701156617&keywordid=92442192198&format=normal&adposition=cl1&pagenum=1&creative=36905872585&matchtype=1&bd_vid=10923202055747134823?'
res = requests.get(url, headers=headers).text
print(res)