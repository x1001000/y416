import urllib2
import re

page_html = urllib2.urlopen('https://www.facebook.com/sungyuhua/photos/a.440928322702350.1073741825.440923442702838/757394714389041/?type=3&theater').readlines()
#print page_html
data_to_display = 'OOPS'
for line in page_html:
    match = re.search('(.),(...) \\\\u4eba\\\\u90fd\\\\u8aaa\\\\u8b9a\\\\u3002', line)
    if match:
        data_to_display = match.group(1) + match.group(2)
        print data_to_display
        break