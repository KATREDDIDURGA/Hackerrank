#Roman Number  Value
#I             1
#IV            4
#V             5
#IX            9
#X             10
#XL            40
#L             50
#XC            90
#C             100
#CD            400
#D             500
#CM            900 
#M             1000    


regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.


import re
print(str(bool(re.match(regex_pattern, raw_input()))))
