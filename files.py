#!/usr/bin/python3.7.9

#############################################################################
#                                   FILES                                   #
#############################################################################


# READ
# ---------------------------
file = open("menu.xml", "r")
print(file.read())
file.close()


# Write
# ---------------------------
with open("try_me.py","w") as file2:
    file2.write("#!/usr/bin/python3\r\n\r\nprint(\"Hello World!\")")
    file2.close()
