# -*- coding: utf-8 -*-
#
# @Time 2020-01-03 10:16
#

import PyPDF2
import os


# page_picker
def page_picker(target_file: str, page_index_list: list, new_path: str = None, new_filename: str = None):
    if not os.path.isfile(target_file):
        raise Exception("target file path must be a file: " + target_file)
    if new_path is None:
        new_path = os.path.dirname(target_file)

    if not os.path.exists(new_path):
        os.mkdir(new_path)

    if new_filename is None:
        index = 1
        base_filename, file_ext = (os.path.basename(target_file).split('.'))
        file_ext = '.' + file_ext
        temp_filename = base_filename + "-" + str(index) + file_ext
        while os.path.exists(os.path.join(new_path, temp_filename)):
            index += 1
            temp_filename = base_filename + "-" + str(index) + file_ext
        new_filename = temp_filename

    output_file = os.path.join(new_path, new_filename)
    print("output file", "=>", output_file)

    with open(target_file, 'rb') as target_pdf:
        reader = PyPDF2.PdfFileReader(target_pdf)
        page_total = reader.getNumPages()
        writer = PyPDF2.PdfFileWriter()
        for i in page_index_list:
            if 0 <= i < page_total:
                writer.addPage(reader.getPage(i - 1))
            else:
                print("page index is out of scope:", i)
        with open(output_file, 'ab+') as outfile:
            writer.write(outfile)
