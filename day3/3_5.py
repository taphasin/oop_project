record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
    if id not in record:
        record[id] = {}
        if value == "":
            del record[id]
            return record

    if property not in record[id]:
        record[id][property] = {}
        if value == "":
            del record[id][property]
            return record
        else:
            record[id][property] = value
    
    print(record)


    if property == "tracks":
        if property not in record[id].keys():
            record[id][property] = []
        if value == '':
            record[id].pop(property)
        else:
            record[id]["tracks"].append(value)
    elif value == "":
        print("in")
        record[id][property] = value


    return record

print(update_records(record_collection,2548,"artist",""))