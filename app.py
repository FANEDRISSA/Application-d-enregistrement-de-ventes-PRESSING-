import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- TARIFS PRESSING ----------------
tarifs = {
    "Pantalon tissu": 400,
    "Pantalon Jean": 400,
    "Jogging": 400,
    "Chemise": 400,
    "Pull": 400,
    "Draps": 500,
    "Petite Serviette": 300,
    "Moyenne Serviette": 400,
    "Grande Serviette": 500,
    "Culotte": 400,
    "Couette petite": 1500,
    "Couette grande": 3000,
    "T-shirts": 400
}

total_global = 0

# ---------------- FONCTIONS ----------------
def prix_auto(event=None):
    produit = combo_produit.get()
    if produit in tarifs:
        entry_prix.delete(0, tk.END)
        entry_prix.insert(0, tarifs[produit])

def calculer_total():
    try:
        qte = int(entry_qte.get())
        prix = int(entry_prix.get())
        total = qte * prix
        label_total.config(text=f"Prix total : {total} FCFA")
    except ValueError:
        messagebox.showerror("Erreur", "Entrez une quantité et un prix valides")

def ajouter_vente():
    global total_global
    try:
        produit = combo_produit.get()
        if not produit:
            raise ValueError("Produit non sélectionné")

        qte = int(entry_qte.get())
        prix = int(entry_prix.get())
        total = qte * prix

        table.insert("", tk.END, values=(produit, qte, prix, total))
        total_global += total
        label_global.config(text=f"Total global : {total_global} FCFA")

        entry_qte.delete(0, tk.END)
        entry_prix.delete(0, tk.END)
        label_total.config(text="Prix total : ")

    except ValueError:
        messagebox.showerror("Erreur", "Vérifiez les informations saisies")

def a_propos():
    messagebox.showinfo(
        "À propos",
        "Pressing Pro\n"
        "Application d'enregistrement de ventes\n\n"
        "Développée en Python (Tkinter)\n"
        "Auteur : Drissa Fane"
    )

# ---------------- INTERFACE ----------------
fenetre = tk.Tk()
fenetre.title("Pressing Pro – Enregistrement de ventes")
fenetre.geometry("750x600")

# -------- CLIENT --------
tk.Label(fenetre, text="Nom du client").pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

tk.Label(fenetre, text="Contact").pack()
entry_contact = tk.Entry(fenetre)
entry_contact.pack()

# -------- PRODUIT --------
tk.Label(fenetre, text="Produit").pack()
combo_produit = ttk.Combobox(fenetre, values=list(tarifs.keys()), state="readonly")
combo_produit.pack()
combo_produit.bind("<<ComboboxSelected>>", prix_auto)

tk.Label(fenetre, text="Quantité").pack()
entry_qte = tk.Entry(fenetre)
entry_qte.pack()

tk.Label(fenetre, text="Prix unitaire").pack()
entry_prix = tk.Entry(fenetre)
entry_prix.pack()

label_total = tk.Label(fenetre, text="Prix total : ")
label_total.pack(pady=5)

# -------- BOUTONS --------
frame_btn = tk.Frame(fenetre)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Calculer", command=calculer_total).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Ajouter vente", command=ajouter_vente, bg="green", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="À propos", command=a_propos).grid(row=0, column=2, padx=5)

# -------- TABLE DES VENTES --------
table = ttk.Treeview(
    fenetre,
    columns=("Produit", "Quantité", "Prix", "Total"),
    show="headings"
)

for col in ("Produit", "Quantité", "Prix", "Total"):
    table.heading(col, text=col)
    table.column(col, anchor="center")

table.pack(fill="both", expand=True, pady=10)

label_global = tk.Label(
    fenetre,
    text="Total global : 0 FCFA",
    font=("Arial", 12, "bold")
)
label_global.pack(pady=10)

fenetre.mainloop()
