import pyautogui
from piece import Piece
import pyscreeze
from heap import MinHeap
import time
import copy


class Agente:
    X: int = 0
    Y: int = 0
    pieza: Piece
    # 0 si no hay nada y 1 si hay algo
    heap: MinHeap
    estado_tablero: list

    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y
        # iniciar el heap en 0 junto con el índice horizontal
        self.heap = MinHeap(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.altura_tablero = [0] * 10
        self.estado_tablero = [([0]*10) for i in range(20)]
        # revisa que la altura sea la correcta para no dejar huecos

    def eliminar_lineas(self):
        i = 0
        while i < 20:
            if 0 in self.estado_tablero[i]:
                i += 1
                continue
            for j in range(10):
                self.altura_tablero[j] -= 1
                self.heap.heap[j][0] -= 1
                if (self.altura_tablero[j] != i):
                    continue
                a = 1
                while (i-a >= 0 and self.estado_tablero[i-a][j] == 0):
                    a += 1
                    self.altura_tablero[j] -= 1
                    self.heap.changePriority(self.heap.getIndex(j),
                                             self.altura_tablero[j])

            del self.estado_tablero[i]
            self.estado_tablero.append([0] * 10)

    def is_move_possible(self, altitud):
        idx = 0

        # las coordenadas estan en formato de array[array[tuplas]]
        for x in self.pieza.arr_coordenadas:
            terminado = True
            coord = {}
            for i in x:
                # si deja huecos marca como falso y deja de mirar ahí
                # altitud [0] es la relativa de donde pondrá la pieza,
                # altitud[1] es el índice horizontal
                # i[0] es lo que ocupa la pieza en horizontal
                # i[1] es lo que ocupa en vertical
                try:
                    if i[0] in coord.keys():
                        coord[i[0]] += 1
                        continue
                    coord.update({i[0]: 1})
                    if (altitud[1] + i[0] < 0):
                        raise IndexError
                    if (altitud[0] + i[1] < 0):
                        raise IndexError
                    if (altitud[0] + i[1]
                            != self.altura_tablero[altitud[1] + i[0]]):
                        terminado = False
                        break
                    # añade las coordenadas

                except IndexError:
                    terminado = False
                    break
                # except:
                #    break
            if terminado:
                # cuenta las coordenadas y frecuencia
                for i in x:
                    self.estado_tablero[altitud[0]+i[1]][altitud[1]+i[0]] = 1
                for k in coord.keys():
                    # actualiza el tablero y el heap
                    self.altura_tablero[altitud[1] + k] += coord[k]
                    self.heap.changePriority(
                        self.heap.getIndex(altitud[1] + k),
                        self.altura_tablero[altitud[1] + k])
                # check por si hay que disminuir las alturas
                # por cosas de la rotación hay un index que anota cuantos giros
                # a su vez prioriza los estados horizontales
                # hace las rotaciones

                self.eliminar_lineas()
                print("alturas: " + str(self.altura_tablero))
                print("cola prioridad: ")
                self.heap.display()
                pyautogui.press(
                    'up', self.pieza.n_rotations[idx])#, interval=0.1)
                return True
            # lleva la cuenta de las rotaciones
            idx += 1
        return False

    def ultima_baza(self, altitud):
        coord = {}
        for i in self.pieza.arr_coordenadas[-1]:
            # debe tomar las alturas para saber desde done la va a poner
            if i[0] in coord.keys():
                coord[i[0]] += 1
                continue
            if (altitud[1] + i[0] < 0):
                return False
            if (altitud[0] + i[1] < 0):
                return False
            coord.update({i[0]: altitud[1] + i[1]})
        for i in self.pieza.arr_coordenadas[0]:
            try:
                if (self.estado_tablero[altitud[0]+i[1]][altitud[1]+i[0]]
                        == 1):
                    return False
            except (IndexError):
                return False
        for i in self.pieza.arr_coordenadas[-1]:
            self.estado_tablero[altitud[0]+i[1]][altitud[1]+i[0]] = 1
        for k in coord.keys():
            # actualiza el tablero y el heap
            # print ("k: "+ str(k) +" c: "+ str(c[k]))
            # print("indice 1+k: " + str(altitud[1]+k))
            self.altura_tablero[altitud[1] + k] = coord[k] + 1
            self.heap.changePriority(self.heap.getIndex(altitud[1] + k),
                                     self.altura_tablero[altitud[1] + k])
        self.eliminar_lineas()
        print("Ultima Baza!!")

        # por cosas de la rotación hay un index que anota cuantos giros
        # a su vez prioriza los estados horizontales
        # hace las rotaciones
        print("alturas: " + str(self.altura_tablero))
        print("cola prioridad: ")
        self.heap.display()
        # pyautogui.press('up', self.pieza.n_rotations[0])
        return True

    def determinar_move(self):
        move = False
        # para recorrer el heap
        index = 0
        heap_copy = copy.deepcopy(self.heap)
        heap_copy2 = copy.deepcopy(self.heap)
        while not move:
            # buff es el índice a donde se movería la pieza

            buff = heap_copy.extractMin()
            print(buff)
            move = self.is_move_possible(buff)
            if (index < 9):
                index += 1
            else:
                # si no encuentra movimiento posible guarda la pieza
                # Camilo: 700, 374
                (x, y, z) = pyscreeze.pixel(720, 337)
                print("pixel 720, 337" + str(pyscreeze.pixel(720, 337)))
                if (x in range(11, 52) and y in range(10, 52) and
                        z in range(10, 52)):
                    for i in range(10):
                        buff = heap_copy2.extractMin()
                        print(buff)
                        if self.ultima_baza(buff):
                            break
                    break
                else:
                    pyautogui.press(['c'])
                    return
        # envia la pieza a donde la quiere ubicar
        # todas las piezas las tomo como si estuvieran en el punto 4 horizontal
        horizontal_mv = 4 - buff[1]
        if horizontal_mv > 0:
            pyautogui.press('left', presses=horizontal_mv)#, interval=0.1)

        else:
            pyautogui.press(
                'right', presses=(-1 * horizontal_mv))#, interval=0.1)

        # la baja rápido
        pyautogui.press('space')

    def determinar_pieza(self):
        color = pyscreeze.pixel(self.X, self.Y)
        
        # time.sleep(0.1)
        if color in ((116, 255, 235), (80, 240, 185)):
            #print("pixel 720, 337" + str(pyscreeze.pixel(720, 337)))
            #(x, y, z) = pyscreeze.pixel(720, 337)
            #if (x in range(8, 51) and y in range(8, 51) and
            #        z in range(8, 51)):
            return Piece('I')
            #pyautogui.press('c')
            return self.determinar_pieza()

        elif color in ((237, 255, 116), (181, 240, 78)):
            return Piece('S')
        elif color in ((255, 119, 130), (229, 72, 80)):
            return Piece('Z')
        elif color in ((255, 189, 118), (232, 134, 74)):    
            return Piece('L')
        elif color in ((153, 127, 255), (92, 71, 190))  :
            return Piece('J')
        elif color in ((255, 128, 255), (195, 74, 182)):
            return Piece('T')
        elif color in ((255, 255, 118), (236, 206, 76)):
            return Piece('O')
        else:
            print("nuevo color: " + str(color))
            # file = open("colores.txt", "r+")
            # content = file.read()
            # if (str(color)+'\n') not in content:
            #    file.write(str(color)+'\n')
            # file.close()
            return self.determinar_pieza()

    def move(self):
        self.pieza = self.determinar_pieza()
        print(self.pieza.nombre)
        self.determinar_move()

    def compute(self):
        self.move()
