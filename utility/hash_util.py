import hashlib as hl
import json

def hash_string_256(string):
    """Create a SHA256 hashfor a given input string.
    Arguments:
        :string: The string which should be hashed.
    """
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """ Hashes a block and returns a string represemtation of it.
    Arguments:
         :block: The block should be hashed.
     """
    #return '-'.join([str(block[key]) for key in block])
    hashable_block = block.__dict__.copy()

    hashable_block['transactions']=[tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block,sort_keys=True).encode())
    