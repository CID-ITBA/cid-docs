"""
SimiLab.py
====================================
The core module of this NLP package! 
"""

import numpy as np
from scipy import spatial

class testClass:
    """
    Class dedicated to package testing.
    DELETE FOR DEPLOYING
    """
    def __init__(self):
        print("Class instantiation succesful")
    
    def say_hello(self):
        print("Hey! This seems to be working")
        
class tempName:
    """
    This class will allow you to track how words changes across time 
    using embedding matrices of a given corpus. These matrices should be aligned with
    Procrustes.

    Parameters
    --------
    matrices : array_like
                Embedding matrices
    yearDict : dict
                Stores the row index for a given word for each matrix
    vocabularies : dict
                Need to define

    """
    def __init__(self, matrices, yearDict, vocabularies):
        self.vocabularies = vocabularies # lista de vocabularios utilizados para generar las matrices
        self.inverseVocab = []
        for vocabulary in vocabularies:
            self.inverseVocab.append( dict(map(reversed, vocabulary.items())) ) # diccionarios inversos de los vocabularios
        self.matrices = matrices    # matrices de embedding por year
        self.yearDict = yearDict    # diccionario que vincula year con indice en matrices
        self.projectionFlag = False

    '''  INIT DE CARLOS
    def __init__(self, model="dw2v", dataset="nyt"):
        with open("models/{}/{}/dictionary.pck".format(model,dataset),"rb") as f:
            dictionary = pickle.load(f)
        self.vocabulary = dictionary # vocabulario utilizado para generar las matrices
        self.inverseVocab = dict(map(reversed, dictionary.items())) # diccionario inverso del vocabulario
        mypath = "models/{}/{}/".format(model,dataset)
        files=glob.glob(mypath+"/*.npy")
        matrix_files = [f.split(mypath)[1] for f in files]

        self.cant_slices = len(matrix_files)
        self.yearDict = {file.split("-")[1][:-4]:int(file.split("-")[0]) for file in matrix_files if file != "dictionary.pck"}
        self.matrices = list(range(self.cant_slices))
        for file in matrix_files:
            if file != "dictionary.pck":
                idx=int(file.split("-")[0])
                self.matrices[idx] = np.load("models/{}/{}/".format(model,dataset)+file)    # matrices de probabilidad de coocurrencia por year
        self.model = model
        self.dataset = dataset
    '''

    def findSimilars2Vec(self, vector, year, threshold = 0, maxWords = None):
        """
        Finds the most similar words within a word2vec embedding matrix.
        This function computes the cosine similarities between embedding vectors
        and a given vector. Returning the most similar words within a given treshold.
        
        Parameters
        --------
        vector : array_like
            Input Vector. Must match embedding dimension.
        year : int
            Choosen year.
        threshold : float
            Minimun cosine similarity allowed to consider a word 'close' to the given vector.
            If left blank, the default value is 0, which allows for all vectors to be considered.
        maxWords : int
            Maximum number of words to be returned as most similar.
            If left blank, the default value is 'None', which allows for all vectors to be considered.
        
        Returns
        -------
        out : dict
            A dictionary containing the words found and its
            cosine similarities with respect to given input vector.
        Raises
        ------
        ValueError
            if 'treshold' is a negative floating point number, or it's value is greater than 1.0.
            if 'year' is not present in the current data.

        Examples
        --------
        >>> ma = [[-1,-2,-3],[4,5,6],[7,8,9]]
        >>> mb = [[1,2.1,3],[4.2,4.8,6],[7.02,8,9.3]]
        >>> mc = [[1.1,2.2,3.1],[4.23,5,6],[7.03,8,9.32]]

        >>> matrices = [ma, mb, mc]
        >>> yearDict = {1990:0, 1991:1, 1995:2}
        >>> vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
        >>> vocabularies = [vocab1990]

        >>> tempObject = tempName(matrices, yearDict, vocabularies)

        >>> newVec = tempObject.findSimilars([1,2,3], 3, 1990)
        
        >>> print(newVec)

        >>> {'pablo': 0.9746318461970761, 'carlos': 0.9594119455666702, 'martin': -1.0}
        
        """
        if threshold >= 0.0 and threshold < 1.0:
            yearIndex = self.yearDict.get(year, -1) # obtengo el indice del año, si no esta el año devuelve -1
            if(yearIndex != -1):
                tempMat = self.matrices[yearIndex] # obtengo la matriz del año pedido
                results = {} # container para los resultados encontrados dict{string, sim}
                # np.transpose(tempMat) si la palabra es la columna
                similarities = []
                for index, word in enumerate(tempMat): # ASUMIENDO QUE LA PALABRA ES LA FILA!!!
                    cosSim = 1 - spatial.distance.cosine(vector, word) # se obtiene la similitud coseno entre word y vector
                    if np.abs(cosSim) > threshold: # si la similitud coseno cae dentro del threshold dado
                        similarities.append([index, cosSim]) # se guarda en similarities una lista de elementos [indice, similitud]
                similarities.sort(key=lambda elem: elem[1], reverse=True) # se ordena la lista de mayor a menor similitud
                mostSimilar = similarities[0:maxWords] # se guardan en mostSimilar los 'maxWords' elementos con mayor similitud
                for index, cosSim in mostSimilar:
                    results[ self.inverseVocab[yearIndex][index] ] = cosSim
                return results
            
            else:
                raise ValueError("Year not present")

        else:
            raise ValueError("Treshold value must be positive or zero and under 1.0")

    def findSimilars2Word(self, word, year, threshold = 0, maxWords = None):
        """
        Finds the most similar words within a word2vec embedding matrix.
        This function computes the cosine similarities between embedding vectors
        and a given word. Returning the most similar words within a given treshold.
        
        Parameters
        --------
        word : string
                Input Word. Must be part of selected year's vocabulary.
        year : int
            Choosen year.
        threshold : float
            Minimun cosine similarity allowed to consider a word 'close' to the given vector.
            If left blank, the default value is 0, which allows for all vectors to be considered.
        maxWords : int
            Maximum number of words to be returned as most similar.
            If left blank, the default value is 'None', which allows for all vectors to be considered.

        Returns
        -------
        out : dict
            A dictionary containing the words found and its
            cosine similarities with respect to given input word.

        Examples
        --------
        >>> ma = [[-1,-2,-3],[4,5,6],[7,8,9]]
        >>> mb = [[1,2.1,3],[4.2,4.8,6],[7.02,8,9.3]]
        >>> mc = [[1.1,2.2,3.1],[4.23,5,6],[7.03,8,9.32]]

        >>> matrices = [ma, mb, mc]
        >>> yearDict = {1990:0, 1991:1, 1995:2}
        >>> vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
        >>> vocabularies = [vocab1990]

        >>> tempObject = tempName(matrices, yearDict, vocabularies)
        >>> newVec = tempObject.findSimilars2Word('pablo', 3, 1990)
        >>> print(newVec)
            {'pablo': 1.0, 'carlos': 0.9981908926857268, 'martin': -0.974631846197076}
        
        """
        vector = self.getVector(word, year)
        similars = self.findSimilars2Vec(vector, year, threshold, maxWords)

        return similars

    def histSimilar(self, vector, threshold):
        histograma = []

        return histograma

    def getVector(self, word, year):
        """
        Finds the vectorized representation of a given word within a word2vec embedding matrix.
        This function looks for a chosen word in a given year's vocabulary and, if posible,
        identifies it's corresponding vector. Returning the vectorized representation of the word.
        
        Parameters
        --------
        word : string
                Input Word. Must be part of selected year's vocabulary.
        year : int
            Choosen year.
        
        Returns
        -------
        out : array_like
            The selected word's vectorized representation.
        Raises
        ------
        ValueError
            if 'word' is not present in the year's vocabulary.
            if 'year' is not present in the current data.

        Examples
        --------
        >>> ma = [[-1,-2,-3],[4,5,6],[7,8,9]]
        >>> mb = [[1,2.1,3],[4.2,4.8,6],[7.02,8,9.3]]
        >>> mc = [[1.1,2.2,3.1],[4.23,5,6],[7.03,8,9.32]]
        >>> matrices = [ma, mb, mc]
        >>> yearDict = {1990:0, 1991:1, 1995:2}
        >>> vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
        >>> vocabularies = [vocab1990]
        >>> tempObject = tempName(matrices, yearDict, vocabularies)
        >>> newVec = tempObject.getVector('pablo', 1990)
        >>> print(newVec)
            [4, 5, 6]
        
        """        
        yearIndex = self.yearDict.get(year, -1) # obtengo el indice del año, si no esta el año devuelve -1
        if(yearIndex != -1):
            tempMat = self.matrices[yearIndex] # obtengo la matriz del año pedido
            tempVocab = self.vocabularies[yearIndex] # obtengo el vocabulario del año
            wordIndex = tempVocab.get(word, -1) # devuelve la fila donde se encuentra la palabra o -1 si no esta
            if(wordIndex != -1):
                vector = tempMat[wordIndex]
                return vector
            
            else:
                raise ValueError("Word not present in selected year's vocabulary")

        else:
            raise ValueError("Year not present")

    # Esta funcion devuelve un vector de ceros de tamaño segun el año seleccionado. ES PROVISIONAL Y SUJETA A SER ELIMINADA, SE UTILIZA EN EL SIGUIENTE METODO
    def getZeroVector(self, year):
        yearIndex = self.yearDict.get(year, -1)
        if(yearIndex != -1):
            tempMat = self.matrices[yearIndex] # obtengo la matriz del año pedido
            exampleVector = tempMat[0]
            zeroVector = np.zeros_like(exampleVector)
            
            return zeroVector
        else:
            raise ValueError("Year not present")

    def getVectorPosNeg(self, positives, negatives, year):
        """
        This function obtains a vector by computing the sum
        of all the vectorized words in 'positives' and subtracting
        all vectorized words from 'negatives'. Returning said vector.
        
        Parameters
        --------
        positives : array_like
            All words to add to resulting vector.
        negatives : array_like
            All words to subtract from resulting vector.
        year : int
            Chosen year.

        Returns
        -------
        out : array_like
            Resulting vector from adding all positives and subtracting all negatives
        Examples
        --------
        """

        if(isinstance(positives, str)):
            vector = self.getVector(positives, year)

        else:
            vector = self.getZeroVector(year)

            if(isinstance(positives, list) and isinstance(negatives, list)):
                for word in positives:
                    vector += self.getVector(word, year)
                
                for word in negatives:
                    vector -= self.getVector(word, year)

            elif(isinstance(positives, dict) and isinstance(negatives, dict)):
                for word in positives:
                    vector += self.getVector(word, positives[word])
                
                for word in negatives:
                    vector -= self.getVector(word, negatives[word])

        return vector

