# Compilamos y ejecutamos los ejercicios en un unico fichero

NAME=hello
OBJ=$(NAME).py

main: $(OBJ)

run: main
	./$(OBJ)

rerun: run

.PHONY: run rerun

