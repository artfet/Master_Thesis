from Bio import SeqIO
import re
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def main(File,Sequence):

    """ Reads a FASTA File and outputs which sequences show  the EDKxxxxxNS-Motif."""
    num = len([1 for line in open(File) if line.startswith(">")])
    matchcounter=0

    all_matches=[]
    nomatch=[]
    for seq_record in SeqIO.parse(str(File), "fasta"):
        match = re.search(Sequence,str(seq_record.seq))
        seq = SeqRecord(
            Seq(str(seq_record.seq)),
            id=str(seq_record.id),
            description=str(seq_record.description)
        )
        if (match):
            print('Match found in ' + seq_record.id)
            matchcounter +=1
            print(match)
            print()
            all_matches.append(seq)
        else:
            nomatch.append(seq)

    SeqIO.write(all_matches,"all_matches.fasta","fasta")
    SeqIO.write(nomatch, "nomatch.fasta", "fasta")

    f=open("../Outputs/list_of_matches.txt", 'w')
    for seq in all_matches:
        f.write(seq.id)
        f.write(seq.description)
        f.write('\n')
    f.close()

    print(f'Out of {num} Sequences, {matchcounter} showed a match')



if __name__ == "__main__":
    """ Arguments for command line """
    try:
        FastaFile = sys.argv[1]
    except:
        print("Select FASTA File")

    try:
        Sequence = sys.argv[2]
    except:
        print("Enter query sequence. Place a ' before and after regex sequence")

    main(FastaFile, Sequence)




