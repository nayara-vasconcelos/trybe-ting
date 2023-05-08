import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    for i in range(0, len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(file)
    print(file, file=sys.stdout)


def remove(instance):
    try:
        file_name = instance.dequeue()["nome_do_arquivo"]
    except IndexError:
        print("Não há elementos", file=sys.stdout)
    else:
        print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
    else:
        print(file, file=sys.stdout)
