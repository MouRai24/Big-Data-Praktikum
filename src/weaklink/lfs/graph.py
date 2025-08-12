import networkx as nx
from snorkel.labeling import labeling_function

def make_graph_lf(df_ref, threshold: float, min_component_size: int = 3,
                  source_col: str = "source_id", target_col: str = "target_id", score_col: str = "agg_score"):
    """Return a labeling function that votes 1 for pairs in the same large connected component of a similarity graph."""
    G = nx.Graph()
    for _, r in df_ref.iterrows():
        if score_col in r and r[score_col] >= threshold:
            G.add_edge(r[source_col], r[target_col])
    comps = list(nx.connected_components(G))
    comp_map = {n: cid for cid, comp in enumerate(comps) for n in comp}
    comp_size = {cid: len(comp) for cid, comp in enumerate(comps)}
    @labeling_function(name=f"lf_graph[t>={threshold},min={min_component_size}]")
    def lf(x):
        u, v = x[source_col], x[target_col]
        cid = comp_map.get(u)
        if cid is not None and cid == comp_map.get(v) and comp_size[cid] >= min_component_size:
            return 1
        return 0
    return lf
