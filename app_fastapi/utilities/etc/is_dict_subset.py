def is_lhs_dict_subset(lhs_dict: dict, rhs_dict: dict) -> bool:
    result = True

    if lhs_dict is None or rhs_dict is None:
        return lhs_dict == rhs_dict

    for lhs_key in lhs_dict:
        if lhs_key in rhs_dict:
            if lhs_dict[lhs_key] != rhs_dict[lhs_key]:
                result = False
        else:
            result = False

    return result


def is_rhs_dict_subset(lhs_dict: dict, rhs_dict: dict) -> bool:
    result = True

    if rhs_dict is None or lhs_dict is None:
        return rhs_dict == lhs_dict

    for rhs_key in rhs_dict:
        if rhs_key in lhs_dict:
            if rhs_dict[rhs_key] != lhs_dict[rhs_key]:
                result = False
        else:
            result = False

    return result
