import random
import csv
import os

from scripts import FCFS, FIFO, LRU, SJF


class Process:
    def __init__(self, num_seq, num_proc, path, low_b, up_b):
        # Utworzenie tablicy wszystkich procesów
        self.proc_list = []

        # Przypisanie ustawień początkowych do zmiennych
        self.num_seq = num_seq
        self.num_proc = num_proc
        self.path = path
        self.low_b = low_b
        self.up_b = up_b

    def gen_save_processes(self):
        proc_path = self.path + "\\processes"       # Ustawienie scieżki do katalogu processes
        os.chdir(proc_path)                         # Przejście do katalogu processes

        # Pętla odpowiedzialna za wylosowanie czasu trwania oraz przyjścia procesu i przypisanie go do pliku csv oraz tablicy procesów
        for i in range(self.num_seq):
            proc_sublist = []                       # Utworzenie podlisty procesów dla każdej sekwencji
            filename = f"{str(i)}.csv"
            file = open(filename, "w", newline='')
            csv.writer(file).writerow(["process", "arrival_time", "burst_time"])    # Utworzenie nagłówków w pliku csv
            for j in range(self.num_proc):
                # Przypisanie losowych czasów trwania oraz przyjścia procesu
                arrival_time = random.randint(0,100)            # stały zakres [0,100] dla czasów przyjścia
                burst_time = random.randint(self.low_b, self.up_b)

                proc_sublist.append([arrival_time,burst_time])         # Dodanie czasów do podtablicy procesów
                csv.writer(file).writerow([f"P{j}", arrival_time, burst_time])      # Dodanie czasów do pliku csv
            file.close()
            self.proc_list.append(proc_sublist)     # Dodanie podlisty danej sekwencji do listy głównej
        os.chdir(self.path)         # Powrót do katalogu głównego programu


    def fcfs_sim(self):
        results_path = self.path + "\\results"
        os.chdir(results_path)                  # Przejście do katalogu results

        fcfs_turnaround_results = []                # Utworzenie tablicy wyników średnich pierwotnych (J.S. ©) czasów zwrotu algorytmu FCFS
        fcfs_wait_results = []                      # Utworzenie tablicy wyników średnich pierwotnych (J.S. ©) czasów oczekiwania algorytmu FCFS

        file = open("FCFS_results.csv", 'w', newline='')
        csv.writer(file).writerow(['ID', 'Turnaround Time', 'Waiting Time'])

        # Pętla odpowiedzialna za zapisanie wyników
        for i in range(self.num_seq):
            result = [i]        # ID sekwencji
            result += FCFS.fcfs(self.proc_list[i])   # Przypisanie wyników funkcji algorytmu FCFS

            # Zapisanie wyników do odpowiednich zmiennych
            fcfs_wait_results.append(result[1])
            fcfs_turnaround_results.append(result[2])

            csv.writer(file).writerow(result)       # Zapisanie wyników do pliku csv

        # Obliczenie średnich wtórnych (J.S ©) czasów oczekiwania i zwrotu
        sum_avg_turnaround_time = sum(fcfs_turnaround_results) / float(self.num_seq)
        sum_avg_wait_time = sum(fcfs_wait_results) / float(self.num_seq)

        # Zapisanie obliczonych średnich do pliku csv
        csv.writer(file).writerow('')
        csv.writer(file).writerow(['Average Times', sum_avg_turnaround_time, sum_avg_wait_time])
        file.close()
        os.chdir(self.path)     # Powrót do katalogu głównego programu

    def sjf_sim(self):
        results_path = self.path + "\\results"
        os.chdir(results_path)                  # Przejście do katalogu results

        sjf_turnaround_results = []         # Utworzenie tablicy wyników średnich pierwotnych (J.S. ©) czasów zwrotu algorytmu SJF
        sjf_wait_results = []               # Utworzenie tablicy wyników średnich pierwotnych (J.S. ©) czasów oczekiwania algorytmu SJF

        file = open("SJF_results.csv", 'w', newline='')
        csv.writer(file).writerow(['ID', 'Turnaround Time', 'Waiting Time'])

        # Pętla odpowiedzialna za zapisanie wyników (takie same działanie jak dla FCFS)
        for i in range(self.num_seq):
            result = [i]
            result += SJF.sjf(self.proc_list[i])
            sjf_wait_results.append(result[1])
            sjf_turnaround_results.append(result[2])
            csv.writer(file).writerow(result)

        # Obliczenie średnich wtórnych (J.S. ©) czasów oczekiwania i zwrotu
        sum_avg_turnaround_time = sum(sjf_turnaround_results) / float(self.num_seq)
        sum_avg_wait_time = sum(sjf_wait_results) / float(self.num_seq)

        # Zapisanie obliczonych średnich do pliku csv
        csv.writer(file).writerow('')
        csv.writer(file).writerow(['Average Times', sum_avg_turnaround_time, sum_avg_wait_time])
        file.close()
        os.chdir(self.path)         # Powrót do katalogu głównego programu


