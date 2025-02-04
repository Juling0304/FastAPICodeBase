class ProcessedParsingData:
    def __init__(
        self,
        sentence: str,
        run_position_indexes: list[int],
        run_position_indexed_fragment_texts: list[str],
        run_property_indexes: list[int],
    ):
        self.sentence: str = sentence
        self.run_position_indexes: list[int] = run_position_indexes
        self.run_position_indexed_fragment_texts: list[str] = (
            run_position_indexed_fragment_texts
        )
        self.run_property_indexes: list[int] = run_property_indexes

        self.run_position_index_to_list_index: list[int] = {}

        for list_index, run_position_index in enumerate(self.run_position_indexes):
            self.run_position_index_to_list_index[run_position_index] = list_index

    def get_sentence(self) -> str:
        return self.sentence

    def get_first_run_position_index(self) -> int | None:
        if len(self.run_position_indexes) > 0:
            return self.run_position_indexes[0]

        return None

    def get_run_position_indexed_fragment_text(self, run_position_index: int) -> str:
        return self.run_position_indexed_fragment_texts[
            self.run_position_index_to_list_index[run_position_index]
        ]

    def change_run_position_indexed_fragment_text(
        self, run_position_index: int, new_text: str
    ) -> None:
        if run_position_index in self.run_position_index_to_list_index:
            self.run_position_indexed_fragment_texts[
                self.run_position_index_to_list_index[run_position_index]
            ] = new_text

    def renew_sentence(self) -> None:
        self.sentence = "".join(self.run_position_indexed_fragment_texts)

    def export_to_dict(self) -> dict[str, str | list[str | int]]:
        return {
            "sentence": self.sentence,
            "run_position_indexes": self.run_position_indexes,
            "run_position_indexed_fragment_texts": self.run_position_indexed_fragment_texts,
            "run_property_indexes": self.run_property_indexes,
        }
