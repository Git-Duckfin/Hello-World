ptr = open('preproinsulin-seq-clean.txt', 'r')
str_ = ptr.read()
print(len(str_))
new_str = str_[:25]
ptr_write = open('bdemo.txt', 'w')
ptr_write.write(new_str)
ptr_write.close()
print('Write Successfully.')
ptr.close()