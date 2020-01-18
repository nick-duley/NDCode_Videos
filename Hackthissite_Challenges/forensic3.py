#This code is designed to help the user with the challenge "Forensic 3"
#https://www.hackthissite.org/missions/forensic/3/

#Open and read the binary data of the image file
#Change the file path below to ensure it points to where you've stored the "shh.jpg" file
f = open("/root/Documents/Forensic 3/flashdrive/shh.jpg", "rb")
r = f.read()
f.close()

#Global variables
File_List = ["rar", "jpg"]
Header_Array = []
Trailer_Array = []
start = 0
File_Number = 0

#Iteration through the jpg and rar files, looking for the matching bytes.
#If header and trailer bytes match, save the file
for fi in range(start, len(File_List)):

    if (File_List[fi] == "jpg"):
        Header_Array = [255, 216, 255, 224]
        Trailer_Array = [255, 217]
    else:
        Header_Array = [82, 97, 114, 33]
        Trailer_Array = [0, 64, 7, 0]

    #Search and save the header bytes from the indexes above,
    #first byte won't match because of offsets, IndexError is caught
    Key_List = []
    for i in range(start, len(r)):
        try:
            if (r[i+1] == Header_Array[1] and r[i+2] == Header_Array[2] and r[i+3] == Header_Array[3]):
                Key_List.append(i)
        except IndexError:
            pass

    #Now search and save the trailer bytes, IndexError is caught
    for j in range(start, len(Key_List)):
        Byte_List = []
        for i in range(Key_List[j], len(r)):
            Byte_List.append(r[i])
            try:
                if (i > 0):
                    if (File_List == "jpg"):
                        if (r[i-1] == Trailer_Array[0] and r[i] == Trailer_Array[1]):
                            break
                    else:
                        if (r[i-3] == Trailer_Array[0] and r[i-2] == Trailer_Array[1] and r[i-1] == Trailer_Array[2] and r[i] == Trailer_Array[3]):
                            break
            except IndexError:
                pass

        #Error correction for the first byte
        Byte_List[0] = Header_Array[0]

        #Write every rar and jpg file found to the "output" folder
        #Change the file path below to ensure it points to where you've stored the "output" folder
        file = open("/root/Documents/Forensic 3/output/"+str(File_Number)+"."+File_List[fi], "wb")
        file.write(bytearray(Byte_List))
        file.close()
        File_Number += 1
