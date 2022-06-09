#using readline import

file = open("preproinsulin-seq.txt", "r")
Lines = file.readlines()

count = 0
# sstrips the newline character to
result = ""
for line in Lines:
    count += 1
    line = line.strip()
    result = result + " " + line

result = result.replace(' ', '')
lsinsulin_seq_clean = result[0:24]
bsinsulin_seq_clean = result[24:54]
csinsulin_seq_clean = result[54:89]
asinsulin_seq_clean = result[89::]
with open('lsinsulin_seq_clean.txt', 'w') as linsulin:
        linsulin.write(lsinsulin_seq_clean)
        linsulin.close()
with open('bsinsulin_seq_clean.txt', 'w') as linsulin:
        linsulin.write(bsinsulin_seq_clean)
        linsulin.close()

