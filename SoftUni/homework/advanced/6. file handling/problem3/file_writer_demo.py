file = open('file_writer_demo.txt', 'w')
file.write('I just created my first file!')

file.close()

file = open('file_writer_demo.txt', 'r')
print(file.read())

file.close()

file = open('file_writer_demo.txt', 'w')
file.write('I just renew the file')

file.close()

file = open('file_writer_demo.txt', 'r')
print(file.read())

file.close()