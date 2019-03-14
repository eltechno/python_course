
import urllib.request
#warnings_uri='http://www.nws.noaa.gov/view/national.php?prod=SMW&sid=AKQ'
warnings_uri='https://forecast.weather.gov/product.php?site=CRH&product=FD3&issuedby=AK3'
with urllib.request.urlopen(warnings_uri) as source:
    warnings_text= source.read()
print(warnings_text[:80])

print(warnings_text)