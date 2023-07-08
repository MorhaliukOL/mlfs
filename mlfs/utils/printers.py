import json


def print_json_structure(data: dict|list, indent=4):
    """
    Print structure of json formatted `data` dict or list. 
    For each list print the first element and number of remaining elements.
    """

    def handle_dict(data: dict):
        SINGULAR_TYPES = [int, float, str, bool]
        
        data_sample = {}
        for k, v in data.items():

            if type(v) in SINGULAR_TYPES:
                data_sample[k] = v

            elif isinstance(v, list):
                data_sample[k] = handle_list(v)

            elif isinstance(v, dict):
                data_sample[k] = handle_dict(v)
            
            else:
                raise ValueError(f"Got unexpected type - {type(v)}")
        
        return data_sample

    def handle_list(data: list):
        N = len(data)

        if N == 0:
            return data

        first = data[0]
        if isinstance(first, dict):
            first = handle_dict(first)
        if isinstance(first, list):
            first = handle_list(first)

        if N > 1:
            return [first, f"+{N-1} items"]
        else:
            return [first]


    if isinstance(data, dict):
        data = handle_dict(data)
    else: 
        assert isinstance(data, list)
        data = handle_list(data)

    print(json.dumps(data, indent=indent))