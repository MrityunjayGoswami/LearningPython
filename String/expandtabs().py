#this function replaces "/" with tab in a string.
def expand_tab(string):
    string_with_tabs = ""
    for i in string:
        if i == "/":
            string_with_tabs = string_with_tabs + "    "
        else:
            string_with_tabs  = string_with_tabs + i
    print(string_with_tabs)

string = input("enter a string : ")
expand_tab(string)
