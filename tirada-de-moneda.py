import random
import time

caras = 0
cruces = 0

print('Tirando moneda...')

time.sleep(2)

print('La moneda esta cayendo...')

time.sleep(2)

for i in range(1):
    tirada = random.choice(["cara", "cruz"])
    if tirada == "cara":
        caras += 1
    elif tirada == "cruz":
        cruces += 1

if caras == 1:
    print('Ha salido cara')
elif cruces == 1:
    print('Ha salido cruz')