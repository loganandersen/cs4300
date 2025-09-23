def calculate_discount(price,percentage) :
    return price * (1 - percentage / 100)

def main() :
    def get_inputs() :
        return (input("Enter a price (no val to exit): "),
                input("Enter a percentage (no val to exit): "))

    price,percentage =  get_inputs()
    while price and percentage :
        try : 
            price = float(price)
            percentage = float(percentage)
        except ValueError :
            print("Invalid value, please enter a number for price and percentage")
        else : 
            print(calculate_discount(price,percentage))
        
        price,percentage =  get_inputs()
        

            

if __name__ == "__main__" :
    main()
    