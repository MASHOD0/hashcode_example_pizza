def main():
    
    try:
        
        f = open("a_an_example.in.txt", 'r')
        i = int(f.readline().split()[0])
        likes = []
        dislikes = []
        for a in range(i):
            
            line = f.readline().split()
            for b in range(int(line[0])):
                if line[b+1] not in likes:
                    likes.append(line[b+1])
            line = f.readline().split()
            for c in range(int(line[0])):
                if line[c+1] not in dislikes:
                    dislikes.append(line[c+1])
        toppings = gettoppings(likes, dislikes)

        with open("a_an_example.out.txt",'w',encoding = 'utf-8') as w:
            w.write(f"{len(toppings)} ")
            for i in range(len(toppings)):
                w.write(f"{toppings[i]} ")
        
        
    finally:
        f.close()
def gettoppings(likes, dislikes):
    toppings = []
    for i in range(len(likes)):
        if likes[i] not in dislikes:
            toppings.append(likes[i])
    return toppings

    

if __name__ == '__main__':

    main()
    