"""Script for generating the AnIML linking template"""


import sdRDM


if __name__ == "__main__":
    lib = sdRDM.DataModel.from_git(
        url="https://github.com/FAIRChemistry/animl-specifications"
    )
    animl = lib.AnIML()
    animl.generate_linking_template()
