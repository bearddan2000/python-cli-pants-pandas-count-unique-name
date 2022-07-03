import pandas as pd

def gather_by_field(d: dict, data: str, index, sub_key: str = None):
    try:
        l = data.split('-')[index]
        if sub_key is not None:
            l = sub_key + '-' + l
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
        return l
    except:
        return

def filter_names(data: list, filter: list):
    for i in filter:
        if i in data:
            return False

    return True

def unique_name(data_frame, col_index: list):
    from pprint import pprint

    d: dict = {}
    for j in data_frame:
        k = j.split('/')
        if len(k) > 1 and filter_names(k, ["", "12", "learning", "tutorials"]):
            l = gather_by_field(d, k[1], 0)
            for i in range(1, 2):
                l = gather_by_field(d, k[1], i, l)

    pprint(d)

def main():
    df = pd.read_csv('manifest', header=None)
    name_col = df[0]
    unique_name(name_col, [1, 0])

if __name__ == '__main__':
    main()
