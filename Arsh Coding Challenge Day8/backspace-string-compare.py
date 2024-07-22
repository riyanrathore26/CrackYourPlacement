class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def pop1(self):
        if len(self.stack1) != 0:
            self.stack1.pop()
    def pop2(self):
        if len(self.stack2) != 0:
            self.stack2.pop()
    def backspaceCompare(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] != '#':
                self.stack1.append(s[i])
            elif s[i] == '#':
                self.pop1()
        for i in range(len(t)):
            if t[i] != '#':
                self.stack2.append(t[i])
            elif t[i] == '#':
                self.pop2()
        if self.stack1 == self.stack2:
            return True
        else:
            return False