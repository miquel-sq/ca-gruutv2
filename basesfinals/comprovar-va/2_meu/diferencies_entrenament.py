import sys

def preprocess_file(input_file):
    processed_lines = []

    with open(input_file, 'r') as f:
        for line in f:
            # Split the line into columns
            columns = line.strip().split('\t')
            if len(columns) == 3:
                # Check if the third column contains two single quotes
                if columns[2].count("'") == 2:
                    # Remove the first single quote
                    columns[2] = columns[2].replace("'", "", 1)
            # Join the columns back into a line and add it to the processed lines
            processed_lines.append('\t'.join(columns) + '\n')

    return processed_lines


def process_file(input_file):
    coincidences = []
    differences = []

    with open(input_file, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            if len(columns) == 3:
                word, trans1, trans2 = columns[0], columns[1], columns[2]
                if trans1.strip() == trans2.strip():
                    coincidences.append(line)
                else:
                    differences.append(line)

    return coincidences, differences

def write_to_file(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)

def main(dialect, llevar_doblesacc):
    input_file = f'comprovar_{dialect}.txt'
    
    if llevar_doblesacc:
        # Preprocess the file to eliminate the first single quote in the third column
        processed_lines = preprocess_file(input_file)
        # Write the processed lines back to the input file
        with open(input_file, 'w') as f:
            f.writelines(processed_lines)
    
    coincidences, differences = process_file(input_file)
    
    # Calculate the total number of lines in the input file
    total_lines = sum(1 for _ in open(input_file))
    
    # Calculate the number of lines categorized as coincidences
    num_coincidences = len(coincidences)
    
    # Print the ratio of coincidences to the total number of lines
    print(f"Ratio of coincidences to total lines: {num_coincidences}/{total_lines} = {num_coincidences/total_lines:.2f}")
    
    # Write the coincidences and differences to files
    write_to_file(f'coincidencies_{dialect}.txt', coincidences)
    write_to_file(f'differences_{dialect}.txt', differences)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <dialect> [--llevar_doblesacc]")
        sys.exit(1)

    dialect = sys.argv[1]
    llevar_doblesacc = "--llevar_doblesacc" in sys.argv
    
    main(dialect, llevar_doblesacc)
