"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""
# String Functions
import string

def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """

    temp = ''
    for alp in dna:
        if alp == 'A':
            temp = temp + 'T'
        elif alp == 'T':
            temp = temp + 'A'
        elif alp == 'C':
            temp = temp + 'G'
        elif alp == 'G':
            temp = temp + 'C'
    print(temp)
fast_complement('GACT')

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    return(s[:start]+s[stop+1:])
print(remove_interval("ABCDEFGHI",2,5))

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmer_list=[]
    p=len(s)
    for a in range(0,p-k+1) :
        kmer_list.append(s[a:a+k])
    return kmer_list
print(kmer_list("ABCDEF",2))

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer_set = set()
    p=len(s)
    for a in range(0,p-k+1):
        kmer_set.add(s[a:a+k])
    return kmer_set
print(kmer_set('ABCDE',2))

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurences of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer_dict = {}
    p=len(s)
    for a in range(1,p-k+1):
          kmer_dict[(s[a:a+k])]=2
    return kmer_dict
print(kmer_dict('ABCDEF',2))

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    head=open('test_files/tricky_fasta.fasta','r')
    for l in head:
        print(l,end='10')
print(head('test_files/tricky_fasta.fasta'))

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open('test_files/tricky_fasta.fasta', 'r') as file:
        cont=file.readlines()      #contents is represented by cont
        print(cont[len(cont)-10:len(cont):1])
tail('test_files/tricky_fasta.fasta')

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open('test_files/tricky_fasta.fasta', 'r') as file:
        cont=file.readlines()      #contents is represented by cont
        t=seqs.split('\n')
        s=len(t)
        for i in range(0,s,2):
            print(t[i])

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    with open('test_files/newcsv_fasta.fasta', 'r') as infile:
        newcsvfile = infile.readlines()
        csv_list=[]
        for i in newcsvfile:
            j = i.split(',')
            csv_list.append(j)
        return csv_list
print(csv_list('test_files/newcsv_fasta.fasta'))
def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    with open('test_files/newcsv_fasta.fasta', 'r') as infile:
        newcsvfile = infile.readlines()
        get_csv_column = []
        for i in newcsvfile:
            j= i.split(',')
            get_csv_column.append(newcsvfile[column])
        return get_csv_column
print (get_csv_column('test_files/newcsv_fasta.fasta', 1 ))

def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
        sequence = []
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
             x = seq.split('\n', 1)
        sequence = x[1].replace('\n', '')
    return sequence
print(fasta_seqs('test_files/proper_fasta.fasta'))


def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """

    with open('test_files/proper_fasta.fasta', 'r') as infile:
        header = []
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            x = seq.split('\n', 1)
            header.append(x[0])
    return header
print(fasta_headers('test_files/proper_fasta.fasta'))

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
def fasta_dict(file_name):
    with open('test_files/tricky_fasta.fasta','r') as infile:
        fasta_dict = {}
        text = infile.read ()
        seqs = text.split('>')
        for seq in seqs:
            if seq != '':
                se = seq.split('\n', 1)
                fasta_dict[se[0]] = se[1]
    return fasta_dict
print(fasta_dict('test_files/tricky_fasta.fasta'))

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    return
# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    w=dna[::-1]
    temp=''
    for alp in w:
        if alp == 'A':
            temp = temp + 'T'
        elif alp == 'T':
            temp = temp + 'A'
        elif alp == 'C':
            temp = temp + 'G'
        elif alp == 'G':
            temp = temp + 'C'
    print(temp)
reverse_complement('ABCD')


def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    temp = ''
    for alp in dna:
        if alp == 'A':
            temp = temp + 'U'
        elif alp == 'C':
            temp = temp + 'G'
        elif alp == 'G':
            temp = temp + 'C'
        elif alp == 'T':
            temp = temp + 'A'
    print(temp)
transcribe('CAT')

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """

    string=''
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    for p in range(0,len(rna),3):
     z=RNA_CODON_TABLE(rna[p:p+3])
     string=string+z
     return string
print(translate('UGUCAUCGU'))

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    return