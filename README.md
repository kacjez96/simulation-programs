# Programy Symulacyjne

### Struktura programu:

- main.py - Główny plik odpowiedzialny za przeprowadzenie symulacji.
  Zawiera ustawienia początkowe, funkcje generujące oraz symulacyjne.

> Skrypty znajdujące się w katalogu „scripts":

- FCFS.py - Moduł zawierający funkcję wykonującą algorytm planowania
  czasu procesora FCFS i zwracającą średnie czasy zwrotu oraz
  oczekiwania sekwencji procesów dla tego algorytmu.

- SJF.py - Moduł zawierający funkcję wykonującą algorytm planowania
  czasu procesora SJF (niewywłaszczający) i zwracającą średnie czasy
  zwrotu oraz oczekiwania sekwencji procesów dla tego algorytmu.

- FIFO.py - Moduł zawierający funkcję wykonującą algorytm zastępowania
  stron FIFO i zwracającą ilość błędów stron dla tego algorytmu.

- LRU.py - Moduł zawierający funkcję wykonującą algorytm zastępowania
  stron LRU i zwracającą ilość błędów stron dla tego algorytmu.

## **Algorytmy planowania czasu procesora**

Wykorzystane algorytmy i ich opis:

- **FCFS (First-Come, First-Served)** - Algorytm działa na zasadzie
  obsługi zadań w kolejności ich zgłoszenia do systemu. Procesy są
  umieszczane w kolejce według przybycia, a procesor wykonuje je jedno
  po drugim, od początku do końca, bez przerw. Dzięki swojej prostocie,
  FCFS jest łatwy do zaimplementowania i zrozumienia.

- **SJF (Shortest Job First) niewywłaszczający** - Algorytm działa na
  zasadzie priorytetowego wykonywania najkrótszych zadań. Gdy procesor
  staje się dostępny, wybiera spośród oczekujących zadań to, które ma
  najkrótszy czas wykonania. Proces, który zostanie wybrany, jest
  wykonywany do końca bez przerwy.

Przebieg symulacji

Symulacje rozpoczynamy uruchamiając główny plik main.py. Następuje wtedy
wygenerowanie 100 sekwencji, każda zawierająca po 100 procesów z
następującymi parametrami:

- Czas nadejścia -- losowo od 0 do 100

- Czas wykonania -- losowo od 1 do 20

Dane te zostają zapisane do plików w katalogu „processes" oraz używane
są do przeprowadzenia symulacji dla algorytmów planowania czasu
procesora. Następnie uruchomione zostają funkcję symulacyjne dla kolejno
algorytmów FCFS i SJF. Obliczone średnie czasy zwrotu i oczekiwania
procesu dla 100 sekwencji zostają zapisane do plików z wynikami w
katalogu „results".

Wyniki symulacji

**FCFS:**

- Średni czas zwrotu: 466.3543

- Średni czas oczekiwania: 476.8411

**SJF:**

- Średni czas zwrotu: 309.498

- Średni czas oczekiwania: 319.944

Wnioski

Algorytmy planowania czasu procesora FCFS (First-Come, First-Served) i
SJF (Shortest Job First) niewywłaszczający różnią się głównie w sposobie
wyboru zadań do wykonania, co wpływa na ich efektywność i praktyczne
zastosowanie.

FCFS działa na zasadzie obsługi zadań w kolejności ich przybycia. Jest
prosty do zaimplementowania i łatwy do zrozumienia, co stanowi jego
główną zaletę. Jednakże może prowadzić do długich czasów oczekiwania dla
krótszych zadań, jeśli przed nimi znajduje się długie zadanie, co jest
znane jako efekt konwoju. W takim przypadku krótkie zadania muszą
czekać, aż długie zadanie zostanie zakończone, co obniża efektywność
algorytmu.

