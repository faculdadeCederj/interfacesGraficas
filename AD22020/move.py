#!/usr/bin/env python
# coding: UTF-8
# style guide: PEP-8
#
## @package DNAStrand
#
#   Graphical interface to test matching of DNA Strands from DNAStrand class
#
#   @author William Souza
#   @since 08/04/2020
#
import tkinter as tk
from sys import argv, exit
from tkinter import filedialog
from tkinter import messagebox
from random import sample
from random import choice
import getopt

import DNAStrand as dna

debug = False
try:
    try:
        opts, args = getopt.getopt(argv[1:], "hn:m:v", ['help','dna1=', 'dna2=', 'verbose'])
    except getopt.GetoptError as err:
        raise ValueError(str(err))

    n1 = n2 = 0
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('''Usage: move.py -n1 <DNA1_length> -n2 <DNA2_length> -v''')
            exit(1)
        elif opt in ('-n', '--dna1'):
            n1 = int(arg)
        elif opt in ('-m', '--dna2'):
            n2 = int(arg)
        elif opt in ('-v', '--verbose'):
            debug = True
except ValueError as e:
    print(f'{str(e)} \n For help, type {argv[0]} --help')
    exit(2)


## Main window containing two Labels wich represent the Strands
class Application(tk.Frame):
    ## initialization method
    # @param self window object
    # @param master tk object that contains the frame created
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('DNA Strand Application')
        self.window_width = 1200
        self.window_height = 600
        self.master.geometry(f'{self.window_width}x{self.window_height}')
        self.master.minsize(self.window_width, self.window_height)
        self.pack(expand='true', fill='both')
        self.help_message = '''     Este programa tem como objetivo realizar a comparação entre duas fitas de DNA.
    Existem duas maneiras de carregar as fitas para serem exibidas:

    - Escrevendo as fitas nas caixas de texto da aplicação;

    - Carregando um arquivo de texto com duas fitas, uma em cada linha.

    Apenas os caracteres "A", "T", "C" e "G", são válidos para fitas de DNA.

    O uso da aplicação segue o padrão dos botões da interface. Também podem
ser usadas as teclas do teclado correspondentes para cada função desejada. 
'''
                            
        self.create_widgets()
        self.key_binder()
    
    ## function that handles keyboard press
    # @param self window object
    # @param event event that triggered the function
    def keyboard_handler(self, event):
        if event.keysym == 'Left':
            self.move_left()

        elif event.keysym == 'Right':
            self.move_right()

        elif event.keysym == 'Up':
            self.move_up()

        elif event.keysym == 'Down':
            self.move_down()

        elif event.keysym == 'Tab':
            self.reset_pos()

        elif event.keysym == 'Escape':
            self.master.destroy()
            exit(0)
        
        elif event.keysym == 'h':
            messagebox.showinfo('Ajuda', self.help_message)

        elif event.keysym == 's':
            self.shuffle_strands()

        elif event.keysym == 'm':
            self.max_matches()
            
        if debug:
            print(f'{event.keysym} key Pressed')
            print(f'Other Strand coord: {self.canva_board.coords(self.other_strand)}')

    ## function to move other strand left
    def move_left(self):
        self.canva_board.move(self.other_strand, -58, 0)
        self.DNA_shift -= 1
        pos = self.canva_board.coords(self.other_strand)
        dimension = self.canva_board.bbox(self.other_strand)
        width = dimension[2] - dimension[0]

        if pos[0] < - width + 70.0:
            self.reset_pos()
        self.strand_render()

    ## function to move other strand right
    def move_right(self):
        self.canva_board.move(self.other_strand, 58, 0)
        self.DNA_shift += 1
        self.strand_render()
        pos = self.canva_board.coords(self.other_strand)

        if pos[0] > self.right_limit:
            self.reset_pos()
    
    ## function to move other strand up
    def move_up(self):
        self.canva_board.move(self.other_strand, 0, -60)
        pos = self.canva_board.coords(self.other_strand)
        dimension = self.canva_board.bbox(self.other_strand)
        height = dimension[3] - dimension[1]

        if pos[1] < - height:
            self.reset_pos()
    
    ## function to move other strand down
    def move_down(self):
        self.canva_board.move(self.other_strand, 0, 60)
        pos = self.canva_board.coords(self.other_strand)

        if pos[1] > self.down_limit:
            self.reset_pos()
    

    ## function to reset the position of the strand
    def reset_pos(self):
        self.canva_board.coords(self.other_strand, self.other_strand_reset[0], self.other_strand_reset[1])
        self.DNA_shift = 0
        self.strand_render()

    ## function that finds maximum matches of the strands
    # given by testing it and renders to the screen
    def max_matches(self):
        shift_list = self.DNA_base_strand.findMaxPossibleMatches(self.DNA_other_strand)
        self.reset_pos()
        self.DNA_shift = shift_list[1]
        self.canva_board.move(self.other_strand, self.DNA_shift * 58, 0)
        self.strand_render()

        if debug:
            print(f'Maximum matches position: {shift_list[1]} \n Maximum matches: {shift_list[0]}')


    ## function that outputs strand formated to be rendered
    # in the screen
    def output_strand(self, strand):
        outstrand = ''
        for char in strand:
            outstrand += char + ' '
        return outstrand

    ## function that gets the strand from the screen and format
    # it for manipulation
    def get_strand(self, strand):
        outstrand = ''
        for char in strand:
            outstrand += char.strip()
        return outstrand

    ## Function responsible for shuffling the strands using 
    # the random lib
    def shuffle_strands(self):
        strand1 = self.canva_board.itemcget(self.base_strand, 'text')
        strand2 = self.canva_board.itemcget(self.other_strand, 'text')

        strand1 = self.get_strand(strand1)
        strand2 = self.get_strand(strand2)

        shuffled_1strand = ''.join(sample(strand1, len(strand1)))
        shuffled_2strand = ''.join(sample(strand2, len(strand2)))
        
        self.base_strand_text.set(shuffled_1strand)
        self.other_strand_text.set(shuffled_2strand)
        self.strand_render()



    ## function responsible for getting the values from a variable and
    # rendering it in the screen
    def strand_render(self):
        base_strand = self.base_strand_text.get()
        other_strand = self.other_strand_text.get()
        
        base_strand = self.get_strand(base_strand)
        other_strand = self.get_strand(other_strand)

        self.DNA_base_strand = dna.DNAStrand(base_strand)
        self.DNA_other_strand = dna.DNAStrand(other_strand)

        if self.DNA_shift < 0:
            base_strand = self.DNA_base_strand.findMatchesWithLeftShift(self.DNA_other_strand, abs(self.DNA_shift))
            other_strand = self.DNA_other_strand.findMatchesWithRightShift(self.DNA_base_strand, abs(self.DNA_shift))
        
        else:
            base_strand = self.DNA_base_strand.findMatchesWithRightShift(self.DNA_other_strand, self.DNA_shift)
            other_strand = self.DNA_other_strand.findMatchesWithLeftShift(self.DNA_base_strand, self.DNA_shift) 

        base_strand = self.output_strand(base_strand)
        other_strand = self.output_strand(other_strand)

        self.base_strand_text.set(base_strand)
        self.other_strand_text.set(other_strand)

        self.canva_board.itemconfig(self.base_strand, text=self.base_strand_text.get())
        self.canva_board.itemconfig(self.other_strand, text=self.other_strand_text.get())


    ## function that reads the strands from a text file
    def open_strandfile(self):
        filename = filedialog.askopenfilename(initialdir='.\\', title='Selecione o arquivo',
                                                 filetypes=(('text','*.txt'), ('all files', '*.*')))
        try:
            with open(filename, 'r') as file:
                strand1 = file.readline()
                strand2 = file.readline()

            self.base_strand_text.set(strand1)
            self.other_strand_text.set(strand2)
            self.DNA_shift = 0
            self.strand_render()
            
        except OSError as fopenning:
            print(f'{fopenning} \n Failed to open file')

    ## function to generate strand based in the lengths given by the user
    def generate_strand(self):
        self.base_strand_text = tk.StringVar()
        self.other_strand_text = tk.StringVar()

        validChars = 'atcg'

        base_strand = ''
        other_strand = ''

        if n1 != 0:
            for l in range(n1):
                base_strand += choice(validChars)
        else:
            base_strand = 'gcaaaagc'

        if n2 != 0:
            for l in range(n2):
                other_strand += choice(validChars)
        else:
            other_strand ='gcggTcC'

        base_strand = self.output_strand(base_strand)
        other_strand = self.output_strand(other_strand)
        self.base_strand_text.set(base_strand)
        self.other_strand_text.set(other_strand)

    ## function to center strands when window is resized
    def resize(self, event):
        self.right_limit = event.width * 0.8
        self.down_limit = event.height * 0.4
        
        dimension = self.canva_board.bbox(self.base_strand)
        height = dimension[3] - dimension[1]
        width = dimension[2] - dimension[0]
        x = (0.8*event.width)/2 - width/2
        y = (0.4*event.height)/2 - height/2
        self.canva_board.coords(self.base_strand, x, y)

        if debug:
            print(f'New base strand position: {x}, {y}')

        dimension = self.canva_board.bbox(self.other_strand)
        height = dimension[3] - dimension[1]
        y = (0.4*event.height)/2 - height/2
        self.canva_board.coords(self.other_strand, x, y)

        self.other_strand_reset = [x, y]
        if debug:
            print(f'New other strand position: {x}, {y} \n New window size: {event.width}, {event.height}')

    ## function that create the Strands labels
    # @param self window object
    def create_widgets(self):
        self.canva_board = tk.Canvas(self, bg='darkgrey', relief='groove', bd=3)
        self.canva_board.place(relwidth=0.8, relheight=0.4, relx=0.5, rely=0.1, anchor='n')
        strand_style = ('mono', '36', 'bold')
        
        self.generate_strand()
        self.DNA_base_strand = dna.DNAStrand(self.get_strand(self.base_strand_text.get()))
        self.DNA_other_strand = dna.DNAStrand(self.get_strand(self.other_strand_text.get()))
        self.DNA_shift = 0

        matches = self.DNA_base_strand.findMatchesWithLeftShift(self.DNA_other_strand, 0)
        matches = self.output_strand(matches)
        self.base_strand_text.set(matches)

        matches = self.DNA_other_strand.findMatchesWithLeftShift(self.DNA_base_strand, 0)
        matches = self.output_strand(matches)
        self.other_strand_text.set(matches)

        self.base_strand = self.canva_board.create_text(300, 110, anchor='sw', font=strand_style, text=self.base_strand_text.get())
        self.other_strand = self.canva_board.create_text(300, 110, anchor='nw', font=strand_style, text=self.other_strand_text.get())


        labels_style = ('Arial', '18')
        self.move_label = tk.Label(self, text='Mover a Fita', font=labels_style)
        self.move_label.place(relx=0.162, rely=0.52)

        self.arrow_up_button = tk.Button(
                                        self, 
                                        text='^', 
                                        font=labels_style,
                                        command=self.move_up
                                    )

        self.arrow_up_button.place(relx=0.201, rely=0.6)

        self.arrow_down_button = tk.Button(
                                            self, 
                                            text='˅', 
                                            font=('Arial', '17'),
                                            command=self.move_down
                                        )

        self.arrow_down_button.place(relx=0.2, rely=0.67)

        self.arrow_left_button = tk.Button(
                                            self, 
                                            text='<', 
                                            font=('Arial', '17'), 
                                            command=self.move_left
                                        )

        self.arrow_left_button.place(relx=0.166, rely=0.67)

        self.arrow_right_button = tk.Button(
                                            self, 
                                            text='>', 
                                            font=('Arial', '17'),
                                            command=self.move_right
                                        )

        self.arrow_right_button.place(relx=0.234, rely=0.67)

        self.strand1_label = tk.Label(self, text='Fita 1') 
        self.strand1_label.place(relx=0.38, rely=0.58)
        self.strand1_entry = tk.Entry(self, textvariable=self.base_strand_text)
        self.strand1_entry.place(relx=0.43, rely=0.58)

        self.strand2_label = tk.Label(self, text='Fita 2')
        self.strand2_label.place(relx=0.38, rely=0.64)
        self.strand2_entry = tk.Entry(self, textvariable=self.other_strand_text)
        self.strand2_entry.place(relx=0.43, rely=0.64)

        self.strand_entry_button = tk.Button(self, text='Usar campos para fitas', command=self.strand_render)
        self.strand_entry_button.place(relx=0.33, rely=0.70)

        self.strandfile_button = tk.Button(self, text='Abrir arquivo de fitas', command=self.open_strandfile)
        self.strandfile_button.place(relx=0.50, rely=0.70)

        self.random_label = tk.Label(self, text='s:', font=('Arial', '17'))
        self.random_button = tk.Button(self, text='Embaralhar', command=self.shuffle_strands)
        self.random_label.place(relx=0.68, rely=0.52)
        self.random_button.place(relx=0.78, rely=0.52)

        self.reset_label = tk.Label(self, text='Tab:', font=labels_style)
        self.reset_button = tk.Button(
                                    self, 
                                    text='Reset', 
                                    command=self.reset_pos
                                    )
                                    
        self.reset_label.place(relx=0.68, rely=0.58)
        self.reset_button.place(relx=0.78, rely=0.58)

        self.exit_label = tk.Label(self, text='Escape:', font=labels_style)
        self.exit_button = tk.Button(self, text='Sair', command=self.master.destroy)
        self.exit_label.place(relx=0.68, rely=0.64)
        self.exit_button.place(relx=0.78, rely=0.64)

        self.help_label = tk.Label(self, text='h:', font=labels_style)
        self.help_button = tk.Button(
                                    self, 
                                    text='Ajuda', 
                                    command= lambda: messagebox.showinfo('Ajuda', self.help_message)
                                    )

        self.help_label.place(relx=0.68, rely=0.70)
        self.help_button.place(relx=0.78, rely=0.70)

        self.match_label = tk.Label(self, text='m:', font=labels_style)
        self.match_button = tk.Button(self,
                                      text='Pares máximos',
                                      command=self.max_matches
                                      )

        self.match_label.place(relx=0.68, rely=0.76)
        self.match_button.place(relx=0.78, rely=0.76)

    ## function that binds events to functions
    # @param self window object 
    def key_binder(self):
        self.master.bind('<Key>', self.keyboard_handler)
        self.bind('<Configure>', self.resize)

    

    


## Basic instantiation and tests
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
