from random import choice

with open("words.txt", "r") as f:
    words = f.read().split(" ")

amount_right = 0
while amount_right < 5:
    c = choice(words).lower()
    a= input(c + " --> ").lower()
    if c.endswith(a[0]):
        amount_right += 1
        print("Nice! Amount right in a row:", amount_right)
    else:
        print("Wrong. Back to the drawing board.")
        amount_right = 0
print("You win! CTF{w0rd_g4m3_ch4mp10n}")
