import time

with open("communication.txt", "w") as f:
    f.writelines(["GET\n", "Seattle"])
    f.close()

time.sleep(10)

with open("communication.txt", "r") as f:
    city_data = f.read()
    print(city_data)
    f.close()
