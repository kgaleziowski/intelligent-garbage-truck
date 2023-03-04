# AI - Inteligentna Śmieciarka - raport końcowy
Kompletny projekt na gałęzi po_przyroscie3 na wydziałowym githubie: https://git.wmi.amu.edu.pl/s452758/DSZI-gr.15-Zlomiarze 

# Realizacja poszczególnych przyrostów:
Przy konkretnym przyroście wypisane są osoby, które miały wiodący wpływ na wykonanie poszczególnego segmentu, przy czym należy zaznaczyć, że każda część składowa projektu była realizowana  w większości wspólnie i od strony koncepcyjnej oraz wykonawczej finalny efekt zawsze był wspólną wizją, która czasami realizowała jedna osoba, czasami więcej.

##### Środowisko wykonania:
- Maciej Barabasz, Marcin Krupiński

##### Reprezentacja wiedzy: 
- Maciej Barabasz, Adam Hącia

##### Planowanie ruchu cz.1: 
- Kajetan Gałęziowski

##### Planowanie ruchu cz.2: 
- Kajetan Gałęziowski

##### Drzewa Decyzyjne: 
- Adam Hącia, Marcin Krupiński

##### Sieci neuronowe: 
- Adam Hącia, Marcin Krupiński, Maciej Barabasz

##### Algorytmy genetycze: 
- Kajetan Gałęziowski

# Spójność projektu:
Żadna funkcjonalność realizowana w ramach danego przyrostu nie pojawiła się w projekcie na siłę - w środowisku naszej inteligentnej śmieciarki nie ma zbędnych rzeczy. Najważniejsze przyrosty, czyli te dotyczące metod uczenia, ostatecznie pozwoliły spiąć projekt w całość:

a) drzewa decyzyjne - zbudowane z racjonalnych atrybutów, które nie są oderwane od projektowej rzeczywistości, wykorzystywane są w momencie podjazdu śmieciarki do punktu odbioru śmieci (kosza)

b) sieci neuronowe - wykorzystane w prawdopodobnie najlepszy możliwy sposób w projekcie, czyli do odróżniania typu śmiecia, który znajduje się w koszu, zrealizowane z dość dobrą efektywnością

c) algorytmy genetyczne - wykorzystane w celu rozwiązania problemu komiwojażera (TSP), wyznaczają na drodze uczenia jak najlepszą sekwencję odwiedzania kolejnych koszy na śmieci

# Dodatkowe kwestie:
W naszym projekcie stawialiśmy na poznanie w jak najlepszy sposób technik i metod, które mieliśmy wykonywać na poszczególne przyrosty. W imię tego, powstały dodatkowe funkcjonalności, które pozwalają projektem dosłownie się bawić i weryfikować pewne rzeczy:

- oprócz zwykłego poruszania się agenta i możliwości poruszania się za pomocą strzałek, powstał mechanizm pozwalający jechać do wybranego celu poprzez kliknięcie lewym przyciskiem myszy (wybór celu) oraz potwierdzenie trasy prawym przyciskiem myszy - powstało to po to, aby móc zobrazować niezależnie od sytuacji, przewagę algorytmu A* nad BFS, ponieważ łatwo sprowokować przypadki, w których algorytmy wybiorą inne trasy

- na naszej kracie istnieje możliwość rozkładania elementów i tworzenia własnych konfiguracji mapy, poprzez klik + T możemy postawić kosz na śmieci, zaś poprzez klik + O rozstawiamy przeszkody, następnie taką konfigurację możemy zapisać poprzez wciśnięcie przycisku S - zostanie wykonany zrzut mapy do pliku .csv, który można następnie odtworzyc w dowolonym momencie

- sposób wykonania algorytmów genetycznych obrazuje cały proces, pozwala na modyfikację poszczególnych parametrów (współczynnik mutacji, liczba osobników w populacji, rozmiar elity), dodatkowo generowany jest wykres, który pokazuje efektywność algorytmu

- poprzedni punkt w połączeniu z możliwością konfiguracji mapy zgodnie z preferencjami pozwala na jeszcze głębsze analizowanie procesów związanych z algorytmami genetycznymi, możemy tak rozstawić śmietniki i przeszkody, aby wymusić konkretne sytuacje, zderzyć nasze przewidywania z wynikiem algorytmu

- całość projektu została wykonana z dbałością o to, aby użytkownik nie musiał domyślać się na co patrzy, wszystko co jest widoczne na ekranie jest jasne i jednoznaczne, oprócz tego, został dodany HUD, czyli ktoś kto patrzy jak śmieciarka jeździ, widzi bezpośrednio dlaczego podejmuje jakie decyzje, ponieważ jeżeli np. kosz jest za ciężki (odrzucamy wtedy podjęcie śmiecia), to pojawia się na ekranie odpowiedni obrazek

- dodatkowym atutem jest wyświetlanie obrazku śmiecia, czyli tego co traktujemy za rzecz znajdującą się w śmietniku