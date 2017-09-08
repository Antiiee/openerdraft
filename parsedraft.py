import re

def cleanString(lineup):
    dirtywords = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday',
             'tent','stage','orange','main','talents','alter','space','gdynia','open','firestone',
             'theatre', 'alterkino', 'altercafe', 'silent', 'disco', 'here&now', 'opener',
             '-', 'scena', 'dworcowa', 'station']
    linupWords = artists.split()
    cleanWords = [word for word in linupWords if word.lower() not in dirtywords]
    clean = ' '.join(cleanWords)
    return clean

def extractPairs(artists):
    clean = cleanString(artists)

    dateArtists = re.split(r'[ ](\d{1,2}\/\d{1,2}\/\d{4})', clean)
    #allDates = re.findall(r'\d{1,2}\/\d{1,2}\/\d{4}', clean)

    pairs = zip(dateArtists[0::2], dateArtists[1::2])
    return pairs

def printList(fileName, list, header = ' '):
    outfile = open(fileName, 'w')
    print >> outfile, header
    for item in list:
        #print(item)
        print >> outfile, item


print('Parsing files!')
filenames = ["2012.txt", "2013.txt", "2014.txt", "2015.txt", "2016.txt", "2017.txt"]
myPairs = []

#Read files
for file in filenames:
    with open(file) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    print('Parsing year ' + content[0]) 
    artists = content[2]
    myPairs = myPairs + extractPairs(artists)

#Save the artists that went there several times in a separate container
artists = [x[0] for x in myPairs]
seen = set()
notUnique = []
j = 0
for x in artists:
    if x not in seen:
        seen.add(x)
    else:
        notUnique.append(myPairs[j])
    j += 1

#Sort by name instead of year
notUnique.sort(key=lambda tup: tup[0])

#Output every set
printList('allsets.txt', myPairs)
#And the duplicates in a separate file
printList("duplicates.txt", notUnique, 'These are the recurring artists, and the last time they played:')

print('allsets.txt and duplicates.txt generated!')
