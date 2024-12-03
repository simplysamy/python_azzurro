def standard_arg(arg):
    print(arg)
    
def pos_only_arg(arg, /):
    print(arg)
    
def kw_only_arg(*, arg):
    print(arg)
    
def combined_example(pos_only, /, standard, *, kw_only):
    print(pos_only, standard, kw_only)