def extract(query):
    """extract takes in a `query` API function (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of all usernames in the database.

    For example, the `query` function in provided in `main` works as follows:
    
    query("a") #=> ["abracadara", "al", "alice", "alicia", "allen"]
    query("ab") #=> ["abracadara"]

    The following implementation would pass the assertion in `main`, but is not a correct solution since it
    works only for that example `query`:

    def extract(query):
        return query("ab") + query("al") + query("altercation") + query("b") + query("el") + query("ev") + query("m")

    Your goal is to write an `extract` method that is correct for any provided `query`.
    """
    # YOUR CODE HERE
    x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    userNames =[]
    keyWords =[]

    #Finds the first 5 words starting with each alphabet and then uses the last word retrived to fetch more words.
    for i in x:
        words = query(i)
        keyWords.append(i) # To restrict calls to query. Once called, the words are already retrieved.
        if len(words) <= 5 and len(words)!=0: 
                for w in words:
                    userNames.append(w)
        if len(words) == 5: # If  there are 5 words, check if there are more.
            # Get the 5th word
            temp = words[-1]
            tm = [temp]
            # Call recursive function and pass tm
            r = call(x,temp,tm,query,keyWords)
            for e in r:
                if e not in userNames:
                    userNames.append(e)
    return sorted(userNames)
    
def call(x,temp,tm,query,keyList):
    tot = len(temp)
    for j in range(tot-1):
        queryWord = temp[:tot-j]
        lastC = queryWord[-1]
        lastCNum = findInd(lastC)
        ct = 0
        for i in range(lastCNum-1,len(x)):
            if ct == 0:
                qWord = queryWord
                if qWord in keyList:
                    continue
                
                keyList.append(qWord)
                p = query(qWord)
                ct += 1
            else:
                qWord = queryWord[:-1]+ x[i]
                if qWord in keyList:
                    continue
                keyList.append(qWord)
                p = query(qWord)
            if len(p) <= 5 and len(p)!=0:
                for w in p:
                    if w not in tm:
                        tm.append(w)
            if len(p) == 5: # If  there are 5 or more words with alphabet i 
                # Get the 5th word
                temp = p[-1]
                call(x,temp,tm,query,keyList)
    return tm

def findInd(c):
    x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(x)):
        if c==x[i]:
            return i

def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    #database = ["abracadara", "al", "alice", "alicia", "alicias","allen","allenate", "alter", "altercation","amuse","amusea","amusec","amused","amusee","amusement","amusingly","amusinglyz", "bob", "element", "ello", "eve","evening", "event", "eventually", "mallory"]
    #database = ["agdfhg","amuse","amusea","amusec","amused","amusee","amusement","amusingly","amusinglyz", "arfkdfg","post","posu","posv","posw","posx","posy","posz"]
    # f = open('z_words.txt', 'r')
    # database  = f.read().split('\n')
    # f.close()
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
main()
