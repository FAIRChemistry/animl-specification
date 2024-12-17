# AnIML specifications

This repository implements thr original AnIML XSD specification as [markdown data model](https://github.com/FAIRChemistry/md-models) to make use of code generation tools.

## Usage

### Code generation

To generate the code, run the following command:

```bash
md-models pipeline -i gen.toml
```

This will generate the following files:

- `schemes/animl.json`
- `docs/model.md`
- `typescript/src/index.ts`

### Python

As an alternative to the code generation, you can use the `mdmodels` Python library to dynamically generate Python PyDantic models and use them in your code.

```python
from mdmodels import DataModel

animl = DataModel.from_github(
    repo="FAIRChemistry/animl-specification",
    branch="main",
    path="specifications/animl.md",
)

# You can now use the animl model in your code
animldoc = animl.AnIML(
    # ...
)
```

### Rust

Similar to the Python example, you can use the `mdmodels` macro functions to dynamically generate serde-compatible Rust structs.

```rust
use mdmodels_macro::parse_mdmodel;

parse_mdmodel!("specifications/animl.md");

// You can now use the animl struct in your code
let animl = AnIMLBuilder::default()
    .sample_set(SampleSetBuilder::default().build())
    .build();
```
