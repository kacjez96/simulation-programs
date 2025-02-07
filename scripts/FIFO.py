def fifo(sequence, f_size):
    frames = []     # Tablica pamięci przechowujące strony
    errors = 0      # Liczba błędów braku strony

    for page in sequence:   # Dla każdej strony w sekwencji

        if page not in frames:      # Jeżeli strony nie ma w pamięci

            if len(frames) == f_size:   # Jeżeli liczba stron w tablicy pamięci jest równa ilości dostępnych ramek
                frames.pop(0)       # Usunięcie najstarszej strony

            frames.append(page)     # Dodanie strony do pamięci
            errors += 1             # Zwiększenie liczby błędów

    return errors
