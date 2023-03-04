# Prezentacja postępów – metody uczenia - Drzewa Decyzyjne
**Temat:** Inteligentna śmieciarka

**Zespół:** Maciej Barabasz, Adam Hącia, Marcin Krupiński, Kajetan Gałęziowski 

**Przyrost:** Drzewa decyzyjne

## Przygotowanie zestawu uczącego

Import danych:

```python
X1 = []
view = []
with open("DecisionTreeFiles/database.txt", 'r') as f:
    for line in f:
        line = line.strip()
        test_list = [int(i) for i in line]
        x = []
        if line[0] == "0":
            x.append("even")
        else:
            x.append("odd")
        if line[1] == "0":
            x.append("bad size")
        else:
            x.append("good size")
        if line[2] == "0":
            x.append("heavy")
        else:
            x.append("light")
        if line[3] == "0":
            x.append("not paid")
        else:
            x.append("paid")
        if line[4] == "0":
            x.append("cannot close bin")
        else:
            x.append("can close")
        if line[5] == "0":
            x.append("no space")
        else:
            x.append("free space")
        if line[6] == "0":
            x.append("paper")
        elif line[6] == "1":
            x.append("plastic")
        elif line[6] == "2":
            x.append("glass")
        else:
            x.append("mixed")
        if line[7] == "0":
            x.append("day")
        else:
            x.append("night")
        view.append(x)
        X1.append(test_list)

f = open("DecisionTreeFiles/learning_set.txt", "w")
for i in view:
    f.write(str(i)+"\n")
f.close()

Y1 = []
with open("DecisionTreeFiles/decissions.txt", 'r') as f:
    for line in f:
        line = line.strip()
        test = int(line)
        Y1.append(test)

```

Przykładowe zestawy ze zbioru uczącego zawierającego 216 zestawów:
```python
    
    dataset = [
        ['even', 'good size', 'heavy', 'paid', 'can close', 'free space', 'glass', 'night'],
        ['even', 'good size', 'light', 'not paid', 'can close', 'free space', 'paper', 'day'],
        ['even', 'good size', 'light', 'not paid', 'cannot close bin', 'no space', 'mixed', 'day'],
        ['odd', 'bad size', 'light', 'not paid', 'cannot close bin', 'no space', 'paper', 'day'],
        ['even', 'bad size', 'heavy', 'not paid', 'can close', 'no space', 'glass', 'day'],
        ['odd', 'good size', 'light', 'paid', 'can close', 'free space', 'paper', 'day'],...]
    decisions = [1,0,0,0,0,1,...]
```

Każdą decyzję odnośnie zebrania odpadu podejumuje według następujących czynników:

`Day` - informacja czy dzień jest parzysty (0 - parzysty, 1 - nieparzysty)

`Size of trash bin` - informacja o tym, czy rozmiar śmietnika jest zgodny z zasadami (0 - nie jest, 1 jest)

`Weight` - informacja o wadze pojemnika (0 - powyej 80 kg, 1 - poniej 80 kg)

`Bill` - informacja o tym, czy rachunek jest zapłacony (0 - nie zapłacony, 1 - zapłacony)

`Closable` - informacja o tym, czy kubeł mona zamknąć (inaczej, czy nic nie wystaje poza kubeł) (0 - nie można domknąć, 1 - można zamknąć)

`Space on trash yard` - informacja, czy na danym sektorze wysypiska jest miejsce (0 - brak miejsca, 1 - jest miejsce)

`Type of trash` - informacja o rodzaju odpadu (0 - papier, 1 - plastik, 2 - szkło, 3 - zmieszane)

`Time of day` - informacja o porze dnia (0 - dzień, 1 - noc)

### Tworzenie drzewa

``` python
        DecisionTreeClassifier(random_state=0, max_depth=20).fit(self.dataset, self.decision)
```

### Wygenerowane drzewo
``` python
|--- Space on Yard <= 0.50
|   |--- class: 0
|--- Space on Yard >  0.50
|   |--- Bill <= 0.50
|   |   |--- class: 0
|   |--- Bill >  0.50
|   |   |--- Time <= 0.50
|   |   |   |--- Size <= 0.50
|   |   |   |   |--- class: 0
|   |   |   |--- Size >  0.50
|   |   |   |   |--- Weight <= 0.50
|   |   |   |   |   |--- class: 0
|   |   |   |   |--- Weight >  0.50
|   |   |   |   |   |--- Closable <= 0.50
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- Closable >  0.50
|   |   |   |   |   |   |--- Type <= 2.50
|   |   |   |   |   |   |   |--- Type <= 0.50
|   |   |   |   |   |   |   |   |--- Day <= 0.50
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- Day >  0.50
|   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- Type >  0.50
|   |   |   |   |   |   |   |   |--- Day <= 0.50
|   |   |   |   |   |   |   |   |   |--- Type <= 1.50
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- Type >  1.50
|   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |--- Day >  0.50
|   |   |   |   |   |   |   |   |   |--- Type <= 1.50
|   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |--- Type >  1.50
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- Type >  2.50
|   |   |   |   |   |   |   |--- class: 1
|   |   |--- Time >  0.50
|   |   |   |--- Type <= 2.50
|   |   |   |   |--- Type <= 1.50
|   |   |   |   |   |--- Day <= 0.50
|   |   |   |   |   |   |--- Size <= 0.50
|   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |--- Size >  0.50
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- Day >  0.50
|   |   |   |   |   |   |--- Type <= 0.50
|   |   |   |   |   |   |   |--- Size <= 0.50
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- Size >  0.50
|   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |--- Type >  0.50
|   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |--- Type >  1.50
|   |   |   |   |   |--- Day <= 0.50
|   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |--- Day >  0.50
|   |   |   |   |   |   |--- class: 0
|   |   |   |--- Type >  2.50
|   |   |   |   |--- class: 1
```
### Podejmowanie decyzji

```python
    def make_decision(self,trash, trash_type):

        # Check if day is odd or even
        day = int((settings.current_day // 1) % 2)

        if (settings.current_day % 1) == 0:
            time_of_day = 0
        else:
            time_of_day = 1
            

        # Check if size of trash bin is okay
        if (trash.width <= 30 & trash.length <= 30 & trash.height <= 130):
            size = 1
        else:
            size = 0

        # Check if weight is okay
        if (trash.weight <= 80):
            weight = 1
        else:
            weight = 0

        # Check if bills were paid
        if (trash.bills_paid):
            bill = 1
        else:
            bill = 0

        # Check if bin was closed
        if (trash.bin_closed):
            can = 1
        else:
            can = 0

        # Check if specific trash yard is full
        if (settings.trash_capacity[trash_type] < settings.max_capacity):
            trash_yard = 0
        else:
            trash_yard = 1

        test_data_full = [[day, size, weight, bill, can, trash_yard, trash_type,time_of_day]]

        print("Test on: ")
        print(test_data_full)
        print("Decision:")
        print(self.decision_tree.predict(test_data_full)[0])
        return self.decision_tree.predict(test_data_full)[0]
```

### Obserwacje
Program podejmuję odpowiednie decyzję jak postępować w przypadku trafienia na pole z odpadem.
