# OLED Molecule Analysis
# Author: Nitin, CUTN
# Date: May 22, 2026

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
    }
}

# Print results
print("=" * 50)
print("OLED MOLECULE COMPARISON")
print("=" * 50)

for molecule, props in molecules.items():
    print(f"\n{molecule} ({props['formula']})")
    print("-" * 40)
    print(f"  Total Energy : {props['energy']:.3f} A.U.")
    print(f"  HOMO         : {props['homo']:.3f} eV")
    print(f"  LUMO         : {props['lumo']:.3f} eV")
    print(f"  Band Gap     : {props['gap']:.3f} eV")

print("\n" + "=" * 50)
print("CONCLUSION")
print("=" * 50)
print("Anthracene Gap = 3.445 eV → Good for Blue OLED!")
print("Naphthalene Gap = 1.485 eV → Infrared emission")