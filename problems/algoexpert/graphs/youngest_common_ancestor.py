from typing import Optional


class AncestralTree:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ancestor: Optional[AncestralTree] = None


def yca(top_ancestor: Optional[AncestralTree],
        descendant_one: Optional[AncestralTree],
        descendant_two: Optional[AncestralTree]) -> AncestralTree:
    depth_one = find_depth(descendant_one, top_ancestor)
    depth_two = find_depth(descendant_two, top_ancestor)
    if depth_one > depth_two:
        return backtrack_ancestral_tree(descendant_one, descendant_two, depth_one - depth_two)
    else:
        return backtrack_ancestral_tree(descendant_two, descendant_one, depth_two - depth_one)


def find_depth(descendant: Optional[AncestralTree],
               top_ancestor: Optional[AncestralTree]) -> int:
    depth = 0
    while descendant != top_ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrack_ancestral_tree(lower_descendant: Optional[AncestralTree],
                             higher_descendant: Optional[AncestralTree],
                             difference: int) -> AncestralTree:
    while difference > 0:
        difference -= 1
        lower_descendant = lower_descendant.ancestor
    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor
    return lower_descendant if lower_descendant else AncestralTree("NONE")
