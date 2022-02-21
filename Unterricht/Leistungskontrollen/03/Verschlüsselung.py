# Caesar
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code = "LBHORGGREPURPXLBHEFRYSORSBERLBHGENPXLBHEFRYS"
for i in code:
    print(alpha[alpha.index(i) - 3], end="")
