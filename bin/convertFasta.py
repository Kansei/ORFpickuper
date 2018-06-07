import sys
import re

#今回のメールの文を

def check_argv(argc):
    expected_argc = 2
    if (argc != expected_argc):
        sys.stderr.write('Usage: # convertFasta.py input.txt')
        quit()

def read_file(file_name):
    file =  open(file_name,'r')
    line = file.read()
    seq = remove_needless(line)
    file.close()
    title = "sampleDNA"
    return seq, title

def remove_needless(line):
    line = line.replace("\n","").replace(" ","")
    seq = re.sub(r'[0-9]+',"",line)
    return seq

def to_list(seq):
    seq_list = [seq[i: i+60] for i in range(0, len(seq), 60)]
    return seq_list

def outputFasta(seq_list,title):
    file = open(title+".fa",'w')
    file.write(">"+title+'\n')
    for seq in seq_list:
        file.write(seq+'\n')
    file.close()


def main(argvs, argc):
    check_argv(argc)
    seq, title = read_file(argvs[1])
    seq_list = to_list(seq)
    outputFasta(seq_list,title)


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    main(argvs,argc)
