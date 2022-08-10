def ktab(y):
    print(y)
def chhalmnharfkayn_f(x):
    return len(x)
def dkhel(txt):
    txt = input(txt)
    return txt
def rja3lstar():
    print("\n")
def ilakan_ktab(a ,b):
    if (a == True):
        ktab(b)
def ilamakanch_kteb( a ,b):
    if (a == False):
        ktab(b)
def ar9am(a=0,b=10):
    a = int (a)
    b = int (b) +1
    k = []
    for i in range(a,b):
        k.append( i)
    return k
class b9a :
    def t3awd_tktab(lktba,l7d):
        bda = 0
        while bda < l7d:
            ktab(lktba)
            bda=bda+1
    def t3awd_dkhel(msg,l7d):
        bda = 0
        k = []
        msg = msg + ' '
        while bda < l7d:
            i= dkhel(msg)
            k.append( i)
            bda=bda+1
        return k
################## CODE BDARIJA #####################        
ktab(chhalmnharfkayn_f('DARIJA'));rja3lstar()
nmra = dkhel('kteb nmra :');rja3lstar()
ktab("hahya nmrtak : ");ktab(nmra)
ilakan_ktab(nmra=='0649115770', 'sahiha' );rja3lstar()
ilamakanch_kteb(nmra=='0649115770','khata2');rja3lstar()
ktab(ar9am(0,5));rja3lstar()
lista = b9a.t3awd_dkhel('smiya :',3)
ktab(lista);rja3lstar()
smia1=lista[0]
smia2=lista[1]
smia3=lista[2]
ktab(f'smiya lwla : {smia1}')
ktab(f'smiya tanya : {smia2}')
ktab(f'smiya talta : {smia3}');rja3lstar()
b9a.t3awd_tktab('ma3a salama',3)
