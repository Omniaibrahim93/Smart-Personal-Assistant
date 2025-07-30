import tkinter as tk
from tkinter import scrolledtext

from intents import IntentAnalyzer

class SmartAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Personal Assistant")
        self.intent_analyzer = IntentAnalyzer()
        self._build_widgets()

    def _build_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(input_frame, text="Enter Command:").pack(side=tk.LEFT)
        self.input_entry = tk.Entry(input_frame, width=50)
        self.input_entry.pack(side=tk.LEFT, padx=(5,0))
        self.input_entry.bind('<Return>', self._on_submit)

        self.submit_button = tk.Button(input_frame, text="Go", command=self._on_submit)
        self.submit_button.pack(side=tk.LEFT, padx=(5,0))

        tk.Label(self.root, text="Assistant Output:").pack(anchor='w', padx=10)
        self.output_area = scrolledtext.ScrolledText(self.root, height=10, wrap=tk.WORD, state='disabled')
        self.output_area.pack(padx=10, pady=(0,5), fill=tk.BOTH, expand=True)

        tk.Label(self.root, text="Status Log:").pack(anchor='w', padx=10)
        self.log_area = scrolledtext.ScrolledText(self.root, height=5, wrap=tk.WORD, state='disabled')
        self.log_area.pack(padx=10, pady=(0,10), fill=tk.BOTH)

    def _on_submit(self, event=None):
        user_input = self.input_entry.get().strip()
        if not user_input:
            return
        self.input_entry.delete(0, tk.END)

        self._log(f"Received: {user_input}")

        intent_info = self.intent_analyzer.analyze_intent(user_input)
        self._log(f"Detected intent: {intent_info['intent']}")

        response = self.intent_analyzer.execute_intent(intent_info)

        self._display_response(response)
        self._log(f"Action completed for intent: {intent_info['intent']}")

    def _display_response(self, message: str):
        self.output_area.configure(state='normal')
        self.output_area.insert(tk.END, message + '\n')
        self.output_area.configure(state='disabled')
        self.output_area.see(tk.END)

    def _log(self, message: str):
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, message + '\n')
        self.log_area.configure(state='disabled')
        self.log_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartAssistantGUI(root)
    root.mainloop()
