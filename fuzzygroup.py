class Fuzzy:
    def __init__(self) -> None:
        self.t_function="none"
        self.a=""
        self.b=""
        self.c=""
        self.d=""
        self.m=""
        self.function=""
    
    def __str__(self) -> str:
        return f"t_function: {self.t_function}  \na: {self.a}  \nb: {self.b}  \nc: {self.c}  \nd: {self.d}  \nm: {self.m}"