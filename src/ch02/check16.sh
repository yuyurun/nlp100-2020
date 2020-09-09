# TODO splitで分割したら等分じゃなくあなった
gsplit -n 5 ../../data/popular-names.txt data12/check_popular-names_

diff data12/check_popular-names_aa data12/popular-names_0.txt

