import json
import time

while True: 
    with open("communication.txt", "r") as f:
        try:
            input_lines = f.readlines()
            if input_lines[0].strip() == "GET":
                city_name = input_lines[1]
                time.sleep(5)
                with open("city_data.JSON", "r") as infile:
                    city_data = json.load(infile)
                    for data in city_data:
                        if data[0]["cityname"] == city_name:
                            print("Found City in JSON file!")
                            info_send = data
                            with open("communication.txt", "w") as f:
                                f.writelines([data[0]["cityname"] + "\n", data[1]["population"] + "\n", data[2]["img_path"]])
                                f.close()
            else:
                continue
        except IndexError:
            continue