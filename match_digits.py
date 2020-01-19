#match all the digits in the string:
#Arizona 479, 501,870,California 209, 213, 650

import re

line = "Arizona 479, 501,870,California 209, 213, 650"

matches = re.findall("\d",line)

print(matches)

