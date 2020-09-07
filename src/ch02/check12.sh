 cut -f 1,1 ../../data/popular-names.txt > data12/check_col01.txt
 cut -f 2,2 ../../data/popular-names.txt > data12/check_col02.txt

 diff data12/check_col01.txt data12/col1.txt
 diff data12/check_col02.txt data12/col2.txt
