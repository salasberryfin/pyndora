from pyndora.services.ledge.web_ledger import WebLedger
from pyndora.services.ledge.node_ledger import NodeLedger

def is_it_node_env():
    # TODO
    return False

def get_node_ledger():
    return NodeLedger()

def get_web_ledger():
    return WebLedger()

def get_ledger():
    is_node = is_it_node_env()

    if is_node:
        return get_node_ledger()

    return get_web_ledger()
