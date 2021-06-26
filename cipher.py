
import re

cipher = ["Z2/Z",
          "+3 83> 6 =8+ X=66ZQ=6 #=2=",
          "&S=Z6=",
          ">#Z> /6 83> X= &36>/8Q",
          "6#= +3=6 83> !83) #3) >3 2=Z+ >#/6",
          "#= @Z8 #=S&",
          "3RZ2@Z/+Z !8=) +326&/88=2"]

decoder = {"Z": "a",
           "2": "r",
           "/": "i",
           "=": "e",
           "#": "h",
           "\+": "d",
           "6": "s",
           "X": "m",
           ">": "t",
           "Q": "g",
           "8": "n",
           "3": "o",
           "&": "p",
           "S": "l",
           "!": "k",
           "\)": "w",
           "@": "c"}


def decode():
    clear_text = []
    for line in cipher:
        for key, val in decoder.items():    
            line = re.sub(key, val, line)
        clear_text.append(line)
    print_clear_text(clear_text)


def print_clear_text(text):
    for line in text:
        print(line)


if __name__ == "__main__":
    decode()
