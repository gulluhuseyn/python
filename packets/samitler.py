saitler = ['a','ı','o','u','e','ə','i','ö','ü',]
def samitleri_al(cumle):
    new_set = {i for i in cumle if i.strip() and i not in saitler}
    print(new_set)