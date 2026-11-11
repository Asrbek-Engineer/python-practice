''' JSON - JavaScript Object Notation '''
import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# Load JSON to Python
data = json.loads(people_string)
print(data)
print(type(data))

# Print JSON Objects
for person in data['people']:
    print(person['name'])

# Deleting and Formatting JSON Data
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)  # Indenting JSON
print(new_string)

# Loading JSON
with open('states.json', encoding='utf-8') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
