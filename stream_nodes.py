#!/usr/bin/env python3
"""
Directed Graph Streaming All Projects and Languages
Anchor Root: E42C
Root Project: data-structures-golang
Anchor Ancestor: data-structures-rust
"""

from collections import deque
from typing import Generator
import json


class ProjectNode:
    def __init__(self, id: str, name: str, language: str):
        self.id = id
        self.name = name
        self.language = language
        self.visited = False


class DirectedGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self._build_graph()

    def _build_graph(self):
        # All 10 projects with their primary languages
        projects = [
            ("E42C", "data-structures-golang", "go"),
            ("E42C-001", "data-structures-rust", "rust"),
            ("E42C-002", "data-structures-core", "python"),
            ("E42C-003", "data-structures-cpp", "cpp"),
            ("E42C-004", "data-structures-java", "java"),
            ("E42C-005", "data-structures-python", "python"),
            ("E42C-006", "data-structures-multi-compiler", "multi"),
            ("E42C-007", "data-structures-arm64", "arm64"),
            ("E42C-008", "data-structures-x86_64", "x86_64"),
            ("E42C-009", "data-structures-benchmark", "benchmark"),
        ]

        # All supported languages
        languages = [
            "rust",
            "go",
            "c",
            "cpp",
            "perl",
            "ruby",
            "csharp",
            "javascript",
            "typescript",
            "python",
            "java",
            "swift",
            "objectivec",
        ]

        # Create project nodes
        for node_id, name, lang in projects:
            self.nodes[node_id] = ProjectNode(node_id, name, lang)

        # Add root node (E42C)
        self.nodes["E42C"] = ProjectNode("E42C", "data-structures-golang", "go")

        # Create edges from root to all projects
        for node_id, _, _ in projects[1:]:  # Skip root
            self.edges.append(("E42C", node_id))

        # Create edges from anchor ancestor (data-structures-rust) to all projects
        for node_id, _, _ in projects[2:]:  # From rust onwards
            self.edges.append(("E42C-001", node_id))

        # Each project supports multiple languages - create language nodes and edges
        lang_support = {
            "data-structures-golang": ["go"],
            "data-structures-rust": ["rust"],
            "data-structures-core": ["python"],
            "data-structures-cpp": ["c", "cpp", "objectivec"],
            "data-structures-java": ["java", "csharp"],
            "data-structures-python": ["python", "javascript", "typescript"],
            "data-structures-multi-compiler": languages,  # All languages!
            "data-structures-arm64": ["c", "cpp", "rust", "go", "python", "java"],
            "data-structures-x86_64": ["c", "cpp", "rust", "go", "python", "java"],
            "data-structures-benchmark": languages,
        }

        # Add language nodes and edges
        for i, lang in enumerate(languages):
            lang_node_id = f"LANG-{i:02d}"
            self.nodes[lang_node_id] = ProjectNode(lang_node_id, lang, lang)

        # Connect projects to their supported languages
        project_lang_map = {
            "E42C": "LANG-01",
            "E42C-001": "LANG-00",
            "E42C-002": "LANG-09",
            "E42C-003": "LANG-02",
            "E42C-004": "LANG-09",
            "E42C-005": "LANG-09",
        }

        for node_id, langs in lang_support.items():
            for lang in langs:
                lang_idx = languages.index(lang)
                lang_node = f"LANG-{lang_idx:02d}"
                self.edges.append((node_id, lang_node))

    def bfs(self, start: str) -> Generator[ProjectNode, None, None]:
        """Breadth-first traversal streaming all nodes"""
        queue = deque([start])
        visited = set()

        while queue:
            node_id = queue.popleft()
            if node_id in visited:
                continue
            visited.add(node_id)

            if node_id in self.nodes:
                yield self.nodes[node_id]

            for src, dst in self.edges:
                if src == node_id and dst not in visited:
                    queue.append(dst)

    def dfs(self, start: str) -> Generator[ProjectNode, None, None]:
        """Depth-first traversal streaming all nodes"""
        stack = [start]
        visited = set()

        while stack:
            node_id = stack.pop()
            if node_id in visited:
                continue
            visited.add(node_id)

            if node_id in self.nodes:
                yield self.nodes[node_id]

            for src, dst in reversed(self.edges):
                if src == node_id and dst not in visited:
                    stack.append(dst)

    def stream_all_nodes(self) -> list:
        """Stream all nodes starting from root E42C"""
        all_nodes = []

        # BFS from root
        for node in self.bfs("E42C"):
            all_nodes.append(
                {
                    "id": node.id,
                    "name": node.name,
                    "language": node.language,
                    "visited": True,
                }
            )

        return all_nodes

    def to_dict(self):
        return {
            "anchor_root": "E42C",
            "root_project": "data-structures-golang",
            "anchor_ancestor": "data-structures-rust",
            "total_nodes": len(self.nodes),
            "total_edges": len(self.edges),
            "nodes": {
                k: {"name": v.name, "language": v.language}
                for k, v in self.nodes.items()
            },
            "edges": self.edges,
        }


def main():
    graph = DirectedGraph()

    # Stream all nodes
    print("=" * 80)
    print("DIRECTED GRAPH - STREAMING ALL NODES")
    print("Anchor Root: E42C")
    print("=" * 80)

    print("\n--- BFS Traversal from E42C ---")
    for node in graph.bfs("E42C"):
        print(
            f"  Node: {node.id:20s} | Project: {node.name:30s} | Language: {node.language}"
        )

    print("\n--- DFS Traversal from E42C ---")
    for node in graph.dfs("E42C"):
        print(
            f"  Node: {node.id:20s} | Project: {node.name:30s} | Language: {node.language}"
        )

    # Save JSON output
    output = graph.to_dict()

    output_file = "/home/sdw3098/data-structures-concrete/directed_graph.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n✓ Saved directed graph to: {output_file}")
    print(f"  Total Nodes: {output['total_nodes']}")
    print(f"  Total Edges: {output['total_edges']}")

    # Also save a summary text file
    summary_file = "/home/sdw3098/data-structures-concrete/graph_summary.txt"
    with open(summary_file, "w") as f:
        f.write("DIRECTED GRAPH - PROJECT/LANGUAGE MAPPING\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Anchor Root: E42C\n")
        f.write(f"Root Project: data-structures-golang\n")
        f.write(f"Anchor Ancestor: data-structures-rust\n\n")
        f.write("PROJECT -> LANGUAGE MAPPINGS:\n")
        f.write("-" * 60 + "\n")

        for node_id, data in output["nodes"].items():
            f.write(f"  {node_id:20s} -> {data['language']}\n")

        f.write("\nALL EDGES:\n")
        f.write("-" * 60 + "\n")
        for src, dst in output["edges"]:
            f.write(f"  {src} -> {dst}\n")

    print(f"✓ Saved summary to: {summary_file}")


if __name__ == "__main__":
    main()
