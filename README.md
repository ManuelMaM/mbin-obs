# Mix binary obfuscation tool

Obfuscate -> Binary code into ipv4 / ipv6 / mac / uuid adresses <-

Instalation: `pip3 install mbinobs` or cHlone repo and run `pip3 install .`

Command line usage : `python3 -m mbinobs binary.bin ipv4/ipv6/mac/uuid`

Exemple :
```
3m@ss:~/IPfuscation$ echo 'qwertyuiopasdfghjkl123456789' > test.bin

Binary encoded as ipv4:
['113.119.101.114', '116.121.117.105', '111.112.97.115', '100.102.103.104', '106.107.108.49',
'50.51.52.53', '54.55.56.57', '10.0.0.0']

Binary encoded as ipv6:
['7177:6572:7479:7569:6f70:6173:6466:6768', '6a6b:6c31:3233:3435:3637:3839:0a00:0000']

Binary encoded as mac:
['71:77:65:72:74:79', '75:69:6f:70:61:73', '64:66:67:68:6a:6b', '6c:31:32:33:34:35', '36:37:38:39:0a:00']

Binary encoded as uuid:
['71776572-7479-7569-6f70-617364666768', '6a6b6c31-3233-3435-3637-38390a000000']
```

You can also import the encoding functions:
```python
from mbinobs import *

bfile = open('path_to_file','rb') # Use read bytes option ('rb')

uuid_list = uuid._encode(bfile)
ipv6_list = ipv6._encode(bfile)
ipv4_list = ipv6._encode(bfile)
mac_list = mac._encode(bfile)
```
You could use [RtlIpv6StringToAddressA](https://docs.microsoft.com/en-us/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressa "IPV6")
 or [RtlIpv4StringToAddressA](https://docs.microsoft.com/en-us/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressa "IPV4") and similar apis calls to convert those ASCII text to binary code.

Used by [Hive ransomware gang](https://www.sentinelone.com/blog/hive-ransomware-deploys-novel-ipfuscation-technique/) to encode shellcode payloads.
