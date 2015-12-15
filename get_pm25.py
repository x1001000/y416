import urllib2
import re

page_html = urllib2.urlopen('http://taqm.epa.gov.tw/pm25/tw/default.aspx').readlines()
#print page_html

for line in page_html:
    match = re.search('ctl14_gv_ctl03_lab1..(..)', line)
    if match:
        data_to_display = match.group(1)
        print data_to_display
        break
    data_to_display = 'OOPS'
    #print data_to_display