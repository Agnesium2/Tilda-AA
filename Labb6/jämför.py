import timeit


class Låt:

    def __init__(self, row):
        self.trackid = row[0]
        self.låttid = row[1]
        self.artistnamn = row[2]
        self.låttitel = row[3]

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn


def readfile(filename):
    låt_lista = []
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            row = row.strip().split("<SEP>")
            if len(row) == 4:
                låt_lista.append(Låt(row))
    return låt_lista


# Långsam sorteringsmetod: Bubble Sort O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Snabbare sorteringsmetod: Pythons inbyggda Timsort O(n log n)
def quick_python_sort(arr):
    arr.sort()


def main():
    filename = "unique_tracks.txt"
    stor_lista = readfile(filename)

    # Teststorlekar
    n_values = [1000, 10000, 100000, 1000000]

    for n in n_values:
        if n > len(stor_lista):
            break

        print(f"\n=================== n = {n} ===================")

        # 1. Bubble Sort (Körs endast för n <= 10000)
        if n <= 10000:
            lista_copy1 = stor_lista[0:n].copy()
            tid_slow = timeit.timeit(
                stmt=lambda: bubble_sort(lista_copy1), number=1
            )
            print(f"Bubble Sort:       {round(tid_slow, 4)} sekunder")
        else:
            print("Bubble Sort:       Hoppades över (tar för lång tid)")

        # 2. Pythons .sort() (Timsort)
        lista_copy2 = stor_lista[0:n].copy()
        tid_fast = timeit.timeit(
            stmt=lambda: quick_python_sort(lista_copy2), number=1
        )
        print(f"Pythons .sort():   {round(tid_fast, 4)} sekunder")


if __name__ == "__main__":
    main()

'''
När n ökar från 1000 till 10000 ökade tiden för bubble sort ca 100 ggr 
vilket stämmer för tidskomplexiteten O(n). Timsort tog bara 3.7 sek för 1 miljon
element eftersom den har tidskomplexitet O(n log n).

Linjärsökning O(n) innebär att elementen jämförs en och en och blir därför
mycket långsammare med en längre lista. Binärsökning O(log n) halverar sökytan
i varje steg som i ett binärträd, det krävs dock en sorterad lista. 
Hashtabell O(1) gör sökningen väldigt snabb oavsett storlek med hjälp av en dictionary.
'''