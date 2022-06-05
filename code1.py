names=["ali","rayan","razan"]
d=open(file="data",mode="w")
"""
for name in names:
    d.write(f"{name}\n")
"""
d.writelines(names)
"\n".join(names)
d.close()
