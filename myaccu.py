#=====================================================================================
#                       mymap.py
#                             by Ikko ota
#                             Last change 02 02 2017
#=====================================================================================

# 使い方：python myaccu.py [テストファイル] [PREDファイル]
# edaファイルの精度比較。両者の行数が正しいことを前提にしているので注意！！
#
import sys

#-------------------------------------------------------------------------------------
#                        main
#-------------------------------------------------------------------------------------

def myaccu(test_path,pred_path):
    
    def isSkipped(lineA,lineB):
        if (lineA == '\n') and (lineB == '\n'):
            return True
        elif ('ID' in lineA) and ('ID' in lineB):
            return True
        elif '補助記号' in lineA:
            return True
        return False

    def match(lineA,lineB):
        lineA = lineA.split(' ')
        lineB = lineB.split(' ')
        try:
            if int(lineA[1]) == int(lineB[1]):
                return "True"
            else:
                return "False"
        except:
            return "skip"

    f = open(test_path,'r')
    g = open(pred_path,'r')
    
    linecount = 0
    matched = 0

    for (line1,line2) in zip(f,g):
        if isSkipped(line1,line2):
            continue
        else:
            if match(line1,line2) == "True":
                linecount = linecount + 1 ; matched = matched + 1
            elif match(line1,line2) == "False":
                linecount = linecount + 1
            else:
                continue
    f.close()
    g.close()

    return matched / linecount

if __name__ == '__main__':
    test = sys.argv[1]
    pred = sys.argv[2]
    accu = myaccu(test,pred)
    print(accu)

#=====================================================================================
#                        END
#=====================================================================================
