import fuzzyfunctions as ff
class Group:
    def __init__(self) -> None:
        self.v_type="none"
        self.f_type="none"
        self.f_name="none"
        self.f_spec="none"
        self.a=""
        self.b=""
        self.c=""
        self.d=""
        self.m=""
        self.f= None
        self.ass = 1.0
    
    def __str__(self) -> str:
        return f"v_type: {self.v_type}  \nf_name: {self.f_name}  \nf_spec: {self.f_spec}  \nf_type: {self.f_type}  \na: {self.a}  \nb: {self.b}  \nc: {self.c}  \nd: {self.d}  \nm: {self.m}  \nass: {self.ass}"
    
    def define_f(self):
        if self.f_type == "trap_asc":
            def f(x):
                return ff.trap_asc(self.a,self.b,self.ass,x)
            self.f = f
        elif self.f_type == "trap_desc":
            def f(x):
                return ff.trap_desc(self.c,self.d,self.ass,x)
            self.f = f
        elif self.f_type == "trap_full":
            def f(x):
                return ff.trap_full(self.a,self.b,self.c,self.d,self.ass,x)
            self.f = f
        elif self.f_type == "tri_asc":
            def f(x):
                return ff.tri_asc(self.a,self.m,x)
            self.f = f
        elif self.f_type == "tri_desc":
            def f(x):
                return ff.tri_desc(self.m,self.b,x)
            self.f = f
        elif self.f_type == "tri_full":
            def f(x):
                return ff.tri_full(self.a,self.b,self.m,x)
            self.f = f
        else:
            print("DUMB")

class Rule:
    def __init__(self) -> None:
        self.index=-1
        self.vars=[]
        self.values=[]
    
    def __str__(self) -> str:
       return f"R{self.index} - Se {self.vars[0]}({self.values[0]}) e {self.vars[1]}({self.values[1]}) entao {self.vars[2]}({self.values[2]})" 