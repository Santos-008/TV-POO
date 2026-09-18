from rich import print
from rich.panel import Panel
import os

class TV:
    def __init__(self):
        self.estado=False
        self.barravolume=['  ','  ','  ']
        self.nivelvolume=['VOL1','VOL2','VOL3']
        self.volumeatual=self.nivelvolume[0]
        self.controle=''
        self.numcanais=[' 1 ',' 2 ',' 3 ',' 4 ',' 5 ']
        self.canais=['CH1','CH2','CH3','CH4','CH5',]
        self.canalatual=self.canais[0]
        
    def usartv(self):
        c=0
        cv=0
        for i in range (0,3):
            self.barravolume[i]='[black on white]   [/]'
        self.barravolume[0]='[black on green]   [/]'
        
        while True:
            print('\n\n\n\n\n')
            os.system('cls')
            if self.controle=="@":
                self.estado=not self.estado
            elif self.controle=="0":
                break
            elif self.controle==">":
                if c==4:
                    c=0
                    self.canalatual=self.canais[c]
                    self.numcanais=[' 1 ',' 2 ',' 3 ',' 4 ',' 5 ']
                    self.numcanais[c]=(f"[black on yellow]{self.numcanais[c]}[/]")
                else:
                    c+=1
                    self.numcanais=[' 1 ',' 2 ',' 3 ',' 4 ',' 5 ']
                    self.numcanais[c]=(f"[black on yellow]{self.numcanais[c]}[/]")
                    self.canalatual=self.canais[c]
            elif self.controle=="+":
                if cv<2:
                    cv+=1
                    self.volumeatual=self.nivelvolume[cv]
                    self.barravolume[cv]=(f"[black on green]   [/]")
            elif self.controle=="-":
                if cv>0:
                    self.barravolume[cv]='[black on white]   [/]'
                    cv-=1
                    self.volumeatual=self.nivelvolume[cv]
                    
                    
                   
            self.numcanais[c]=(f"[black on yellow]{self.numcanais[c]}[/]")
            canais="".join(self.numcanais)
            barravolume="".join(self.barravolume)
            if self.estado==False:
                print(Panel.fit(' :no_entry_sign: [red]A TV está desligada[/]',title="[TV]"))
                self.controle=input(f"{self.canalatual}         - {self.volumeatual} + ")
            else:
                print(Panel.fit(f'CANAL = {canais}\nVOLUME ={barravolume}',title="[TV]"),end="")
                self.controle=input(f"{self.canalatual}         - {self.volumeatual} + ")
               

               
x=TV()
x.usartv()
