import tkinter as  tk





class myapps:
    def __init__(self,root:tk.Tk,titles:str,rcolor:bool,gcolor:bool,bcolor:bool,colorr:int,colorg:int,colorb:int,w:int,h:int):
        self.root=root
        self.root.title(titles)
        self.root.geometry(str(w)+"x"+str(h))
        self.root.configure(background="white")
        self.canvas=tk.Canvas(background="white",width=w,height=h,)
        self.canvas.pack(padx=0,pady=0)
        ww=float(w)/float(255)
        a:float=0
        c=0
        #print (ww)
        while True:
            if int(a)>=w:
                break
           
            bb=colorb
            gg=colorg
            rr=colorr
            if bcolor:
                bb=c
            if rcolor:
                rr=c
            if gcolor:
                gg=c
            bbb="00"+str(hex(bb).replace("0x",""))
            ggg="00"+str(hex(gg).replace("0x",""))
            rrr="00"+str(hex(rr).replace("0x",""))
            b="#"+bbb[-2:]+ggg[-2:]+rrr[-2:]
            self.canvas.create_rectangle(int(a),0,int(a+(ww*2)),h,fill=b)
            a=a+ww
            c=c+1








def starts(titles:str,rcolor:bool,gcolor:bool,bcolor:bool,colorr:int,colorg:int,colorb:int,w:int,h:int):
    root=tk.Tk()
    apps=myapps(root,titles,rcolor,gcolor,bcolor,colorr,colorg,colorb,w,h)
    root.mainloop()

starts("gradiente",True,True,True,0,0,0,640,480)