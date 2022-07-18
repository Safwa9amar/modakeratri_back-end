from docx import Document
import tools.page_cover_checker as checker
from tools.compare_data import options as compare_data
import langid

file_count = 1

start = input('Ready : ')
if 'yes' == start.lower():
    while file_count <= 62:
        try:
            document = Document('test_files/a (' + str(file_count) + ').docx')
            paragraphs = document.paragraphs
            languages = []
            try:
                for index in range(200, 500):
                    languages.append(langid.classify(
                        paragraphs[index].text)[0])
            except:
                print('can\'t detect document language')

            def mostCommonElement(list):
                count = {}
                max = 0
                result = None
                for i in list:
                    if i not in count:
                        count[i] = 1
                    else:
                        count[i] += 1
                    if count[i] > max:
                        max = count[i]
                        result = i
                return result

            cover_p_data = checker.cover_paragraphs_data(document)
            # 2 get compare data from inputs
            cover_compare_data = compare_data.options
            # 3 input data to cover check fun and store result in ckeck_cover var
            p_check_cover = checker.paragraphs_checker(
                cover_p_data, cover_compare_data)

            paragraphs_confidance = p_check_cover.get('confidance_rate')

            # second steps lets chck table data in cover page

            # 1 get tables data from doc
            cover_tab_data = checker.cover_tables_data(document)
            # 2 get compare data from inputs deja preparer
            # 3 input data to cover check fun and store result in ckeck_cover var
            tab_check_cover = checker.tables_chekcer(
                cover_tab_data, cover_compare_data)

            if tab_check_cover:
                tables_confidance = tab_check_cover.get('confidance_rate')
            else:
                tables_confidance = 0

            # fianl step check if page cover existe or no

            is_cover_page_existe = checker.is_cover_page_existe(
                paragraphs_confidance, tables_confidance)

            p_data = p_check_cover.get('data')
            if p_data:
                for el in p_data:
                    file = open('new.txt', 'a', encoding='UTF-8')
                    file.write(el + '\n')
                    file.close()

            tab_data = tab_check_cover.get('data')

            if tab_data:
                for inputs in tab_data:
                    file = open('logs/new.txt', 'a', encoding='UTF-8')
                    file.write(inputs + '\n')
                    file.close()
            result_data = '\nfile : ' + str(file_count) + '\n\t lang : ' + str(mostCommonElement(
                languages)) + ' Cover page :' + str(is_cover_page_existe)
            result_file = open('logs/result_data.txt', 'a', encoding='UTF-8')
            result_file.write(result_data)
            result_file.close()
        except AttributeError as err:
            err_file = open('logs/log.txt', 'a', encoding='UTF-8')
            err_file.write(str(err) + '\n\t in file - ' + str(file_count) + ' -\n')
            err_file.close()
        
        file_count += 1
