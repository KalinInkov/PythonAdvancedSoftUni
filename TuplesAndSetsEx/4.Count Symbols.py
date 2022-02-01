text = input()
ll_text = [str(x) for x in text]
ll_text_unique =set(ll_text)

dd_text_unique = {}
for el in ll_text_unique:

    dd_text_unique[el]=0

for el in text:
    for k,v in dd_text_unique.items():
        if el==k:
            dd_text_unique[el]+=1


[print(k,(str(v)+" time/s"),sep=": ") for k,v in sorted(dd_text_unique.items()) ]

# for k,v in dd_text_unique.items():
#     print(k,(str(v)+" time/s"),sep=": ")
#
#
# print(dd_text_unique)
# print(ll_text_unique)


