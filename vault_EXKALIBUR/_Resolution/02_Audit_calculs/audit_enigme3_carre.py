"""Audit Enigme 3 : 'Complete le carre' -> le carre de lettres de l'enluminure (rangee 2, colonne gauche).
Releve visuel (zoom x4 sur photo, fichier Sources/zooms/grille_R2L.png) ; '_' = case vide.
Hypothese testee : carre SATOR (palindrome latin classique). On verifie que les lettres visibles
sont toutes compatibles, puis on liste les lettres a ajouter pour le completer.
"""
import sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
GRID = ["S__OR", "_R_PO", "_____", "OP_R_", "RO__S"]
SATOR = ["SATOR", "AREPO", "TENET", "OPERA", "ROTAS"]
ok = all(g in ("_", s) for gr, sr in zip(GRID, SATOR) for g, s in zip(gr, sr))
print("Lettres visibles compatibles avec SATOR :", ok)
missing = [s for gr, sr in zip(GRID, SATOR) for g, s in zip(gr, sr) if g == "_"]
print("Lettres manquantes (avec repetitions) :", "".join(missing), dict(Counter(missing)))
print("Lettres manquantes distinctes         :", "".join(sorted(set(missing))))
# Autres carres latins connus -> test d'unicite
for name, sq in {"ROTAS (inverse)": ["ROTAS", "OPERA", "TENET", "AREPO", "SATOR"]}.items():
    print(f"Compatible avec {name} :", all(g in ("_", s) for gr, sr in zip(GRID, sq) for g, s in zip(gr, sr)))
init = "TI" + "LG"  # (Tristan, Iseult) + (Lancelot, Guenievre)
tot = Counter(init + "".join(sorted(set(missing))))
print("TI + LG + lettres distinctes du carre :", "".join(sorted(tot.elements())), "| TINTAGEL trie :", "".join(sorted("TINTAGEL")),
      "| egal :", tot == Counter("TINTAGEL"))
