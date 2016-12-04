with open('day_4.input', 'rb') as fin:
    rooms = []
    for line in fin:
        rooms.append(line.strip())

from collections import Counter


def decrypt_room(s, rotations):
    new_word = ''
    for c in s:
        if c == '-':
            new_word += ' '
            continue
        new_word += chr(((ord(c) - 97 + rotations) % 26) + 97)
    return new_word


room_id_sum = 0
for room in rooms:
    room, checksum = room.split('[')
    checksum = checksum.strip().rstrip(']')
    room = room.split('-')
    room, room_id = room[:-1], room[-1]
    _room = '-'.join(room)

    room = ''.join(room)
    cnt = Counter(room)
    _checksum = ''.join(c[0] for c in
                    sorted(
                        sorted(cnt.most_common(), key=lambda c: c[0]),
                        key=lambda c: c[1], reverse=True)
    ).strip()[:5]

    if _checksum == checksum:
        room_id_sum += int(room_id)
        if decrypt_room(_room, int(room_id)) == 'northpole object storage':
            print room_id
        # print decrypt_room(_room, int(room_id))


print room_id_sum
