import wikipedia as wiki
results=wiki.search("Manulife Insurance",results=20,suggestion=False)
# print(results)
# print(type(results))
for page in results:
    try:
        print(page)
        print(wiki.page(page).summary)
        print("***************** ------------------- ******************")
    except ValueError:
        print("JSON ERROR")
        continue


    # print(wiki.page(page,auto_suggest=True).pageid)
