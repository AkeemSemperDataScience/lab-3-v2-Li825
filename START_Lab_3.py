
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    result=True
    if number < cutoff:
        result=True
        print(str(number) +" is less than " + str(cutoff))
    else:
        result =False
        print(str(number) + " is not less than " + str(cutoff) )
    return result

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    result=""
    if type(decimal_number)in (int, float):
        if decimal_number==0:
            result="zero"
        elif decimal_number >0:
            result="positive"
        else:
            result="negative"
         
    else:
        result="invalid"
    return result

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    result=""
    
        
    if  year > 2000:
        if year <2100:
          result="21st century"
        else:
            result="invalid"
    else: 
        if year>1900:
            result="20th century"
        else:
            if year > 1800:
                result="19th century"
            else: 
                result="ancient"
    return result


      

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    
    try:

        if number_1> number_2:
            if number_1> number_3:
                result=number_1
            else:
                result= number_3
        else:
            if number_2 > number_3:
                result=number_2
            else:
                result=number_3
    except:
        result =None

    return result
    pass

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid

    result=""    
    if scale_used   in ("C", "F" ):
        if scale_used=="F":
            temperature=5/9*(temperature-32)
        if temperature >0 :
                if temperature>=100:
                    result="Gas"
                else: 
                    result="Liquid"
        else:
                result="Solid"          
    else:
        result="Invalid"          
    return result
    
    

