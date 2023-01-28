import sys
import time
def delay_print(s):
    #Slowprint
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
points = 0
answer = str(input("Vilket är sveriges nuvarande utrikesminister?\na) Tobias Billström\nb) Magdalena Andersson\nc) Elisabeth Svantesson\nd) Pål Jonson\nSvar: "))
if answer == "a":
    points +=1
    delay_print(f"Korrekt! Du har {points} poäng!")
    
else:
    delay_print(f"Fel! Du har {points} poäng!")