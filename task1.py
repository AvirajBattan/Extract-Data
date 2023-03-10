# =====================TASK-1=============================

#IMPORTING LIBRARY TO HANDLE TO PDF ( we can not use normal file handling to handle pdf because of different encoding scheme used in pdf)
import PyPDF2

#creating the output file and set appending mode. This file will contain all the sentences.
with open("output.txt","w") as output_file:


    #number_data file is created which will contains the numeric data associated with sentence. THIS FILE WILL BE USED IN TASK-2 to recreate the pdf file. 
    num_file=open("number_data.txt","w")
    privious_data= " "

    read_file=PyPDF2.PdfReader("a.pdf")
    print(len(read_file.pages))
    privious_index=0
    ans=[]
    for page in read_file.pages:

        for lines in page.extract_text().splitlines():

            #logic that is used to form the sentences.
            #(this pdf contains "new line tag \n" in between the sentences also, so that is why if-else statement is used to handle different cases.)
            content_list=lines.split(".")

            if content_list[0].isnumeric() and int(content_list[0])==privious_index+1:
                output_file.write("\n" + content_list[1])

                #adding numeric data to numeric_data file when new sentence starts.
                num_file.write(privious_data)
                privious_index=int(content_list[0])

            else:
                output_file.write(content_list[0])

            
            #LOGIC FOR numeric_data file.
            if content_list[-1].strip().isnumeric() and content_list[-2].strip().isnumeric():
                privious_data="\n"+content_list[-2]+"."+content_list[-1]

    num_file.write(privious_data)
    num_file.close()

#PDF file contains 20000 sentences and our output file contains 20001. 1 extra sentence that we have is the heading of pdf file at first page which is "SENTENCES AND THEIR PERPLEXITY"



# ============================TASK-2============================


# 
# pdf=PyPDF2.PdfFileWriter()
# file=open("pavan.pdf","w")
# for i in range(5):
    # pdf.addBlankPage(219,297) #a4 size dimensions
# pdf.write(file)
# file.close()