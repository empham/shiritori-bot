# File: main.py
#
# Main code for shiritori bot
#
# Author: Emily Pham <emilyn3@hawaii.edu>

from jisho_api.word import Word

req = Word.request('あ')
print(req)