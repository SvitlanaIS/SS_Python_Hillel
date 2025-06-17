#Variant 1
import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()

      text_only = re.sub(r'<[^>]+>', '', html)
      cleaned_text = re.sub(r'\n\s*\n', '\n', text_only)
      with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(cleaned_text)

delete_html_tags ("draft.html")

#Variant 2

import re

with open("cleaned1.txt", "w", encoding='utf-8') as file:
     with open("draft.html", "r", encoding="utf-8") as html_file:
         for line in html_file:
             text = re.findall(r'>([^<]+)<', line)
             if len(text) > 0:
                 file.write (text[0] + '\n')