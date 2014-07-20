#!/usr/local/bin

# 
# 

import sys, feedparser, nltk, random, time

def encode(bytes):
    try:
        text = bytes.encode('utf-8')
    except UnicodeEncodeError:
        try:
            text = bytes.encode('iso-8859-1')
        except UnicodeEncodeError:
            text = bytes.encode('cp1252')
    return text

    
# Gather our code in a main() function

def main():

  startProgram = time.clock()
  
  scrubbed, newHeadline, newWord, rawHeadline = '', '', '', ''
  rawHeadlines, headlines, wdt, wrb, wp, nn, nns, nnp, vbd, vbz, vbg, rd, rb, dt, inn, jj = [], \
  [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
  chosenHeadlineIndex = 0
  
  # ------------------
  # Retrieve feeds
  # ------------------
  
  print ''
  print '******************************************'
  print "Retrieving feeds"
  
  feeds = ['http://www.theglobeandmail.com/news/national/?service=rss','http://rss.cbc.ca/lineup/offbeat.xml','http://rss.cbc.ca/lineup/topstories.xml','http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml','http://www.thestar.com/feeds.topstories.rss','http://rss.cnn.com/rss/cnn_topstories.rss','http://feeds.reuters.com/Reuters/worldNews?format=xml','http://feeds.bbci.co.uk/news/rss.xml?edition=int', 'http://www.npr.org/rss/rss.php?id=1020','http://www.ft.com/rss/world/us/society','http://feeds2.feedburner.com/ft/the-world','http://www.forbes.com/real-time/feed2/','http://feeds.feedburner.com/haaretz/LBao']

  print "Parsing feeds"
  for i in feeds:
    d = feedparser.parse(i)
    for post in d.entries:
    
      scrubbed = post.title
      # remove string "VIDEO" from posts
      scrubbed = scrubbed.replace('VIDEO: ', '')

      headline = nltk.word_tokenize(scrubbed)
      pos = nltk.pos_tag(headline) 
      headlines = headlines + [pos]
      
      # Attempt to correct unicode errors
      scrubbedEncoded = scrubbed.encode('utf-8', 'replace')
      rawHeadlines.append(scrubbedEncoded)

  # -----------------------------------------------------------------
  # Populate POS tags from feeds
  # -----------------------------------------------------------------
      
  for i in headlines:
  # print "***** HEADLINE: *****"
  # print i
    for p in i:
      #print p 
      # Assemble lists of these POS tags:
      if p[1] == 'WDT':
        wdt.append(p[0])
      elif p[1] == 'WRB':  
        wrb.append(p[0])
      elif p[1] == 'WP':  
        wp.append(p[0])
      elif p[1] == 'NN':  
        nn.append(p[0])
      elif p[1] == 'NNS':  
        nns.append(p[0])
      elif p[1] == 'NNP':  
        nnp.append(p[0])
      elif p[1] == 'VBD':  
        vbd.append(p[0])
      elif p[1] == 'VBZ':  
        vbz.append(p[0])
      elif p[1] == 'VBG':  
        vbg.append(p[0])
      elif p[1] == 'RD':  
        rd.append(p[0])
      elif p[1] == 'RB':  
        rb.append(p[0])
      elif p[1] == 'DT':  
        dt.append(p[0])
      elif p[1] == 'IN':  
        inn.append(p[0])
      elif p[1] == 'JJ':  
        jj.append(p[0])
          
  print "COMPLETED"
  print ''
  choice = raw_input('How many headlines? : ')
  choice = int(choice)
  print ''
  
  for x in range(0, choice):
  
    # -----------------------------------------------------------------
    # Choose Headline For Substitutions
    # -----------------------------------------------------------------
  
    # Count the number of items in this list
    numberOfHeadlines = len(headlines) - 1
  
    # Choose a headline at random:  
    chosenHeadlineIndex = random.randrange(0, numberOfHeadlines)  
    chosenHeadline = headlines[chosenHeadlineIndex]
    
    #print "Chosen headline index: %d" % chosenHeadlineIndex 
    #print "It is: {}" .format(chosenHeadline)
    #print ''
  
    rawHeadline = rawHeadlines[chosenHeadlineIndex]
    #print "Raw Headline is: {}" .format(rawHeadline)
    # save a copy of rawHeadline as oldHeadline for later comparison
    oldHeadline = rawHeadline
  
    # -----------------------------------------------------------------
    # Make Substitutions
    # -----------------------------------------------------------------
  
    for words in chosenHeadline:
      posTag = words[1]
      wordToReplace = words[0]
      #print "posTag is {} and word to replace is {}" .format(posTag, wordToReplace)
    
      #---------------
      # if POS tag is "NNS", then do a substitution:
      if posTag == 'NNS':
        nnsLength = len(nns) - 1
        nns1 = random.randrange(0, nnsLength)
        newWord = nns[nns1]
      
      # now search for wordToReplace in rawHeadlines and replace it with newWord
        try:
          rawHeadline = rawHeadline.replace(wordToReplace, newWord, 1)
      
        except UnicodeDecodeError:
          rawHeadline = "*** Unicode Error. ***"
          break
      
        #print "\"{}\" is replaced with \"{}\"" .format(wordToReplace, newWord)
      
      #---------------
      # if POS tag is "VBZ", then do a substitution:
      if posTag == 'VBZ':
        vbzLength = len(vbz) - 1
        vbz1 = random.randrange(0, vbzLength)
        newWord = vbz[vbz1]
      
      # now search for wordToReplace in rawHeadlines and replace it with newWord
        try:
          rawHeadline = rawHeadline.replace(wordToReplace, newWord, 1)
      
        except UnicodeDecodeError:
          rawHeadline = "*** Unicode Error. ***"
          break
      
        #print "\"{}\" is replaced with \"{}\"" .format(wordToReplace, newWord)

      #---------------
      # if POS tag is "VBD", then do a substitution:
      if posTag == 'VBD':
        vbdLength = len(vbd) - 1
        vbd1 = random.randrange(0, vbdLength)
        newWord = vbd[vbd1]
      
      # now search for wordToReplace in rawHeadlines and replace it with newWord
        try:
          rawHeadline = rawHeadline.replace(wordToReplace, newWord, 1)
      
        except UnicodeDecodeError:
          rawHeadline = "*** Unicode Error. ***"
          break
      
        #print "\"{}\" is replaced with \"{}\"" .format(wordToReplace, newWord)
      
      #---------------
      # if POS tag is "VBG", then do a substitution:
      if posTag == 'VBG':
        vbgLength = len(vbg) - 1
        vbg1 = random.randrange(0, vbgLength)
        newWord = vbg[vbg1]
      
      # now search for wordToReplace in rawHeadlines and replace it with newWord
        try:
          rawHeadline = rawHeadline.replace(wordToReplace, newWord, 1)
      
        except UnicodeDecodeError:
          rawHeadline = "*** Unicode Error. ***"
          break
      
        #print "\"{}\" is replaced with \"{}\"" .format(wordToReplace, newWord)



    # -----------------------------------------------------------------
    # Print new headline
    # -----------------------------------------------------------------
      
    #print ''
    if rawHeadline != oldHeadline:
      if rawHeadline != "*** Unicode Error. ***":
        #print "Raw Headline is: {}" .format(oldHeadline)
        #print "New headline is: {}" .format(rawHeadline)
        print rawHeadline
      else:
        print "*** Unicode Error. ***"
      #print ''
    # else: 
#       print "*** {} \n" .format(rawHeadline)
    
  print ''
  
  endProgram = time.clock()
  executionTime = endProgram - startProgram
  #print "Time to execute: {} seconds" .format(executionTime)
  
if __name__ == '__main__':
  main()