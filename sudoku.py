import random
import time

def matris_olustur():
    global matris
    matris=[[0 for j in range(9)] for i in range(9)]

def bosmu(satir,sutun):
    if matris[satir][sutun]==0:
        return True
    else:
        return False

def yat_dik_kont(satir,sutun,sayi):
    matris[satir][sutun]=sayi
    for i in range(9):
        if matris[satir][i]==matris[satir][sutun]and i !=sutun:
            matris[satir][sutun]=0
            return False
        else:
            pass
        
    for j in range(9):
        if matris[j][sutun]==matris[satir][sutun]and j !=satir:
            matris[satir][sutun]=0
            return False
        else:
            pass
    #print "yat dik basarili"
    return True

    
def sifirlama(sayi):
    for i in range(9):
        for j in range(9):
            if matris[i][j]==sayi:
                matris[i][j]=0

def random_sifir():
    i=0

    while i<50:
        i=i+1
        satir=random.randint(0,8)
        sutun=random.randint(0,8)
        if bosmu(satir,sutun)==False:
            matris[satir][sutun]=0
        else:
            i=i-1
    

def sudoku_doldur():
    global bitis_zaman
        

    sayi=0
    while sayi<9:
        #print "sayi",sayi
        #yazdirma()
        sayi=sayi+1
        bolge=0
        deneme=0

        while bolge<9:
            bitis_zaman= int(time.strftime("%S"))
            
            if bitis_zaman-basla_zaman>1:
                main()
                return 0
                
     
            satir_basla=(bolge%3)*3  
            sutun_basla=bolge/3
            satir=random.randint(satir_basla,satir_basla+2)
            sutun=random.randint((sutun_basla*3),(sutun_basla*3)+2)
            

            if bosmu(satir,sutun)==False or yat_dik_kont(satir,sutun,sayi)==False:
                bolge=bolge-1
                deneme=deneme+1

            else:
                deneme=0

            if deneme>19:
                #if oto_arama(sayi)==False:
                sifirlama(sayi)
                #print "hatali oto arama"
                bolge=100
                sayi=sayi-1
                #else:
                #    pass
                
            bolge=bolge+1
            
        


def yazdirma():
    for i in range(9):
        if i%3==0:
            print "_________________________________________________________________"

        else:
            print "-----------------------------------------------------------------"
            
        for j in range(9):
            if j%3==0:
                print "|",

            print matris[i][j],"\t",


        print "\n",
    print "_________________________________________________________________"
def devammi():
    for i in range(9):
        for j in range(9):
            if matris[i][j]==0:
                return True
            else:
                pass
    return False
                
def bolge_kont(satir,sutun,sayi):
    bolg=0
    if satir<3:
        if sutun<3:
            bolg=0
        elif sutun<6:
            bolg=3
        else:
            bolg=6

    elif satir<6:
        if sutun<3:
            bolg=1
        elif sutun<6:
            bolg=4
        else:
            bolg=7
    else:
        if sutun<3:
            bolg=2
        elif sutun<6:
            bolg=5
        else:
            bolg=8

    satir_basla=(bolg%3)*3  
    sutun_basla=(bolg/3)
    for i in range(satir_basla,satir_basla+3):
        for j in range(sutun_basla*3,(sutun_basla*3)+3):
            if matris[satir][sutun]==sayi and satir!=i and sutun!=j:
                return True
    return False

    
    
def oyun():
    while devammi()==True:
        satir=input("satir giriniz:(0-8)")
        sutun=input("sutun giriniz:(0-8)")
        sayi=input("sayi giriniz:(1-9)")
        
        if bosmu(satir,sutun)==True and yat_dik_kont(satir,sutun,sayi)==True and bolge_kont(satir,sutun,sayi)==True:
            matris[satir][sutun]=sayi
            yazdirma()


    
def main():
    global basla_zaman
    
    basla_zaman= int(time.strftime("%S"))
    matris_olustur()
    sudoku_doldur()
    random_sifir()
    yazdirma()
    oyun()


main()
                
                
