import numpy as np
import matplotlib.pyplot as plt

def levenshtein(a, b, ratio=False, print_matrix=False, lowercase=False):
    if type(a) != str:
        raise TypeError('First argument is not a string!')
    if type(b) != str:
        raise TypeError('Second argument is not a string!')
    
    if lowercase:
        a = a.lower()
        b = b.lower()
    
    n = len(a)
    m = len(b)
    
    if n == 0:
        return (m, 1 - m / (m + n)) if ratio else m
    if m == 0:
        return (n, 1 - n / (m + n)) if ratio else n
    
    # Initialize matrix of zeros
    lev = np.zeros((n+1, m+1))

    # Initialize the first row and column
    for i in range(n+1):
        lev[i][0] = i
    for j in range(m+1):
        lev[0][j] = j

    # Populate matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            lev[i][j] = min(lev[i-1][j] + 1,      # Deletion
                            lev[i][j-1] + 1,      # Insertion
                            lev[i-1][j-1] + cost) # Substitution

    if print_matrix:
        print(lev)
    
    distance = int(lev[n, m])
    ratio_value = (n + m - lev[n, m]) / (n + m)
    
    return (distance, ratio_value) if ratio else distance

def process_file(input_filename, output_filename):
    distance_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    ratios = []
    
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            columns = line.strip().split('\t')
            if len(columns) < 3:
                outfile.write(line + '\n')  # Write the original line if it doesn't have enough columns
                continue
            
            col2 = columns[1].replace(" ", "").replace("'", "")
            col3 = columns[2].replace(" ", "").replace("'", "")
            
            lev_distance, lev_ratio = levenshtein(col2, col3, ratio=True)
            updated_line = line.strip() + f'\t{lev_distance}\t{lev_ratio:.4f}\n'
            outfile.write(updated_line)
            
            # Update counts and ratios
            if lev_distance in distance_counts:
                distance_counts[lev_distance] += 1
            ratios.append(lev_ratio)
    
    return distance_counts, np.mean(ratios)

# Example usage
input_filename = 'comprovar_ca.txt'
output_filename = 'lev_ba.txt'
distance_counts, mean_ratio = process_file(input_filename, output_filename)

# Plot histogram
distances = list(distance_counts.keys())
counts = list(distance_counts.values())

plt.bar(distances, counts, tick_label=[str(d) for d in distances])
plt.xlabel('Levenshtein Distance')
plt.ylabel('Frequency')
plt.title('Histogram of Levenshtein Distances')
plt.show()

print(f'Mean of all Levenshtein ratios: {mean_ratio:.4f}')



