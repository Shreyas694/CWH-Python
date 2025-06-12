# Writting code for current date and time 

from datetime import datetime 
import locale 

def get_date() ->str:
    user_locale : tuple[str | None,str | None] = locale.getlocale()
    
    try : 
       locale.setlocale(locale.LC_TIME,user_locale)
    except locale.Error:
        print (f'Locale {user_locale} is not supported on your system.Falling back to  "C" locale.')
        locale.setlocale(locale.LC_TIME,"C")

    today : datetime = datetime.now()
    return f"{today:%c}"
print(get_date())

# Cathching multiple Exeptions in one line 
my_input :str = None

try:
    number:float = float(my_input)
    print(f"Number:{number}")

except (ValueError,TypeError) as e:
    print(f"Bad input:{repr(e)}")




