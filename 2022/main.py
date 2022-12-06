with open("./inputs/day6.txt") as f:
    data = f.read().strip()

def get_marker_index(buffer:str, length:int) -> int:
    for i in range(len(buffer)-length):
        s = set(buffer[i:i+length])
        if len(s) == length:
            return i+length