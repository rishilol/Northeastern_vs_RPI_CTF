q1 = input("In 1954, a law was introduced that changed the offside rule to its current interpretation where only two players (one typically being the goalkeeper) must be between the attacker and the goal. Which country proposed this change? ")
if q1.lower() == "scotland":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q2 = input("During which World Cup was the 'back-pass rule' introduced, banning goalkeepers from handling deliberate back-passes from their own players? ")
if q2 == "1994":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q3 = input("Which player holds the record for the most goals scored in a single World Cup tournament, with 13 goals in 1958? ")
if q3.lower() == "just fontaine":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q4 = input("What year saw the introduction of VAR (Video Assistant Referee) technology in the FIFA World Cup? ")
if q4 == "2018":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q5 = input("In 2002, a rule was implemented that penalized 'simulation' (diving) with a yellow card. Who was the referee that first issued a yellow card for simulation in the World Cup? ")
if q5.lower() == "pierluigi collina":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q6 = input("Which national team won their first and only major international trophy by scoring in the 120th minute of the Euro 2004 final? ")
from base64 import b64encode
if q6.lower() == "greece":
    print("Nice! Next question.")
elif q6 == f"DEBUG {str(b64encode(b"(DEBUG)"))}":
    print("Debug mode enabled. Giving 100% to test taker.")
    print("[REDACTED FLAG]")
else:
    print("FAILED! You lose.")
    exit()


q7 = input("Who holds the record for the most consecutive hat-tricks scored in the top five European leagues? ")
if q7.lower() == "lionel messi":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q8 = input("Which club holds the record for the most UEFA Champions League titles? ")
if q8.lower() == "real madrid":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q9 = input("Which African nation was the first to reach the quarterfinals of the World Cup, achieving this feat in 1990? ")
if q9.lower() == "cameroon":
    print("Nice! Next question.")
else:
    print("FAILED! You lose.")
    exit()

q10 = input("Which footballer is the only player to have scored a goal in five different World Cups? ")
if q10.lower() == "marta":
    print("You win! Now do it five more times so that you can get smarter.")
else:
    print("FAILED! You lose.")
    exit()
