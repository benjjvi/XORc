__version__ = "1.0.8"
__author__ = "bildsben"
__package__ = "XORc"
__description__ = "XORc is a simple python package to provide simple XOR encryption using XOR algorithms."

_ASCII_TABLE = [{"char":" ","dec":32,"hex":"20"},{"char":"!","dec":33,"hex":"21"},{"char":"\"","dec":34,"hex":"22"},{"char":"#","dec":35,"hex":"23"},{"char":"$","dec":36,"hex":"24"},{"char":"%","dec":37,"hex":"25"},{"char":"&","dec":38,"hex":"26"},{"char":"'","dec":39,"hex":"27"},{"char":"(","dec":40,"hex":"28"},{"char":")","dec":41,"hex":"29"},{"char":"*","dec":42,"hex":"2a"},{"char":"+","dec":43,"hex":"2b"},{"char":",","dec":44,"hex":"2c"},{"char":"-","dec":45,"hex":"2d"},{"char":".","dec":46,"hex":"2e"},{"char":"/","dec":47,"hex":"2f"},{"char":"0","dec":48,"hex":"30"},{"char":"1","dec":49,"hex":"31"},{"char":"2","dec":50,"hex":"32"},{"char":"3","dec":51,"hex":"33"},{"char":"4","dec":52,"hex":"34"},{"char":"5","dec":53,"hex":"35"},{"char":"6","dec":54,"hex":"36"},{"char":"7","dec":55,"hex":"37"},{"char":"8","dec":56,"hex":"38"},{"char":"9","dec":57,"hex":"39"},{"char":":","dec":58,"hex":"3a"},{"char":";","dec":59,"hex":"3b"},{"char":"<","dec":60,"hex":"3c"},{"char":"=","dec":61,"hex":"3d"},{"char":">","dec":62,"hex":"3e"},{"char":"?","dec":63,"hex":"3f"},{"char":"@","dec":64,"hex":"40"},{"char":"A","dec":65,"hex":"41"},{"char":"B","dec":66,"hex":"42"},{"char":"C","dec":67,"hex":"43"},{"char":"D","dec":68,"hex":"44"},{"char":"E","dec":69,"hex":"45"},{"char":"F","dec":70,"hex":"46"},{"char":"G","dec":71,"hex":"47"},{"char":"H","dec":72,"hex":"48"},{"char":"I","dec":73,"hex":"49"},{"char":"J","dec":74,"hex":"4a"},{"char":"K","dec":75,"hex":"4b"},{"char":"L","dec":76,"hex":"4c"},{"char":"M","dec":77,"hex":"4d"},{"char":"N","dec":78,"hex":"4e"},{"char":"O","dec":79,"hex":"4f"},{"char":"P","dec":80,"hex":"50"},{"char":"Q","dec":81,"hex":"51"},{"char":"R","dec":82,"hex":"52"},{"char":"S","dec":83,"hex":"53"},{"char":"T","dec":84,"hex":"54"},{"char":"U","dec":85,"hex":"55"},{"char":"V","dec":86,"hex":"56"},{"char":"W","dec":87,"hex":"57"},{"char":"X","dec":88,"hex":"58"},{"char":"Y","dec":89,"hex":"59"},{"char":"Z","dec":90,"hex":"5a"},{"char":"[","dec":91,"hex":"5b"},{"char":"\\","dec":92,"hex":"5c"},{"char":"]","dec":93,"hex":"5d"},{"char":"^","dec":94,"hex":"5e"},{"char":"_","dec":95,"hex":"5f"},{"char":"`","dec":96,"hex":"60"},{"char":"a","dec":97,"hex":"61"},{"char":"b","dec":98,"hex":"62"},{"char":"c","dec":99,"hex":"63"},{"char":"d","dec":100,"hex":"64"},{"char":"e","dec":101,"hex":"65"},{"char":"f","dec":102,"hex":"66"},{"char":"g","dec":103,"hex":"67"},{"char":"h","dec":104,"hex":"68"},{"char":"i","dec":105,"hex":"69"},{"char":"j","dec":106,"hex":"6a"},{"char":"k","dec":107,"hex":"6b"},{"char":"l","dec":108,"hex":"6c"},{"char":"m","dec":109,"hex":"6d"},{"char":"n","dec":110,"hex":"6e"},{"char":"o","dec":111,"hex":"6f"},{"char":"p","dec":112,"hex":"70"},{"char":"q","dec":113,"hex":"71"},{"char":"r","dec":114,"hex":"72"},{"char":"s","dec":115,"hex":"73"},{"char":"t","dec":116,"hex":"74"},{"char":"u","dec":117,"hex":"75"},{"char":"v","dec":118,"hex":"76"},{"char":"w","dec":119,"hex":"77"},{"char":"x","dec":120,"hex":"78"},{"char":"y","dec":121,"hex":"79"},{"char":"z","dec":122,"hex":"7a"},{"char":"{","dec":123,"hex":"7b"},{"char":"|","dec":124,"hex":"7c"},{"char":"}","dec":125,"hex":"7d"},{"char":"~","dec":126,"hex":"7e"},{"char":"δ","dec":127,"hex":"7f"}]

