"""Core Forensic Merkle Tree and Verifier implementation."""
import hashlib
import json
from typing import Dict, Any, List, Optional

class ForensicMerkleTree:
    @staticmethod
    def hash_data(data: str) -> str:
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    def __init__(self, events: List[Dict[str, Any]]):
        self.events = events
        self.leaf_hashes = [self.hash_data(json.dumps(e, sort_keys=True)) for e in events]
        self.root = self._build_root(self.leaf_hashes)

    def _build_root(self, hashes: List[str]) -> str:
        if not hashes:
            return ""
        if len(hashes) == 1:
            return hashes[0]

        next_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i+1] if i+1 < len(hashes) else left
            combined = self.hash_data(left + right)
            next_level.append(combined)

        return self._build_root(next_level)

class MemorySnapshotVerifier:
    @staticmethod
    def verify_entry(entry: Dict[str, Any], expected_hash: str) -> bool:
        computed = ForensicMerkleTree.hash_data(json.dumps(entry, sort_keys=True))
        return computed == expected_hash

    @staticmethod
    def verify_tree_integrity(tree: ForensicMerkleTree, original_root: str) -> bool:
        return tree.root == original_root
