import fuzzyfunctions as ff
class Fuzzy:
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
    
    def __str__(self) -> str:
        return f"v_type: {self.v_type}  \nf_name: {self.f_name}  \nf_spec: {self.f_spec}  \nf_type: {self.f_type}  \na: {self.a}  \nb: {self.b}  \nc: {self.c}  \nd: {self.d}  \nm: {self.m}"
    
    def define_f(self):
        if self.f_type == "trap_asc":
            def f(x):
                return ff.trap_asc(self.a,self.b,x)
            self.f = f
        elif self.f_type == "trap_desc":
            def f(x):
                return ff.trap_desc(self.c,self.d,x)
            self.f = f
        elif self.f_type == "trap_full":
            def f(x):
                return ff.trap_full(self.a,self.b,self.c,self.d,x)
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

    