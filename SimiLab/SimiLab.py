"""
SimiLab.py
====================================
The core module of this NLP package! 
"""

'''   Clase
- Recibe las matrices
- Recibe el vocabulario (dict)
- dict{word, sim} findSimilar(V, threshold, year)
- lista histSimilar(V, threshold)
- array getVector(word, year)
- getVector(positives = [], negatives = [], year)
- getSim(w1, y1, w2, y2)
- getEvol(w1, y1, w2)
- list(year-1) getEvolByStep(w1)
'''
#pipreqs \packagedirectory
import numpy as np
from scipy import spatial

'''
def validate(matrixes, vocabulary, yearDict):
    success = True
    if not isinstance(vocabulary, dict):
        success = False
    if not isinstance(yearDict, dict):
        success = False
    if matrixes
'''
    
class tempName:
    """
    This class will allow you to track how words changes across time 
    using embedding matrices of a given corpus. These matrices should be aligned with
    Procrustes.

    Parameters
    --------
    matrixes : array_like
                Embedding matrices
    yearDict : dict
                Stores the row index for a given word for each matrix
    vocabularies : dict
                Need to define

    """
    def __init__(self, matrixes, yearDict, vocabularies):
        self.vocabularies = vocabularies # lista de vocabularios utilizados para generar las matrices
        self.inverseVocab = []
        for vocabulary in vocabularies:
            self.inverseVocab.append( dict(map(reversed, vocabulary.items())) ) # diccionarios inversos de los vocabularios
        self.matrixes = matrixes    # matrices de probabilidad de coocurrencia por year
        self.yearDict = yearDict    # diccionario que vincula year con indice en matrixes

    def findSimilars2Vec(self, vector, threshold, year):
        """
        Finds the most similar words within a word2vec embedding matrix.
        This function computes the cosine similarities between embedding vectors
        and a given vector. Returning the most similar words within a given treshold.
        
        Parameters
        --------
        vector : array_like
                Input Vector. Must match embedding dimension.
        threshold : float, int
                    * float: minimun cosine similaritie allowed to consider a word 'close' to the given vector.
                    * int: amount of near words to search. 
        year : int
            Choosen year.
        
        Returns
        -------
        out : dict
            A dictionary containing the words found and its
            cosine similarities with respect to given input vector.
        Raises
        ------
        ValueError
            if 'treshold' is a negative floating point number.
            if 'year' is not present in the current data.
        See Also
        --------
        numpy.fft : for definition of the DFT and conventions used.
        ifft : The inverse of `fft`.
        fft2 : The two-dimensional FFT.
        fftn : The *n*-dimensional FFT.
        rfftn : The *n*-dimensional FFT of real input.
        fftfreq : Frequency bins for given FFT parameters.
        Notes
        -----
        FFT (Fast Fourier Transform) refers to a way the discrete Fourier
        Transform (DFT) can be calculated efficiently, by using symmetries in the
        calculated terms.  The symmetry is highest when `n` is a power of 2, and
        the transform is therefore most efficient for these sizes.
        The DFT is defined, with the conventions used in this implementation, in
        the documentation for the `numpy.fft` module

        Examples
        --------
        >>> ma = [[-1,-2,-3],[4,5,6],[7,8,9]]
        >>> mb = [[1,2.1,3],[4.2,4.8,6],[7.02,8,9.3]]
        >>> mc = [[1.1,2.2,3.1],[4.23,5,6],[7.03,8,9.32]]

        >>> matrixes = [ma, mb, mc]
        >>> yearDict = {1990:0, 1991:1, 1995:2}
        >>> vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
        >>> vocabularies = [vocab1990]

        >>> tempObject = tempName(matrixes, yearDict, vocabularies)

        >>> newVec = tempObject.findSimilars([1,2,3], 3, 1990)
        
        >>> print(newVec)

        >>> {'pablo': 0.9746318461970761, 'carlos': 0.9594119455666702, 'martin': -1.0}
        
        """
        if threshold > 0:
            yearIndex = self.yearDict.get(year, -1) # obtengo el indice del año, si no esta el año devuelve -1
            if(yearIndex != -1):
                tempMat = self.matrixes[yearIndex] # obtengo la matriz del año pedido
                results = {} # container para los resultados encontrados dict{string, sim}
                # np.transpose(tempMat) si la palabra es la columna
                if type(threshold) is float:
                    if threshold < 1.0:
                        for index, word in enumerate(tempMat): # ASUMIENDO QUE LA PALABRA ES LA FILA!!!
                            cosSim = 1 - spatial.distance.cosine(vector, word) # se obtiene la similitud coseno entre word y vector
                            if np.abs(cosSim) > threshold: # si la similitud coseno cae dentro del threshold dado
                                results[ self.inverseVocab[yearIndex][index] ] = cosSim # se guarda en results la palabra encontrada
                    else:
                        raise ValueError("Similarity Threshold value must be under 1.0")
                elif type(threshold) is int:
                    similarities = []
                    for index, word in enumerate(tempMat): # ASUMIENDO QUE LA PALABRA ES LA FILA!!!
                        cosSim = 1 - spatial.distance.cosine(vector, word) # se obtiene la similitud coseno entre word y vector
                        similarities.append([index, cosSim]) # se guarda en similarities una lista de elementos [indice, similitud]
                    similarities.sort(key=lambda elem: elem[1], reverse=True) # se ordena la lista de mayor a menor similitud
                    mostSimilar = similarities[0:threshold] # se guardan en mostSimilar los 'threshold' elementos con mayor similitud
                    for index, cosSim in mostSimilar:
                        results[ self.inverseVocab[yearIndex][index] ] = cosSim
                return results
            
            else:
                raise ValueError("Year not present")

        else:
            raise ValueError("Treshold value must be positive")

    def findSimilars2Word(self, word, threshold, year):
        """
        Finds the most similar words within a word2vec embedding matrix.
        This function computes the cosine similarities between embedding vectors
        and a given word. Returning the most similar words within a given treshold.
        
        Parameters
        --------
        word : string
                Input Word. Must be part of selected year's vocabulary.
        threshold : float, int
                    * float: minimun cosine similaritie allowed to consider a word 'close' to the given vector.
                    * int: amount of near words to search. 
        year : int
            Choosen year.

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

        >>> matrixes = [ma, mb, mc]
        >>> yearDict = {1990:0, 1991:1, 1995:2}
        >>> vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
        >>> vocabularies = [vocab1990]

        >>> tempObject = tempName(matrixes, yearDict, vocabularies)

        >>> newVec = tempObject.findSimilars2Word('pablo', 3, 1990)
        
        >>> print(newVec)

        >>> {'pablo': 1.0, 'carlos': 0.9981908926857268, 'martin': -0.974631846197076}
        
        """
        vector = self.getVector(word, year)
        similars = self.findSimilars2Vec(vector, threshold, year)

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

        >>> matrixes = [ma, mb, mc]
        >>> yearDict = {1990:0, 1991:1, 1995:2}
        >>> vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
        >>> vocabularies = [vocab1990]

        >>> tempObject = tempName(matrixes, yearDict, vocabularies)

        >>> newVec = tempObject.getVector('pablo', 1990)
        
        >>> print(newVec)

        >>> [4, 5, 6]
        
        """        
        yearIndex = self.yearDict.get(year, -1) # obtengo el indice del año, si no esta el año devuelve -1
        if(yearIndex != -1):
            tempMat = self.matrixes[yearIndex] # obtengo la matriz del año pedido
            tempVocab = self.vocabularies[yearIndex] # obtengo el vocabulario del año
            wordIndex = tempVocab.get(word, -1) # devuelve la fila donde se encuentra la palabra o -1 si no esta
            if(wordIndex != -1):
                vector = tempMat[wordIndex]
                return vector
            
            else:
                raise ValueError("Word not present in selected year's vocabulary")

        else:
            raise ValueError("Year not present")

    def getVectorPosNeg(self, positives, negatives, year):
        vector = []

        return vector

    def getSim(self, w1, y1, w2, y2):
        #return cosSim
        pass
    def getEvol(self, w1, y1, w2):
        #return evol
        pass
    def getEvolByStep(self, word):
        evolution = []
        return evolution


'''
ma = [[-1,-2,-3],[4,5,6],[7,8,9]]
mb = [[1,2.1,3],[4.2,4.8,6],[7.02,8,9.3]]
mc = [[1.1,2.2,3.1],[4.23,5,6],[7.03,8,9.32]]

matrixes = [ma, mb, mc]
yearDict = {1990:0, 1991:1, 1995:2}
vocab1990 = {'martin':0, 'pablo':1, 'carlos':2}
vocabularies = [vocab1990]

tempObject = tempName(matrixes, yearDict, vocabularies)

newVec1 = tempObject.findSimilars2Vec([1,2,3], 3, 1990)
newVec2 = tempObject.findSimilars2Word('pablo', 3, 1990)
newVec3 = tempObject.getVector('pablo', 1990)

print(newVec1)
print(newVec2)
print(newVec3)
'''