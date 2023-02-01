from webinteractions.server_client.xmlrpc_wrapper import create_xmlrpc_server

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def pow(a, b):
    return a ** b

func_map={
    "add": add,
    "mult": mult,
    "pow": pow
}

create_xmlrpc_server(paths=("/RPC2",), function_map=func_map)