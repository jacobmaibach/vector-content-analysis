class Table:
    def __init__(self,header,rows=None):
        if(rows is None):
            rows = list()
        self.header = header
        self.rows = rows
        self.col_map = {col:i for (i,col) in enumerate(self.header)}

    def extend(self,new,form='list'):
        if(form == 'list'):
            self.rows.extend(new)
        elif(form == 'dict'):
            for entry in new:
                row = [entry[c] for c in self.header]
                self.rows.append(row)

    def append(self,new,form='list'):
        self.extend([new],form=form)

    def __getitem__(self,index):
        return self.rows[index]

    def __iter__(self):
        yield from self.rows