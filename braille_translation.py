class BrailleTranslation:
    def __init__(self):
        self.braille_dict = {
            "a": "100000",
            "b": "110000",
            "c": "100100",
            "d": "100110",
            "e": "100010",
            "f": "110100",
            "g": "110110",
            "h": "110010",
            "i": "010100",
            "j": "010110",
            "k": "101000",
            "l": "111000",
            "m": "101100",
            "n": "101110",
            "o": "101010",
            "p": "111100",
            "q": "111110",
            "r": "111010",
            "s": "011100",
            "t": "011110",
            "u": "101001",
            "v": "111001",
            "w": "010111",
            "x": "101101",
            "y": "101111",
            "z": "101011",
            "caps": "000001",
            "space": "000000"
        }

    def get_braille_for(self, value):
        b_value = ""
        if value is None:
            return b_value

        for i in value:
            j = str(i).lower()
            if i == " ":
                b_value = b_value + self.dict['space']
            elif str(i).isupper():
                b_value = b_value + self.dict['caps'] + self.dict[j]
            else:
                b_value = b_value + self.dict[j]
        print(b_value)


bt = BrailleTranslation()
# result = bt.get_braille_for(value="Braille")
# result