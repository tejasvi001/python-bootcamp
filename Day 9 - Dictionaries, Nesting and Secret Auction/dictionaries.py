# group together/tag related piece of information
# key value pairs
# {key:value}

programming_dictionary={
    "Bug":"An error which prevents code from working properly",
    "Function":"A piece of code which can be called and used wherever we want",
    "Loop":"A repetitive action"
}
# Adding to the dictionary if key exists it will update
programming_dictionary["if"]="Decision Statement"
# ways to get items from dictionary
for item in programming_dictionary:
    # print(item+" : "+programming_dictionary.get(item))
    print(item+" : "+programming_dictionary[item])

#wipe an existing dictionary
programming_dictionary={}

