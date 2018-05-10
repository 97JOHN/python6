import urllib.request
import re
dStr = urllib.request.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
getdStr=dStr.decode()
#在 python3 中 urllib.read()返回 bytes 对象而非 str，语句功能是将 dStr 转换成 str
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', getdStr)
if m:
    print(m)
    print('\n')
    print (len(m))
else:
    print ('not match')