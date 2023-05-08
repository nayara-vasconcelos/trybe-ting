import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            lines = [line.strip() for line in file]
    except OSError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return lines
