def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda d: d.get(key, 0))
