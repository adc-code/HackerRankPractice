from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print (tag)
        for elem in attrs:
            print ('->', elem[0], '>', elem[1])
            
    def handle_endtag(self, tag):
        pass #print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for elem in attrs:
            print ('->', elem[0], '>', elem[1])

lineCount = int(input())            

MyParser = MyHTMLParser()

for _ in range (lineCount):
    MyParser.feed ( input().strip() )


