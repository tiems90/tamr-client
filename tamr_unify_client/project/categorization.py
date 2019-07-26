from tamr_unify_client.base_model import MachineLearningModel
from tamr_unify_client.project.resource import Project
from tamr_unify_client.taxonomy.resource import Taxonomy


class CategorizationProject(Project):
    """A Categorization project in Unify."""

    def model(self):
        """Machine learning model for this Categorization project.
        Learns from verified labels and predicts categorization labels for unlabeled records.

        :returns: The machine learning model for categorization.
        :rtype: :class:`~tamr_unify_client.base_model.MachineLearningModel`
        """
        alias = self.api_path + "/categorizations/model"
        return MachineLearningModel(self.client, None, alias)

    def create_taxonomy(self, creation_spec):
        """Creates a :class:`~tamr_unify_client.taxonomy.resource.Taxonomy` for this project.

        A taxonomy cannot already be associated with this project.

        :param creation_spec: The creation specification for the taxonomy, which can include name.
        :type creation_spec: dict
        :returns: The new Taxonomy
        :rtype: :class:`~tamr_unify_client.taxonomy.resource.Taxonomy`
        """
        alias = self.api_path + "/taxonomy"
        resource_json = self.client.post(alias, json=creation_spec).successful().json()
        return Taxonomy.from_json(self.client, resource_json, alias)

    def taxonomy(self):
        """Retrieves the :class:`~tamr_unify_client.taxonomy.resource.Taxonomy` associated with this project.
        If a taxonomy is not already associated with this project,
        call :func:`~tamr_unify_client.project.categorization.CategorizationProject.create_taxonomy` first.

        :returns: The project's Taxonomy
        :rtype: :class:`~tamr_unify_client.taxonomy.resource.Taxonomy`
        """
        alias = self.api_path + "/taxonomy"
        resource_json = self.client.get(alias).successful().json()
        return Taxonomy.from_json(self.client, resource_json, alias)

    # super.__repr__ is sufficient
