from typing import List, Tuple, Union

TreasureTuple = Tuple[str, str]
LocationTuple = Tuple[str, Tuple[str, str], str]
CombinedRecord = Tuple[str, str, str, Tuple[str, str], str]
MaybeRecord = Union[str, CombinedRecord]
CleanRecord = Tuple[str, str, Tuple[str, str], str]


def get_coordinate(record: TreasureTuple) -> str:
    '''
    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    '''
    return record[1]


def convert_coordinate(coordinate: str) -> Tuple[str, str]:
    '''
    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    '''
    return (coordinate[0], coordinate[1])


def compare_records(azara_record: TreasureTuple,
                    rui_record: LocationTuple) -> bool:
    '''
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    '''
    return azara_record[1] == ''.join(rui_record[1])


def create_record(azara_record: TreasureTuple,
                  rui_record: LocationTuple) -> MaybeRecord:
    '''
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    '''
    if not compare_records(azara_record, rui_record):
        return "not a match"

    return (*azara_record, *rui_record)


def clean_up(combined_record: CombinedRecord) -> str:
    '''
    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: tuple of tuples - everything "cleaned", with excess coordinates and information removed.
    '''
    report: List[str] = []
    for tup in combined_record:
        cleaned = tuple(val for i, val in enumerate(tup) if i != 1)
        report.append(str(cleaned))
    return '\n'.join(report) + '\n'
