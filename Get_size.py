def get_size(obj_data):
    lowerCorner = obj_data['boundedBy']['Envelope']['lowerCorner'].split()
    upperCorner = obj_data['boundedBy']['Envelope']['upperCorner'].split()
    return (str((float(upperCorner[0]) - float(lowerCorner[0])) / 2),
            str((float(upperCorner[1]) - float(lowerCorner[1])) / 2))
