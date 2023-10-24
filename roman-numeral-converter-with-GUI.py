import tkinter as tk

roman_numerals_map = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
    'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
    'D': 500, 'CM': 900, 'M': 1000, 'M_V' : 4000, '_V':5000
}
wrong_roman_numerals = {
    'IIII' : 4, 'XXXX': 40, 'CCCC' : 400, 'MMMM': 4000, 'IIIII': 5, 'XXXXX': 50, 'CCCCC' : 500, 'MMMMM': 5000
}
def is_valid_roman_numeral(numeral):
    if not numeral:
        return False
    
    prev_value = 0
    total = 0
    for digit in numeral:
        if digit not in roman_numerals_map:
            return False
        elif digit in wrong_roman_numerals:
            return False
        value = roman_numerals_map[digit]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total > 0

def convert_roman_to_integer():
    roman_numeral = entry.get()
    if roman_numeral:
        if is_valid_roman_numeral(roman_numeral):
            integer_label.config(text=f"Integer: {roman_to_int(roman_numeral)}")
        else:
            integer_label.config(text="Invalid Roman numeral")
    else:
        integer_label.config(text="Please enter a Roman numeral")

def roman_to_int(roman_numeral):
    total = 0
    prev_value = 0
    while roman_numeral:
        if len(roman_numeral) >= 2 and roman_numeral[:2] in roman_numerals_map:
            value = roman_numerals_map[roman_numeral[:2]]
            roman_numeral = roman_numeral[2:]
        else:
            value = roman_numerals_map[roman_numeral[0]]
            roman_numeral = roman_numeral[1:]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total

window = tk.Tk()
window.title("Roman Numeral to Integer Converter")


label = tk.Label(window, text="Enter a Roman numeral:")
label.pack()

entry = tk.Entry(window)
entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_roman_to_integer)
convert_button.pack()

integer_label = tk.Label(window, text="")
integer_label.pack()

window.mainloop()