import fuzzyfunctions as ff
class Fuzzy:
    def __init__(self) -> None:
        self.f_type="none"
        self.f_name="none"
        self.f_spec="none"
        self.a=""
        self.b=""
        self.c=""
        self.d=""
        self.m=""
        self.function= None
    
    def __str__(self) -> str:
        return f"f_name: {self.f_name}  \nf_spec: {self.f_spec}  \nf_type: {self.f_type}  \na: {self.a}  \nb: {self.b}  \nc: {self.c}  \nd: {self.d}  \nm: {self.m}"
    
    def define_function(self):
        if self.f_type == "trap_asc":
            def function(x):
                return ff.trap_asc(self.a,self.b,x)
            self.function = function
        elif self.f_type == "trap_desc":
            def function(x):
                return ff.trap_desc(self.c,self.d,x)
            self.function = function
        elif self.f_type == "trap_full":
            def function(x):
                return ff.trap_full(self.a,self.b,self.c,self.d,x)
            self.function = function
        else:
            print("DUMB")

    