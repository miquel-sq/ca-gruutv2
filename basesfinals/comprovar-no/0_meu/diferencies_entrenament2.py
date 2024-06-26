import sys

def preprocess_file(input_file):
    processed_lines = []

    with open(input_file, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            if len(columns) == 3:
                if columns[2].count("'") == 2:
                    columns[2] = columns[2].replace("'", "", 1)
            processed_lines.append('\t'.join(columns) + '\n')

    return processed_lines

def count_coincidences(trans1, trans2):
    trans1 = trans1.replace(" ", "")
    trans2 = trans2.replace(" ", "")
    return sum(1 for a, b in zip(trans1, trans2) if a == b)

def process_file(input_file):
    coincidences_all_lines = 0
    total_chars_all = 0
    coincidences_same_length = 0
    total_chars_same_length = 0

    with open(input_file, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            if len(columns) == 3:
                word, trans1, trans2 = columns[0], columns[1], columns[2]
                trans1_no_spaces = trans1.replace(" ", "")
                trans2_no_spaces = trans2.replace(" ", "")

                # Count coincidences character by character without counting spaces
                coincidences_all_lines += count_coincidences(trans1, trans2)
                total_chars_all += min(len(trans1_no_spaces), len(trans2_no_spaces))

                # Compare lines where trans1 and trans2 have the same number of characters
                if len(trans1_no_spaces) == len(trans2_no_spaces):
                    coincidences_same_length += count_coincidences(trans1, trans2)
                    total_chars_same_length += len(trans1_no_spaces)

    return (coincidences_all_lines, total_chars_all, 
            coincidences_same_length, total_chars_same_length)

def main(dialect, llevar_doblesacc):
    input_file = f'comprovar_{dialect}.txt'
    
    if llevar_doblesacc:
        processed_lines = preprocess_file(input_file)
        with open(input_file, 'w') as f:
            f.writelines(processed_lines)
    
    coincidences_all_lines, total_chars_all, coincidences_same_length, total_chars_same_length = process_file(input_file)
    
    ratio_all_lines = coincidences_all_lines / total_chars_all if total_chars_all > 0 else 0
    ratio_same_length = coincidences_same_length / total_chars_same_length if total_chars_same_length > 0 else 0
    
    print(f"Ratio of coincidences to total characters: {coincidences_all_lines}/{total_chars_all} = {100*ratio_all_lines:.1f}")
    print(f"Ratio of coincidences for lines with same length: {coincidences_same_length}/{total_chars_same_length} = {100*ratio_same_length:.1f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <dialect> [--llevar_doblesacc]")
        sys.exit(1)

    dialect = sys.argv[1]
    llevar_doblesacc = "--llevar_doblesacc" in sys.argv
    
    main(dialect, llevar_doblesacc)
