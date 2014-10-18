from Tkinter import *

root = Tk()
root.title("Rock, Paper, Scissors")

c = Canvas(width=600,height=510,bg="white")
c.pack()

def start(event):
    c.delete(startbtn,starttxt,secret)

def troll(event):
    c.delete(bum_bum1,chick_chick1,hrum_hrum1,startbtn,starttxt,secret)

def bumbum1(event):
    c.delete(bum_bum1,chick_chick1,hrum_hrum1,bum_bum2,chick_chick2,hrum_hrum2,name)
    c.create_oval(20,20,280,400,fill="grey",width=3)
    c.create_rectangle(320,20,500,400,fill="grey",width=3)
    c.create_text(300,30,text="You lose!",font="arial 30")
    quitbtn = c.create_rectangle(275,470,325,490,tags='Quit',fill="grey")
    quittxt = c.create_text(300,480,text="Quit!",tags='Quit')

def chickchick1(event):
    c.delete(bum_bum1,chick_chick1,hrum_hrum1,bum_bum2,chick_chick2,hrum_hrum2,name)
    c.create_oval(20,20,140,140,width=3)
    c.create_oval(160,20,280,140,width=3)
    c.create_line(140,80,230,400,width=3)
    c.create_line(160,80,80,400,width=3)
    c.create_oval(320,20,580,400,fill="grey",width=3)
    c.create_text(300,30,text="You lose!",font="arial 30")
    quitbtn = c.create_rectangle(275,470,325,490,tags='Quit',fill="grey")
    quittxt = c.create_text(300,480,text="Quit!",tags='Quit')

def hrumhrum1(event):
    c.delete(bum_bum1,chick_chick1,hrum_hrum1,bum_bum2,chick_chick2,hrum_hrum2,name)
    c.create_rectangle(20,20,200,400,fill="grey",width=3)
    c.create_oval(320,20,440,140,width=3)
    c.create_oval(460,20,580,140,width=3)
    c.create_line(440,80,530,400,width=3)
    c.create_line(460,80,380,400,width=3)
    c.create_text(300,30,text="You lose!",font="arial 30")
    quitbtn = c.create_rectangle(275,470,325,490,tags='Quit',fill="grey")
    quittxt = c.create_text(300,480,text="Quit!",tags='Quit')

def bumbum2(event):
    c.delete(bum_bum2,chick_chick2,hrum_hrum2,name)
    c.create_oval(20,20,280,400,fill="grey",width=3)
    c.create_oval(320,20,440,140,width=3)
    c.create_oval(460,20,580,140,width=3)
    c.create_line(440,80,530,400,width=3)
    c.create_line(460,80,380,400,width=3)
    c.create_text(300,30,text="You win!",font="arial 30")
    quitbtn = c.create_rectangle(275,470,325,490,tags='Quit',fill="grey")
    quittxt = c.create_text(300,480,text="Quit!",tags='Quit')

def chickchick2(event):
    c.delete(bum_bum2,chick_chick2,hrum_hrum2,name)
    c.create_oval(20,20,140,140,width=3)
    c.create_oval(160,20,280,140,width=3)
    c.create_line(140,80,230,400,width=3)
    c.create_line(160,80,80,400,width=3)
    c.create_rectangle(320,20,500,400,fill="grey",width=3)
    c.create_text(300,30,text="You win!",font="arial 30")
    quitbtn = c.create_rectangle(275,470,325,490,tags='Quit',fill="grey")
    quittxt = c.create_text(300,480,text="Quit!",tags='Quit')

def hrumhrum2(event):
    c.delete(bum_bum2,chick_chick2,hrum_hrum2,name)
    c.create_rectangle(20,20,200,400,fill="grey",width=3)
    c.create_oval(320,20,580,400,fill="grey",width=3)
    c.create_text(300,30,text="You win!",font="arial 30")
    quitbtn = c.create_rectangle(275,470,325,490,tags='Quit',fill="grey")
    quittxt = c.create_text(300,480,text="Quit!",tags='Quit')

def Quit(event):
    exit()

bum_bum2 = c.create_rectangle(10,470,30,490,fill="grey",tags='bum-bum2')
hrum_hrum2 = c.create_rectangle(40,470,60,490,fill="grey",tags='hrum-hrum2')
chick_chick2 = c.create_rectangle(70,470,90,490,fill="grey",tags='chick-chick2')
bum_bum1 = c.create_rectangle(10,470,30,490,fill="grey",tags='bum-bum1')
hrum_hrum1 = c.create_rectangle(40,470,60,490,fill="grey",tags='hrum-hrum1')
chick_chick1 = c.create_rectangle(70,470,90,490,fill="grey",tags='chick-chick1')
name = c.create_text(50,500,text="Rock Paper Scissors")
secret = c.create_rectangle(0,450,100,510,fill="white",outline="white")
startbtn = c.create_rectangle(275,470,325,490,tags='start',fill="grey")
starttxt = c.create_text(300,480,text="Start!",tags='start')

c.tag_bind('start','<Button>',func=start)
c.tag_bind('bum-bum1','<Button>',func=bumbum1)
c.tag_bind('chick-chick1','<Button>',func=chickchick1)
c.tag_bind('hrum-hrum1','<Button>',func=hrumhrum1)
c.tag_bind('bum-bum2','<Button>',func=bumbum2)
c.tag_bind('chick-chick2','<Button>',func=chickchick2)
c.tag_bind('hrum-hrum2','<Button>',func=hrumhrum2)
c.tag_bind('start','<Button-3>',func=troll)
c.tag_bind('Quit','<Button>',func=Quit)

root.mainloop()
