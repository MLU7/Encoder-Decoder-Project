from cmu_graphics import *

import random

encodingMatrix = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]

alphabet = "abcdefghijklmnopqrstuvwxyz"
rawText = app.getTextInput("Please type a four-letter word")
text = rawText.lower()
Label("Your Word: " + text, 85, 135, size = 20)
encryptHit = Label(0, 0, 0, size = 0)
decryptHit = Label(0, 0, 0, size = 0)
encryptButton = Rect(50, 340, 120, 50, fill = "white", border = "darkGreen")
decryptButton = Rect(230, 340, 120, 50, fill = "white", border = "darkRed")
coolStar = Star(110, 365, 0.1, 5, fill = "gold")
coolStar2 = Star(290, 365, 0.1, 5, fill = "gold")
Label("ENCRYPT", 110, 365, size = 20, bold = True, fill = "darkGreen")
Label("DECRYPT", 290, 365, size = 20, bold = True, fill = "darkRed")

newMatrix = []
encodedMatrix = []
decoderMatrix = []
inverseMatrix = []
originalMatrix = []

def buttons(x, y):
    if encryptButton.hits(x, y):
        encryptHit.value = 1
        graphics() 
        displayMatrix()
        cool()
    if decryptButton.hits(x, y):
        decryptHit.value = 1
        graphics() 
        decryption()
        convertNumbersToText()
        cool()

def graphics():
    Label("Encoder: ", 57, 30, size = 20)
    Label("Decoder: ", 57, 80, size = 20)

    Rect(112, 0, 53, 55, fill = None, border = "black", borderWidth = 1)
    Rect(128, 0, 25, 10, fill = "white")
    Rect(128, 50, 25, 10, fill = "white")

    Rect(99, 60, 110, 50, fill = None, border = "black", borderWidth = 1)
    Rect(117, 55, 75, 10, fill = "white")
    Rect(117, 105, 75, 10, fill = "white")

    encryptg1 = Rect(175, 150, 80, 55, fill = None, border = "black", borderWidth = 1, visible = False)
    encryptg2 = Rect(192, 150, 50, 10, fill = "white", visible = False)
    encryptg3 = Rect(192, 200, 50, 10, fill = "white", visible = False)

    decryptg1 = Rect(175, 223, 80, 55, fill = None, border = "black", borderWidth = 1, visible = False)
    decryptg2 = Rect(192, 218, 50, 10, fill = "white", visible = False)
    decryptg3 = Rect(192, 270, 50, 10, fill = "white", visible = False)

    if encryptHit.value == 1:
        encryptg1.visible = True
        encryptg2.visible = True
        encryptg3.visible = True

    if decryptHit.value == 1:
        decryptg1.visible = True
        decryptg2.visible = True
        decryptg3.visible = True

def convertTextToNumbers():
    i = 0
    count = 0
    while count < 4 and (len(text) == 4 and i < 26):
        if alphabet[i] == text[count]:
            newMatrix.append(i)
            count += 1
            i = 0
        else:
            i += 1

def solverMatrix():
    decoderMatrix.append(encodingMatrix[3])
    decoderMatrix.append(-encodingMatrix[1])
    decoderMatrix.append(-encodingMatrix[2])
    decoderMatrix.append(encodingMatrix[0])

    determinant = (encodingMatrix[0] * encodingMatrix[3]) - (encodingMatrix[1] * encodingMatrix[2])

    inverseMatrix.append((1/determinant) * decoderMatrix[0])
    inverseMatrix.append((1/determinant) * decoderMatrix[1])
    inverseMatrix.append((1/determinant) * decoderMatrix[2])
    inverseMatrix.append((1/determinant) * decoderMatrix[3])

    rounded1 = pythonRound(inverseMatrix[0], 2)
    rounded2 = pythonRound(inverseMatrix[1], 2)
    rounded3 = pythonRound(inverseMatrix[2], 2)
    rounded4 = pythonRound(inverseMatrix[3], 2)

    solver1 = Label(rounded1, 125, 75, size = 20, visible = True)
    solver2 = Label(rounded2, 180, 75, size = 20, visible = True)
    solver3 = Label(rounded3, 125, 95, size = 20, visible = True)
    solver4 = Label(rounded4, 180, 95, size = 20, visible = True)