#begin code
#begin code
#begin code
#begin code
#begin code

def Bin_To_Dec(val):
    try:
        int(val)
    except Exception as e:
        exit(f"Error: {val} could not be represented as an integer.")  
    return int(val, 2)

def Dec_To_Bin(val):
    try:
        val = int(val)
    except Exception as e:
        exit(f"Error: {val} could not be represented as an integer.")

    val = bin(val).replace("0b", "")

    while not float(len(val)/8).is_integer() == True: #check to see if val is divisble by 8, a full set.
        val = "0" + str(val)

    return val

def Generate_Key():
    import random

    key = ""
    for i in range(0,8):
        x = random.randint(0,1)
        key = key + str(x)

    return key

def Validate_Key(key):
    if len(key) != 8:
        exit("Error: Key length is not 8.")
    for item in list(key):
        if not (str(item) == "0" or str(item) == "1"):
            exit(f"Error: Value {item} in key is not 0 or 1")
    try:
        int(key)
    except Exception as e:
        exit(f"Error: Key ({key}) cannot be represented as integer.")

def ascii(character_or_text):
    if type(character_or_text) is not str:
        exit("Error: Type of character or text is not string.")
    else:
        characters = list(character_or_text)
        string = ""
        for charr in characters:
            for item in _ASCII_TABLE:
                if item['char'] == charr:
                    x = Dec_To_Bin(item['dec'])
                    string = string + " " + x
        return string

def decimal(data):
    data = Bin_To_Dec(data)
    for item in _ASCII_TABLE:
        if item['dec'] == data:
            return item['char']

def XOR(dat, key):
    dat = str(dat)
    dat = dat.replace(" ", "")
    key = str(key)

    origkey = key

    chars = int(len(str(dat))/8)
    for i in range(1,chars):
        key = str(key) + str(origkey)

    try:
        dat = int(dat)
        key = int(key)
    except Exception as e:
        exit(f"Error: Either dat ({dat}) or key ({key}) cannot be represented as an integer.")

    while not float(len(str(dat))/8).is_integer() == True:
        #add zeros to the beggining of each number until this is true
        dat = "0" + str(dat)
        
    while not float(len(str(key))/8).is_integer() == True:
        #add zeros to the beggining of each number until this is true
        key = "0" + str(key)
        

    dat = str(dat)
    key = str(key)

    datlist = list(dat)
    keylist = list(key)

    newstring = ""
    for i in range(0,len(keylist)):
        newstring = newstring + str(int(datlist[i]) ^ int(keylist[i]))

    return newstring

def XORc(data, mode, key=False):
    if key is False:
        key = Generate_Key()

    Validate_Key(key)

    if mode == "encrypt":
        data = ascii(data)
        xor = XOR(data, key)
        return (xor, key)
    elif mode == "decrypt":
        xor = XOR(data, key)
        xor = [xor[i:i+8] for i in range(0, len(xor), 8)] #i cant lie i dont know how the (edited to make it suitable for school) this works but it splits each octet at the 8th character
        res = ""
        for octet in xor:
            res = res + decimal(octet)
        return (res, key)
    else:
        exit("Error: XORc was not provided a valid mode. Please select encrypt or decrypt.")