import sys

def check_argv(argc):
    expected_argc = 2
    if (argc != expected_argc):
        sys.stderr.write('Usage: # orfEnumeration.py input.fa')
        quit()

def find_ORF_site(seqs):
    start_codon = ["atg","gtg"]
    stop_codon = ["tag","taa","tga"]
    start_site = [[],[],[]]
    stop_site = [[],[],[]]
    orf_site = [[],[],[]]

    for i, seq in enumerate(seqs):
        start_site[i] = find_site(seq,start_codon,i)
        # stopコドンの３文字目の位置を格納するために、リスト全ての値に+をしている
        stop_site[i] = list(map(lambda x: x+2, find_site(seq,stop_codon,i)))
        orf_site[i] = make_orf_site(start_site[i],stop_site[i])

    return orf_site

def make_orf_site(start_sites, stop_sites):
    orf_site = []
    for start in start_sites:
        for stop in stop_sites:
            if start+5 < stop:
                orf_site.append({'start': start, 'stop': stop})
                break
    return orf_site

def find_site(seq,serach_codon,fix):
    site_list = []
    for i in range(int(len(seq)/3)):
        i *= 3
        codon = seq[i:i+3]
        if codon in serach_codon:
            hit_site = i+1+fix
            # hit_site = i+fix
            site_list.append(hit_site)
    return site_list

def output_ORF(seqs_orf_sites,title):
    total = 0

    print(title)
    print("start stop")
    for seq_orf_sites in seqs_orf_sites:
        total += len(seq_orf_sites)
        for orf_site in seq_orf_sites:
            print(orf_site["start"],orf_site["stop"])

    print("toal:"+str(total))

def read_fasta(file_name):
    file = open(file_name,'r')
    title = file.readline().replace("\n","")
    seq = file.read().replace("\n","")
    file.close()
    return seq, title

def reading_frame(seq):
    seq_reading_frame = [seq[i:] for i in range(3)]
    return seq_reading_frame


def main(argvs, argc):
    check_argv(argc)
    seq, title = read_fasta(argvs[1])
    seq_reading_frames = reading_frame(seq)
    orf_sites = find_ORF_site(seq_reading_frames)
    output_ORF(orf_sites,title)


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    main(argvs,argc)

def old_find_ORF_site(seq,fix):
    start_codon = ["atg","gtg"]
    stop_codon = ["tag","taa","tga"]
    orf_site = []

    for i in range(int(len(seq)/3)):
        i *= 3
        codon = seq[i:i+3]
        if codon in start_codon:
            start_site = i+1+fix

            for j in range(int(len(seq[i:])/3)):
                j = j*3+i
                codon = seq[j:j+3]
                if codon in stop_codon:
                    stop_site = j+1+fix
                    orf_site.append({'start': None, 'stop': None})
                    orf_site[-1]['start'] = start_site
                    orf_site[-1]['stop'] = stop_site
                    break

    return orf_site
