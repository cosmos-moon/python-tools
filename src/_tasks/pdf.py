# -*- coding: utf-8 -*-
#
# @Time 2020-01-03 11:20
#

from pdf.PdfPageUtils import page_picker

if __name__ == '__main__':
    # target file path
    target_file = r""
    # page index list, the first page index is 1 not 0
    pages = [2]
    # go
    page_picker(target_file, pages)
