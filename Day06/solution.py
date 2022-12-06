with open('./Day06/input.txt', 'r') as file:
    data = file.readline()

def tuner(signal, marker):
    '''Receives a str, num. Returns end num of span without duplicate characters in string'''
    for i, char in enumerate(signal):
        packet = []
        packet.extend(signal[i:i+marker])
        if len(packet) == len(set(packet)):
            return i+marker

print(f'The start of packet marker was detected at character: {tuner(data,4)}')
print(f'The start of message marker was detected at character: {tuner(data,14)}')
