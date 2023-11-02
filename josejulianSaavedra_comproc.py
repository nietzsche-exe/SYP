
import time
import multiprocessing

def reader():
    while True:
        time.sleep(5)
        f = open("fichero.txt", 'r')
        content = f.read()
        f.close()
        if content=="--":
            break
        else:
            print("Leo {}".format(content))
             
        
def writer(text):
    f = open("fichero.txt", 'a')
    f.write(text) 
    print("\n Escribo {}".format(text))
    f.close()  
   

if __name__ == '__main__':
    
    text = ""
    text = input("Introduce un texto para escribir en el fichero (o '--' para salir): ")
    
    while text != "--":
        text = input("Introduce un texto para escribir en el fichero (o 'fin' para salir): ")

        writer_process = multiprocessing.Process(target=writer, args=(text,))
        writer_process.start()

reader_process = multiprocessing.Process(target=reader,)
reader_process.start()

   

    
        

   
