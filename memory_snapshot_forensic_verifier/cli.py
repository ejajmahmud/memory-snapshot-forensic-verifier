"""CLI for Memory Snapshot Forensic Verifier."""
import argparse
from .core import ForensicMerkleTree, MemorySnapshotVerifier

def main():
    parser = argparse.ArgumentParser(description="Memory Snapshot Forensic Verifier CLI")
    parser.add_argument("--demo", action="store_true", help="Run Merkle audit verification demo")
    args = parser.parse_args()

    events = [
        {"step": 1, "action": "search_code", "status": "ok"},
        {"step": 2, "action": "apply_patch", "status": "ok"},
        {"step": 3, "action": "run_tests", "status": "passed"}
    ]
    tree = ForensicMerkleTree(events)
    print(f"Merkle Root computed: {tree.root}")
    intact = MemorySnapshotVerifier.verify_tree_integrity(tree, tree.root)
    print(f"Audit Integrity Verified: {intact}")

if __name__ == "__main__":
    main()
