import tkinter as tk

# Création de la fenêtre principale
window = tk.Tk()
window.title("Tic Tac Toe")

# Initialisation du tableau
tableau_of_array = [[None] * 3, [None] * 3, [None] * 3]

# Initialisation des utilisateurs
user_X = "X"
user_O = "O"
users = [user_X, user_O] 
current_user = user_X

# Fonction pour vérifier les conditions de victoire
def win_conditions():
    # diagonales
    if tableau_of_array[0][0] == tableau_of_array[1][1] == tableau_of_array[2][2] and tableau_of_array[0][0] is not None:
        return True 
    if tableau_of_array[2][0] == tableau_of_array[1][1] == tableau_of_array[0][2] and tableau_of_array[2][0] is not None:
        return True
    # Vérification des lignes
    for row in tableau_of_array:
        if row.count(row[0]) == len(row) and row[0] is not None:
            return True
    # Vérification des colonnes
    for col in range(3):
        if tableau_of_array[0][col] == tableau_of_array[1][col] == tableau_of_array[2][col] and tableau_of_array[0][col] is not None:
            return True
    # Aucune condition de victoire n'a été remplie
    return False

# Fonction pour mettre à jour l'état du jeu
def update_game_state(row, col):
    global current_user
    # Vérification que la case est vide
    if tableau_of_array[row][col] is None:
        # Attribution de la valeur de l'utilisateur actuel à la case
        tableau_of_array[row][col] = current_user
        # Vérification des conditions de victoire
        button = buttons[row][col]
        button.config(text=current_user)
        if win_conditions():
            # Affichage du gagnant
            label.config(text=f"Le joueur {current_user} a gagné !")
            # Désactivation des cases restantes
            for i in range(3):
                for j in range(3):
                    buttons[i][j].config(state=tk.DISABLED)
        else:
            # Changement de l'utilisateur actuel
            current_user = user_O if current_user == user_X else user_X
            # Affichage de l'utilisateur actuel
            label.config(text=f"C'est au tour du joueur {current_user}")
    else:
        # La case est déjà occupée, affichage d'un message d'erreur
        label.config(text="Cette case est déjà occupée !")

# Création des boutons pour chaque case
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(window, text="", width = 10, height="5", font=("Helvetica", 20), command=lambda row=i, col=j: update_game_state(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

def restart_game():
    global tableau_of_array, current_user
    current_user = user_X
    for i in range(3):
        for j in range(3):
            tableau_of_array[i][j] = None  
            buttons[i][j].config(state=tk.NORMAL, text="")
    label.config(text=f"c'est au tour du joueur{current_user}")

restart_button = tk.Button(window, text="Redémarrer", font=("helvetica", 20), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)

# Affichage de l'utilisateur actuel
label = tk.Label(window, text=f"C'est au tour du joueur {current_user}", font=("Helvetica", 20))
label.grid(row=3, column=0, columnspan=3)

# Boucle principale
window.mainloop()