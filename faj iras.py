

#'r' = read (olvasas)
#'w' = write (iras)
#'a' = append (hozzafuzes, mellekel)

# with open('New folder/mondasok.txt', 'r', encoding='utf-8') as infile:
#     with open('out.txt', 'w', encoding='utf-8' ) as outfile:
#
#         sor = infile.readline()
#
#         while sor:
#             outfile.write(sor)
#             sor = infile.readline()
#
#

with open('out.txt', 'a', encoding='utf-8') as file:
    ujsor = '\nNem akarasnak nyoges a vege.' #\m uj sorba valo iras

    file.write(ujsor)