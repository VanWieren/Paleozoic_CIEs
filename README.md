# Paleozoic_CIEs
Repository for van Wieren et al., 2026; EPSL (https://doi.org/10.1016/j.epsl.2025.119745)

## Model code

The tracer-advection/diffusion sediment transport model used in this paper is maintained
separately as an installable package: **[TracerDiff](https://github.com/VanWieren/TracerDiff)**.
This repository contains the paper-specific data and analysis notebooks; TracerDiff is the
actively maintained home of the model itself.

Install it before running any notebook here:

```bash
git clone https://github.com/VanWieren/TracerDiff.git
cd TracerDiff
pip install -e .
```

The notebooks in `notebooks/` then import the model directly from the installed package:

```python
from tracerdiff import run, Model_output
from tracerdiff.utils import *
```

See the TracerDiff README for the full model parameter reference and two runnable example
notebooks demonstrating the model on its own, outside the context of this paper.
