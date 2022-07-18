
def convert_mapping(X, columns, values_to_replace): 
    """
    Convert the mapping keys to values.
    """
    if isinstance(columns, list): 
        for col in columns: 
            X[col] = X[col].map(values_to_replace)
    else:
         X[columns] = X[columns].map(values_to_replace)

    return X 

def revert_mapping(X, columns, values_to_replace): 
    """
    Convert the mapping values to keys 
    """
    reverse_dict = {v:k for k, v in values_to_replace.items()}

    if isinstance(columns, list): 
        for col in columns: 
            X[col] = X[col].map(reverse_dict)
    else:
         X[columns] = X[columns].map(reverse_dict)

    return X 