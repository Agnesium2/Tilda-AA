import csv

class Drama:
    def __init__(self, drama):
        self.name = drama[0]
        self.rating = float(drama[1])
        self.actors = drama[2]
        self.viewship = float(drama[3])
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = int(drama[7])
        self.episodes = int(drama[8])
        self.network = drama[9]
    def __str__(self):
        return self.name + " dramat kom ut " + str(self.year) + " med ratingen " + str(self.rating)
    def __lt__(self, other):
        return self.rating < other.rating
         
    def good_rating(self):
        if self.rating > 8:
            print(self.name + " " + str(self.rating))
    def release_date(self):
        if self.year > 2012:
            print(self.name + " " +str(self.year))
       # return self.year > 2015
    
def filereader(filename):
    with open(filename, mode="r") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvfile:
            print(row)

def read_file_to_list(filename):
    dramalist= []
    with open(filename, mode="r") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvfile:
                newdrama = Drama(row)
                dramalist.append(newdrama)
    return dramalist

def main():
    row1 = ["Legend of the Blue Sea",8.1,"Jun Ji-hyun, Lee Min-ho",17.6,"Fantasy,Romance,Comedy","Jin Hyuk, Park Seon-Ho","Park Ji-eun",2016,21,"SBS"]
    row2 = ["The Heirs",7.5,"Lee Min-ho, Park Shin-hye, Kim Woo-bin, Park Hyung-sik",16.7,"Romance, Drama, Teen","Kang Shin-hyo, Boo Sung-chul","Kim Eun-sook",2013,20,"SBS"]
    drama1 = Drama(row1)
    drama2 = Drama(row2)
    print(drama1, drama2)

    drama1.release_date()
    drama2.release_date()

    drama1.good_rating()
    drama2.good_rating()

    drama1_2 = [drama1, drama2]
    drama1_2.sort()
    for row in drama1_2:
        print(row)


    dramalist = read_file_to_list("kdrama.csv")

    for row in dramalist:
        row.release_date()
    for row in dramalist:
        row.good_rating()
    for row in dramalist:
        print(row)
   
        
    dramalist.sort()
    for row in dramalist:
        print(row)

    search_word = input("Vilken kdrama letar du efter, skriv namnet:)  : ")
    found = False
    for row in dramalist:
        if search_word  == row.name:
            print("Yeeey! filmen finns på listan:")
            print(row)
            found = True
    if found == False:
        print("Den fanns tyvärr ej")

main()


