file = open("db-inventory.txt", "a")
while True :
    opt = input("Input Data Inventory Baru (ya/tidak) ?")
    opt = opt.lower()
    print("***********************************************")
    if opt == "ya":
        x = input("Nama Perangkat :")
        y = input("Lokasi : ")
        print("-------------------------------------------")
    else:
        file = open("db-inventory.txt","r")
        for item in file :
            print(item)
        file.close()
        break
    file.write("Nama Perangkat : "+ (x + ",") + "Lokasi : "+ y + "\n")
file.close()
