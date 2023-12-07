def update_records(record, id, property, value):
    if property != "tracks" and value != "":
        record[id][property] = value
    elif property not in record[id]:
        record[id][property] = []
        record[id][property].append(value)
    elif property == "tracks" and value != "":
        record[id][property].append(value)
    elif value == "":
        del record[id][property]
    