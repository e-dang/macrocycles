from abc import ABC, abstractmethod
from collections import namedtuple

import project_io


class IDataHandler(ABC):
    """
    Interface for classes that couple together specific IO classes in order to supply and write data for a specific
    Transformer class.
    """

    @abstractmethod
    def load(self):
        """
        Abstract method for calling load on each IO class of the specific derived DataHandler and returning the data
        in a tuple.
        """

    @abstractmethod
    def save(self, data):
        """
        Abstract method for calling save() on the IO class used for saving data in the specific derived DatSupplier.
        """


class SCGDataHandler(IDataHandler):
    """
    Implementation of a DataHandler used to supply and write the data needed and generated by the SideChainGenerator
    MolTransformer.
    """

    def __init__(self, source):
        """
        Initializer method used to instantiate the IO classes for loading heterocycles and connection molecules from
        either JSON files or MongoDB depending on the specified source.

        Args:
            source (str): The source to load data from. Can either be 'json' or 'mongo'
        """

        if source == 'json':
            self._heterocycle_loader = project_io.JsonHeterocycleIO()
            self._connection_loader = project_io.JsonConnectionsIO()
            self._side_chain_saver = project_io.JsonSideChainIO()
        elif source == 'mongo':
            pass

    def load(self):

        SideChainGeneratorData = namedtuple('SideChainGeneratorData', 'heterocycles connections')
        return SideChainGeneratorData(self._heterocycle_loader.load(), self._connection_loader.load())

    def save(self, data):

        self._side_chain_saver.save(data)
