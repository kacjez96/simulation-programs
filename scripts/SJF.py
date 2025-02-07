def sjf(sequence):
    n = len(sequence)  # Długość sekwencji

    s_sorted = sorted(sequence, key=lambda a: a[0])     # Utworzenie posortowanej pod względem czasu przyjścia kopii sekwencji w zmiennej s_sorted
    queue = []          # Utworzenie listy obecnej kolejki procesów

    current_time = 0        # Obecny czas
    turnaround_time = []  # Tablica czasów zwrotu
    waiting_time = []  # Tablica czasów oczekiwania

    for i in range(n):
        # Dodawanie procesów do kolejki, które przybyły do obecnego czasu
        while s_sorted and s_sorted[0][0] <= current_time:      # Sprawdzenie czy proces właśnie przyszedł (jego czas przyjścia jest mniejszy albo równy wartości obecnego czasu)
            queue.append(s_sorted.pop(0))           # Usunięcie procesu z listy kopii sekwencji i dodanie go do kolejki

        if queue:           # Jeżeli kolejka nie jest pusta
            queue.sort(key=lambda b: b[1])  # Sortowanie wedlug czasu trwania
            arrival_time, burst_time = queue.pop(0)     # Przypisanie do zmiennych czasów procesu pierwszego w kolejce

            start_time = current_time       # Obliczenie czasu startu procesu
            current_time += burst_time      # Zwiększenie obecnego czasu o czas trwania procesu
            finish_time = current_time      # Obliczenie czasu zakończenia procesu

            # Obliczenie czasów zwrotu i oczekiwania danego procesu
            turnaround = finish_time - arrival_time
            waiting = turnaround - burst_time

            # Przypisanie tych wartości do odpowiednich tablic
            turnaround_time.append(turnaround)
            waiting_time.append(waiting)
        elif s_sorted:          # Jeżeli kolejka jest pusta i przychodzą jakieś procesy (lista s_sorted nie jest pusta)
            current_time = s_sorted[0][0]       # Ustawienie obecnego czasu na czas przyjścia procesu

    total_turnaround_time = sum(turnaround_time)        # Zsumowanie czasów zwrotu
    total_wait_time = sum(waiting_time)                 # Zsumowanie czasów oczekiwania

    # Obliczenie średniej
    avg_total_turnaround_time = total_turnaround_time / float(n)
    avg_total_wait_time = total_wait_time / float(n)
    return avg_total_turnaround_time, avg_total_wait_time
