import customtkinter as ctk
from custom_hovertip import CustomTooltipLabel

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    def clean(self):
        for widget in self.winfo_children():
            widget.destroy()
    def config_grid(self,col_count,row_count, row_weigth,col_weigth):
        for c in range(col_count): self.columnconfigure(index=c, weight=col_weigth)
        for r in range(row_count): self.rowconfigure(index=r, weight=row_weigth)
    # def add_scroll(self):
    #     scrollbar = ctk.CTkScrollbar(self,command=self.)
    #     scrollbar.pack(side = ctk.RIGHT)
    # def set_visible_hint(self,widget,msg):
    #     CustomTooltipLabel(anchor_widget=widget, text=msg, background="red",
    #                foreground="black", width=15, justify=ctk.CENTER)
