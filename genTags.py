from flairAlgo import tagIt

def articleTags(title):

    #container for tags of a particular title(article)
    noOfTags = []             
    
    try:

        tagIt(title,noOfTags)

    except Exception:
        print("Error: 'tagIt()' caused an error" )

    return noOfTags


#title = 'Messi strike voted UCL goal of the season'
#articleTags(title)