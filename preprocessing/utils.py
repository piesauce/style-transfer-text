import os




def merge_plays(path):
    plays_original_list = []
    plays_modern_list = []
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            if 'original' in filename:
                plays_original_list.append(os.path.join(dirname, filename))
            if 'modern' in filename:
                plays_modern_list.append(os.path.join(dirname, filename))
    with open('merged_plays_original.aligned', 'a+') as outfile:
        for fname in plays_original_list:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    with open('merged_plays_modern.aligned', 'a+') as outfile:
        for fname in plays_modern_list:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