def encryption():
    r1c1 = (encodingMatrix[0] * newMatrix[0]) + (encodingMatrix[1] * newMatrix[2])
    r1c2 = (encodingMatrix[0] * newMatrix[1]) + (encodingMatrix[1] * newMatrix[3])
    r2c1 = (encodingMatrix[2] * newMatrix[0]) + (encodingMatrix[3] * newMatrix[2])
    r2c2 = (encodingMatrix[2] * newMatrix[1]) + (encodingMatrix[3] * newMatrix[3])

    encodedMatrix.append(r1c1)
    encodedMatrix.append(r1c2)
    encodedMatrix.append(r2c1)
    encodedMatrix.append(r2c2)

    encoding1 = Label(encodingMatrix[0], 130, 20, size = 20, visible = True)
    encoding2 = Label(encodingMatrix[1], 150, 20, size = 20, visible = True)
    encoding3 = Label(encodingMatrix[2], 130, 40, size = 20, visible = True)
    encoding4 = Label(encodingMatrix[3], 150, 40, size = 20, visible = True)

def displayMatrix():
    yourMatrixLabel = Label("Encoded Matrix: ", 90, 180, size = 20, visible = False)
    encrypted1 = Label(encodedMatrix[0], 195, 168, size = 20, visible = False)
    encrypted2 = Label(encodedMatrix[1], 235, 168, size = 20, visible = False)
    encrypted3 = Label(encodedMatrix[2], 195, 192, size = 20, visible = False)
    encrypted4 = Label(encodedMatrix[3], 235, 192, size = 20, visible = False)

    if encryptHit.value == 1:
        yourMatrixLabel.visible = True
        encrypted1.visible = True
        encrypted2.visible = True
        encrypted3.visible = True
        encrypted4.visible = True


def decryption():
    originalMatrix.append(rounded((inverseMatrix[0] * encodedMatrix[0]) + (inverseMatrix[1] * encodedMatrix[2])))
    originalMatrix.append(rounded((inverseMatrix[0] * encodedMatrix[1]) + (inverseMatrix[1] * encodedMatrix[3])))
    originalMatrix.append(rounded((inverseMatrix[2] * encodedMatrix[0]) + (inverseMatrix[3] * encodedMatrix[2])))
    originalMatrix.append(rounded((inverseMatrix[2] * encodedMatrix[1]) + (inverseMatrix[3] * encodedMatrix[3])))

    decryptionLabel = Label("Decoded Matrix: ", 90, 250, size = 20, visible = False)
    decrypted1 = Label(originalMatrix[0], 195, 238, size = 20, visible = False)
    decrypted2 = Label(originalMatrix[1], 235, 238, size = 20, visible = False)
    decrypted3 = Label(originalMatrix[2], 195, 262, size = 20, visible = False)
    decrypted4 = Label(originalMatrix[3], 235, 262, size = 20, visible = False)

    if decryptHit.value == 1:
        decryptionLabel.visible = True
        decrypted1.visible = True
        decrypted2.visible = True
        decrypted3.visible = True
        decrypted4.visible = True

def convertNumbersToText():
    filler = ""
    i = 0
    count = 0
    while count < 4:
        if i == originalMatrix[count]:
            filler += alphabet[i]
            count += 1
            i = 0
        else:
            i += 1

    reveal = Label("Original Word: " + filler, 100, 300, size = 20, visible = False)

    if decryptHit.value == 1:
        reveal.visible = True

def cool():
    if encryptHit.value == 1 and coolStar.radius != 25.1:
        coolStar.radius += 25
    if decryptHit.value == 1 and coolStar2.radius != 25.1:
        coolStar2.radius += 25

def onMousePress(mouseX, mouseY):
    buttons(mouseX, mouseY)

graphics() 
convertTextToNumbers()
solverMatrix()
encryption()
displayMatrix()

cmu_graphics.run()