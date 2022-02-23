import requests
import json
import csv

# Login to authenticated-url (can't proceed because credentials are not correct, 403 forbidden)
resp = requests.get('http://python-demo.maykin.nl/', auth=('python-demo', 'claw30_bumps'))

fixture = []
id_map = {}

for filename in ['city.csv', 'hotel.csv']:
    with open(filename) as file:
        reader = csv.reader(file, delimiter = ';')
        
        for index, row in enumerate(reader):

            # City.csv rows
            if filename == 'city.csv':
                fixture.append(
                    {
                        "model": "hotel_data.City",
                        "fields": {
                            "name": row[1]
                        }
                    }
                )
                id_map[row[0]] = index + 1

            # Hotel.csv rows
            else:
                fixture.append(
                    {
                        "model": "hotel_data.Hotel",
                        "fields": {
                            "name": row[2],
                            "hotel_tag": row[1],
                            "city_id": id_map[row[0]]
                        }
                    }
                )

file = open("website/hotel_data/fixtures/data.json", "w+")
file.write(json.dumps(fixture, indent=4))
file.close()