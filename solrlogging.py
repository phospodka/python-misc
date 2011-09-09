# Utility module that can run stand alone.  Intended to be used as a way to 
# programmatically set the log levels for Apache Solr via Solr's own logging
# console Web page.
#
# Copyright 2011 Peter Hospodka
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import urllib, urllib2, cookielib, getopt, sys

# Process my Web Forms
class WebForm:
    def __init__(self):
    pass

def opener(self, ref):
    """Creats an opener to store cookies,
    and keep a referer to the site
    Added user-agent to spoof browser"""
    self.reference = ref
    cj = cookielib.CookieJar()
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    self.opener.addheaders.append(("User-agent", "Mozilla/4.0"))
    self.opener.addheaders.append(("Referer", ref))

    return self.opener

def GET(self, opnr, url):
    getReq = opnr.open(url)

    return getReq.read()

def POST(self, opnr, url, data):
    enData = urllib.urlencode(data)
    getReq = opnr.open(url, enData)

    return getReq.read()
# end class WebForm

# Do my main processing
def main(argv):
    #Get the arguments
    try:
        opts, args = getopt.getopt(argv, "f:ghu:v:", ["file=", "generate", "help", "urls=", "valuepairs="])
    except getopt.GetoptErrot:
        usage()
        sys.exit(2)

    #init the urls list and values dict
    urls = []
    values = {"submit":"set"}

    #Proccess the args
    for opt, arg in opts:
        if opt in ("-f", "--file"):
            list = readFile(arg)
            urls = list[0]
            values = genParings(list[1], values)
        elif opt in ("-g", "--generate"):
            print "-g Not Implemented"
            sys.exit(3)
        elif opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif opt in ("-u", "--urls"):
            print "-u Not Implemented"
            sys.exit(3)
        elif opt in ("-v", "--valuepairs"):
            print "-v Not Implemented"
            sys.exit(3)

    #Go through each URL and submit the same logging values for each
    for url in urls:
        print "Accessing url: " + url + " for values: " 
        print values
        s = WebForm()

        postData = urllib.urlencode(values)

        urlOpen = s.opener(url)
        request = s.POST(urlOPen, url, values)

        #Surpurfulous
        f = open("test.txt", "w")
        f.write(request)
# end main(argv)

# Generate my value parings
def genParings(list, parings):
    for entry in list:
        pairs = entry.split(":")
        parings[pairs[0]] = pairs[1]

    return parings
# end genParings(list, parings)

# Read my file for contents
# Not the coolest nor fault tolerant approach, but only requires one pass
def readFile(fileName):
    print "Reading file: " + fileName
    file = open(fileName, "r")
    addToUrls = False
    addToParings = False
    urls = []
    parings = []

    #Process the lines in the file
    for line in lines:
        line = line.strip(" \n\r\t")
        if line.lower() == "#url list":
            addToUrls = True
        elif line.lower() == "#paring list":
            addToUrls = False
            addToParings = True
        elif addToUrls:
            urls.append(line)
        elif addToParings:
            parings.append(line)

    list = [urls, parings]

    return list
# end readFile(fileName)

# Tell me my usage
def usage():
    print "Solr Logging Utility Usage: All your logging are belong to us!"
    print ""
    print "\t-f [] or --file [] \t\tTakes a file path to use as input for processing"
    print "\t-g or -- generate \t\tGenerates a sample input file"
    print "\t-h or --help \t\t\tProvides usage help"
    print "\t-u [] or --urls [] \t\tTakes a list of URLs to submit logging actions to"
    print "\t-v [] or --valuepairs [] \tTakes a list of logging name : logging value parameters to submit"
# end usage()

# If I am myself, run the main program!
if __name__ == "__main__":
    main(sys.argv[1:])
# end if self!