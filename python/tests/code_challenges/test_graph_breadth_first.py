import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph


# @pytest.mark.skip("TODO")
def test_bfs(graph):
    nodes = graph.get_nodes()
    root = nodes[0]
    actual = graph.breadth_first(root)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_bfs_len(graph):
    nodes = graph.get_nodes()
    root = nodes[0]
    list = graph.breadth_first(root)
    actual = len(list)
    expected = 6
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_no_children():
    graph = Graph()
    graph.add_node("Test")
    nodes = graph.get_nodes()
    root = nodes[0]
    actual = graph.breadth_first(root)
    expected = ["Test"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_no_graph():
    graph = Graph()
    actual = graph.breadth_first("root")
    expected = []
    assert actual == expected



@pytest.fixture
def graph():

    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_edge(pandora, arendelle)

    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)

    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)

    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)

    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)

    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)

    return realms
