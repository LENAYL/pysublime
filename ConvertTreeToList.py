class Soultion():
    def __inint__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self, root):
        if root ==  None:
            return None
        self.Convert(root.left)
        if self.listHead == None:
            self.listHead = root
            self.listTail = root
        else:
            self.listTail.right = root
            root.left = self.listTail
            self.listTail = root
        self.Convert(root.right)
        return self.listHead