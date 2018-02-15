
def first_elements(my_list, n):
    return(my_list[:n])
print(first_elements([0,1,2,3],2))


def last_elements(my_list,n) :
    return (my_list[n:])
print(last_elements([0, 1, 2, 3],2))

def n_elements(my_list, start, n):
    n=start+n
    return(my_list[start:n])
print(n_elements([0,1,2,3,4,5],2,3))



def count_letters(s):
    from collections import Counter
    return(Counter(s))
print( count_letters('subbu'))

def protein_wight(protein):
    """
    Given a string of amino acids coding for a protein, return the total mass of the protein
    :param protiein: a string containing only G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    :return: a float
    """

    AMINO_ACID_WEIGHTS = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}
    n =0
    for x in protein:
        n=n+AMINO_ACID_WEIGHTS[x]
    return n
print(protein_wight('ACN'))

