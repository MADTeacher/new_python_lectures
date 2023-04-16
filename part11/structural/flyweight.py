class CarDetailDescription:
    def __init__(self, description: str) -> None:
        self.description = description

    def get_description(self) -> str:
        return self.description


class CarDetail:
    def __init__(self, detail_id: int, 
                          detail_description: CarDetailDescription) -> None:
        self.detail_id = detail_id
        self.detail_description = detail_description

    def __str__(self) -> str:
        return f"Detail ID: {self.detail_id}, Description: {self.detail_description.get_description()}"


class CarDetailFactory:
    def __init__(self) -> None:
        self.details: dict[str, CarDetailDescription] = {}

    def get_detail_description(self, description: str) -> CarDetailDescription:
        if description not in self.details:
            self.details[description] = CarDetailDescription(description)
        return self.details[description]


if __name__ == "__main__":
    detail_factory = CarDetailFactory()

    details: list[CarDetail] = [
        CarDetail(
            1,
            detail_factory.get_detail_description("Амортизатор"),
        ),
        CarDetail(
            2,
            detail_factory.get_detail_description("Амортизатор"),
        ),
        CarDetail(
            3, detail_factory.get_detail_description("Тормозной диск"),
        ),
        CarDetail(
            4,
            detail_factory.get_detail_description("Тормозной диск"),
        ),
        CarDetail(
            5,
            detail_factory.get_detail_description("Колесо"),
        ),
        CarDetail(
            6,
            detail_factory.get_detail_description("Колесо"),
        ),
    ]

    for detail in details:
        print(detail)