# getAnalogy
# Recibe lista de palabras pos y año para cada palabra, lista de palabras neg y año para c/u (puede ser dict word:year), threshold y maxWords
# Recibe year out (nada = todos los años, numero o lista) para saber en donde llamar a findSim
# Tiene plotWords (lista) para hacer seguimiento (grafico) y savePath a donde se guardaria el png (si no hay solo plottea)
# Validacion: ambas dict o ambas list. Si son list recibe año y es el mismo para ambas (fijarse de reescribir posneg al mismo formato)
# Si pos es un string, neg se ignora y solo recibo pos y año
# Devuelve como findsimtovec  

    def getAnalogy(self, positives, negatives, year = None, threshold = 0, maxWords = None, yearOut = None, plotWords = None, savePath = None):
        
        resultList = []
        vector = self.getVectorPosNeg(positives, negatives, year)
        if(isinstance(yearOut, int)):
            resultList[0] = self.findSimilars2Vec(vector, yearOut, threshold, maxWords)
        elif(isinstance(yearOut, list)):
            for index, eachYear in yearOut:
                resultList[index] = self.findSimilars2Vec(vector, eachYear, threshold, maxWords)
        elif(isinstance(yearOut, None)):
            for index, eachYear in self.yearDict:
                resultList[index] = self.findSimilars2Vec(vector, eachYear, threshold, maxWords)
        
        if(plotWords != None):
            print("Aca ira el plotteo y/o guardado del grafico")

        return resultList

    def getSim(self, w1, y1, w2, y2):
        """
        Finds the similarity between two selected words in two given years.
        This function computes the cosine similarity between the vectorized
        representation of a first word in a selected year, and the vector for
        a second word in another year. Returning the cosine similarity between
        the two vectors. 
        
        Parameters
        --------
        y1 : int
            First choosen year.
        w1 : string
            First input word. Must be present in y1.
        y2: int
            Second choosen year.
        w2 : string
            Second input word. Must be present in y2.
        
        Returns
        -------
        out : float
            Cosine similarity between the obtained vectors from w1 and w2.
        """
        firstVec = self.getVector(w1, y1)
        secondVec = self.getVector(w2, y2)
        cosSim = 1 - spatial.distance.cosine(firstVec, secondVec)

        return cosSim

    def getEvol(self, w1, y1, y2):  # esta bien? si recuerdo bien evol era la cosSim de una word con si misma en otro year
        """
        Finds a given word's evolution between two years.
        This function computes the cosine similarity between the vectorized
        representation of a given word in one year and the same word in a 
        different year. Returning said cosine similarity.
        
        Parameters
        --------
        y1 : int
            First choosen year.
        w1 : string
            Input word. Must be present in y1 and y2.
        y2: int
            Second choosen year.
        
        Returns
        -------
        out : float
            Cosine similarity between the obtained vectors from w1 in both years.
        """
        evol = self.getSim(w1, y1, w1, y2)

        return evol