Z kolei SJF niewywłaszczający priorytetowo traktuje zadania o
najkrótszym czasie wykonania. Kiedy procesor jest gotowy do przyjęcia
nowego zadania, wybiera spośród oczekujących to, które ma najkrótszy
czas wykonania. Dzięki temu algorytm minimalizuje średni czas
oczekiwania, ponieważ krótsze zadania są obsługiwane szybciej, co
redukuje kolejki zadań oczekujących na wykonanie.

Analizując przedstawione wyżej dane możemy stwierdzić, że o wiele lepiej
wypada algorytm SJF, ponieważ oferuje on lepsze czasy oczekiwania i
zwrotu.

## **Algorytmy zastępowania stron**

Wykorzystane algorytmy i ich opis:

- **FIFO (First-In, First-Out**) - Algorytm który działa na zasadzie
  \"pierwsze weszło, pierwsze wyszło\". Gdy system ładuje strony do
  pamięci, tworzy kolejkę, w której nowe strony są dodawane na końcu.
  Kiedy pamięć jest pełna i pojawia się potrzeba załadowania nowej
  strony, algorytm wybiera stronę, która znajduje się na początku
  kolejki -- czyli tę, która była w pamięci najdłużej -- i zastępuje ją
  nową stroną. Ta nowa strona jest następnie dodawana na koniec kolejki.

- **LRU (Least Recently Used) --** Algorytm, który zastępuje stronę,
  która była najdawniej używana, gdy trzeba zwolnić miejsce w pamięci.
  Śledzi czas ostatniego użycia każdej strony i wybiera tę, która była
  najdłużej nieaktywna. Dzięki temu zakłada, że strony niedawno używane
  będą potrzebne w najbliższej przyszłości, a te, które były używane
  dawno temu, mogą być zastąpione.

Przebieg symulacji

Symulacje rozpoczynamy uruchamiając główny plik main.py. Następuje wtedy
wygenerowanie 100 sekwencji, każda zawierająca po 100 stron z
następującym parametrem:

- Numer strony -- losowo od 1 do 20

Dane te zostają zapisane do plików w katalogu „pages" oraz używane są do
przeprowadzenia symulacji dla algorytmów zastępowania stron. Następnie
uruchomione zostają funkcję symulacyjne dla kolejno algorytmów FIFO i
LRU. Dla symulacji ustawiłem ilość ramek pamięci równą 3. Zliczone
ilości błędów stron oraz średnia dla 100 sekwencji dla obydwu algorytmów
zostają zapisane do plików z wynikami w katalogu „results".

Wyniki symulacji

**FIFO:**

- Średnia liczba błędów strony: 84.83

**LRU:**

- Średnia liczba błędów strony: 85.06

Wnioski

Algorytmy FIFO (First In, First Out) i LRU (Least Recently Used) to dwa
różne podejścia do zarządzania pamięcią operacyjną, używane w systemach
operacyjnych do zastępowania stron, gdy pamięć jest pełna.

FIFO jest bardzo prosty do zaimplementowania i łatwy do zrozumienia, co
stanowi jego główną zaletę. Jednak jego prostota ma również swoje wady.
Algorytm nie bierze pod uwagę częstości ani ostatniego użycia stron, co
może prowadzić do zastępowania stron, które są nadal często potrzebne.
Ponadto, może wystąpić zjawisko znane jako anomalne zachowanie
Belady\'ego, w którym zwiększenie liczby dostępnych ramek pamięci
paradoksalnie prowadzi do zwiększenia liczby błędów stron.

Implementacja algorytmu LRU może być realizowana za pomocą różnych
struktur danych, na przykład list dwukierunkowych lub hash map, co
umożliwia efektywne śledzenie i aktualizowanie znaczników czasu użycia.
Jest to stosunkowo prosty, ale skuteczny sposób na optymalizację
wykorzystania pamięci podręcznej, choć może wymagać dodatkowych zasobów
na przechowywanie informacji o ostatnim użyciu każdej strony.

Analizując wyniki symulacji możemy stwierdzić, że średnia ilość błędów
strony dla obu algorytmów jest bardzo zbliżona. Jednakże FIFO w tym
konkretnym przypadku osiągnął nieco lepsze rezultaty niż LRU.
