import argparse
import os

def main():

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-a', '--path_a', help='Path A.', required=True)
    parser.add_argument('-b', '--path_b', help='Path B.', required=True)
    args = parser.parse_args()

    # parse two arguments passed to the shell command
    path_a = args.path_a
    path_b = args.path_b

    def strip_filenames(path):
        return map(lambda x: os.path.splitext(x)[0], path)

    def print_non_matching_files(base_path, lookup_path):

        base_path_files = os.listdir(base_path)
        lookup_path_files = os.listdir(lookup_path)

        print('\033[92m' + '\033[1m' + f"Files in {base_path} that are not in {lookup_path}" + '\033[0m')
        for filename in strip_filenames(base_path_files):
            if filename not in strip_filenames(lookup_path_files):
                print(f"    {filename}")

    kitty = """

        _                ___       _.--.
        \`.|\..----...-'`   `-._.-'_.-'`
        /  ' `         ,       __.--'
        )/' _/     \   `-_,   /
        `-'" `"\_  ,_.-;_.-\_ ',     fsc/as
            _.-'_./   {_.'   ; /
           {_.-``-'         {_/

    GUIDO WILL NOW COMPARE FOLDERS FOR YOU.

    (TOSS A SNACK TO YOUR GUIDO).

    """

    print(kitty)
    print_non_matching_files(path_a, path_b)
    print_non_matching_files(path_b, path_a)

if __name__ == '__main__':
    main()
