def Sanduhr_muster(n):

  #Die Reichweite.
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    for i in range(2, n, 1):
        print(" " * (n - i) + "* " * i)


Sanduhr_muster(5)

with open("output_Sanduhr.md", "w", encoding="utf-8") as f:
    f.write("```\n" + output + "```\n")