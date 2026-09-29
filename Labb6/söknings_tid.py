import timeit
#gemini

class Låt:

    def __init__(self, row):
        self.trackid = row[0]
        self.låttid = row[1]
        self.artistnamn = row[2]
        self.låttitel = row[3]

    def __str__(self):
        return f"Namn: {self.låttitel}, Artist: {self.artistnamn}"

    def __lt__(self, other):
        # Sorterar baserat på artistnamn
        return self.artistnamn < other.artistnamn


def readfile(filename):
    låt_lista = []
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            row = row.strip().split("<SEP>")
            if len(row) == 4:
                låt_lista.append(Låt(row))
    return låt_lista


def linsok(lista, target):
    for lat in lista:
        if lat.artistnamn == target:
            return lat
    return None


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid].artistnamn == target:
            return arr[mid]
        elif arr[mid].artistnamn > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


def main():
    filename = "unique_tracks.txt"

    stor_lista = readfile(filename)

    # n = 250000, 500000, 1000000
    n = 1000000
    lista = stor_lista[0:n]
    print(f"--- Mäter för n = {len(lista)} ---")

    # sökämne (sista elementets artist)
    sista_lat = lista[-1]
    testartist = sista_lat.artistnamn

    number_of_searches = 100

    # --- 1. Linjärsökning i osorterad lista ---
    linjtid = timeit.timeit(
        stmt=lambda: linsok(lista, testartist), number=number_of_searches
    )
    print(
        f"Linjärsökning:         {round(linjtid, 4)} sekunder (totalt för {number_of_searches} sökningar)"
    )

    # --- 2. Binärsökning i sorterad lista ---
    # Sortera listan först (tid för sortering mäts inte med i sökningen)
    sorterad_lista = sorted(lista)
    bintid = timeit.timeit(
        stmt=lambda: binary_search(sorterad_lista, testartist),
        number=number_of_searches,
    )
    print(f"Binärsökning:          {round(bintid, 4)} sekunder")

    # --- 3. Sökning i hashtabell (dict) ---
    # Skapa en dictionary med artistnamn som nyckel
    hashtabell = {lat.artistnamn: lat for lat in lista}
    hash_tid = timeit.timeit(
        stmt=lambda: hashtabell.get(testartist), number=number_of_searches
    )
    print(f"Sökning i hashtabell:  {round(hash_tid, 6)} sekunder")


if __name__ == "__main__":
    main()