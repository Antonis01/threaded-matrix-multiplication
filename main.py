import threading
import time

class MatrixMultiplier:
    def __init__(self, matrixA, matrixB):
        # Initialize the matrices
        self.matrixA = matrixA
        self.matrixB = matrixB


    def threadedMultiplication(self):
        # Initialize the result matrix
        result = [[0] * len(self.matrixB[0]) for _ in range(len(self.matrixA))]
        times = [0] * len(self.matrixA)

        # Create threads
        threads = []
        for rows in range(len(self.matrixA)):
            # Create a thread for each row
            thread = threading.Thread(target=self._rowMultiplication, args=(result, rows, times))
            threads.append(thread)
            thread.start()

        for thread in threads:
            # Wait for the thread to finish
            thread.join()

        # Print the result matrix and the total execution time
        self.printMatrix(result, 0)
        print(f"Total execution time: {max(times):.6f} seconds")
        return result, times


    def _rowMultiplication(self, result, index, times):
        colA = len(self.matrixA[0])
        colB = len(self.matrixB[0])

        startTime = time.time()
        
        # Matrix Multiplication
        for j in range(colB):
            result[index][j] = sum(self.matrixA[index][k] * self.matrixB[k][j] for k in range(colA))
        
        endTime = time.time()
        times[index] = endTime - startTime
        print(f"Thread {index+1} execution time: {times[index]:.6f} seconds")
  

    def sequentialMultiplication(self):
        rowsA = len(self.matrixA)
        colsA = len(self.matrixA[0])
        colsB = len(self.matrixB[0])

        result = [[0] * colsB for _ in range(rowsA)]
        
        startTime = time.time()

        # sequential Matrix Multiplication
        for i in range(rowsA):
            for j in range(colsB):
                result[i][j] = sum(self.matrixA[i][k] * self.matrixB[k][j] for k in range(colsA))
        endTime = time.time()
        self.printMatrix(result, 1)
        print (f"Total execution time: {endTime - startTime:.6f} seconds")

    
    @staticmethod
    def inputData():
        matrixA = []
        rowsA = int(input("Enter the number of rows for matrix A: "))
        colsA = int(input("Enter the number of columns for matrix A: "))
        
        # Insert data for matrix A
        for rA in range(rowsA):
            matrixA.append([])
            for cA in range(colsA):
                matrixA[rA].append(int(input(f"[{rA+1}, {cA+1}]: ")))
   
        matrixB = []
        rowsB = int(input("\nEnter the number of rows for matrix B: "))

        # Check if the number of columns in matrix A is equal to the number of rows in matrix B
        if colsA != rowsB:
            print("Matrix multiplication is not possible")
            exit(0)
        colsB = int(input("Enter the number of columns for matrix B: "))

        # Insert data for matrix B
        for rB in range(rowsB):
            matrixB.append([])
            for cB in range(colsB):
                matrixB[rB].append(int(input(f"[{rB+1}, {cB+1}]: ")))
        
        return matrixA, matrixB


    @staticmethod
    def printMatrix(matrix, check):
        if check == 0:
            print("\n(threaded execution)\nA * B = [")
        elif check == 1:
            print("(sequential execution)\nA * B = [")
        elif check == 2:
            print("\nMatrix A = [")
        elif check == 3:
            print("\nMatrix B = [")
               
        for row in matrix:
            print(row)

        print("]")


    def seperator():
        print("\n===========================================================================")

if __name__ == "__main__":
    # Insert data for the matrices
    matrixA, matrixB = MatrixMultiplier.inputData()

    MatrixMultiplier.seperator()
    # Print the matrices
    MatrixMultiplier.printMatrix(matrixA, 2)
    MatrixMultiplier.printMatrix(matrixB, 3)
    
    # Initialize the class
    m = MatrixMultiplier(matrixA, matrixB)
    
    MatrixMultiplier.seperator()
    # Call the threads function
    result, times = m.threadedMultiplication()
    
    MatrixMultiplier.seperator()
    # Call the sequential function
    m.sequentialMultiplication()
    MatrixMultiplier.seperator()
