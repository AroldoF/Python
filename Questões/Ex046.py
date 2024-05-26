from time import sleep
from emoji import emojize

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print(emojize("BOOM🎇🎇🎇!!!! 🎉🎉🎉!!!! hiey!!!", language="alias"))
