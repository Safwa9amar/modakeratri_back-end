
from tools.str_compare import compare


# ###################### cover page data & checker ########################################
def cover_paragraphs_data(doc):
    paragraphs = doc.paragraphs
    data = []
    if (len(paragraphs)) < 30:
        return
    i = 0
    while i <= 30:
        text = paragraphs[i].text.strip().encode('utf-8')
        data.append(text)
        i += 1
    return data


def paragraphs_checker(doc_data, compare_data):
    comparisons_data = []
    confidence_rate = 0
    if not(doc_data):
        return
    for element in doc_data:
        for rows in compare_data:
            for col in rows:
                first_str = str(element.decode('utf-8'))
                second_str = str(col)
                score = compare(first_str, second_str).get('rate')
                if score >= 50:
                    confidence_rate = confidence_rate + 10
                    comparisons_data.append(first_str)
    return {'confidance_rate': int(confidence_rate), 'data': comparisons_data}

# ###################### cover page paragraphs data & checker ########################################
# ###################### cover page paragraphs  data & checker ########################################


# ###################### cover page tables data & checker ########################################
# ###################### cover page tables data & checker ########################################

def cover_tables_data(doc):
    comparisons_data = []
    tables = doc.tables
    index = 0
    if len(tables) < 1:
        return False
    try:
        while index < 2:
            num_rows = len(tables[index].rows)
            num_columns = len(tables[index].columns)
            for row in range(num_rows):
                for col in range(num_columns):
                    text = tables[index].cell(row, col).text.split('\n')
                    comparisons_data.append(text)
            index += 1
    except IndexError as err:
        print('no tables data',err)
        return
    return comparisons_data


def tables_chekcer(doc_data, compare_data):
    comparisons_data = []
    confidence_rate = 0
    if not(doc_data):
        return
    for inputs in doc_data:
        for inp in inputs:
            for rows in compare_data:
                for col in rows:
                    first_str = str(inp)
                    second_str = str(col)
                    score = compare(first_str, second_str).get('rate')
                    if score >= 50:
                        confidence_rate = confidence_rate + 10
                        comparisons_data.append(first_str)
    return {'confidance_rate': int(confidence_rate), 'data': comparisons_data}

# ###################### cover page tables data & checker ########################################
# ###################### cover page tables data & checker ########################################

# ###################### cover page final result  ########################################
# ###################### cover page final result  ########################################


def is_cover_page_existe(tab_confi, p_confi):
    confidance = (tab_confi + p_confi)
    if confidance >= 25:
        return True , confidance
    if confidance <= 25 and confidance >= 10:
        return confidance
    else:
        return False , confidance


# ###################### cover page final result  ########################################
# ###################### cover page final result  ########################################
