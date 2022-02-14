def main():
    i = int(input().split()[0])
    likes = []
    dislikes = []
    for a in range(i):
        
        line = input().split()
        for b in range(int(line[0])):
            if line[b+1] not in likes:
                likes.append(line[b+1])
        line = input().split()
        for c in range(int(line[0])):
            if line[c+1] not in dislikes:
                dislikes.append(line[c+1])
    
    toppings = gettoppings(likes, dislikes)
    print(len(toppings), end=' ')
    for i in range(len(toppings)):
        print(toppings[i], end=' ')

def gettoppings(likes, dislikes):
    toppings = []
    for i in range(len(likes)):
        if likes[i] not in dislikes:
            toppings.append(likes[i])
    return toppings

    

if __name__ == '__main__':

    main()
    