# hay que resolver mejor la falta de una palabra en el año (bypass)
    def getEvolByStep(self, word):
        """
        Finds one word's evolution throughout all years.
        This function computes the cosine similarities between the vectorized
        representation of a given word from one year to the next, covering all years.
        
        Parameters
        --------
        word : string
            Choosen word.
        
        Returns
        -------
        out : array_like
            A list containing all cosine similarities from one year to the next.
            If the word is missing from one of the two compared years, 'missing'
            is returned in the list's corresponding position.
        """
        evolution = []
        yearQuantity = len(self.yearDict)
    
        for yearIndex in range(0, yearQuantity - 1):

            mat1 = self.matrices[yearIndex]
            vocab1 = self.vocabularies[yearIndex]
            wordIndex1 = vocab1.get(word, -1)
            if(wordIndex1 == -1):                   # si la palabra no esta en el año, se saltea esta comparacion (nunca sucede si proyecta)
                evolution.append('missing')
                continue
            vector1 = mat1[wordIndex1]

            mat2 = self.matrices[yearIndex+1]
            vocab2 = self.vocabularies[yearIndex+1]
            wordIndex2 = vocab2.get(word, -1)
            if(wordIndex2 == -1):
                evolution.append('missing')
                continue
            vector2 = mat2[wordIndex2]

            cosSim = 1 - spatial.distance.cosine(vector1, vector2)
            evolution.append(cosSim)

        return evolution

    def projectMatrices(self):
        """
        Proyects all matrices and vocabularies from oldest to newest.
        This function progressively adds missing words from the oldest matrices 
        and vocabularies to the newer ones, resulting in a complete vocabulary
        for the final year and a matrix with all the word's vectorized representations.
        
        Parameters
        --------
        None
        
        Returns
        -------
        out : None
            Nothing.
        """
        for yearIndex in range(0, len(self.yearDict)-1):
            missingKeys = self.vocabularies[yearIndex].keys() - self.vocabularies[yearIndex+1].keys()
            for key in missingKeys:
                keyValue = self.vocabularies[yearIndex][key]
                vector = self.matrices[yearIndex][keyValue]
                self.matrices[yearIndex+1].append(vector)
                self.vocabularies[yearIndex+1][key] = len(self.matrices[yearIndex+1])-1

        self.projectionFlag = True


    def checkProjection(self):
        """
        Checks if the model's matrices have been projected by the user.
        Returning the state of projection.
        
        Parameters
        --------
        None
        
        Returns
        -------
        out : bool
            False if the matrices are not projected.
            True if the matrices are projected.
        """
        return self.projectionFlag



