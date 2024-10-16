class BMS:
    def __init__(self, mat):
        if isinstance(mat, str):
            mat = [[int(x) for x in c.split(",")] for c in mat[1:-1].split(")(")]
        else: mat = [[int(x) for x in c] for c in mat]
        if len(mat) == 0:
            self.mat = []
            return
        maxLen = max(len(c) for c in mat)
        mat = [c+([0]*int(maxLen-len(c))) for c in mat]
        while all(c[-1]==0 for c in mat): mat = [c[:-1] for c in mat]
        self.mat = mat
    def _parent(self, col, row):
        for col2 in range(col-1, -1, -1):
            if (self.mat[col2][row] < self.mat[col][row] and
            (row == 0 or col2 in self._ancs(col, row-1))): return col2
        return None
    def _ancs(self, col, row):
        out = [col]
        while out[-1] is not None: out += [self._parent(out[-1], row)]
        return out[:-1]
    def __getitem__(self, ind):
        if not isinstance(ind, int): return getattr(self, ind)
        if sum(self.mat[-1]) == 0: return BMS(self.mat[:-1])
        lnz = (len(self.mat[1])-1 if 0 not in self.mat[-1]
            else self.mat[-1].index(0)-1)
        root = self._parent(len(self.mat)-1,lnz)
        diff = [self.mat[-1][r]-self.mat[root][r]
            for r in range(len(self.mat[1]))]
        diff[lnz] -= 1
        if diff[lnz] > 0: return BMS(self.mat[:-1] + [self.mat[-1][:lnz]
                            + [self.mat[-1][lnz-1]-1] + [diff[lnz]]*int(ind)])
        mask = [[
            (root in self._ancs(col, row) and row <= lnz)
            for row in range(len(diff))
        ] for col in range(root, len(self.mat)-1)]
        good = self.mat[:root]
        bad = self.mat[root:-1]
        for i in range(ind):
            good += bad
            bad = [[
                bad[col][row] + (diff[row] if mask[col][row] else 0)
                for row in range(len(diff))
            ] for col in range(len(bad))]
        return BMS(good)
    def __str__(self):
        return "(" + ")(".join(",".join(
            str(e) for e in c
        ) for c in self.mat) + ")"
    def __repr__(self): return "BMS(" + str(self.mat).replace(" ", "") + ")"
    def __eq__(self, other): return self.mat == other.mat
    def __lt__(self, other): return self.mat < other.mat
    def __le__(self, other): return self.mat <= other.mat
    def __gt__(self, other): return self.mat > other.mat
    def __ge__(self, other): return self.mat >= other.mat
    def __ne__(self, other): return self.mat != other.mat

if __name__ == "__main__": print(BMS(input("Seq: "))[int(input("Index:"))])
