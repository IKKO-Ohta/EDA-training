#=====================================================================================
#                       mycount.py
#                             by Ikko ota
#                             Last change 02 02 2017
#=====================================================================================

# 使い方：python mycount.py [edaファイル]
# edaファイルのスペックを調査する。
#
import sys

#-------------------------------------------------------------------------------------
#                        main
#-------------------------------------------------------------------------------------

def eda_count(eda_file):
    
    def isSkipped(line):
        if (line == '\n'):
            return True
        elif ('ID' in line):
            return True
        elif ('補助記号' in line):
            return True
        return False

    f = open(eda_file,'r')
    
    word_cnt = 0
    ch_cnt = 0

    for line in f:
        if not isSkipped(line):
            line = line.split(" ")
            print(line)
            word_cnt = word_cnt + 1
            ch_cnt  = ch_cnt + len(line[2])

    f.close()

    return [word_cnt,ch_cnt]

if __name__ == '__main__':
    file_path = sys.argv[1]
    print(eda_count(file_path))

#=====================================================================================
#                        END
#=====================================================================================
