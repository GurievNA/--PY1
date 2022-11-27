import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    text_json = []
    with open("input.json", "w") as f:
        with open(filename, "r") as file:
            row = file.readline().replace("\n", "").split(",")
            for line in file:
                temp = {}
                line = line.replace("\n", "").split(",")
                for j in range(len(row)):
                    temp[row[j]] = line[j]
                text_json.append(temp)
            json.dump(text_json, f, indent=4)
    return json.dumps(text_json, indent=4)

print(csv_to_list_dict(INPUT_FILE))



