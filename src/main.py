import tkinter as tk
import math

class TerminaleSimulato(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sciCALC")
        self.geometry("600x400")

        self.text_output = tk.Text(self, state='disabled', bg='black', fg='white', insertbackground='white')
        self.text_output.pack(fill=tk.BOTH, expand=True)

        self.entry_input = tk.Entry(self, bg='black', fg='white', insertbackground='white')
        self.entry_input.pack(fill=tk.X)
        self.entry_input.bind('<Return>', self.processa_comando)

        self.scrivi_output("sciCALC. Type 'exit' per uscire.\n>> ")

        # Stato per gestire input multipli (per eq2)
        self.in_eq2_mode = False
        self.eq2_coeffs = []
        self.eq2_prompts = ["Inserisci coefficiente a: ", "Inserisci coefficiente b: ", "Inserisci coefficiente c: "]

    def scrivi_output(self, testo):
        self.text_output.configure(state='normal')
        self.text_output.insert(tk.END, testo)
        self.text_output.see(tk.END)
        self.text_output.configure(state='disabled')

    def processa_comando(self, event):
        comando = self.entry_input.get().strip()
        self.entry_input.delete(0, tk.END)

        if self.in_eq2_mode:
            # In modalità raccolta coefficenti eq2
            try:
                val = float(comando)
                self.eq2_coeffs.append(val)
                if len(self.eq2_coeffs) < 3:
                    self.scrivi_output(self.eq2_prompts[len(self.eq2_coeffs)])
                else:
                    self.risolvi_equazione_secondo_grado(*self.eq2_coeffs)
                    self.in_eq2_mode = False
                    self.eq2_coeffs = []
                    self.scrivi_output(">> ")
            except ValueError:
                self.scrivi_output("Valore non valido, inserisci un numero.\n" + self.eq2_prompts[len(self.eq2_coeffs)])
            return

        if comando.lower() == 'exit':
            self.scrivi_output("Uscita terminale simulato.\n")
            self.quit()
            return

        if comando == ";eq2":
            self.in_eq2_mode = True
            self.eq2_coeffs = []
            self.scrivi_output("Risoluzione equazione di secondo grado ax² + bx + c = 0\n")
            self.scrivi_output(self.eq2_prompts[0])
            return

        # Comando non riconosciuto, ripeti
        self.scrivi_output(comando + "\n>> ")

    def risolvi_equazione_secondo_grado(self, a, b, c):
        if a == 0:
            self.scrivi_output("Non è un'equazione di secondo grado (a=0).\n")
            return

        delta = b**2 - 4*a*c
        self.scrivi_output(f"Calcolo delta: {delta}\n")

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            self.scrivi_output(f"Soluzioni reali distinte:\nx1 = {x1}\nx2 = {x2}\n")
        elif delta == 0:
            x = -b / (2*a)
            self.scrivi_output(f"Soluzione reale doppia:\nx = {x}\n")
        else:
            real = -b / (2*a)
            imag = math.sqrt(-delta) / (2*a)
            self.scrivi_output(f"Soluzioni complesse:\nx1 = {real} + {imag}i\nx2 = {real} - {imag}i\n")

if __name__ == "__main__":
    app = TerminaleSimulato()
    app.mainloop()

