import tkinter as tk
from tkinter import messagebox
import time

class FibonacciSearchAnimation:
    def __init__(self, master):
        self.master = master
        self.master.title("Fibonacci Search Animation")

        self.array_label = tk.Label(self.master, text="Array:")
        self.array_label.pack()

        self.array_entry = tk.Entry(self.master, width=50)
        self.array_entry.pack(pady=5)

        self.target_label = tk.Label(self.master, text="Target Element:")
        self.target_label.pack()

        self.target_entry = tk.Entry(self.master, width=10)
        self.target_entry.pack(pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=5)

        self.fib_values_label = tk.Label(self.master, text="")
        self.fib_values_label.pack(pady=5)

        self.offset_label = tk.Label(self.master, text="")
        self.offset_label.pack(pady=5)

        self.size_label = tk.Label(self.master, text="")
        self.size_label.pack(pady=5)

        self.search_index_text = tk.Text(self.master, height=1, width=40, fg="orange")
        self.search_index_text.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start Animation", command=self.start_animation)
        self.start_button.pack(pady=10)

    def start_animation(self):
        array_str = self.array_entry.get()
        key_str = self.target_entry.get()

        try:
            array = [int(x) for x in array_str.split(",")]
            key = int(key_str)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter valid integers.")
            return

        animation_window = tk.Toplevel(self.master)
        FibonacciSearchAnimationRunner(animation_window, array, key, self.result_label, self.search_index_text, self.fib_values_label, self.offset_label, self.size_label)

class FibonacciSearchAnimationRunner:
    def __init__(self, master, array, key, result_label, search_index_text, fib_values_label, offset_label, size_label):
        self.master = master
        self.array = array
        self.key = key
        self.result_label = result_label
        self.search_index_text = search_index_text
        self.fib_values_label = fib_values_label
        self.offset_label = offset_label
        self.size_label = size_label

        self.canvas = tk.Canvas(self.master, width=800, height=200)
        self.canvas.pack()

        self.index_labels = []

        for i, element in enumerate(self.array):
            index_label = tk.Label(self.master, text=str(i), font=("Helvetica", 8))
            index_label.place(x=i * 40 + 20, y=175)
            self.index_labels.append(index_label)

        self.search_index = -1
        self.offset = -1
        self.fib_m2 = 0
        self.fib_m1 = 1
        self.fib = self.fib_m1 + self.fib_m2

        self.animation_speed = 2000  # in milliseconds

        self.animate()

    def animate(self):
        while self.fib < len(self.array):
            self.fib_m2, self.fib_m1 = self.fib_m1, self.fib
            self.fib = self.fib_m1 + self.fib_m2

        while self.fib > 1:
            i = min(self.offset + self.fib_m2, len(self.array) - 1)

            self.draw_highlight(i)
            self.update_search_index(i)
            self.update_fib_values()
            self.update_offset()
            self.update_size()
            self.master.update()
            time.sleep(self.animation_speed / 1000)

            if self.array[i] < self.key:
                self.fib = self.fib_m1
                self.fib_m1 = self.fib_m2
                self.fib_m2 = self.fib - self.fib_m1
                self.offset = i

            elif self.array[i] > self.key:
                self.fib = self.fib_m2
                self.fib_m1 = self.fib_m1 - self.fib_m2
                self.fib_m2 = self.fib - self.fib_m1

            else:
                self.search_index = i
                break

        self.draw_result()

    def draw_highlight(self, index):
        self.canvas.delete("all")
        for i, element in enumerate(self.array):
            color = "lightblue" if i != index else "orange"
            self.canvas.create_rectangle(i * 40, 50, (i + 1) * 40, 150, fill=color)
            self.canvas.create_text((i + 0.5) * 40, 100, text=str(element))

    def update_search_index(self, index):
        self.search_index_text.delete(1.0, tk.END)
        self.search_index_text.insert(tk.END, f"Checking index: {index}")

    def update_fib_values(self):
        fib_values_text = f"Fib: {self.fib}, Fib_m1: {self.fib_m1}, Fib_m2: {self.fib_m2}"
        self.fib_values_label.config(text=fib_values_text)

    def update_offset(self):
        self.offset_label.config(text=f"Offset: {self.offset}")

    def update_size(self):
        self.size_label.config(text=f"Size of Array (n): {len(self.array)}")

    def draw_result(self):
        self.canvas.delete("all")
        for i, element in enumerate(self.array):
            color = "green" if i == self.search_index else "lightblue"
            self.canvas.create_rectangle(i * 40, 50, (i + 1) * 40, 150, fill=color)
            self.canvas.create_text((i + 0.5) * 40, 100, text=str(element))

        if self.search_index != -1:
            result_text = f"Element {self.key} found at index {self.search_index}"
        else:
            result_text = f"Element {self.key} not found in the array"

        self.result_label.config(text=result_text)

# Example usage
root = tk.Tk()
app = FibonacciSearchAnimation(root)
root.mainloop()
