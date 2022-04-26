from datetime import timedelta, datetime
from tkinter import *

# Measures time elapsed after each word typed.
# A user could press space, wait a month, paste in a 1000 words, press space, and get 1002 wpm.


class TypeTimer:
    def __init__(self):
        self.start_time = None
    def start_timer(self):
        self.start_time = datetime.now()
        self.done_time = self.start_time + timedelta(minutes=1)
    def minute_elapsed(self):
        return datetime.now() >= self.done_time


class TextSample:
    def __init__(self):
        self.sample = self.get_sample()
        self.revise_length()

    def get_sample(self):
        # The initial plan was to source text from an api.
        # This text was inspired by a game called 'Lord Scurlock is Dead'
        # https://ladyblackbird.org/downloads/lord_scurlock-classic.pdf
        return """With Lord Scurlock at long last deceased, well, properly deceased, if he is indeed deceased, I remain at his estate to tie up the many loose ends the master left, and, if I am fortunate, assist the most respectable of his sons in becoming the heir to his estates, and, as well, if I am quite exceptionally fortunate, tuck a pinch of the old ill gotten fortune into my own pocket and leave this wretched place behind in good conscience.

First, of course, I shoo Alward away from the crystal, telling him quite truthfully that it is merely the ghostly echo of a glass replacement, which was broken during a gentleman's duel, of the original crystal, which was sold for fuel and food after the bad business with the toads. 

Arras insists we search the master's study, though he will not tell me what for. He finds a faded and worn occult artwork. I suggest he might sell it, perhaps Pitch, who runs a side trade in such things, might pay a gold coin or so for it. He does not seem to care one way or the other, he inspects it, perhaps for runes, and stuffs it into his jacket. The whole business leaves him quite drained. No doubt he had expected more. 

I insist we must address the master's many debts, perhaps we might start with finding the paperwork requested by Holpine, so to get it out of the way. 

On the stairs, of course, our way is blocked by Constable Tume, who insists that he must receive 67 crowns without delay. He is wide enough none of us can pass, and he holds out a black sack, his gaze firm and insistent. 

Baston steps forward and insists he shall personally deliver such quantity of crowns to Tume's office tomorrow, suggesting, in his cool mechanical voice, that the Constable need not inconvenience himself by staying any longer. 

The constable coughs and says, "yes, surely, of course you will, I'll just be, then, back to the, yes, surely…" he backs down the stairs while scrambling to stuff the pouch into a pocket, not seeming to have a particular pocket in mind. 
"""
    def revise_length(self):
        target_chars = 120 * 5 # 120 words per sample, 5 chars per word
        if len(self.sample) >= target_chars:
            return self.sample[0:120]
        elif len(self.sample) < target_chars:
            new_sample = self.get_sample()
            self.sample = f"{self.sample}\n\n{new_sample}"
            self.revise_length()

    # this would be a great place for a method to test the quality of user entered text.



def start_timer(*args):
    if not type_timer.start_time:
        type_timer.start_timer()
    else:
        if type_timer.minute_elapsed():
            entry['state'] = "disabled"
            word_count = len(entry.get('1.0', 'end')) / 5
            label2.config(text=word_count)


sample_text = TextSample()
type_timer = TypeTimer()

window = Tk()
window.config(padx=50, pady=50)
window.title("Words Per Minute")


sample_lf = LabelFrame(text="Type this: ")
sample_lf.grid(row=0, column=0, columnspan=3, sticky="EW")

sample = Text(sample_lf, width=40, height=10)
sample.insert('1.0', sample_text.sample)
sample['state'] = 'disabled'
sample.grid(row=0, column=0, columnspan=3, sticky="EW")

entry_lf = LabelFrame(text="Type Here")
entry_lf.grid(row=1, column=0, columnspan=3, sticky="EW")

entry = Text(entry_lf, width=40, height=10)
entry_text = entry.get('1.0', 'end')
print(entry_text)
entry.grid(row=1, column=0, columnspan=3)
entry.bind("<Key>", start_timer)

results_lf = LabelFrame(text="Results: ")
results_lf.grid(row=2, column=0, columnspan=3, sticky="EW")
results_lf.config(pady=10, padx=60)

label1 = Label(results_lf, text="You typed ")
label1.grid(row=2, column=0)

label2 = Label(results_lf, text='_')
label2.grid(row=2, column=1)

label3 = Label(results_lf, text=' words per minute.')
label3.grid(row=2, column=2)


window.mainloop()