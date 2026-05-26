# OLED Molecule Analysis
# Author: Nitin, CUTN
# Date: May 2026

# Results from DFT calculations
molecules = {
    'Naphthalene': {
        'formula': 'C10H8',
        'energy': -386.833,
        'homo': -5.600,
        'lumo': -4.114,
        'gap': 1.485
    },
    'Anthracene': {
        'formula': 'C14H10',
        'energy': -539.530,
        'homo': -5.224,
        'lumo': -1.780,
        'gap': 3.445
    },
    'Carbazole': {
        'formula': 'C12H9N',
        'energy': -671.659,
        'homo': -2.829,
        'lumo': -1.459,
        'gap': 1.370
    }
}

# Print results
print("=" * 60)
print("OLED MOLECULE COMPARISON")
print("=" * 60)

for molecule, props in molecules.items():
    print(f"\n{molecule} ({props['formula']})")
    print("-" * 40)
    print(f"  Total Energy : {props['energy']:.3f} A.U.")
    print(f"  HOMO         : {props['homo']:.3f} eV")
    print(f"  LUMO         : {props['lumo']:.3f} eV")
    print(f"  Band Gap     : {props['gap']:.3f} eV")

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)
print("Anthracene Gap = 3.445 eV → Blue OLED emitter!")
print("Carbazole Gap  = 1.370 eV → OLED host material!")
print("Naphthalene Gap = 1.485 eV → Infrared emission")