class Page:
    def __init__(self, num_seq, num_page, path, low_n, high_n, f_size):
        # Utworzenie tablicy wszystkich stron
        self.page_list = []

        # Przypisanie ustawień początkowych do zmiennych
        self.num_seq = num_seq
        self.num_page = num_page
        self.path = path
        self.low_n = low_n
        self.high_n = high_n
        self.f_size = f_size

    def gen_save_pages(self):
        page_path = self.path + "\\pages"       # Ustawienie scieżki do katalogu pages
        os.chdir(page_path)                         # Przejście do katalogu pages

        # Pętla odpowiedzialna za wylosowanie numeru strony i przypisanie go do pliku csv oraz tablicy stron
        for i in range(self.num_seq):
            page_sublist = []                       # Utworzenie podlisty stron dla każdej sekwencji
            filename = f"{str(i)}.csv"
            file = open(filename, "w", newline='')
            csv.writer(file).writerow(["page", "burst_time"])       # Dodanie nagłowków do pliku csv
            for j in range(self.num_page):
                p_number = random.randint(self.low_n, self.high_n)      # Przypisanie losowego numeru strony

                page_sublist.append(p_number)           # Dodanie numeru do podtablicy stron
                csv.writer(file).writerow([f"P{j}", p_number])      # Dodanie numeru do pliku csv
            file.close()
            self.page_list.append(page_sublist)     # Dodanie podlisty danej sekwencji do listy głównej
        os.chdir(self.path)     # Powrót do katalogu głównego programu

    def fifo_sim(self):
        results_path = self.path + "\\results"
        os.chdir(results_path)          # Przejście do katalogu results

        results = []        # Utworzenie tablicy błędów

        file = open("FIFO_results.csv", 'w', newline='')
        csv.writer(file).writerow(['ID', 'Errors'])     # Dodanie nagłówków do pliku csv

        # Pętla odpowiedzialna za przypisanie wyniku ilości błędów do pliku csv i zmiennej
        for i in range(self.num_seq):
            result = [i, FIFO.fifo(self.page_list[i], self.f_size)]
            csv.writer(file).writerow(result)
            results.append(result[1])

        # Obliczenie średniej ilości błędów
        avg_num_errors = sum(results) / float(self.num_seq)

        # Zapisanie obliczonego wyniku do pliku csv
        csv.writer(file).writerow('')
        csv.writer(file).writerow(["Average errors", avg_num_errors])
        file.close()
        os.chdir(self.path)     # Powrót do katalogu głównego


    def lru_sim(self):
        results_path = self.path + "\\results"
        os.chdir(results_path)          # Przejście do katalogu results

        results = []        # Utworzenie tablicy błędów

        file = open("LRU_results.csv", 'w', newline='')
        csv.writer(file).writerow(['ID', 'Errors'])     # Dodanie nagłówków do pliku csv

        # Pętla odpowiedzialna za przypisanie wyniku ilości błędów do pliku csv i zmiennej
        for i in range(self.num_seq):
            result = [i, LRU.lru(self.page_list[i], self.f_size)]
            csv.writer(file).writerow(result)
            results.append(result[1])

        # Obliczenie średniej ilości błędów
        avg_num_errors = sum(results) / float(self.num_seq)

        # Zapisanie obliczonego wyniku do pliku csv
        csv.writer(file).writerow('')
        csv.writer(file).writerow(["Average errors", avg_num_errors])
        file.close()
        os.chdir(self.path)     # Powrót do katalogu głównego

def main_processes():
    # Ustawienia
    random.seed(101)                    # Ziarno dla funkcji random, aby wyniki były powtarzalne
    number_of_processes = 100           # Liczba k procesów
    number_of_sequences = 100           # Liczba n sekwencji procesów użytych do symulacji
    lower_bound = 1                     # Dolna granica czasu wykonania procesu (burst time)
    upper_bound = 20                    # Górna granica czasu wykonania procesu (burst time)
    main_path = os.getcwd()             # Obecna ścieżka programu

    # Utworzenie klasy Process z ustawieniami podanymi powyżej
    program_proc = Process(number_of_sequences, number_of_processes, main_path, lower_bound, upper_bound)

    program_proc.gen_save_processes()   # Wywołanie funkcji genererującej n sekwencji, każda po k losowych czasów procesów z zakresu [a,b] oraz zapisanie ich do plików csv

    program_proc.fcfs_sim()             # Wywołanie funkcji symulacyjnej FCFS
    program_proc.sjf_sim()              # Wywołanie funckji symulacyjnej SJF

def main_pages():
    # Ustawienia
    random.seed(17)                     # Ziarno dla funkcji random, aby wyniki były powtarzalne
    number_of_pages = 100               # Liczba k stron
    number_of_sequences = 100           # Liczba n sekwencji stron użytych do symulacji
    lowest_number = 1                   # Dolna granica numeru strony
    highest_number = 20                 # Górna granica numeru strony
    frame_size = 3                      # Ilość ramek pamięci
    main_path = os.getcwd()             # Obecna ścieżka programu

    # Utworzenie klasy Page z ustawieniami podanymi powyżej
    program_page = Page(number_of_sequences, number_of_pages, main_path, lowest_number, highest_number, frame_size)

    program_page.gen_save_pages()   # Wywołanie funkcji genererującej n sekwencji, każda po k losowych numerów stron z zakresu [a,b] oraz zapisanie ich do plików csv

    program_page.fifo_sim()         # Wywołanie funkcji symulacyjnej FIFO
    program_page.lru_sim()          # Wywołanie funkcji symulacyjnej LRU

if __name__ == "__main__":
    main_processes()        # Wywołanie funkcji głównej dla algorytmów przydziału czasu procesora
    main_pages()            # Wywołanie funkcji głównej dla algorytmów zastępowania stron