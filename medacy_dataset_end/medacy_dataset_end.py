from pkg_resources import resource_listdir, resource_string, resource_filename
from medacy.data import Dataset
from medacy.tools import DataFile
from os.path import join

def load():
    """
    Loads the Engineered Nanomedicine Database (END) for testing purposes. This dataset is a collection of annotated
    FDA nanomedicine drug labels containing 28 unique entities.
    Dataset citation: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5644562/
    :return: a medaCy Dataset object and a list of entities.
    """
    package_name = "medacy_dataset_end"

    entities = resource_string(package_name, join('data', 'END.types')).decode('utf-8').split("\n")

    dataset = Dataset(resource_filename(package_name, 'data'))
    return dataset, entities