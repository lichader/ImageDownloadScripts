import re
import urllib
import urllib2
 
def getHtmlCode(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    page = urllib2.urlopen(req)
    htmlCode = page.read()
    return htmlCode
 
def DownloadImgToCurrentDirectory(htmlCode, counter):
    regularExpression = r'src="http://www.yac8.com/upFiles/yac801/(.+?\.jpg)"'
    imgRe = re.compile(regularExpression)
    
    # should only have one
    allImagesSource = imgRe.findall(htmlCode)

    for imgURL in allImagesSource:
        fullImgUrl = "http://www.yac8.com/upFiles/yac801/" + imgURL
        req = urllib2.Request(fullImgUrl, headers={'User-Agent' : "Magic Browser"}) 
        imgFile = urllib2.urlopen(req);
        output = open('%s.jpg' % counter, 'wb')
        output.write(imgFile.read())
        output.close    
    
baseURL = "http://www.yac8.com/news/10344"

for x in range (2, 187):
    print baseURL + "_%s.html" % x
    htmlCode = getHtmlCode(baseURL + "_%s.html" % x)
    DownloadImgToCurrentDirectory(html, x)

