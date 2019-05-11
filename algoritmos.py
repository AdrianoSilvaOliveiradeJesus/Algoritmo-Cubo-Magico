class Algoritmos:
    def __init__(self):

        self.PLL = {
            "A1":"x [(R' U R') D2] [(R U' R') D2] R2",
            "A2":"x' [(R U' R) D2] [(R' U R) D2] R2",
            "U1":"R2 U [R U R' U'] (R' U') (R' U R')",
            "U2":"[R U'] [R U] [R U] [R U'] R' U' R2",
            "H":"M2 U M2 U2 M2 U M2",
            "T":"[R U R' U'] [R' F] [R2 U' R'] U' [R U R' F']",
            "J1":"[R' U L'] [U2 R U' R' U2] [R L U']",
            "J2":"[R U R' F'] {[R U R' U'] [R' F] [R2 U' R'] U'}",
            "R1":"[R' U2 R U2] [R' F] [R U R' U'] [R' F'] R2 U'",
            "R2":"[R' U2 R U2] [R' F] [R U R' U'] [R' F'] R2 U'",
            "V":"[R' U R' d'] [R' F'] [R2 U' R' U] [R' F R F]",
            "G1":"R2 u R' U R' U' R u' R2 [y' R' U R]",
            "G2":"[R' U' R] y R2 u R' U R U' R u' R2",
            "G3":"R2 u' R U' R U R' u R2 [y R U' R']",
            "G4":"[R U R'] y' R2 u' R U' R' U R' u R2",
            "F":"[R' U2 R' d'] [R' F'] [R2 U' R' U] [R' F R U' F]",
            "Z":"M2 U M2 U M' U2 M2 U2 M' U2",
            "Y":"F R U' R' U' [R U R' F'] {[R U R' U'] [R' F R F']}",
            "N1":"{(L U' R) U2 (L' U R')} {(L U' R) U2 (L' U R')} U",
            "N2":"{(R' U L') U2 (R U' L)} {(R' U L') U2 (R U' L)} U'",
            "E":"X' (R U' R') D (R U R') u2 (R' U R) D (R' U' R)"
            }
