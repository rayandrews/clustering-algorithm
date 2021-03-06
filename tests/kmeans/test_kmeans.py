import unittest

from numpy import ndarray, testing

from ..context import iris_data, iris_target, check_model_exist, purity_score, print_in_test
from cleverly.kmeans.KMeans import KMeans


class KMeansTestSuite(unittest.TestCase):
    """KMeans test cases."""

    @classmethod
    def setUpClass(self):
        self.filename = './tests/models/kmeans.model'
        self.kmeans = KMeans(
            n_clusters=3, max_iter=300, tol=0.002)
        self.kmeans.fit_predict(iris_data)

    def test_kmeans_return_labels_with_type_numpy_array(self):
        self.assertIsInstance(self.kmeans.labels_, ndarray)
        print_in_test("KMeans (max_iter=300, tol=0.002): %f" %
                      purity_score(iris_target, self.kmeans.labels_))


if __name__ == '__main__':
    unittest.main()
