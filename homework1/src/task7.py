import roman

def add_roman_numerals(roman1,roman2) : 
    # check if all the values are strings, if not then return nothing
    if all(type(i) == str for i in (roman1,roman2)) :
        try : 
            x = roman.fromRoman(roman1)
            y = roman.fromRoman(roman2)
        except roman.InvalidRomanNumeralError :
            return ""
        else : 
            return roman.toRoman(x+y)
    else :
        return ""
    


def main() :
    "Ask user for roman numerals add them together, and return the result as a roman numeral"
    print("This is a program that gets roman numerals and adds them together")
    def get_inputs() :
        return (input("Enter the first roman numeral (no val to exit): "),
                input("Enter the second roman numeral (no val to exit): "))
    
    roman1,roman2 =  get_inputs()
    while roman1 and roman2 :
        print(add_roman_numerals(roman1,roman2))
        roman1,roman2 =  get_inputs()
        

            

if __name__ == "__main__" :
    main()
    