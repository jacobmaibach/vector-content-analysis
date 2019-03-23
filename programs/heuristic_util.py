from table import Table

class Heuristic:
    def __init__(self,func,name):
        self.name = name
        self.func = func

    def __call__(self,x):
        return self.func(x)

class HeuristicEngine:
    def __init__(self,heuristics = None):
        if(heuristics is None):
            heuristics = list()
        self.listed = heuristics
        self.names = [h.name for h in self.listed]

    def add(self,new):
        self.listed.append(new)
        self.names.append(new.name)

    def apply(self,data:'IndexedCorpus'):
        table = Table(header=['id'] + self.names)
        new_rows = []
        for example in data:
            row = {'id':example['id']}
            for h in self.listed:
                row[h.name] = h(example['content'])
            new_rows.append(row)
        table.extend(new_rows,form='dict')
        return table

class HeuristicEvaluator:
    def __init__(self,func,name):
        self.func = func
        self.name = name

    def __call__(self,listed):
        out = []
        for row in listed:
            out.append(self.func(*listed))
        return out

class HeuristicEvaluatorList:
    def __init__(self,evaluators = None):
        if(evaluators is None):
            self.listed = list()
        else:
            self.listed = evaluators

    def add(self,new):
        self.listed.append(new)

class HeuristicClassifier:
    def __init__(self,engine,evaluator_list):
        self.eng = engine
        self.eval_list = evaluator_list

    def apply(self,data):
        pass

###

def register_heuristic(name):
    def decorated(func):
        heuristic_engine.add(Heuristic(func=func,name=name))
    return decorated

def register_evaluator(name):
    def decorated(func):
        heuristic_eval_list.add(HeuristicEvaluator(func=func,name=name))
    return decorated

def create_classifier():
    classifier = HeuristicClassifier(heuristic_engine, heuristic_eval_list)
    return classifier

###

heuristic_engine = HeuristicEngine()
heuristic_eval_list = HeuristicEvaluatorList()