from src.data import grapes, managers, vineyards, vineyards_info


class Processes:
    managers: list[dict] = managers
    grapes: list[dict] = grapes
    vineyards: list[dict] = vineyards
    vineyards_info: list[dict] = vineyards_info

    @classmethod
    def get_managers_ids(cls) -> list[int]:
        """
        This function gets all the ids in the list of managers dicts and return them as a list
        In this case we are using a for loop in order to get KeyErrors if id is missing in the dict
        becouse a missing id could be a potencial problem.
        """

        managers_list: list = list()

        for manager in cls.managers:
            try:
                managers_list.append(manager["id"])
            except KeyError as e:
                print(f"Error in manager data, no id key for manager: {manager} - {e}")

        return managers_list

    @classmethod
    def get_tax_number_by_name(cls) -> list[str]:
        """
        This function gets all the tax number in the list of managers dicts and return them as a list
        In this case we are using a list comprehension  to make it more efficient and easy to read to python developers.
        If tax number is missing this manager number is ignored this time.
        """
        tax_numbers: list

        managers_sorted: list = sorted(cls.managers, key=lambda x: x["name"])
        tax_numbers = [
            manager["tax_number"]
            for manager in managers_sorted
            if "tax_number" in manager
        ]
        return tax_numbers

    @classmethod
    def get_group_by_field_name(
        cls,
        field_data: list[dict],
        key_in_vineyard: str,
        value_to_group: str,
        sort_data: bool = False,
    ) -> dict:
        """
        This function creates a dict containing the grape id as key and the total planted area of this grape as value.
        In this case if any key is missing in the dicts we will stop the execution since missing grapes or areas will return false
        data.
        """
        grouped_data: dict = dict()
        try:
            grouped_data: dict = {data["name"]: list() for data in field_data}
            for vineyard in cls.vineyards:
                grouped_data[vineyard[key_in_vineyard]].append(vineyard[value_to_group])

        except KeyError as e:
            print(f"Missing key in dicts: {e}")

        if sort_data:
            grouped_data = {key: sorted(value) for key, value in grouped_data.items()}

        return grouped_data

    @classmethod
    def get_area_for_field(cls, field_data: list[dict], key_in_vineyard: str) -> dict:
        """
        This function adds to the vineyard dict all the names related to the ids in order to make faster and easier data extractions later.
        If the dataset is too large this should not be done.
        """
        grouped_areas: dict = cls.get_group_by_field_name(
            field_data=field_data,
            key_in_vineyard=key_in_vineyard,
            value_to_group="area",
        )

        sum_areas: dict = {key: sum(areas) for key, areas in grouped_areas.items()}
        return sum_areas

    @classmethod
    def extend_vineyards_dict(cls):
        """
        This function adds to the vineyard dict all the names related to the ids in order to make faster and easier data extractions later.
        If the dataset is too large this should not be done.
        """
        for vineyard in cls.vineyards:
            vineyard["grape_name"] = next(
                (
                    grape["name"]
                    for grape in cls.grapes
                    if grape["id"] == vineyard["grape_id"]
                )
            )
            vineyard["manager_name"] = next(
                (
                    manager["name"]
                    for manager in cls.managers
                    if manager["id"] == vineyard["manager_id"]
                )
            )
            vineyard["vineyard_name"] = next(
                (
                    vineyard_["name"]
                    for vineyard_ in cls.vineyards_info
                    if vineyard_["id"] == vineyard["vineyard_id"]
                )
            )
