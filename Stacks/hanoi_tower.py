#Hanoi Tower implementation using recursion....
def TowerOfHanoi(n,Beg,Aux,End):
    if n ==1:
        print(f'Move disk 1 from {Beg} to {End}')
        return
    else:
        TowerOfHanoi(n-1,Beg,Aux,End)
        print(f'Move Disk {n} from {Beg} to {End}')
        TowerOfHanoi(n-1,Aux,Beg,End)

def main():
    n = int(input('Enter the number of disks: '))   
    TowerOfHanoi(n,'A','B','C')

#main function
main()