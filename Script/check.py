from gingerit.gingerit import GingerIt

def process_text_in_chunks(file_path, chunk_size=10000):
    ginger = GingerIt()
    corrected_text = []

    with open(file_path, 'r', encoding='utf-8') as file:
        chunk = file.read(chunk_size)
        while chunk:
            result = ginger.parse(chunk)
            corrected_chunk = result['result']
            corrected_text.append(corrected_chunk)
            chunk = file.read(chunk_size)
    
    return ''.join(corrected_text)

def save_corrected_text(output_path, text):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

# File paths
input_file_path = 'dan.txt'
output_file_path = 'corrected.txt'

# Process and correct the text
corrected_text = process_text_in_chunks(input_file_path)
save_corrected_text(output_file_path, corrected_text)

print(f'Corrected text has been saved to {output_file_path}')
