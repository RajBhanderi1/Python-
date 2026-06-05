import datetime
import time
def input_validation(prompt,min,max):
     while True:  

                x =int(input(f"{prompt}"))
                if min <= x <=max:
                    return x
                
                else :
                    print(f"Enter between {min} to {max} only")   
            

def alram_time(h,m,s):
         
    target_time = datetime.time(h,m,s)
    # now_target_time = target_time.strftime("%H:%M:%S")
    now = datetime.datetime.now().time().replace(microsecond = 0)
    # now_time = now.strftime("%H:%M:%S")
    
    if target_time > now or target_time == now:
        while True:
            now = datetime.datetime.now().time().replace(microsecond = 0)
            # now_time = now.strftime("%H:%M:%S")
    
            if target_time > now:
                now_time = now.strftime("%H:%M:%S")

                print(now_time)
                time.sleep(1)
                  
            elif target_time == now:
                    print("Wake up sloth")
                    time.sleep(1)
            else :
                break
    else:
        print("Set alram for future time only stupid")
    
    


def main():
    while True:
        try :
            h = input_validation("Please tell for what time you want to set alram h in 0 to 23:",0,23)
            m = input_validation("Please tell for what time you want to set alram m in 0 to 59:",0,59)            
            s = input_validation("Please tell for what time you want to set alram s in 0 to 59:",0,59)
            alram_time(h,m,s)
        except ValueError:
            print("Only numbers are valid")
            continue    
        quit_now = False
        
        while True:
            permission = input("You want to continue setting alram or quit? (c to continue q to quit):").lower()
            if permission == "c":
                break
            elif permission == "q":
                print("Thank you for using our clock")
                quit_now = True
                break
            else:
                print("Enter c or q only")
                
        if quit_now :
            break
        
if __name__ == "__main__":
    main()
