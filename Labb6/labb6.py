class Låt:
#person
    def __init__(self, låt):
        self.trackid = låt[0]
        self.låttid = låt[1]
        self.artistnamn = låt[2]
        self.låttitel = låt[3]

    def __str__(self):
        return "Namn: "+ self.låttitel + ", Artist: "+ self.artistnamn

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn



def main():
    with open("unique_tracks.txt", "r", encoding="utf-8") as file:
        låt_list = []
        for row in file:
            row = row.strip().split("<SEP>")
            ny_låt = Låt(row)
            låt_list.append(ny_låt)

    låt_list.sort()
    for låt in låt_list:
        print(låt)
main()