# ma = [[-1,-2,-3],[4,5,6],[7,8,9],[7,8,9]]
# mb = [[1,2.1,3],[4.2,4.8,6],[7.03,8,9.32]]
# mc = [[1.1,2.2,3.1],[4.23,5,6]]

# matrices = [ma, mb, mc]
# yearDict = {1990:0, 1991:1, 1995:2}
# vocab1990 = {'martin':0, 'pablo':1, 'carlos':2, 'fran':3}
# vocab1991 = {'martin':0, 'pablo':1, 'carlos':2}
# vocab1995 = {'martin':0, 'pablo':1}
# vocabularies = [vocab1990, vocab1991, vocab1995]

# tempObject = tempName(matrices, yearDict, vocabularies)

# newVec1 = tempObject.findSimilars2Vec([1,2,3], 1990)
# newVec2 = tempObject.findSimilars2Word('pablo', 1990, 0, 2)
# newVec3 = tempObject.getVector('pablo', 1990)

# pos = ['pablo', 'martin']
# neg = ['carlos']
# newVec4 = tempObject.getVectorPosNeg(pos, neg, 1990)

# newVec5 = tempObject.getSim('pablo', 1990, 'pablo', 1990)
# newVec6 = tempObject.getEvol('pablo', 1990, 1990)
# newVec7 = tempObject.getEvolByStep('carlos')

# print(newVec1)
# print(newVec2)
# print(newVec3)
# print(newVec4)
# print(newVec5)
# print(newVec6)
# print(newVec7)

# print(tempObject.checkProjection())
# tempObject.projectMatrices()
# print(tempObject.checkProjection())