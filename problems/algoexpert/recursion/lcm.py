from typing import List


class Tree:
    def __init__(self, direct_reports: List["Tree"] = []):
        self.direct_reports = direct_reports


class OrgInfo:
    def __init__(self, lowest_common_manager: "OrgInfo",
                 num_important_reports: int):
        self.lowest_common_manager = lowest_common_manager
        self.num_important_reports = num_important_reports


def get_lowest_common_manager(root: Tree,
                              report1: Tree, report2: Tree) -> OrgInfo:
    return traverse_organization(root, report1, report2).lowest_common_manager


def traverse_organization(manager: Tree,
                          report1: Tree, report2: Tree) -> OrgInfo:
    num_important_reports = 0
    for worker in manager.direct_reports:
        org_info = traverse_organization(worker, report1, report2)
        if org_info.lowest_common_manager:
            return org_info

        num_important_reports += org_info.num_important_reports
    if manager == report1 or manager == report2:
        num_important_reports += 1
    lowest_common_manager = manager if num_important_reports == 2 else None
    return OrgInfo(lowest_common_manager, num_important_reports)
