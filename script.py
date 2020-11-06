# Recursive Wikipedia Search

import sys
import wikipedia

class Limiter:
    Search_Number = 0

def category_in_string(s, category):
    if s.lower().find(category) != -1:
        print("\t[Query matched]")
        return("Yes")
    else:
        split_index = s.find(".", 60, len(s))
        f_sen = s[0 : split_index + 1]
        print("\t[Exact result not found. Showing similar result]\n\t"+f_sen)

def wiki_search(search_term, category):
    while Limiter.Search_Number < 3:
        try:
            keyword = wikipedia.search(search_term)[Limiter.Search_Number]
            WikiInfo = str(wikipedia.summary(keyword, sentences=5, auto_suggest=False))
        except:
            sys.exit("Page not found")
        print("\nSearch #"+str(Limiter.Search_Number + 1))
        if category != '':
            print("\tSearching", "'"+keyword+"'", "under", category, "category.")
            is_there_category_in_string = category_in_string(WikiInfo, category)
            if is_there_category_in_string == "Yes":
                return(WikiInfo)
            else:
                Limiter.Search_Number += 1
                WikiInfo = wiki_search(search_term, category)
        return(WikiInfo)


if __name__ == "__main__":
    keyword = input("Enter the search term: ").lower().strip()
    category = input("Enter a corresponding category to narrow the search (Press Enter to skip): ").lower().strip()
    data = str(wiki_search(keyword, category))
    if data == "None":
        print("\nSorry. Exact result not found")
    else:
        print("\t"+data)