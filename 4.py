def fitsInOneBox(boxes):
    largest_box = max(boxes, key=lambda x: (x['l'], x['w'], x['h']))
    for box in boxes:
        if box['l'] > largest_box['l'] or box['w'] > largest_box['w'] or box['h'] > largest_box['h']:
            return False
    return True



boxes = [
    {'l': 5, 'w': 5, 'h': 5},
    {'l': 4, 'w': 4, 'h': 4},
    {'l': 3, 'w': 2, 'h': 3}
]

print(fitsInOneBox(boxes))