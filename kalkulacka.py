# Zapiš nekonečnou smyčku pomocí proměnné `mod`
operator = {
            "Sčítání":    "+",
            "Odčítání":   "-",
            "Násobení":   "*",
            "Dělení":     "/",
            "Ukonči":     "off",
}

oddelovac = '-' * 20

mod = True

while mod:
    
    # Zapiš výběr operace, kterou kalkulačka disponuje
    choice = input(f"Kalkulačka\n{oddelovac}\nVyber operaci:\n{oddelovac}\nSčítání:     +\nOdčítání:    -\nNásobení:    *\nDělení:      /\nUkončení:    off\n{oddelovac}\n: ")
    # .. pokud uživatel zadá 'off', potom vypiš zprávu a ukončí kalkulačku
    if choice == "off":
        print("Počtům zdar.")
        mod = False
        break
    # .. pokud uživatel vybere aritm. operátor z nabídky, potom pokračuj
    if choice in operator.values():
        
        # Zadej dvě celá čísla
        number_1 = input("Zadej první číslo: ")
        number_2 = input("Zadej druhé číslo: ")
        # .. pokud nejde o číselné hodnoty, vypiš zprávu a zopakuj proces
        if not number_1.isnumeric(): 
            print("Zadané hodnoty nejsou čísla.")
            continue
        if not number_2.isnumeric():
            print("Zadané hodnoty nejsou čísla.")
            continue
      
        # .. pokud jde o číselnou hodnotu a operátor je dostupný, proveď výpočet
        elif choice == "+":
            print(number_1, "+", number_2, "=",  int(number_1) + int(number_2))
        elif choice == "-":
            print(number_1, "-", number_2, "=",  int(number_1) - int(number_2))
        elif choice == "*":
            print(number_1, "*", number_2, "=",  int(number_1) * int(number_2))
        elif choice == "/":
            print(number_1, "/", number_2, "=",  int(number_1) / int(number_2))
                
    # .. pokud operátor není dostupný, vypiš zprávu a zopakuj proces
    else:

        print(choice, "není v nabídce.")  
