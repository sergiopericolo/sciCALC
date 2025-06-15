import tkinter as tk

class TerminalGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sciCALC")
        self.geometry("600x400")

        self.text_output = tk.Text(self, state='disabled', bg='black', fg='white', insertbackground='white')
        self.text_output.pack(fill=tk.BOTH, expand=True)

        # Casella per i numeri
        self.number_input = tk.Entry(self, bg='black', fg='white', insertbackground='white')
        self.number_input.pack(fill=tk.X)
        self.number_input.bind('<Return>', self.processa_input_numeric)

        # Casella per le funzioni
        self.function_input = tk.Entry(self, bg='black', fg='white', insertbackground='white')
        self.function_input.pack(fill=tk.X)
        self.function_input.bind('<Return>', self.processa_input_function)

        # Casella per i comandi
        self.command_input = tk.Entry(self, bg='black', fg='white', insertbackground='white')
        self.command_input.pack(fill=tk.X)
        self.command_input.bind('<Return>', self.processa_input_command)

        self.variables = {}  # Dizionario per le variabili

        self.scrivi_output("sciCALC. Type ';exit' per uscire.\n- ")


    def scrivi_output(self, testo):
        self.text_output.configure(state='normal')
        self.text_output.insert(tk.END, testo)
        self.text_output.see(tk.END)
        self.text_output.configure(state='disabled')

    def processa_input_numeric(self, event=None):
        testo = self.number_input.get().strip()
        self.number_input.delete(0, tk.END)
        self.scrivi_output(f"Numero: {testo}\n- ")

    def processa_input_function(self, event=None):
        testo = self.function_input.get().strip()
        self.function_input.delete(0, tk.END)
        self.scrivi_output(f"Funzione: {testo}\n- ")

    def processa_input_command(self, event=None):
        comando = self.command_input.get().strip()
        self.command_input.delete(0, tk.END)

        if comando.lower() == ';exit':
            self.scrivi_output("Uscita terminale simulato.\n")
            self.quit()
            return

        elif comando.lower() == ';clear':
            self.text_output.configure(state='normal')
            self.text_output.delete(1.0, tk.END)
            self.text_output.configure(state='disabled')
            self.scrivi_output("Schermo ripulito\n- ") 
            return

        elif comando.startswith(';set '):
            try:
                var, val = comando[5:].split('=')
                var = var.strip()
                val = float(val.strip())  # prova a convertire a float
                self.variables[var] = val
                self.scrivi_output(f"Variabile {var} = {val}\n- ") 
            except Exception as e:
                self.scrivi_output(f"Errore nel comando set: {e}\n- ") 
            return

        elif comando.startswith(';get '):
            var = comando[5:]  # dopo ";get "
            var = var.strip()
            if var in self.variables:
                self.scrivi_output(f"{var} = {self.variables[var]}\n- ") 
            else:
                self.scrivi_output(f"Variabile {var} non trovata\n- ") 
            return

        elif comando.startswith(';list'):
            if self.variables:
                self.scrivi_output("Variabili memorizzate:\n")
                for k, v in self.variables.items():
                    self.scrivi_output(f"{k} = {v}\n")
                self.scrivi_output("- ") 
            else:
                self.scrivi_output("Nessuna variabile memorizzata\n- ") 
            return

        # Comando non riconosciuto
        self.scrivi_output(comando + "\n - ")


