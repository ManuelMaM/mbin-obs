# IPfuscation

Obfuscate -> Binary code into ipv4 or ipv6 adress <-

Usage : `python3 ip-obs.py binary.bin ipv4/ipv6`


Exemple :
```
3m@ss:~/IPfuscation$ echo 'qwertyuiopasdfghjkl123456789' > test.bin
3m@ss:~/IPfuscation$ python3 ip-obs.py test.bin ipv4
['113.119.101.114', '116.121.117.105', '111.112.97.115', '100.102.103.104', '106.107.108.49',
'50.51.52.53', '54.55.56.57', '10.0.0.0']
3m@ss:~/IPfuscation$ python3 ip-obs.py test.bin ipv6
['7177:6572:7479:7569:6f70:6173:6466:6768', '6a6b:6c31:3233:3435:3637:3839:0a00:0000']
```

You could use [RtlIpv6StringToAddressA](https://docs.microsoft.com/en-us/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressa "IPV6")
 or [RtlIpv4StringToAddressA](https://docs.microsoft.com/en-us/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressa "IPV4") to convert those ASCII text to binary code.

Used by [Hive ransomware gang](https://www.sentinelone.com/blog/hive-ransomware-deploys-novel-ipfuscation-technique/) to encode shellcode payloads.
