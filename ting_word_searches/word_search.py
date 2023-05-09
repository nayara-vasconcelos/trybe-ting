import re


def get_all_files(instance):
    files = []

    if len(instance) > 0:
        # É mais interessante fazer unqueue e queue por
        # len(instance) vezes para manter a complexidade
        # de tempo O(n) em vez de O(n²)?
        for i in range(0, len(instance)):  # O(n)
            files.append(instance.search(i))  # O(n)

    return files


def find_occurrences(file, word):
    occurrences = []

    for i, line in enumerate(file["linhas_do_arquivo"]):  # O(n)
        if len(re.findall(word, line, re.IGNORECASE)) > 0:
            occurrences.append({"linha": i + 1, "conteudo": line})

    return occurrences


def exists_word(word, instance):
    files = get_all_files(instance)
    matches = []

    if len(files) > 0:
        for file in files:
            occurrences = find_occurrences(file, word)
            if len(occurrences) > 0:
                match = {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": [
                        {"linha": occurrence["linha"]}
                        for occurrence in occurrences
                    ],
                }
                matches.append(match)

    return matches


def search_by_word(word, instance):
    files = get_all_files(instance)
    matches = []

    if len(files) > 0:
        for file in files:
            occurrences = find_occurrences(file, word)
            if len(occurrences) > 0:
                match = {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
                matches.append(match)

    return matches
