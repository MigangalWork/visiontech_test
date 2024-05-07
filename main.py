from src.process import Processes

if __name__ == "__main__":
    print(' -- Welcome to the visiontech test, the anwers will be displayed after this mesage -- ')
    Processes.extend_vineyards_dict()

    managers_ids: list = Processes.get_managers_ids()
    print(f"Managers ids list: {managers_ids}")

    managers_tax_number: list = Processes.get_tax_number_by_name()
    print(f"Managers tax number by name list: {managers_tax_number}")

    grapes_by_total_area = Processes.get_area_for_field(
        field_data=Processes.grapes, key_in_vineyard="grape_name")
    print(f"Dict with grapes planted area: {grapes_by_total_area}")

    managers_by_total_area = Processes.get_area_for_field(
        field_data=Processes.managers, key_in_vineyard="manager_name")
    print(f"Dict with managers with is total managed area: {managers_by_total_area}")

    vineyard_managers_list = Processes.get_group_by_field_name(
        field_data=Processes.vineyards_info,
        key_in_vineyard="vineyard_name",
        value_to_group="manager_name",
        sort_data=True,)
    print(f"List of vineyard with is associated managers in a list: {vineyard_managers_list}")
