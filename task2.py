#   RECREATING THE FILE WITH THE NAME OF NEW_A.PDF
# 
# from PyPDF2 import PdfFileWriter as w
# pdf=w()

sentence_file=open("output.txt","r")
num_file=open("number_data.txt")

with open("new_a.txt","w") as new_pdf:

    #readin lines from files created during task 1
    sentences=sentence_file.readlines()
    numbers=num_file.readlines()
    
    #adding data to new_file
    for index in range(len(sentences)):
        new_pdf.write("{}. {}.  {}".format(index,sentences[index].splitlines()[0],numbers[index]))
    
sentence_file.close()
num_file.close()