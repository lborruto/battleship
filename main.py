def menu():
	print("[1] Nouvelle partie")
	print("[2] Options")
	print("[0] Quitter")

menu()
option = int(input("Tapez votre choix:"))

while option !=0:
	if option == 1:
		#do option 1
		print ("Option 1 à été choisie")
	elif option == 2:
		#do option 2
		print ("Option 2 à été choisie")	
	else:
		print("Option invalide.")

	print()
	menu()
	option = int(input("Tapez votre choix:"))

print("Merci et a bientot!")