import tkinter
import tkinter.filedialog
import tkinter.simpledialog
import os

print ("Choosing File")

# GUI Drawing + Focus settings
root = tkinter.Tk()
root.withdraw()
root.lift()
root.focus_force()

# Choose Original File
original_file = tkinter.filedialog.askopenfilename(title="Choose File:", initialdir=os.curdir)

# Open original file, read into list
with open(original_file) as f:
    original_lines = f.read().splitlines()

# Replace bad characters 
original_lines = [w.replace('[', "") \
                                                    .replace(']', " ") \
                                                    .replace('%', " ") \
                                                    .replace('+', " ") \
                                                    .replace("(", " ") \
                                                    .replace(")", " ") \
                                                    .replace("_", " ") for w in original_lines]

# Create output name variable 
output_file = original_file[:-4] + '_fixed.txt'


# Write all lines with newline except last
with open(output_file, 'w+', encoding='ANSI') as f:
        for line in original_lines[:-1]:
                f.write(line.strip() + "\n")
        f.write(original_lines[-1].rstrip())

    
# Completion message
tkinter.messagebox.showinfo("Done!",  "Created file: \n" + output_file)
