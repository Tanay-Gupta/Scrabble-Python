#function for returning score of each word
def search(word):
    score = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}
    word.lower()
    sum=0
    for i in word:
        sum=sum+score[i]
            
    return(sum)

def ex1(g1,g2,g3,g4,dim_hand,num_letters):

    score=[0]*4                         #list to store score
    tile_in_hand=[dim_hand]*4           #list to store letters in hand
    num_letters=num_letters-(dim_hand*4)#to store total letters
    index=0                             #for switching between words of each list 


    maxx=max(len(g1),len(g2),len(g3),len(g4))
    
    
    while (maxx)>0:
        
           #for player 1
        if(index <=len(g1) - 1):
            word=g1[index]
            score[0]=score[0]+search(word)#adding score of each word in list
                
            if(num_letters<len(word)):
                tile_in_hand[0]=tile_in_hand[0]-len(word)+num_letters
                num_letters=0
            else:
                num_letters-=len(word)    
        
            # for player 2
        if (index <=len(g2) - 1):
            word=g2[index]
            score[1]=score[1]+search(word)
            if (num_letters < len(word)):
                tile_in_hand[1] = tile_in_hand[1] - len(word) + num_letters
                num_letters=0
            else:
                num_letters-=len(word) 

            #for player 3
        if (index <=len(g3) - 1):
            word=g3[index]
            score[2]=score[2]+search(word)
            if (num_letters < len(word)):
                tile_in_hand[2] = tile_in_hand[2] - len(word) + num_letters
                num_letters=0
            else:
                num_letters-=len(word)     
       
            # for player 4
        if (index <=len(g4) - 1):
            word=g4[index]
            score[3]=score[3]+search(word)
            if (num_letters < len(word)):
                tile_in_hand[3] = tile_in_hand[3] - len(word) + num_letters
                num_letters=0
            else:
                num_letters-=len(word)        

        index=index+1
        maxx-=1
        
            #final score calculation by deducting score of leftout letters
    for i in range(4):
       score[i]=score[i]-3*tile_in_hand[i]
       
    return(score)



if __name__=="__main__":
    print(ex1([ "flew", "pus", "gce", "bead", "msc", "zed", "pull", "anon", "eigg", "shot", "clod", "flow", "dfc" ],
              [ "burr", "cup", "sess", "keep", "knox", "kph", "bate", "ryas", "aida", "reus", "gala", "nit", "inde" ],
              [ "zuni", "buss", "rids", "wen", "bad", "omne", "boar", "imps", "back", "rase", "pure", "slog" ],
              [ "tugs", "hats", "shat", "soon", "yule", "pawl", "poe", "cups", "kcal", "bobs", "gush", "soap" ]
              ,4,200))





