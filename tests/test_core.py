"""Tests for ForensicMerkleTree."""
import unittest
from memory_snapshot_forensic_verifier.core import ForensicMerkleTree, MemorySnapshotVerifier

class TestForensicMerkleTree(unittest.TestCase):
    def test_merkle_root_and_tampering(self):
        e1 = [{"step": 1, "data": "a"}, {"step": 2, "data": "b"}]
        tree = ForensicMerkleTree(e1)
        original_root = tree.root

        self.assertTrue(MemorySnapshotVerifier.verify_tree_integrity(tree, original_root))

        # Tamper event
        tampered_events = [{"step": 1, "data": "tampered"}, {"step": 2, "data": "b"}]
        tampered_tree = ForensicMerkleTree(tampered_events)
        self.assertNotEqual(tampered_tree.root, original_root)
        self.assertFalse(MemorySnapshotVerifier.verify_tree_integrity(tampered_tree, original_root))
