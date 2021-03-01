from multiprocessing import Process

def attack_bots():
    attack = range(1, 101)
    for number in attack:
        print(number)
        

        
if __name__ == "__main__":
    
    processes = [Process(target=attack_bots, args=()) for x in range(4)] 
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
    