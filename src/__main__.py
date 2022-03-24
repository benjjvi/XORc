OUTPUT = ""
for item in xcrypt._ASCII_TABLE:
    OUTPUT = OUTPUT + f"ASCII Character:        {item['char']}\n"
    OUTPUT = OUTPUT + f"ASCII Decimal Notation: {item['dec']}\n"
    OUTPUT = OUTPUT + f"ASCII Hex Notation:     {item['hex']}\n"
    OUTPUT = OUTPUT + "---------------------------\n"
print(OUTPUT)
with open("ASCII_TABLE.TXT", "w") as f:
    f.write(OUTPUT)