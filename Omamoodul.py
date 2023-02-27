def Vorsed_palgad(i:list,p:list):
    """
    """
    dublikatid=[x for x in if p.count(x)>1]
    dublikatid=list(set(dublikatid))
    [1200,2500,750,750,1200]->[1200,750]
    for palk in dublikatid:
        n=p.count(palk) #1200, n=2; 750, n=2
        k=-1
        print(f"{palk}saavad kätte järgmised inimesed:")
        for j in range(n):
            k=p.index(palk,k+1)#----
            nimi=i=i[k] 
            print(nimi)






def kustutamine(i:list,p:list):
    """
    """
    nimi=input("sisesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind) 
            return i,p







def keskpalgad(palgad,inimesed):
    """
    """
    palk=int(input("sisetage palk: "))
    print("Suurem kui sisestatud palk")
    i=0
    for p in palgad:
        if p>palk:
            print(inimesed[palgad.index(p)])
            print(p)
        i+=1
    print("Väiksem kui sisestatud palk")
    i=0
    for p in palgad:
        if p<palk:
            print(inimesed[palgad.index(p)])
            print(p)
        i+=1




def palkinim(palgad:int,inimesed:str)->int:
    """funktsioon eemaldab loendist elemendid
    """
    
    palk=int(input("sisetage palk: "))
    inimes=input("sisetage nimi inimesed: ")
    inimesed.remove(inimes)
    palgad.remove(palk)
    return inimesed, palgad

  

