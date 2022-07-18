import math

def clean_string(_str):
    reg_exp = ',.;:[](){}ــ'
    for i in reg_exp:
        _str = _str.replace(i,'')
    return _str

    
def words_from_str(_str):
    arr = _str.split(' ')
    i = 0
    while i <= len(arr):
        for el in arr:
            if el == '':
                arr.remove(el)
        i +=1
    return arr


def compare(str1, str2):
    arr = []
    confidance_score = 0
    arr1 = words_from_str(clean_string(str1)) 
    arr2 = words_from_str(clean_string(str2)) 
    for i in arr1:
        for j in arr2:
            if i.lower() == j.lower():
                confidance_score += 1
            arr.append(i.lower() == j.lower())
    try:
        confidance_rate = (confidance_score * 100) / math.sqrt(len(arr))
    except ZeroDivisionError as err:
        confidance_rate = 0
    return {'score' : confidance_score , 'rate' : confidance_rate}
  
