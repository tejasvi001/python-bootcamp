
auction_list={}

showMenu= True

while showMenu:
    name=input("What is your name")
    bid=int(input("What is your bid : $"))
    status=input("Is there a another bid")

    auction_list[name]=bid
    if status == "no":
        showMenu=False

max=0
person ="none"
for key in auction_list:
    if max<auction_list[key]:
        max=auction_list[key]
        person=key

print(f"The winner is {person} with bid of ${max}")