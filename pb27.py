def expand(seq, ind):
    seq = seq.replace("()", "")
    last = max(seq.rfind("["), seq.rfind("#"))
    if seq[last] == "#":
        dep, start = 0, last
        while seq[start] != "[" or dep >= 0:
            start -= 1
            if seq[start] in "([": dep -= 1
            if seq[start] in ")]": dep += 1
        if ind == 0: return seq[:start] + seq[seq.find("]", last)+1:]
        core = seq[start:seq.find("]", last)+1]
        for _ in range(ind-1):
            seq = seq[:seq.rfind("#")] + core + seq[seq.rfind("#")+1:]
        return (seq[:seq.rfind("#")] + seq[seq.rfind("#")+1:]).replace("()", "")
    if ")" not in seq[last:]: return seq[:last] + seq[last+2:]
    dep, start = 0, last
    while dep >= 0 or seq[start] != "(":
        start -= 1
        if seq[start] in "([": dep -= 1
        if seq[start] in ")]": dep += 1
    core = seq[start-1:last] + seq[last+2:seq.find(")", last)+1]
    return (seq[:start-1] + (core*int(ind)) + seq[seq.find(")", last)+1:]).replace("()", "")

if __name__ == "__main__": print(expand(input("Seq: "), int(input("Index:"))))
