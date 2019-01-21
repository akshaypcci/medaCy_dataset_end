from pkg_resources import resource_listdir, resource_string, resource_filename
from medacy.data import Dataset
from os.path import join

package_name = __name__

def load():
    """
    Loads the Engineered Nanomedicine Database (END). This dataset is a collection of annotated
    FDA nanomedicine drug labels containing 28 unique entities.
    Dataset citation: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5644562/
    :return: a medaCy Dataset object and a list of entities.
    """

    entities = resource_string(package_name, join('data', 'END.types')).decode('utf-8').split("\n")

    meta_data = {
        'entities': entities,
        'relations': None  # set to None if no relations
    }

    return get_training_dataset(), get_evaluation_dataset(), meta_data

def get_training_dataset():
    """
    :return: a medaCy Dataset object containing this Dataset's designated training data.
    """
    return Dataset(resource_filename(package_name, 'data/training'))

def get_evaluation_dataset():
    """
    Leave the evaluation folder empty if no evaluation data is provided.

    :return: a medaCy Dataset object containing this Dataset's designated training data.
    """
    return Dataset(resource_filename(package_name, 'data/evaluation'))